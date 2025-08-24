# 2025年08月24日 サイバーセキュリティニュースまとめ

## 主要ポイント

*   日本国内では中小企業向けセキュリティ対策の強化とVPN利用規制の動きが注目されています。
*   国際的には、既知の脆弱性を悪用したサイバー犯罪、国家支援型ハッカーによるクラウド・通信インフラへのスパイ活動、そして国際的なサイバー犯罪組織の摘発が報告されています。
*   マルウェアの新たな配布手法や、パスワードマネージャーの脆弱性、ゼロデイ攻撃への対応も重要なトピックです。

## 国内ニュース

### シスコとNTT東日本、中小企業向けITサービスを共同検討へ

シスコとNTT東日本が、中小企業向けに大企業基準のセキュリティ対策を提供するITサービスの共同検討を開始しました。このサービスは、24時間365日の自動監視と最新の脅威への対応を通じて、中小企業でも高度なセキュリティ水準を実現することを目指しています。これにより、中小企業が大企業との取引条件に適合できるようなセキュリティ環境の構築が期待されます。

### 英国におけるVPN利用規制の動き

英国では、規制回避のためにVPN利用者が急増していることを受け、VPN利用に年齢制限を設ける構想が浮上しています。これは、インターネットの匿名性を悪用したサイバー犯罪や不適切なコンテンツへのアクセスを制限するための動きと見られますが、プライバシー保護とのバランスが課題となる可能性があります。

## 海外ニュース

### 既知の脆弱性を悪用したサイバー犯罪の拡大

GeoServerの脆弱性（CVE-2024-36401、CVSSスコア9.8）が悪用され、RedisサーバーがIoTボットネット、居住プロキシ、仮想通貨マイニングインフラとして悪用されるキャンペーンが確認されています。これは、既知の脆弱性がサイバー犯罪者によって迅速に悪用され、多様な悪意ある活動に利用されている現状を示しています。

### 中国系ハッカーによるクラウド・通信インフラへのスパイ活動

中国系のサイバースパイグループ「Murky Panda」（旧Hafnium）が、クラウドの信頼関係を悪用して企業ネットワークに侵入していることが報告されました。このグループは、N-dayおよびゼロデイ脆弱性を迅速に悪用する能力を持ち、政府機関、テクノロジー企業、学術機関などを標的としています。これは、国家支援型ハッカーによる高度なサイバースパイ活動が継続していることを示唆しています。

### 国際的なサイバー犯罪組織の摘発

インターポールは、アフリカ18カ国で実施された「Operation Serengeti」の第2フェーズにおいて、1,209人のサイバー犯罪者を逮捕し、9,740万ドルを回収、11,432の悪意あるインフラを解体したと発表しました。この作戦は、ランサムウェア、オンライン詐欺、ビジネスメール詐欺（BEC）などの重大なサイバー犯罪に対処するための国際的な取り組みであり、サイバー犯罪対策における国際協力の重要性を示しています。

### 新たなマルウェア配布手法とパスワードマネージャーの脆弱性

「ClickFix」というソーシャルエンジニアリング手法と偽のCAPTCHAページを悪用して、多機能バックドア「CORNFLAKE.V3」が展開されていることが明らかになりました。また、新しいマルウェアローダー「QuirkyLoader」が、Agent Tesla、AsyncRAT、Snake Keyloggerなどの情報窃取マルウェアを電子メールスパムキャンペーンを通じて配布しています。さらに、パスワードマネージャーがクリックジャッキング攻撃に対して脆弱であるという研究結果も報告されており、ユーザーはこれらの脅威に対して警戒を強める必要があります。

### Appleによるゼロデイ脆弱性への対応

Appleは、標的型攻撃で悪用されたゼロデイ脆弱性に対処するため、iOSおよびmacOSのアップデートをリリースしました。これは、ベンダーが積極的に脆弱性に対応し、ユーザーのセキュリティを保護するための重要な取り組みです。

# 2025年08月24日 サイバーセキュリティニュース詳細

## ニュース紹介

### 1. Exchange Serverの脆弱性に関する最新の対策ガイドを更新

米国サイバーセキュリティ・インフラストラクチャセキュリティ庁（CISA）とMicrosoftは、Microsoft Exchange Serverに存在する重大な脆弱性「CVE-2025-53786」への対策をまとめたガイドラインを更新しました。この脆弱性は、オンプレミス版で管理者権限を持つ攻撃者が、脆弱な状態にあるハイブリッド参加の設定を悪用することで権限をさらに昇格できるというものです。組織は自社のシステムを直ちに確認し、対策を講じる必要があります。

### 2. OTでのセキュリティリスクを甘く見るな

