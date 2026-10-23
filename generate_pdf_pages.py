# -*- coding: utf-8 -*-
"""
generate_pdf_pages.py
Generates the complete 10-page HTML and converts it to PDF using headless Edge.
"""

import os
import subprocess
import shutil

def build():
    # Write ui/wireframe_detail_export.html
    html_file = os.path.abspath("ui/wireframe_detail_export.html")
    
    # We will construct the 10 pages HTML
    # Page 1: Cover
    # Page 2: 26 UCs catalog + BR-01..07 + NFR-01..06
    # Page 3: BỘ 3 DIAGRAM: Sequence (1), Activity (2), Component (3)
    # Page 4: UC-01 (1 Dễ) - Summary + Wireframe WF-01 + Flows Table (BF, AF, EF)
    # Page 5: UC-04 (Quan trọng) - Summary + Wireframe WF-02 + Flows Table (BF, AF, EF)
    # Page 6: UC-05 (Quan trọng) - Summary + Wireframe WF-03 (Ranking) + Flows Table (BF, AF, EF)
    # Page 7: UC-18 (Quan trọng) - Summary + Wireframe WF-04 (Approve) + Flows Table (BF, AF, EF)
    # Page 8: UC-24 (Quan trọng) - Summary + Wireframe WF-05 (Gale-Shapley) + Flows Table (BF, AF, EF)
    # Page 9: UC-13 (Quan trọng) - Summary + Wireframe WF-06 (VNPay 72h) + Flows Table (BF, AF, EF)
    # Page 10: Ma trận truy vết 1-1 & Nghiệm thu
    pass

if __name__ == '__main__':
    build()
