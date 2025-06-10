## draw.io XML文書作成ガイド (フロー図)

この文書では、draw.ioでフロー図をXML文書として作成する方法を解説します。GUI操作に頼らず、テキストベースでダイアグラムを定義し、draw.ioにインポートする手順をステップごとに説明します。

### draw.io XML形式の基本

draw.ioのXML文書は、mxCell要素を基本として構成されます。mxCell要素は、ノード（図形）やエッジ（線）などのダイアグラムの要素を表します。

* **mxCell (ノード):**
    * `id`: ノードの一意なID (省略可能、draw.ioが自動生成)
    * `value`: ノード内に表示するテキスト
    * `style`: ノードのスタイル (図形の種類、色、フォントなど)
    * `vertex`: ノードが頂点であることを示す属性 (常に `vertex="1"`)
    * `parent`: 親となるmxCellのID (通常は `1`)
* **mxCell (エッジ):**
    * `id`: エッジの一意なID (省略可能、draw.ioが自動生成)
    * `style`: エッジのスタイル (線の種類、色、矢印など)
    * `edge`: エッジであることを示す属性 (常に `edge="1"`)
    * `parent`: 親となるmxCellのID (通常は `1`)
    * `source`: 接続元のmxCellのID
    * `target`: 接続先のmxCellのID
    * `mxGeometry`: エッジの形状を定義する要素

### XML文書作成手順

#### 1. draw.io XMLの基本構造

draw.io XML文書は、以下の基本構造を持ちます。

```xml
<mxfile host="app.diagrams.net" modified="日時" agent="エージェント情報" etag="ETag">
  <diagram id="ダイアグラムID" name="ダイアグラム名">
    <mxGraphModel dx="配置X" dy="配置Y" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- ここにmxCell要素を追加 -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

`<!-- ここにmxCell要素を追加 -->` の部分に、フロー図の要素を記述していきます。

#### 2. サブグラフ (mxCell - group)

サブグラフは、mxCell要素で `group` スタイルを指定することで表現します。

例:
```xml
<mxCell id="subgraph1" value="1. プロセスグループ名" style="group" vertex="1" parent="1">
  <mxGeometry x="20" y="20" width="200" height="150" as="geometry"/>
</mxCell>
```
* `style="group"`: サブグラフであることを指定
* `mxGeometry`: サブグラフの位置とサイズを指定

#### 3. ノード (mxCell - rectangle)

フロー図の各ステップは、mxCell要素で `rectangle` スタイルを指定することで表現します。

例:
```xml
<mxCell id="A1" value="プロセスステップ名" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f9f;strokeColor=#333;strokeWidth=2;" vertex="1" parent="subgraph1">
  <mxGeometry x="30" y="30" width="180" height="40" as="geometry"/>
</mxCell>
```
* `style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f9f;strokeColor=#333;strokeWidth=2;"`: ノードのスタイル (角丸、テキスト折り返し、HTML描画、塗りつぶし色、線色、線幅)
* `parent="subgraph1"`: ノードがサブグラフ `subgraph1` に属することを指定

#### 4. エッジ (mxCell - connector)

プロセスの流れは、mxCell要素で `connector` スタイルを指定することで表現します。

例:
```xml
<mxCell id="edge_A1_A2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="A1" target="A2">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```
* `style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"`: エッジのスタイル (直角線、角丸なし、直角ループ、自動調整、HTML描画)
* `edge="1"`: エッジであることを指定
* `source="A1"`: 接続元ノードのID
* `target="A2"`: 接続先ノードのID

#### 5. XML文書の作成

上記の手順を参考に、フロー図の各要素をmxCell要素としてXML文書に記述していきます。サブグラフ、ノード、エッジの順に記述すると、XML文書が構造化されて分かりやすくなります。

### draw.ioへのインポート

draw.ioでXML文書からフロー図を作成するには、以下の手順に従います。

