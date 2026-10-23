# -*- coding: utf-8 -*-
"""
make_pdf_full.py
Complete 10-page print-ready HTML & PDF generator for KTX Smart Match System.
Strictly adheres to Slide template & Teacher's whiteboard.
"""

import os
import subprocess
import shutil

def build_pdf():
    html_out = os.path.abspath("ui/wireframe_detail_export.html")
    pdf_downloads = os.path.abspath(r"C:\Users\LENOVO\Downloads\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")
    pdf_docs = os.path.abspath(r"docs\Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")

    # Read base components or write the full html
    # Let's write html_out
    with open("pdf_template.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html_code)

    print("1. Written HTML to:", html_out)

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    file_url = "file:///" + html_out.replace("\\", "/")

    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_downloads}",
        file_url
    ]

    print("2. Converting HTML to PDF via Edge Headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Exit code:", res.returncode)

    if os.path.exists(pdf_downloads):
        size = os.path.getsize(pdf_downloads)
        print(f"3. PDF created successfully at {pdf_downloads} ({size} bytes)")
        shutil.copy2(pdf_downloads, pdf_docs)
        print(f"4. PDF copied to {pdf_docs}")
    else:
        print("ERROR: PDF was not generated!")

if __name__ == "__main__":
    build_pdf()
