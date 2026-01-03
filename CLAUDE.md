# CLAUDE.md

このファイルはClaude Codeがこのリポジトリで作業する際のガイドです。

## プロジェクト概要

PDFファイルをDify RAG（Retrieval-Augmented Generation）用のMarkdownに変換するツール。

### 主な機能

- PDF→Markdown変換（pymupdf4llm使用）
- 1 PDF = 1 MDファイルの1対1変換
- YAMLフロントマター自動付与（タグ、ソース情報）
- PDFアーティファクト（ページ番号、ヘッダー、フッター等）の自動除去
- セクション番号に基づくMarkdownヘッダー自動生成
- 画像抽出・保存

### 用途

- Difyナレッジベースへの取り込み用にPDFを構造化Markdownに変換
- 技術書籍・マニュアルのRAG対応フォーマット化

## ディレクトリ構造

```
pdf-converter-4-dify/
├── pdf-converter-4-dify.py  # メインスクリプト
├── common.py                # 共通関数（設定、ユーティリティ）
├── input_pdf/               # 入力PDFファイル配置先
│   └── .gitkeep
├── output_md/               # 変換後Markdown出力先
│   └── .gitkeep
├── requirements.txt         # Python依存関係
├── run_background.ps1       # バックグラウンド実行用スクリプト
├── .gitignore
├── CLAUDE.md                # 本ファイル
└── README.md
```

## 技術スタック

| 技術 | バージョン | 用途 |
|------|-----------|------|
| Python | 3.10+ | メイン言語 |
| pymupdf4llm | 0.0.5+ | PDF→Markdown変換 |
| PyMuPDF | 1.23.0+ | PDF解析エンジン |
| tkinter | 標準 | GUIダイアログ |

### 主要モジュール

**pdf-converter-4-dify.py**
- `convert_pdf_to_md()`: PDF→Markdown変換
- `save_with_yaml()`: YAMLフロントマター付きで保存
- `main()`: CLI引数処理、バッチ変換

**common.py**
- `setup_logging()`: ロギング設定
- `estimate_time()`: 残り時間推定
- `remove_pdf_artifacts()`: PDFアーティファクト除去
- `add_headers_by_pattern()`: セクション番号からヘッダー生成
- `get_yaml_header()`: YAMLフロントマター生成

## 現在の開発状況

### 完了済み

- 基本的なPDF→Markdown変換
- YAMLフロントマター生成
- PDFアーティファクト除去（ページ番号、著作権表示等）
- セクション番号パターンからのヘッダー自動生成
- 画像抽出・保存
- バックグラウンドモード対応
- 進捗推定・ロギング

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
python pdf-converter-4-dify.py input.pdf -o output_md

# ディレクトリ一括変換（GUI）
python pdf-converter-4-dify.py input_pdf/ -o output_md

# バックグラウンドモード（GUIなし）
python pdf-converter-4-dify.py input_pdf/ --background -b "BookTitle" -t "tag1,tag2"

# PowerShellでバックグラウンド実行
.\run_background.ps1
```

### 出力形式

変換後のMarkdownファイルには以下のYAMLフロントマターが付与されます：

```yaml
---
tags:
  - tag1
  - tag2
source: filename.pdf
title: filename
---
```

### ログ

- 変換ログは `conversion.log` に出力
- 進捗状況、エラー、推定完了時間を記録