産業向けサイバーセキュリティサービスを提供するDragosとMarsh McLennanが発表した報告書によると、OT（Operational Technology）環境を混乱させる壊滅的なサイバー攻撃が発生した場合、世界全体での経済的損失は年間3300億ドル近くに達する可能性があると指摘しています。この推定損失は、事業中断による損失のみで1720億ドルを超える想定で、世界的なサプライチェーンへの影響も考慮されています。企業はOT環境のセキュリティリスクを過小評価せず、対策を強化する必要があります。

### 3. Malicious Go ModuleがSSHブルートフォースツールを装い認証情報を窃取

サイバーセキュリティ研究者らは、SSHのブルートフォースツールを装いながら、実際には認証情報を密かに窃取してTelegramボットに送信する悪意のあるGoモジュールを発見しました。この「golang-random-ip-ssh-bruteforce」と名付けられたモジュールは、GitHubアカウント「IllDieAnyway (G3TT)」に関連付けられていましたが、現在はアクセスできません。しかし、pkg.go.devでは引き続き利用可能です。このモジュールは、ランダムなIPv4アドレスで公開されているSSHサービスをスキャンし、埋め込まれたユーザー名とパスワードのリストを使用してブルートフォース攻撃を試み、成功した認証情報を攻撃者に窃取します。

## 深掘り

### 脆弱性管理の重要性

本日のニュースでは、既知の脆弱性がサイバー犯罪に悪用される事例が複数報告されています。GeoServerの脆弱性悪用や、中国系ハッカーによるN-day/ゼロデイ脆弱性の悪用は、組織が脆弱性管理を徹底することの重要性を浮き彫りにしています。脆弱性管理は、システムやソフトウェアの脆弱性を特定し、評価し、修正するプロセスです。これには、定期的な脆弱性スキャン、パッチ管理、そしてセキュリティアップデートの迅速な適用が含まれます。

#### パッチ管理の遅延がもたらすリスク

パッチ管理の遅延は、サイバー攻撃者にとって格好の標的となります。ベンダーが脆弱性に対するパッチをリリースしても、組織がそれを適用しない場合、その脆弱性は未修正のまま残り、攻撃者に悪用されるリスクが高まります。特に、インターネットに公開されているシステムや、広く利用されているソフトウェアの脆弱性は、攻撃者にとって優先度の高いターゲットとなります。

#### ゼロデイ脆弱性への対応

ゼロデイ脆弱性は、ベンダーが認識しておらず、パッチが存在しない脆弱性です。Appleがゼロデイ脆弱性に対応した事例のように、ゼロデイ攻撃は非常に危険であり、迅速な検出と対応が求められます。組織は、高度な脅威検出システムや、セキュリティ専門家による監視体制を強化することで、ゼロデイ攻撃のリスクを軽減する必要があります。

### サイバーセキュリティ対策における自動化の進展

ペネトレーションテスト（ペンテスト）の分野では、従来の静的なPDFレポートではなく、自動化されたプラットフォーム（PlexTracなど）によるリアルタイムな結果提供が進んでいます。これは、脅威の進化が速い現代において、セキュリティ対策の効率化と迅速化が求められていることを示しています。自動化は、脆弱性の特定、脅威の検出、インシデント対応など、サイバーセキュリティの様々な側面で活用され、セキュリティ運用（SecOps）の負担軽減と効果向上に貢献します。

#### セキュリティ運用の効率化

セキュリティ運用の自動化は、手動での作業に比べて、より迅速かつ正確にタスクを実行することを可能にします。例えば、脆弱性スキャンの自動化、脅威インテリジェンスの自動収集、インシデント対応の自動化などが挙げられます。これにより、セキュリティチームは、より戦略的な業務に集中できるようになります。

#### AIと機械学習の活用

サイバーセキュリティ分野では、AI（人工知能）と機械学習（ML）の活用も進んでいます。AI/MLは、大量のデータを分析し、異常なパターンや未知の脅威を検出する能力に優れています。これにより、人間では見逃しがちな脅威を早期に発見し、対応することが可能になります。また、AI/MLは、セキュリティ運用の自動化にも貢献し、脅威の分析や対応の迅速化を支援します。

## 結論

2025年8月24日のサイバーセキュリティニュースは、国内外で多様な脅威が継続していることを示しています。特に、既知の脆弱性の悪用、国家支援型ハッカーによるスパイ活動、そして新たなマルウェア配布手法の出現は、組織にとって継続的な警戒と対策の強化が不可欠であることを強調しています。中小企業から大企業、さらにはOT環境に至るまで、あらゆる組織がサイバーセキュリティ対策を強化し、最新の脅威情報に基づいた迅速な対応が求められます。脆弱性管理の徹底、パッチ適用の迅速化、そして自動化やAI/MLを活用したセキュリティ運用の効率化が、今後のサイバー脅威に対抗するための鍵となるでしょう。

