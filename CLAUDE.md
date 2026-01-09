# CLAUDE.md

このファイルはClaude Codeがこのリポジトリで作業する際のガイドです。

## プロジェクト概要

PDFファイルをMarkdownに変換するツール。

### 主な機能

- PDF→Markdown変換（pymupdf4llm使用）
- 1 PDF = 1 MDファイルの1対1変換
- PDFアーティファクト（ページ番号、ヘッダー、フッター等）の自動除去
- セクション番号に基づくMarkdownヘッダー自動生成
- 画像抽出・保存
- 既存のYAMLメタデータファイル（.yaml）があれば引き継ぎ

### 用途

- PDFを構造化Markdownに変換
- 技術書籍・マニュアルのMarkdown化

## ディレクトリ構造

```
pdf-2-md/
├── pdf-2-md.py              # メインスクリプト
├── common.py                # 共通関数
├── requirements.txt         # 依存パッケージ
├── input_pdf/               # 入力PDF配置
└── output_md/               # Markdown出力先
```

## 技術スタック

| 技術 | バージョン | 用途 |
|------|-----------|------|
| Python | 3.10+ | メイン言語 |
| pymupdf4llm | 0.0.5+ | PDF→Markdown変換 |
| PyMuPDF | 1.23.0+ | PDF解析エンジン |

### 主要モジュール

**pdf-2-md.py**
- `convert_pdf_to_md()`: PDF→Markdown変換
- `load_existing_yaml()`: 既存のYAMLメタデータファイルを読み込み
- `save_md()`: Markdownファイルを保存
- `main()`: CLI引数処理、バッチ変換

**common.py**
- `setup_logging()`: ロギング設定
- `estimate_time()`: 残り時間推定
- `remove_pdf_artifacts()`: PDFアーティファクト除去
- `add_headers_by_pattern()`: セクション番号からヘッダー生成
- `clean_filename()`: ファイル名のサニタイズ

## 現在の開発状況

### 完了済み

- 基本的なPDF→Markdown変換
- PDFアーティファクト除去（ページ番号、著作権表示等）
- セクション番号パターンからのヘッダー自動生成
- 画像抽出・保存
- 進捗推定・ロギング
- 既存YAMLメタデータファイルの引き継ぎ

### 既知の課題

- 複雑なレイアウトのPDFでは変換精度が低下する場合あり
- 日本語PDFの一部で文字化けの可能性

## 今後の予定

特に計画された機能追加はありません。必要に応じて機能拡張を検討。

## 開発時の注意事項

### コマンド

```bash
# 依存関係インストール
pip install pymupdf4llm pymupdf

# 単一PDF変換
python pdf-2-md.py input.pdf -o output_md

# ディレクトリ一括変換
python pdf-2-md.py input_pdf/ -o output_md
```

### YAMLメタデータの引き継ぎ

PDFと同名の `.yaml` ファイルが存在する場合、その内容が出力MDの先頭に付与されます。

例:
- 入力: `document.pdf`, `document.yaml`
- 出力: `document.md`（先頭にdocument.yamlの内容が付与）

### ログ

- 変換ログは `conversion.log` に出力
- 進捗状況、エラー、推定完了時間を記録
