# -*- coding: utf-8 -*-
"""
create_master_pdf_builder.py
Generates the 10-page master PDF specification matching:
1. Teacher's whiteboard (BF, AF, EF with Id, action, actor, Ref -> 100%)
2. 1 Dễ + 1-n Quan trọng
3. Bộ 3 Diagram: Sequence (1), Activity (2), Component (3)
4. Summary Table + Three Types of Flows Table + Blueprint Wireframe for all 6 UCs
5. Traceability Matrix 1-1
"""

html_head = r"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hồ Sơ Đặc Tả Use Case, Bộ 3 Diagram & Wireframe UI - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {
            size: A4 portrait;
            margin: 10mm 8mm 10mm 8mm;
        }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #1e293b;
            background-color: #f8fafc;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }
        .blueprint-bg {
            background-color: #ffffff;
            background-image: 
                linear-gradient(to right, rgba(203, 213, 225, 0.45) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(203, 213, 225, 0.45) 1px, transparent 1px);
            background-size: 16px 16px;
        }
        .page-break {
            page-break-before: always;
            break-before: page;
        }
        .avoid-break {
            page-break-inside: avoid;
            break-inside: avoid;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        .callout-badge {
            display: inline-flex;
            align-items: center;
            padding: 2px 6px;
            font-size: 9px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            border-radius: 4px;
        }
    </style>
</head>
<body class="p-2 md:p-4 space-y-6">
"""

print("Writing create_master_pdf_builder.py setup complete")
