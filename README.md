# pdf-converter-4-dify

PDFファイルをDify RAG用のMarkdownに変換するツール

## 機能

- PDFをMarkdownに変換（pymupdf4llm使用）
- 1つのPDFから1つのMDファイルを出力（1対1変換）
- YAMLフロントマター自動付与（タグ、ソース情報）
- PDFアーティファクト（ページ番号、ヘッダー等）の自動除去

## 必要環境

- Python 3.10以上
- pymupdf4llm
- PyMuPDF (fitz)

## インストール

```
pip install pymupdf4llm pymupdf
```

## 使用方法

```
python pdf-converter-4-dify.py input.pdf -o output_md
```

実行開始時に2つのGUIポップアップが表示されます：
1. **本のタイトル入力** - 出力ファイル名の先頭に付与されるプレフィックス（例: SAP Analytics Cloud）
2. **タグ入力** - すべてのPDFに一括適用されるタグ（例: SAC, Analytics, BW）

### 出力ファイル名の例

- 入力: `007_1.2 SAP's Data and Analytics Strategy.pdf`
- 本のタイトル: `SAP Analytics Cloud`
- 出力: `SAP Analytics Cloud_007_1.2 SAP's Data and Analytics Strategy.md`

### オプション

- `-o`, `--output`: 出力ディレクトリ（デフォルト: output_md）
- `-t`, `--tags`: タグをコマンドラインで指定（GUIをスキップ）
- `-b`, `--book`: 本のタイトルをコマンドラインで指定（GUIをスキップ）
- `--background`: バックグラウンドモード（GUIなし）

### バックグラウンドモードでの使用例

```
python pdf-converter-4-dify.py input_pdf -o output_md --background -b "SAP Analytics Cloud" -t "SAC,Analytics"
```

## ディレクトリ構成

```
pdf-converter-4-dify/
├── pdf-converter-4-dify.py  # メインスクリプト
├── common.py                # 共通関数
├── input_pdf/               # 入力PDF配置
├── output_md/               # Markdown出力先
└── README.md
```

## 関連ツール

- pdf-split - 大きなPDFを章単位で分割（本ツールの前段階で使用）

## ライセンス

個人利用（非公開）
