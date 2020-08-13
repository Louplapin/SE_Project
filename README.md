# 注意点
このリポジトリは、長期的課題提出締め切りから、約半年間のみパブリックリポジトリとする。
それ以降は、プライベートとリポジトリとして扱う。

# 実行環境
- Python3.7.0以降
- Tkinter

# 目標性能
使用するフォントはSerif系の標準体(plain)で12ポイントとする。ノードやリーフの整列間隔は横方向が25ピクセルで縦方向が2ピクセルである。ウィンドウの中に表示しきれない大きな木の場合もあるので、マウスのドラッグ操作より軽快にスクロールできること。また、木のノードやリーフをマウスでクリックすることにより標準出力へ当該の名前を書き出す。

# 制限事項
Java・Python・Smalltalkの標準ライブラリ（必要であれば拡張ライブラリ）を使用して開発を行う。Macintoshシリーズをターゲットにしているが、実装に用いるJava・Python・Smalltalkはプラットフォーム非依存性を仮想マシンによって実現しているプログラミング言語である。したがって、開発したアプリケーションはLinuxやWindowsなどでも動作することが望ましい。

# ファイル構成
```
SE_Project
├── src (プログラムのソースコードディレクトリ)
│  ├── main.py
│  └── DataControl.py
│  └── input.py
│  └── lineClass.py
│  └── treeClass.py
│  └── view.py
├── resource (読み取りテキストファイル保管ディレクトリ)
│  ├── forest.txt
│  └── semilattice.txt
│  └── tree.txt
├── program_documentation (プログラムドキュメントディレクトリ)
│  ├── main.html
│  └── DataControl.html
│  └── input.html
│  └── lineClass.html
│  └── treeClass.html
│  └── view.html
├── project_document (プロジェクトドキュメントディレクトリ)
│  ├── index.html
│  ├── img
│  │  ├── basicdesign.jpg
│  │  ├── DataConrol.jpg
│  │  ├── input.jpg
│  │  ├── layer.jpg
│  │  ├── lineClass.jpg
│  │  ├── macbook-air.jpg
│  │  ├── main.jpg
│  │  ├── plan.jpg
│  │  ├── real.jpg
│  │  ├── sequence.jpg
│  │  ├── treeClass.jpg
│  │  └── view.jpg
│  ├── BasicDesign
│  │  └── index.html
│  ├── DetailDesign
│  │  └── index.html
│  ├── DevelopmentPlan
│  │  └── index.html
│  ├── DevelopmentResult
│  │  └── index.html
│  ├── Manual
│  │  └── index.html
│  ├── Program
│  │  └── index.html
│  ├── Requirement
│  │  └── index.html
│  ├── TestResukt
│  │  └── index.html
│  ├── TestSpecification
│  │  └── index.html
└──README.md
```

# チュートリアル
## Python
- [公式ドキュメント](https://docs.python.org/ja/3.7/)
## Tkinker
- [公式ドキュメント](https://docs.python.org/ja/3/library/tkinter.html)
- [公式チュートリアル](https://tkdocs.com/tutorial/index.html)
- [資料](https://nnahito.gitbooks.io/tkinter/content)
## その他
- [MrkDown](https://qiita.com/kamorits/items/6f342da395ad57468ae3)