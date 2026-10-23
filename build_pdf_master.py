# -*- coding: utf-8 -*-
"""
build_pdf_master.py
Assembles 10 pages and renders print-ready vector PDF using headless Edge.
"""

import os
import subprocess
import shutil

from pdf_pages_part1 import PAGE_HEADER, PAGE_1_COVER, PAGE_2_CATALOG_RULES, PAGE_3_THREE_DIAGRAMS
from pdf_pages_part2 import PAGE_4_UC01, PAGE_5_UC04, PAGE_6_UC05
from pdf_pages_part3 import PAGE_7_UC18, PAGE_8_UC24, PAGE_9_UC13, PAGE_10_TRACE_MATRIX, PAGE_FOOTER

def run():
    full_html = "".join([
        PAGE_HEADER,
        PAGE_1_COVER,
        PAGE_2_CATALOG_RULES,
        PAGE_3_THREE_DIAGRAMS,
        PAGE_4_UC01,
        PAGE_5_UC04,
        PAGE_6_UC05,
        PAGE_7_UC18,
        PAGE_8_UC24,
        PAGE_9_UC13,
        PAGE_10_TRACE_MATRIX,
        PAGE_FOOTER
    ])

    export_html_path = os.path.abspath("ui/wireframe_detail_export.html")
    with open(export_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("1. Written 10-page master HTML to:", export_html_path)

    pdf_downloads = os.path.abspath(r"C:\Users\LENOVO\Downloads\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")
    pdf_docs = os.path.abspath(r"docs\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    file_url = "file:///" + export_html_path.replace("\\", "/")

    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_downloads}",
        file_url
    ]

    print("2. Converting to vector PDF using browser headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Exit code:", res.returncode)

    if os.path.exists(pdf_downloads):
        size = os.path.getsize(pdf_downloads)
        print(f"3. SUCCESS: Created PDF at: {pdf_downloads} ({size} bytes)")
        shutil.copy2(pdf_downloads, pdf_docs)
        print(f"4. SUCCESS: Copied PDF to: {pdf_docs}")
    else:
        print("FAILED: PDF not found in Downloads!")

if __name__ == "__main__":
    run()
