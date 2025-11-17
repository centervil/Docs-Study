# Technical Design for Repository Separation

## 1. Architecture

The proposed architecture separates the documentation (`my-docs`) from the logic that generates it (`my-apps`), using a GitHub Actions workflow as the orchestrator.

-   **`my-docs` Repository**:
    -   **Purpose**: Stores and manages the documentation content (Markdown files, etc.).
    -   **Orchestration**: Contains a GitHub Actions workflow (`.github/workflows/generate-docs.yml`) that controls the entire documentation generation process.
    -   **Responsibilities**:
        -   Holds the canonical source for documentation.
        -   Initiates the generation process.
        -   Commits and pushes the final, generated documentation back to itself.

-   **`my-apps` Repository**:
    -   **Purpose**: A dedicated repository for storing all scripts and tools required for documentation generation.
    -   **Responsibilities**:
        -   Acts as a simple "toolbox."
        -   It is unaware of the `my-docs` repository and holds no credentials or special permissions. Its scripts are designed to be portable and run in any environment where they are checked out.

-   **Workflow Process (`my-docs` side)**:
    1.  The workflow is triggered (e.g., on a schedule, manual dispatch, or push to `main`).
    2.  **Checkout `my-docs`**: The workflow checks out its own repository content.
    3.  **Checkout `my-apps`**: It uses the `actions/checkout@v4` action to clone the `my-apps` repository into a subdirectory within the workspace (e.g., `./apps`).
    4.  **Execute Scripts**: The workflow runs the necessary scripts from the `./apps` directory. These scripts read source materials (if any) and generate the final documentation files.
    5.  **Commit and Push**: The workflow detects changes (new or modified files), and uses a dedicated action (e.g., `stefanzweifel/git-auto-commit-action`) to commit and push them back to the `my-docs` repository.

## 2. Implementation Plan

The implementation will be executed within the `Docs-Study` local workspace.

1.  **Environment Setup**:
    -   Create a `./work` directory.
    -   Clone `https://github.com/<owner>/my-docs.git` into `./work/my-docs`.
    -   Clone `https://github.com/<owner>/my-apps.git` into `./work/my-apps`.

2.  **File Migration**:
    -   Identify all documentation-related directories (`security-news/`, `research/`, etc.) in `Docs-Study`.
    -   Use `rsync` to copy these directories into `./work/my-docs/`.
    -   Identify all documentation generation scripts (e.g., `tools/your-script.sh`).
    -   Copy these scripts into an appropriate structure within `./work/my-apps/` (e.g., `./work/my-apps/tools/doc-generator/`).

3.  **Push Initial State**:
    -   Commit and push the newly added files in both the `my-docs` and `my-apps` local clones to their respective remote repositories.

4.  **Workflow Creation (`my-docs`)**:
    -   Create a new file: `./work/my-docs/.github/workflows/generate-docs.yml`.
    -   The workflow will include the following steps:
        ```yaml
        name: Generate Documentation

        on:
          workflow_dispatch: # Allow manual triggering
          schedule:
            - cron: '0 0 * * *' # Example: Run daily

        jobs:
          build:
            runs-on: ubuntu-latest
            steps:
              - name: Checkout my-docs repository
                uses: actions/checkout@v4
                with:
                  path: my-docs

              - name: Checkout my-apps repository
                uses: actions/checkout@v4
                with:
                  repository: <owner>/my-apps
                  path: my-apps
                  # If my-apps is private, a PAT would be needed here
                  # token: ${{ secrets.MY_APPS_PAT }}

              - name: Run documentation generator
                run: |
                  # Assuming the script is executable
                  bash ./my-apps/tools/doc-generator/your-script.sh

              - name: Commit and push changes
                uses: stefanzweifel/git-auto-commit-action@v5
                with:
                  commit_message: "docs: Auto-generate documentation"
                  # Specify the repository path if not in the root
                  repository: ./my-docs
        ```

5.  **Cleanup `Docs-Study`**:
    -   After verifying the new workflow, remove the migrated directories (`security-news/`, `research/`, `tools/`) from the `Docs-Study` repository to finalize the separation.

## 3. Testing Strategy

1.  **Unit Testing (Scripts)**: If scripts become complex, add unit tests within the `my-apps` repository to ensure their logic is correct.
2.  **Integration Testing (Workflow)**:
    -   The primary testing method will be to manually trigger the `generate-docs.yml` workflow in the `my-docs` repository via `workflow_dispatch`.
    -   **Verification Steps**:
        1.  Confirm the workflow run completes successfully.
        2.  Check the commit history of the `my-docs` repository for a new commit with the specified message.
        3.  Inspect the content of the committed files to ensure they are generated as expected.
        4.  Confirm that no changes were pushed from the `my-apps` repository.
