# pdf-2-md

PDFファイルをMarkdownに変換するツール

## 機能

- PDFをMarkdownに変換（pymupdf4llm使用）
- 1つのPDFから1つのMDファイルを出力（1対1変換）
- PDFアーティファクト（ページ番号、ヘッダー等）の自動除去
- 既存のYAMLメタデータファイル（.yaml）があれば引き継ぎ

## 必要環境

- Python 3.10以上
- pymupdf4llm
- PyMuPDF (fitz)

## インストール

```
pip install pymupdf4llm pymupdf
```

## 使用方法

```bash
# 単一PDF変換
python pdf-2-md.py input.pdf -o output_md

# ディレクトリ一括変換
python pdf-2-md.py input_pdf/ -o output_md

# input_pdf/ ディレクトリのPDFを一括変換（デフォルト）
python pdf-2-md.py
```

### オプション

- `-o`, `--output`: 出力ディレクトリ（デフォルト: output_md）

### YAMLメタデータの引き継ぎ

PDFと同名の `.yaml` ファイルが存在する場合、その内容が出力MDの先頭に付与されます。

例:
- 入力: `document.pdf`, `document.yaml`
- 出力: `document.md`（先頭にdocument.yamlの内容が付与）

## ディレクトリ構成

```
pdf-2-md/
├── pdf-2-md.py              # メインスクリプト
├── common.py                # 共通関数
├── requirements.txt         # 依存パッケージ
├── input_pdf/               # 入力PDF配置
└── output_md/               # Markdown出力先
```

## 関連ツール

- pdf-split - 大きなPDFを章単位で分割（本ツールの前段階で使用）

## ライセンス

個人利用（非公開）
