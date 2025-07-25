# 2025年07月12日 サイバーセキュリティニュースまとめ

## 主要ポイント

*   米当局が「Citrix Bleed 2」の悪用について注意喚起を行いました。
*   新興プラスチックスがランサムウェア攻撃を受け、データ暗号化被害が発生しました。
*   古野電気のサーバが不正アクセスを受け、一部の情報が外部に詐取された可能性があります。

## 脆弱性情報

### 米当局、「Citrix Bleed 2」の悪用に注意喚起

2025年7月10日、米サイバーセキュリティインフラストラクチャセキュリティ庁（CISA）は、「悪用が確認された脆弱性カタログ（KEV）」を更新し、別名「Citrix Bleed 2」とも呼ばれる「CVE-2025-5777」を追加しました。この脆弱性は、入力検証の不備により、域外メモリが読み取られ、トークンを窃取されるおそれがあるものです。CISAは、同脆弱性の悪用が確認されているとして、米国内の行政機関に対し、対策を促し、広く注意を呼びかけています。

出典: [Security NEXT](https://www.security-next.com/172264)

## 国内インシデント事例

### 新興プラスチックスにランサムウェア攻撃、データ暗号化被害が発生

新興プラスチックス株式会社は2025年7月1日、同社へのサイバー攻撃によるシステム障害について発表しました。この攻撃により、データが暗号化される被害が発生しています。

出典: [ScanNetSecurity](https://scan.netsecurity.ne.jp/article/2025/07/11/52607.html)

### 古野電気のサーバに不正アクセス、一部の情報が外部に詐取された可能性

古野電気株式会社は2025年6月30日、同社サーバへの不正アクセスがあったことを発表しました。この不正アクセスにより、一部の情報が外部に詐取された可能性があるとのことです。

出典: [ScanNetSecurity](https://scan.netsecurity.ne.jp/article/2025/07/11/52606.html)

# 2025年07月12日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. 米当局、「Citrix Bleed 2」の悪用に注意喚起

米国サイバーセキュリティインフラストラクチャセキュリティ庁（CISA）は、2025年7月10日に「悪用が確認された脆弱性カタログ（KEV）」を更新し、新たに「Citrix Bleed 2」として知られる「CVE-2025-5777」を追加しました。この脆弱性は、NetScaler ADC（旧Citrix ADC）およびNetScaler Gateway（旧Citrix Gateway）に影響を与えます。入力検証の不備が原因で、攻撃者が域外メモリから情報を読み取り、認証トークンを窃取する可能性があります。CISAは、この脆弱性が実際に悪用されていることを確認しており、米国内の行政機関に対して早急な対策を講じるよう強く勧告しています。この脆弱性は、特にリモートアクセス環境において、認証情報の漏洩や不正アクセスにつながる可能性があるため、企業や組織は速やかにパッチを適用し、セキュリティ対策を強化する必要があります。

### 2. 新興プラスチックスにランサムウェア攻撃、データ暗号化被害が発生

新興プラスチックス株式会社は、2025年7月1日に同社システムへのサイバー攻撃が発生し、ランサムウェアによるデータ暗号化被害を受けたことを公表しました。この攻撃により、業務システムの一部が停止し、事業活動に影響が出ています。同社は現在、外部の専門機関と連携し、被害状況の調査と復旧作業を進めています。ランサムウェア攻撃は、企業にとって深刻な脅威であり、データのバックアップ、多要素認証の導入、従業員へのセキュリティ教育など、多層的な防御策が不可欠です。

### 3. 古野電気のサーバに不正アクセス、一部の情報が外部に詐取された可能性

古野電気株式会社は、2025年6月30日に同社サーバへの不正アクセスが確認されたと発表しました。調査の結果、この不正アクセスにより、一部の情報が外部に詐取された可能性があることが判明しています。同社は、情報漏洩の範囲や内容について詳細な調査を進めるとともに、再発防止策を講じています。不正アクセスは、企業の機密情報や顧客情報の漏洩につながる重大なインシデントであり、定期的なセキュリティ監査、脆弱性診断、アクセスログの監視など、継続的なセキュリティ強化が求められます。

## 深掘り

### ランサムウェア攻撃の現状と対策

ランサムウェア攻撃は、近年最も深刻なサイバー脅威の一つとして認識されています。攻撃者は、企業のシステムに侵入し、データを暗号化して身代金を要求します。身代金を支払ってもデータが復旧しないケースや、復旧しても情報が公開される「二重恐喝」の被害も増加しています。

#### 攻撃手法の多様化

ランサムウェア攻撃は、標的型攻撃、サプライチェーン攻撃、脆弱性悪用など、多様な手法で実行されます。特に、VPN機器やリモートデスクトッププロトコル（RDP）の脆弱性を悪用した侵入が増加傾向にあります。また、フィッシングメールや悪意のあるウェブサイトを通じてマルウェアを感染させる手口も依然として多く見られます。

#### 対策の重要性

ランサムウェア攻撃から企業を守るためには、以下の対策が重要です。

*   **データのバックアップ:** 定期的にデータをバックアップし、オフラインで保管することで、万が一の際にデータを復旧できるようにします。
*   **多要素認証の導入:** システムへのアクセスに多要素認証を導入することで、不正アクセスによる被害を軽減します。
*   **脆弱性管理:** OSやアプリケーションの脆弱性を常に最新の状態に保ち、パッチを迅速に適用します。
*   **セキュリティ教育:** 従業員に対して、フィッシング詐欺や不審なメールに対する注意喚起など、セキュリティ意識を高める教育を定期的に実施します。
*   **インシデントレスポンス計画:** サイバー攻撃が発生した場合に備え、インシデントレスポンス計画を策定し、定期的に訓練を行います。

### 関連知識

#### 用語解説

*   **Citrix Bleed 2 (CVE-2025-5777):** NetScaler ADCおよびNetScaler Gatewayに存在する脆弱性。入力検証の不備により、域外メモリから情報が読み取られ、認証トークンが窃取される可能性がある。
*   **ランサムウェア:** コンピュータシステムへのアクセスを制限したり、ファイルを暗号化したりすることで、身代金（ランサム）を要求するマルウェアの一種。
*   **不正アクセス:** 許可されていない者がコンピュータシステムやネットワークに侵入すること。情報漏洩やデータ改ざんなどの被害につながる。

#### 今後の展望

サイバー攻撃は今後も巧妙化・多様化していくと予想されます。特に、AIを活用した攻撃や、IoTデバイスを標的とした攻撃が増加する可能性があります。企業や個人は、常に最新の脅威情報を収集し、セキュリティ対策を継続的に強化していく必要があります。また、政府やセキュリティ機関との連携を強化し、情報共有や共同での対策を進めることも重要です。

## 結論

本日のサイバーセキュリティニュースでは、国際的な脆弱性情報と国内のインシデント事例が報告されました。特に、Citrix製品の脆弱性悪用や、ランサムウェア攻撃、不正アクセスによる情報漏洩は、企業にとって喫緊の課題であることを示しています。これらの脅威から身を守るためには、技術的な対策だけでなく、従業員のセキュリティ意識向上や、インシデント発生時の迅速な対応計画が不可欠です。常に最新の情報を入手し、多層的な防御策を講じることで、サイバーリスクを低減していくことが求められます。

## 主要引用

*   Security NEXT: [https://www.security-next.com/](https://www.security-next.com/)
*   ScanNetSecurity: [https://scan.netsecurity.ne.jp/](https://scan.netsecurity.ne.jp/)