## 主要引用

*   [2025年8月23日 サイバーセキュリティニュースまとめ - note](https://note.com/clever_chives813/n/n43e199d16baf)
*   [Exchange Serverの脆弱性に関する最新の対策ガイドを更新 CISAとMicrosoft - ITmedia エンタープライズ](https://www.itmedia.co.jp/enterprise/articles/2508/24/news004.html)
*   [OTでのセキュリティリスクを甘く見るな 被害額が3000億ドルに達する恐れも - ITmedia エンタープライズ](https://www.itmedia.co.jp/enterprise/articles/2508/24/news003.html)
*   [Malicious Go Module Poses as SSH Brute-Force Tool, Steals Credentials via Telegram Bot - The Hacker News](https://thehackernews.com/2025/08/malicious-go-module-poses-as-ssh-brute.html)
*   [Cybercriminals Deploy CORNFLAKE.V3 Backdoor via ClickFix Tactic and Fake CAPTCHA Pages - The Hacker News](https://thehackernews.com/2025/08/cybercriminals-deploy-cornflakev3.html)
*   [Apple Patches New iOS & macOS Zero-Day Vulnerability Exploited in Targeted Attacks - The Hacker News](https://thehackernews.com/2025/08/apple-patches-new-ios-macos-zero-day.html)
*   [Massive anti-cybercrime operation leads to over 1,200 arrests in Africa - BleepingComputer](https://www.bleepingcomputer.com/news/security/massive-anti-cybercrime-operation-leads-to-over-1-200-arrests-in-africa/)
*   [Dev gets 4 years for creating kill switch on ex-employer's systems - BleepingComputer](https://www.bleepingcomputer.com/news/security/dev-gets-4-years-for-creating-kill-switch-on-ex-employers-systems/)
*   [New Android malware poses as antivirus from Russian intelligence agency - BleepingComputer](https://www.bleepingcomputer.com/news/security/new-android-malware-poses-as-antivirus-from-russian-intelligence-agency/)
*   [Murky Panda hackers exploit cloud trust to hack downstream customers - BleepingComputer](https://www.bleepingcomputer.com/news/security/murky-panda-hackers-exploit-cloud-trust-to-hack-downstream-customers/)
*   [FTC warns tech giants not to bow to foreign pressure on encryption - BleepingComputer](https://www.bleepingcomputer.com/news/security/ftc-warns-tech-giants-not-to-bow-to-foreign-pressure-on-encryption/)
*   [Microsoft working on fix for ongoing Outlook email issues - BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-working-on-fix-for-ongoing-outlook-email-issues/)
*   [The Hacker News | #1 Trusted Source for Cybersecurity News](https://thehackernews.com/)
*   [ScanNetSecurity](https://scan.netsecurity.ne.jp/article/)
*   [INTERNET Watch](https://internet.watch.impress.co.jp/)
*   [Security Affairs](https://securityaffairs.com/)
*   [Cyware](https://social.cyware.com/cyber-security-news-articles)
*   [Yahoo!ニュース](https://news.yahoo.co.jp/articles/4ea0bf76f6a1834d715baa454abf18dd48a8fa02?page=2)
*   [産経ニュース](https://www.sankei.com/article/20250824-4RQAJLFTFNNXBDP4KYKISUQNKU/)
*   [マイナビニュース](https://news.mynavi.jp/techplus/article/20250824-3412875/)
*   [XenoSpectrum](https://xenospectrum.com/clickfix-social-engineering-attack-surge/)
*   [ITmedia Enterprise Facebook](https://www.facebook.com/ITmediaEnterprise/posts/dragos%E3%81%AE%E5%A0%B1%E5%91%8A%E6%9B%B8%E3%81%AB%E3%81%8A%E3%81%84%E3%81%A6ot%E7%92%B0%E5%A2%83%E3%82%92%E6%B7%B7%E4%B9%B1%E3%81%9B%E3%82%8B%E5%A3%8A%E6%BB%85%E7%9A%84%E3%81%AA%E3%82%B5%E3%82%A4%E3%83%90%E3%83%BC%E6%94%BB%E6%92%83%E3%81%8C%E7%99%BA%E7%94%9F%E3%81%97%E3%81%9F%E5%A0%B4%E5%90%88%E4%B8%96%E7%95%8C%E5%85%A8%E4%BD%93%E3%81%A7%E3%81%AE%E7%B5%8C%E6%B8%88%E7%9A%84%E6%90%8D%E5%A4%B1%E3%81%AF%E5%B9%B4%E9%96%933300%E5%84%84%E3%83%89/1225648009577272/)


