# PDF to Dify-ready Markdown Converter

PDFファイルをDifyナレッジベース用に最適化されたMarkdownに変換するツール。

## 機能

- **PDF→Markdown変換**: pymupdf4llmを使用した高品質なMarkdown変換
- **構造化分割**: チャプター・セクション単位で自動分割（14MB以下に収まるよう調整）
- **YAMLフロントマター**: タグ、ソース、チャプター情報を含むメタデータ自動生成
- **画像抽出**: PDFからの画像を自動抽出し、Markdownにリンク
- **進捗管理**: 中断時の再開機能

## インストール

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本的な使い方

```bash
# input_pdf/ フォルダ内の全PDFを処理
python pdf-converter-4-dify.py

# 単一のPDFファイルを処理
python pdf-converter-4-dify.py document.pdf

# タグを指定
python pdf-converter-4-dify.py -t "SAC,Analytics,BW"

# 出力先を指定
python pdf-converter-4-dify.py -o custom_output

# バックグラウンドモード（GUIプロンプトなし）
python pdf-converter-4-dify.py --background
```

### オプション

| オプション | 説明 |
|------------|------|
| `pdf` | 処理するPDFファイルまたはディレクトリ（省略時は`input_pdf/`内の全PDF） |
| `-o, --output` | 出力ディレクトリ（デフォルト: `output_md`） |
| `-t, --tags` | カンマ区切りのタグ（例: `SAC,Analytics`） |
| `--background` | GUIプロンプトを表示しないバックグラウンドモード |

## フォルダ構成

```
pdf-converter-4-dify/
├── pdf-converter-4-dify.py   # メインスクリプト
├── common.py                 # 共通ユーティリティ
├── requirements.txt          # 依存パッケージ
├── input_pdf/                # 入力PDFを配置
├── output_md/                # 変換されたMarkdownの出力先
│   └── images/               # 抽出された画像
└── intermediate_chunks/      # 中間ファイル（再開用）
```

## 出力形式

### ファイル命名規則

```
[PDFファイル名]_0_Contents.md      # 目次
[PDFファイル名]_1.md               # Chapter 1
[PDFファイル名]_1.1.md             # Section 1.1 (14MB超の場合)
[PDFファイル名]_2.md               # Chapter 2
...
```

### YAMLフロントマター

```yaml
---
tags:
  - SAC
  - Analytics
source: document.pdf
chapter: 1
title: Introduction
---
```

## pdf-splitとの連携

大容量PDF（45MB以上）の場合は、まず[pdf-split](../pdf-split)で分割してから本ツールで変換することを推奨します。

```bash
# Step 1: 大容量PDFを分割
cd ../pdf-split
python pdf-split.py large_document.pdf

# Step 2: 分割されたPDFを変換
cd ../pdf-converter-4-dify
python pdf-converter-4-dify.py ../pdf-split/split_pdf/large_document/
```

## ライセンス

MIT License
