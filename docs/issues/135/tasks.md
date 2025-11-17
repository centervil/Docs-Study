# Task Checklist for Repository Separation

This checklist outlines the concrete steps needed to separate the documentation and scripts into the `my-docs` and `my-apps` repositories.

- [ ] **1. Set up the working environment**
  - Create a `./work` directory in the local `Docs-Study` workspace.
  - Clone the `my-docs` repository into `./work/my-docs`.
  - Clone the `my-apps` repository into `./work/my-apps`.

- [ ] **2. Inventory of unnecessary files**
  - Review all files and directories in the `Docs-Study` repository.
  - Identify any documents or scripts that are obsolete and do not need to be migrated.
  - Delete these unnecessary files.

- [ ] **3. Migrate documents and scripts**
  - Copy all relevant documentation directories (e.g., `security-news/`, `research/`) to `./work/my-docs/`.
  - Copy all documentation generation scripts to `./work/my-apps/tools/doc-generator/`.

- [ ] **4. Commit and push migrated content**
  - In the `./work/my-docs` directory, add, commit, and push the new documentation files to the remote `my-docs` repository.
  - In the `./work/my-apps` directory, add, commit, and push the new script files to the remote `my-apps` repository.

- [ ] **5. Build `my-docs` workflow**
  - Create a new workflow file at `./work/my-docs/.github/workflows/generate-docs.yml`.
  - Implement the workflow steps as defined in the `design.md` document, ensuring it checks out both repositories and executes the scripts.

- [ ] **6. Verify operation**
  - Manually trigger the new workflow in the `my-docs` repository on GitHub.
  - Confirm that the workflow completes successfully.
  - Verify that the documentation is generated correctly and a new commit is pushed to the `my-docs` repository.

- [ ] **7. Clean up the old environment**
  - Once the new workflow is confirmed to be working, delete the migrated documentation and script directories from the `Docs-Study` repository.
  - Remove any old GitHub Actions workflows from `Docs-Study` that are now redundant.

- [ ] **8. Update documentation**
  - Edit the `README.md` in the `my-docs` repository to explain its purpose and how the content is generated.
  - Edit the `README.md` in the `my-apps` repository to explain its role as a toolbox for the documentation project.
