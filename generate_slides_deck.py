# -*- coding: utf-8 -*-
r"""
generate_slides_deck.py
Builds the 22-slide Presentation Deck in Widescreen 16:9 format for VNUK students:
Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu (Viện Nghiên cứu và Đào tạo Việt - Anh, ĐHĐN)
Exports to:
  - C:\Users\LENOVO\Downloads\Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf
  - docs\Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf
  - C:\Users\LENOVO\Downloads\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf (as slide format)
  - docs\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf (as slide format)
"""

import os
import subprocess
import shutil
import pypdf

from slides_data_1 import (
    SLIDE_1, SLIDE_2, SLIDE_3, SLIDE_4, SLIDE_5, SLIDE_6
)
from slides_data_2 import (
    SLIDE_7, SLIDE_8, SLIDE_9, SLIDE_10, SLIDE_11, SLIDE_12, SLIDE_13, SLIDE_14
)
from slides_data_3 import (
    SLIDE_15, SLIDE_16, SLIDE_17, SLIDE_18, SLIDE_19, SLIDE_20, SLIDE_21, SLIDE_22
)

HTML_HEADER = r"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Đồ Án KTX Smart Match - VNUK Nhóm 3 (Châu Tuấn Kiệt - Bùi Đình Hiếu - Lê Hoàng Triệu)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {
            size: 297mm 167.0625mm;
            margin: 0;
        }
        * {
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        html, body {
            margin: 0;
            padding: 0;
            width: 297mm;
            background-color: #0f172a;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #1e293b;
            -webkit-font-smoothing: antialiased;
        }
        .slide {
            width: 297mm;
            height: 167.0625mm;
            max-height: 167.0625mm;
            page-break-after: always;
            break-after: page;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-sizing: border-box;
            padding: 11mm 15mm 9mm 15mm;
            background-color: #ffffff;
        }
        .slide:last-child {
            page-break-after: avoid;
            break-after: avoid;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }
        .blueprint-bg {
            background-color: #ffffff;
            background-image: 
                linear-gradient(to right, rgba(203, 213, 225, 0.45) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(203, 213, 225, 0.45) 1px, transparent 1px);
            background-size: 14px 14px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        .callout-badge {
            display: inline-flex;
            align-items: center;
            padding: 1px 4px;
            font-size: 7.5px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            border-radius: 3px;
        }
    </style>
</head>
<body class="bg-slate-900">
"""

HTML_FOOTER = r"""
</body>
</html>
"""

def generate_presentation_deck():
    slides = [
        SLIDE_1, SLIDE_2, SLIDE_3, SLIDE_4, SLIDE_5, SLIDE_6,
        SLIDE_7, SLIDE_8, SLIDE_9, SLIDE_10, SLIDE_11, SLIDE_12, SLIDE_13, SLIDE_14,
        SLIDE_15, SLIDE_16, SLIDE_17, SLIDE_18, SLIDE_19, SLIDE_20, SLIDE_21, SLIDE_22
    ]
    
    print(f"Loaded {len(slides)} presentation slides.")

    full_html = HTML_HEADER + "\n".join(slides) + HTML_FOOTER

    html_dir = os.path.abspath("ui")
    os.makedirs(html_dir, exist_ok=True)
    html_file = os.path.join(html_dir, "presentation_slides.html")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"1. Saved presentation HTML to: {html_file}")

    # Output paths
    downloads_dir = r"C:\Users\LENOVO\Downloads"
    os.makedirs(downloads_dir, exist_ok=True)
    docs_dir = os.path.abspath("docs")
    os.makedirs(docs_dir, exist_ok=True)

    pdf_slide_target = os.path.join(downloads_dir, "Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf")
    pdf_slide_docs = os.path.join(docs_dir, "Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf")
    pdf_wireframe_downloads = os.path.join(downloads_dir, "Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")
    pdf_wireframe_docs = os.path.join(docs_dir, "Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    file_url = "file:///" + html_file.replace("\\", "/")

    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_slide_target}",
        file_url
    ]

    print("2. Converting to vector PDF presentation using Edge headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Edge return code:", res.returncode)

    if os.path.exists(pdf_slide_target):
        size = os.path.getsize(pdf_slide_target)
        print(f"3. SUCCESS: Created {pdf_slide_target} ({size:,} bytes)")

        # Verify page count with pypdf
        reader = pypdf.PdfReader(pdf_slide_target)
        page_count = len(reader.pages)
        print(f"Verified PDF page count: {page_count} slides")

        # Copy to docs/ and also update the wireframe PDF copies if not locked
        try:
            shutil.copyfile(pdf_slide_target, pdf_slide_docs)
            print(f"Copied to: {pdf_slide_docs}")
        except Exception as e:
            print(f"Notice (docs copy): {e}")

        try:
            shutil.copyfile(pdf_slide_target, pdf_wireframe_docs)
            print(f"Updated: {pdf_wireframe_docs}")
        except Exception as e:
            print(f"Notice (docs wireframe): {e}")

        try:
            shutil.copyfile(pdf_slide_target, pdf_wireframe_downloads)
            print(f"Updated: {pdf_wireframe_downloads}")
        except Exception as e:
            print(f"Notice: C:\\Users\\LENOVO\\Downloads\\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf is open in another program, keeping main Slide PDF intact.")
    else:
        print("ERROR: PDF file was not created!")
        if res.stderr:
            print("Edge Stderr:", res.stderr)

if __name__ == "__main__":
    generate_presentation_deck()