1. **draw.ioを開く:** Webブラウザで [https://app.diagrams.net/](https://app.diagrams.net/) にアクセスし、draw.ioエディタを開きます。
2. **「ファイル」メニューを開く:** draw.ioエディタのメニューバーから「ファイル」をクリックします。
3. **「開く」 > 「XMLをインポート」を選択:** 「ファイル」メニューから「開く」を選択し、さらに「XMLをインポート」をクリックします。
4. **XMLコードを貼り付け:** テキストエリアが表示されるので、作成したXML文書のコード全体をコピーして貼り付けます。
5. **「インポート」をクリック:** XMLコードの貼り付け後、「インポート」ボタンをクリックします。

draw.ioがXML文書を解析し、フロー図がエディタ上に表示されます。

### XML文書の構造

XML文書は、フロー図の要素をmxCell要素で記述します。主要な要素は以下の通りです。

* **`<mxfile>`:** draw.io XMLファイルのルート要素です。
  * `host`: ホスト名 (通常は `app.diagrams.net`)
  * `modified`: 最終更新日時
  * `agent`: エージェント情報 (作成者など)
  * `etag`: ETag (バージョン管理用)
* **`<diagram>`:** ダイアグラムを定義する要素です。
  * `id`: ダイアグラムID
  * `name`: ダイアグラム名
* **`<mxGraphModel>`:** ダイアグラムのモデルを定義する要素です。
  * `dx`, `dy`: ダイアグラムの配置位置
  * `grid`, `gridSize`, `guides`, `tooltips`, `connect`, `arrows`, `fold`, `page`, `pageScale`, `pageWidth`, `pageHeight`, `math`, `shadow`: 描画設定
* **`<root>`:** mxCell要素のルート要素です。
  * **`<mxCell id="0"/>`:** ルートmxCell (固定)
  * **`<mxCell id="1" parent="0"/>`:** ドキュメントmxCell (固定)
  * **`<mxCell>` (サブグラフ):** サブグラフ (グループ) を定義します。
    * `id`: サブグラフID (例: `subgraph1`)
    * `value`: サブグラフ名 (例: `1. プロセスグループ名`)
    * `style="group"`: サブグラフスタイル
    * `vertex="1"`: 頂点属性
    * `parent="1"`: 親mxCell (ドキュメントmxCell)
    * `<mxGeometry>`: 位置とサイズ
  * **`<mxCell>` (ノード):** フロー図のノード (ステップ) を定義します。
    * `id`: ノードID (例: `A1`)
    * `value`: ノードテキスト (例: `プロセスステップ名`)
    * `style`: ノードスタイル (形状、色など)
    * `vertex="1"`: 頂点属性
    * `parent`: 親mxCell (サブグラフまたはドキュメントmxCell)
    * `<mxGeometry>`: 位置とサイズ
  * **`<mxCell>` (エッジ):** フロー図のエッジ (矢印) を定義します。
    * `id`: エッジID (例: `edge_A1_A2`)
    * `style`: エッジスタイル (線の種類、矢印の種類など)
    * `edge="1"`: エッジ属性
    * `parent="1"`: 親mxCell (ドキュメントmxCell)
    * `source`: 接続元ノードID
    * `target`: 接続先ノードID
    * `<mxGeometry>`: 形状

### XML文書の編集とレイアウト調整

XML文書を編集することで、フロー図をカスタマイズできます。特に、図形の配置に関する問題 (線の重なり、図形の貫通など) を解決するためには、以下の点に注意してXML文書を編集してください。

#### ノードの配置

* ノード同士が重ならないように、`<mxGeometry>` 要素の `x` 属性と `y` 属性を調整し、適切な間隔を確保してください。
* サブグラフ (`<mxCell style="group">`) を活用して、関連するノードをグループ化し、レイアウトを整理すると効果的です。サブグラフの `<mxGeometry>` 要素を調整することで、グループ全体の配置を制御できます。
* フロー図全体のバランスを考え、各サブグラフ、ノードの `<mxGeometry>` の `x`, `y` 属性を調整してください。特に、階層的なフロー図の場合は、上位階層のサブグラフの配置を先に決定し、その内部のノード配置を調整すると、レイアウトがまとまりやすくなります。

#### エッジのルーティング

* エッジがノードを貫通したり、不必要に交差したりしないように、エッジのスタイル (`<mxCell style="...">`) を調整してください。
  * `edgeStyle=orthogonalEdgeStyle`: 直角線を使用するスタイルで、線の重なりを減らし、フロー図を明確にします。
  * `rounded=0`: 角を丸めない設定は、直角的なフロー図に適しています。
  * `orthogonalLoop=1`: ループ状エッジを直角に描画。自己ループノードに有効です。
  * `jettySize=auto`: ノードとエッジ接続点のサイズを自動調整。
* エッジ同士が重ならないように、可能であればエッジの `mxGeometry` の `mxPoint` 要素を調整し、経路を変更してみてください。

#### mxGeometryの微調整

* 各mxCell要素の `<mxGeometry>` 要素を細かく調整し、ノードの位置、サイズ、エッジの形状などを精密に制御します。
* 特に、ノードの `<mxGeometry>` 要素の `x`, `y`, `width`, `height` 属性をフロー図全体のバランスを見て調整。
* エッジの `<mxGeometry>` 要素内の `mxPoint` 要素で、エッジの形状を細かく調整可能です。必要に応じて追加・編集してください。

#### レイアウトアルゴリズムの検討 (インポート後)

* XMLインポート後、draw.ioの自動レイアウト機能も活用できます。「レイアウト」メニューから、各種アルゴリズム (例: 「階層型レイアウト」) を試し、自動調整を検討してください。
* XML文書でレイアウトを完全に制御したい場合は、自動レイアウトに頼らず、`<mxGeometry>` 要素を手動調整します。

#### グリッドとガイドの意識

* draw.ioエディタのグリッド線とガイド線 ([表示] > [グリッド]、[表示] > [ガイド]) を利用すると、ノードやエッジを整列しやすくなります。
* XML文書作成時もグリッドとガイドを意識し、座標を揃えると、整ったレイアウトのフロー図になります。

### エッジスタイルの調整例

エッジのスタイル調整で、線の重なりを軽減できます。直角線スタイル (`orthogonalEdgeStyle`) を適用するには、エッジの `<mxCell>` 要素の `style` 属性に `edgeStyle=orthogonalEdgeStyle` を追加します。

```xml
<mxCell id="edge_A1_A2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="A1" target="A2">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

上記の例では、`rounded=0` (角を丸めない)、`orthogonalLoop=1` (直角ループ)、`jettySize=auto` (接続点サイズ自動調整) も追加。これらのスタイル組み合わせで、より明確なフロー図作成が可能です。

### 編集後のインポート

XML文書編集後、再度draw.ioへインポートし、変更を反映します。「ファイル」 > 「開く」 > 「XMLをインポート」から、編集後のXMLコードをインポートしてください。

### 高度なスタイリング

より高度なスタイリングを行いたい場合は、以下のような属性を活用できます：

#### ノードのスタイル属性

* `fillColor`: 塗りつぶし色（例: `#f9f7ed`, `#ff0000`)
* `strokeColor`: 線の色
* `strokeWidth`: 線の太さ
* `fontColor`: テキストの色
* `fontSize`: フォントサイズ
* `fontStyle`: フォントスタイル（例: `0`=通常, `1`=太字, `2`=斜体, `3`=太字+斜体）
* `align`: テキスト水平位置（例: `left`, `center`, `right`）
* `verticalAlign`: テキスト垂直位置（例: `top`, `middle`, `bottom`）
* `dashed`: 破線（例: `1`=有効）
* `dashPattern`: 破線パターン（例: `3 3`）
* `shadow`: 影（例: `1`=有効）

#### エッジのスタイル属性

* `strokeColor`: 線の色
* `strokeWidth`: 線の太さ
* `dashed`: 破線（例: `1`=有効）
* `dashPattern`: 破線パターン（例: `3 3`）
* `startArrow`: 始点の矢印（例: `none`, `classic`, `open`, `diamond`）
* `endArrow`: 終点の矢印（例: `none`, `classic`, `open`, `diamond`）
* `startSize`: 始点矢印のサイズ
* `endSize`: 終点矢印のサイズ
* `curved`: 曲線（例: `1`=有効）

これらの属性を組み合わせることで、より表現力豊かなフロー図を作成できます。

### まとめ

draw.ioのXML文書を使用すると、GUI操作なしでフロー図を定義できます。この方法は、特に複雑なフロー図や、同様のパターンを持つ複数のフロー図を効率的に作成する場合に役立ちます。また、バージョン管理システムとの統合も容易になります。

このガイドを参考に、XML文書を編集し、draw.ioで独自のフロー図を作成してみてください。
