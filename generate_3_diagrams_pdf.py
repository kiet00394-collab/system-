# -*- coding: utf-8 -*-
r"""
generate_3_diagrams_pdf.py
Generates a dedicated 3-page vector PDF containing ONLY the 3 UML Diagrams
visually drawn out according to the teacher's rubric:
1. Sequence Diagram (Sơ đồ tuần tự tương tác chi tiết)
2. Activity Diagram (Sơ đồ hoạt động dạng Swimlanes 4 làn)
3. Component Diagram (Sơ đồ thành phần kiến trúc 5 phân tầng UML 2.0)

Authors: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu (Nhóm 3)
Institution: Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) • Đại học Đà Nẵng
"""

import os
import subprocess
import shutil
import pypdf

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bộ 3 Biểu Đồ UML Hệ Thống KTX Smart Match - VNUK Nhóm 3</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {
            size: 297mm 210mm; /* A4 Landscape */
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
        .page {
            width: 297mm;
            height: 210mm;
            max-height: 210mm;
            page-break-after: always;
            break-after: page;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-sizing: border-box;
            padding: 10mm 14mm 8mm 14mm;
            background-color: #ffffff;
        }
        .page:last-child {
            page-break-after: avoid;
            break-after: avoid;
        }
        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }
        .diagram-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            background-color: #ffffff;
            border: 1.5px solid #cbd5e1;
            border-radius: 12px;
            padding: 8px 12px;
            position: relative;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .uml-component {
            position: relative;
            border: 1.5px solid #334155;
            background: #f8fafc;
            border-radius: 6px;
            padding: 6px 10px;
        }
        .uml-component::before {
            content: "";
            position: absolute;
            top: 6px;
            right: 8px;
            width: 14px;
            height: 10px;
            border: 1px solid #475569;
            background: #ffffff;
        }
        .uml-component::after {
            content: "";
            position: absolute;
            top: 7px;
            right: 17px;
            width: 7px;
            height: 3px;
            border: 1px solid #475569;
            background: #ffffff;
            box-shadow: 0 5px 0 -1px #475569, 0 5px 0 0 #ffffff;
        }
        .arrow-line {
            stroke: #475569;
            stroke-width: 1.5;
            marker-end: url(#arrow);
        }
        .dashed-line {
            stroke: #94a3b8;
            stroke-width: 1.5;
            stroke-dasharray: 4 3;
        }
    </style>
</head>
<body class="bg-slate-900">

<!-- ========================================== -->
<!-- TRANG 1: BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) -->
<!-- ========================================== -->
<div class="page">
    <!-- Header -->
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-black text-xl shadow">🎓</span>
            <div>
                <span class="text-[10px] font-mono font-bold text-indigo-700 uppercase tracking-wider block">VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) • ĐẠI HỌC ĐÀ NẴNG</span>
                <h1 class="text-xl font-black text-slate-900 leading-tight">1/3: Biểu Đồ Tuần Tự (Sequence Diagram) - Quy Trình Ghép Cặp & Thanh Toán Bảo Mật</h1>
            </div>
        </div>
        <div class="text-right">
            <span class="text-[10.5px] font-mono font-bold bg-indigo-50 text-indigo-800 px-3 py-1 rounded-full border border-indigo-200 block">
                NHÓM 3 (VNUK): Kiệt • Hiếu • Triệu
            </span>
            <span class="text-[9.5px] text-slate-500 font-mono mt-0.5 block">Học phần: Phân tích & Thiết kế HT</span>
        </div>
    </div>

    <!-- Description strip -->
    <div class="flex items-center justify-between text-[11px] bg-slate-50 border border-slate-200 rounded-lg px-3 py-1.5 my-1">
        <span class="text-slate-700"><strong>Mục tiêu:</strong> Mô hình hóa tương tác theo thời gian giữa 6 Lifelines, xử lý giải thuật Gale-Shapley (BP=0) và khung kiểm soát 72h thanh toán (BR-04, BR-07).</span>
        <div class="flex gap-2 font-mono text-[10px]">
            <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded font-bold">BF: Luồng Chuẩn</span>
            <span class="px-2 py-0.5 bg-rose-100 text-rose-800 rounded font-bold">EF: Luồng Quá Hạn 72h</span>
        </div>
    </div>

    <!-- Diagram SVG Visual Area -->
    <div class="diagram-container">
        <svg viewBox="0 0 1020 500" class="w-full h-full" style="max-height: 480px;">
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b" />
                </marker>
                <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                </marker>
                <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#e11d48" />
                </marker>
                <marker id="arrow-indigo" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#4f46e5" />
                </marker>
            </defs>

            <!-- ================= LIFELINES HEADERS ================= -->
            <!-- 1. Sinh viên -->
            <g transform="translate(60, 20)">
                <rect x="-45" y="0" width="90" height="32" rx="6" fill="#e0e7ff" stroke="#4338ca" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#312e81" text-anchor="middle">Sinh viên (Actor)</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#4338ca" text-anchor="middle">:SinhVien</text>
            </g>

            <!-- 2. Web Portal -->
            <g transform="translate(230, 20)">
                <rect x="-55" y="0" width="110" height="32" rx="6" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Student Web Portal</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">:Boundary UI</text>
            </g>

            <!-- 3. API Gateway -->
            <g transform="translate(410, 20)">
                <rect x="-55" y="0" width="110" height="32" rx="6" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">API Gateway & Auth</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">:Security Guard</text>
            </g>

            <!-- 4. Gale-Shapley Engine -->
            <g transform="translate(590, 20)">
                <rect x="-65" y="0" width="130" height="32" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#064e3b" text-anchor="middle">Matching Engine</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#059669" text-anchor="middle">:GaleShapley (BP=0)</text>
            </g>

            <!-- 5. Payment Gateway -->
            <g transform="translate(770, 20)">
                <rect x="-55" y="0" width="110" height="32" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#78350f" text-anchor="middle">VNPay Gateway</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#b45309" text-anchor="middle">:Payment API</text>
            </g>

            <!-- 6. Database KTX -->
            <g transform="translate(940, 20)">
                <rect x="-50" y="0" width="100" height="32" rx="6" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                <text x="0" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#4c1d95" text-anchor="middle">KTX Database</text>
                <text x="0" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#7c3aed" text-anchor="middle">:PostgreSQL / SQLite</text>
            </g>

            <!-- ================= DASHED LIFELINES ================= -->
            <line x1="60" y1="52" x2="60" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="230" y1="52" x2="230" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="410" y1="52" x2="410" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="590" y1="52" x2="590" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="770" y1="52" x2="770" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />
            <line x1="940" y1="52" x2="940" y2="480" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 4" />

            <!-- ================= ACTIVATION BARS ================= -->
            <rect x="55" y="70" width="10" height="390" fill="#c7d2fe" stroke="#4338ca" stroke-width="1"/>
            <rect x="225" y="75" width="10" height="380" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
            <rect x="405" y="80" width="10" height="370" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
            <rect x="585" y="145" width="10" height="110" fill="#a7f3d0" stroke="#059669" stroke-width="1"/>
            <rect x="765" y="250" width="10" height="80" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
            <rect x="935" y="95" width="10" height="340" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>

            <!-- ================= MESSAGES & INTERACTIONS ================= -->
            <!-- Step 1 -->
            <line x1="65" y1="80" x2="225" y2="80" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="145" y="74" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">1: Nộp hồ sơ (8 thói quen + Top 1.5x) (BR-06)</text>

            <!-- Step 2 -->
            <line x1="235" y1="95" x2="405" y2="95" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="320" y="89" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">2: POST /api/roommate/register</text>

            <!-- Step 3 -->
            <line x1="415" y1="110" x2="935" y2="110" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="675" y="104" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#4338ca" text-anchor="middle">3: Đối soát MSSV Trường A & Đơn cam kết ở ≥ 1 kỳ (BR-01, BR-02)</text>

            <!-- Step 4 -->
            <line x1="935" y1="125" x2="415" y2="125" stroke="#475569" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow)"/>
            <text x="675" y="121" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#475569" text-anchor="middle">4: return VerifiedProfile (Status: ELIGIBLE)</text>

            <!-- Step 5 -->
            <line x1="415" y1="145" x2="585" y2="145" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="500" y="139" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">5: triggerMatching(CandidatesPool)</text>

            <!-- Step 6 (Query DB) -->
            <line x1="595" y1="165" x2="935" y2="165" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="765" y="159" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">6: SELECT available_beds, preferences (BR-05)</text>

            <!-- Step 7 (Self-call Gale-Shapley) -->
            <path d="M 595 180 L 635 180 L 635 205 L 595 205" fill="none" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="642" y="195" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#047857">7: Run Gale-Shapley (BP=0, BR-07)</text>

            <!-- Step 8 (Save match) -->
            <line x1="595" y1="220" x2="935" y2="220" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="765" y="214" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">8: INSERT RoomMatch (Status: PENDING_PAYMENT, 72h)</text>

            <!-- Step 9 (Return to Gateway) -->
            <line x1="585" y1="235" x2="415" y2="235" stroke="#059669" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-green)"/>
            <text x="500" y="231" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#065f46" text-anchor="middle">9: MatchResult(RoomId, RoommatesList, Expire72h)</text>

            <!-- Step 10 (Call VNPay) -->
            <line x1="415" y1="255" x2="765" y2="255" stroke="#d97706" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="590" y="249" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#92400e" text-anchor="middle">10: createPaymentOrder(Amount: 2.000.000đ, Timeout: 72h)</text>

            <!-- Step 11 (VNPay QR response) -->
            <line x1="765" y1="270" x2="415" y2="270" stroke="#d97706" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow)"/>
            <text x="590" y="266" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#92400e" text-anchor="middle">11: return QRCodeURL + PaymentTransactionId</text>

            <!-- Step 12 (Present to SV) -->
            <line x1="405" y1="285" x2="65" y2="285" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow)"/>
            <text x="235" y="280" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">12: Hiển thị kết quả ghép & Mã QR cọc 72h (WF-04, BR-04)</text>

            <!-- ================= ALT FRAME (72h DECISION) ================= -->
            <rect x="40" y="295" width="940" height="175" rx="6" fill="#f8fafc" stroke="#64748b" stroke-width="1.5" fill-opacity="0.4"/>
            <rect x="40" y="295" width="45" height="18" rx="2" fill="#334155"/>
            <text x="62" y="308" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">alt</text>

            <!-- Case 1: Paid within 72h -->
            <text x="95" y="310" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#059669">[Thanh toán cọc trong 72h (BR-04, BF-Luồng chuẩn)]</text>
            
            <line x1="65" y1="322" x2="765" y2="322" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="415" y="317" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">13a: Sinh viên quét mã QR VNPay thanh toán 2.000.000đ</text>

            <line x1="775" y1="337" x2="415" y2="337" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="595" y="333" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#047857" text-anchor="middle">14a: VNPay Webhook IPN -> verifyPaymentSuccess()</text>

            <line x1="415" y1="352" x2="935" y2="352" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="675" y="348" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#047857" text-anchor="middle">15a: UPDATE RoomMatch SET Status='CONFIRMED', LockBed=1 (BR-05)</text>

            <line x1="405" y1="367" x2="65" y2="367" stroke="#059669" stroke-width="1.5" marker-end="url(#arrow-green)"/>
            <text x="235" y="363" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">16a: Xuất Thẻ KTX điện tử & Hợp đồng thuê đã ký (WF-05)</text>

            <!-- Alt separator line -->
            <line x1="40" y1="378" x2="980" y2="378" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/>

            <!-- Case 2: Timeout > 72h -->
            <text x="95" y="392" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#e11d48">[else Quá hạn 72h không đóng cọc (BR-04, EF-Luồng Ngoại lệ)]</text>

            <line x1="415" y1="408" x2="935" y2="408" stroke="#e11d48" stroke-width="1.5" marker-end="url(#arrow-red)"/>
            <text x="675" y="403" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#be123c" text-anchor="middle">13b: CronJob phát hiện quá 72h -> UPDATE Status='EXPIRED_REVOKED'</text>

            <line x1="935" y1="425" x2="595" y2="425" stroke="#e11d48" stroke-width="1.5" marker-end="url(#arrow-red)"/>
            <text x="765" y="420" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#be123c" text-anchor="middle">14b: Thu hồi giữ chỗ, mở lại giường cho Sinh viên danh sách chờ</text>

            <line x1="405" y1="442" x2="65" y2="442" stroke="#e11d48" stroke-width="1.5" marker-end="url(#arrow-red)"/>
            <text x="235" y="437" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#be123c" text-anchor="middle">15b: Gửi Email thông báo hủy kết quả do quá hạn 72h (Ref: EF-A)</text>
        </svg>
    </div>

    <!-- Footer -->
    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đồ án KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) • Nhóm 3</span>
        <span>Trang 1/3: Biểu Đồ Tuần Tự (Sequence Diagram)</span>
    </div>
</div>

<!-- ========================================== -->
<!-- TRANG 2: BIỂU ĐỒ HOẠT ĐỘNG (ACTIVITY DIAGRAM) -->
<!-- ========================================== -->
<div class="page">
    <!-- Header -->
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-black text-xl shadow">🔄</span>
            <div>
                <span class="text-[10px] font-mono font-bold text-emerald-700 uppercase tracking-wider block">VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) • ĐẠI HỌC ĐÀ NẴNG</span>
                <h1 class="text-xl font-black text-slate-900 leading-tight">2/3: Biểu Đồ Hoạt Động (Activity Diagram) - Luồng Nghiệp Vụ Swimlanes End-to-End</h1>
            </div>
        </div>
        <div class="text-right">
            <span class="text-[10.5px] font-mono font-bold bg-emerald-50 text-emerald-800 px-3 py-1 rounded-full border border-emerald-200 block">
                NHÓM 3 (VNUK): Kiệt • Hiếu • Triệu
            </span>
            <span class="text-[9.5px] text-slate-500 font-mono mt-0.5 block">Học phần: Phân tích & Thiết kế HT</span>
        </div>
    </div>

    <!-- Description strip -->
    <div class="flex items-center justify-between text-[11px] bg-slate-50 border border-slate-200 rounded-lg px-3 py-1.5 my-1">
        <span class="text-slate-700"><strong>Mục tiêu:</strong> Phân định rõ trách nhiệm xử lý qua 4 làn bơi (Swimlanes), tích hợp rẽ nhánh điều kiện (Decision Diamonds) và thanh đồng bộ (Fork/Join).</span>
        <div class="flex gap-2 font-mono text-[10px]">
            <span class="px-2 py-0.5 bg-slate-200 text-slate-800 rounded font-bold">● Khởi đầu</span>
            <span class="px-2 py-0.5 bg-indigo-100 text-indigo-800 rounded font-bold">◇ Rẽ nhánh</span>
            <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded font-bold">❚ Đồng bộ</span>
            <span class="px-2 py-0.5 bg-rose-100 text-rose-800 rounded font-bold">◉ Kết thúc</span>
        </div>
    </div>

    <!-- Diagram SVG Swimlanes Visual Area -->
    <div class="diagram-container">
        <svg viewBox="0 0 1020 500" class="w-full h-full" style="max-height: 480px;">
            <defs>
                <marker id="act-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#334155" />
                </marker>
                <marker id="act-arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#e11d48" />
                </marker>
                <marker id="act-arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                </marker>
            </defs>

            <!-- ================= SWIMLANES BACKGROUNDS & HEADERS ================= -->
            <!-- Lane 1: Sinh viên (0 to 255) -->
            <rect x="0" y="0" width="255" height="495" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
            <rect x="0" y="0" width="255" height="34" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1"/>
            <text x="127" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">LÀN 1: SINH VIÊN (STUDENT)</text>
            <text x="127" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">Actor chính: Nộp hồ sơ, chọn phòng, cọc</text>

            <!-- Lane 2: Cán bộ KTX (255 to 510) -->
            <rect x="255" y="0" width="255" height="495" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <rect x="255" y="0" width="255" height="34" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
            <text x="382" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">LÀN 2: CÁN BỘ KTX (STAFF / ADMIN)</text>
            <text x="382" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">Actor quản trị: Thẩm định hồ sơ, giám sát GS</text>

            <!-- Lane 3: Hệ thống KTX (510 to 765) -->
            <rect x="510" y="0" width="255" height="495" fill="#f0fdf4" stroke="#cbd5e1" stroke-width="1.5"/>
            <rect x="510" y="0" width="255" height="34" fill="#dcfce7" stroke="#cbd5e1" stroke-width="1"/>
            <text x="637" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#065f46" text-anchor="middle">LÀN 3: HỆ THỐNG KTX SMART MATCH</text>
            <text x="637" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#059669" text-anchor="middle">Engine: Gale-Shapley (BP=0), Đếm ngược 72h</text>

            <!-- Lane 4: Cổng Trường & VNPay (765 to 1020) -->
            <rect x="765" y="0" width="255" height="495" fill="#fdf4ff" stroke="#cbd5e1" stroke-width="1.5"/>
            <rect x="765" y="0" width="255" height="34" fill="#fae8ff" stroke="#cbd5e1" stroke-width="1"/>
            <text x="892" y="16" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#701a75" text-anchor="middle">LÀN 4: HỆ THỐNG LIÊN KẾT NGOÀI</text>
            <text x="892" y="27" font-family="'JetBrains Mono', monospace" font-size="8" fill="#a21caf" text-anchor="middle">Trường A REST / LDAP • VNPay QR Webhook</text>

            <!-- ================= WORKFLOW NODES ================= -->

            <!-- Start Node in Lane 1 -->
            <circle cx="127" cy="55" r="10" fill="#0f172a" />
            <text x="127" y="42" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Bắt đầu</text>

            <!-- Action 1: Đăng nhập MSSV -->
            <line x1="127" y1="65" x2="127" y2="80" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>
            <rect x="35" y="80" width="185" height="34" rx="8" fill="#ffffff" stroke="#475569" stroke-width="1.5"/>
            <text x="127" y="94" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">1. Đăng nhập MSSV Trường A</text>
            <text x="127" y="106" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#64748b" text-anchor="middle">Nhập thông tin xác thực Cổng KTX</text>

            <!-- Line to Lane 4 (Verify Trường A) -->
            <path d="M 220 97 L 892 97 L 892 115" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>
            
            <!-- Action 2 in Lane 4: Đối soát Trường A -->
            <rect x="800" y="115" width="185" height="34" rx="8" fill="#ffffff" stroke="#86198f" stroke-width="1.5"/>
            <text x="892" y="129" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#701a75" text-anchor="middle">2. Đối soát CSDL Trường A (BR-01)</text>
            <text x="892" y="141" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#a21caf" text-anchor="middle">Kiểm tra MSSV & Email trường cấp</text>

            <!-- Line to Decision 1 in Lane 4 -->
            <line x1="892" y1="149" x2="892" y2="165" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>
            
            <!-- Decision 1: Hợp lệ trường A? -->
            <polygon points="892,165 927,180 892,195 857,180" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
            <text x="892" y="182" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#92400e" text-anchor="middle">Đúng SV Trường A?</text>

            <!-- Decision 1 -> No (EF-B: Từ chối) -->
            <line x1="927" y1="180" x2="980" y2="180" stroke="#e11d48" stroke-width="1.5"/>
            <line x1="980" y1="180" x2="980" y2="230" stroke="#e11d48" stroke-width="1.5" marker-end="url(#act-arrow-red)"/>
            <circle cx="980" cy="242" r="10" fill="none" stroke="#e11d48" stroke-width="2"/>
            <circle cx="980" cy="242" r="6" fill="#e11d48" />
            <text x="980" y="262" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#be123c" text-anchor="middle">Hủy / Từ chối (EF)</text>
            <text x="942" y="174" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" fill="#be123c">[Sai MSSV]</text>

            <!-- Decision 1 -> Yes (Back to Lane 1) -->
            <path d="M 857 180 L 127 180 L 127 195" fill="none" stroke="#059669" stroke-width="1.5" marker-end="url(#act-arrow-green)"/>
            <text x="490" y="174" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" fill="#047857">[Hợp lệ BR-01]</text>

            <!-- Action 3 in Lane 1: Khai báo 8 thói quen -->
            <rect x="35" y="195" width="185" height="34" rx="8" fill="#ffffff" stroke="#475569" stroke-width="1.5"/>
            <text x="127" y="209" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">3. Khai báo 8 Thói quen & Top 1.5x</text>
            <text x="127" y="221" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#4338ca" text-anchor="middle">Trọng số thói quen BR-06, cam kết BR-02</text>

            <!-- Line to Lane 2: Cán bộ thẩm định -->
            <path d="M 220 212 L 382 212 L 382 230" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>

            <!-- Action 4 in Lane 2: Thẩm định hồ sơ -->
            <rect x="290" y="230" width="185" height="34" rx="8" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
            <text x="382" y="244" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">4. Thẩm định đối tượng ưu tiên</text>
            <text x="382" y="256" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#64748b" text-anchor="middle">Duyệt diện chính sách BR-03</text>

            <!-- Fork Bar in Lane 2 -->
            <line x1="382" y1="264" x2="382" y2="280" stroke="#334155" stroke-width="1.5"/>
            <rect x="320" y="280" width="124" height="4" fill="#0f172a" rx="2"/>
            
            <!-- Parallel tasks: Branch A & Branch B -->
            <path d="M 345 284 L 345 298" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>
            <rect x="265" y="298" width="110" height="26" rx="6" fill="#f8fafc" stroke="#64748b" stroke-width="1"/>
            <text x="320" y="310" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#334155" text-anchor="middle">Khóa quỹ phòng 2,4,6</text>
            <text x="320" y="319" font-family="'JetBrains Mono', monospace" font-size="6.5" fill="#64748b" text-anchor="middle">Tối ưu 100% giường (BR-05)</text>

            <path d="M 420 284 L 420 298" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>
            <rect x="385" y="298" width="115" height="26" rx="6" fill="#f8fafc" stroke="#64748b" stroke-width="1"/>
            <text x="442" y="310" font-family="'Plus Jakarta Sans', sans-serif" font-size="7.5" font-weight="bold" fill="#334155" text-anchor="middle">Cập nhật điểm ưu tiên</text>
            <text x="442" y="319" font-family="'JetBrains Mono', monospace" font-size="6.5" fill="#64748b" text-anchor="middle">Điểm BR-03 gia đình chính sách</text>

            <!-- Join Bar -->
            <path d="M 320 324 L 320 338 L 345 338" stroke="#334155" stroke-width="1.5"/>
            <path d="M 442 324 L 442 338 L 420 338" stroke="#334155" stroke-width="1.5"/>
            <rect x="320" y="338" width="124" height="4" fill="#0f172a" rx="2"/>

            <!-- From Join Bar to Lane 3 (System GS Algorithm) -->
            <path d="M 382 342 L 382 355 L 637 355 L 637 368" fill="none" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>

            <!-- Action 5 in Lane 3: Gale-Shapley Algorithm -->
            <rect x="545" y="368" width="185" height="34" rx="8" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
            <text x="637" y="382" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">5. Kích hoạt Gale-Shapley (BP=0)</text>
            <text x="637" y="394" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#047857" text-anchor="middle">Khử 100% cặp chặn (BR-07), phát mã giữ chỗ 72h</text>

            <!-- Line to Decision 2 (Lane 3: 72h Payment check) -->
            <line x1="637" y1="402" x2="637" y2="415" stroke="#334155" stroke-width="1.5" marker-end="url(#act-arrow)"/>

            <polygon points="637,415 677,430 637,445 597,430" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
            <text x="637" y="432" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#92400e" text-anchor="middle">Đóng cọc &le; 72 giờ?</text>

            <!-- Case > 72h: Hủy kết quả -->
            <line x1="597" y1="430" x2="540" y2="430" stroke="#e11d48" stroke-width="1.5"/>
            <line x1="540" y1="430" x2="540" y2="455" stroke="#e11d48" stroke-width="1.5" marker-end="url(#act-arrow-red)"/>
            <circle cx="540" cy="467" r="10" fill="none" stroke="#e11d48" stroke-width="2"/>
            <circle cx="540" cy="467" r="6" fill="#e11d48" />
            <text x="540" y="487" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#be123c" text-anchor="middle">Hủy cọc > 72h (BR-04 / EF)</text>
            <text x="568" y="424" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#be123c">[Quá 72h]</text>

            <!-- Case <= 72h: Đã thanh toán VNPay -->
            <path d="M 677 430 L 892 430 L 892 445" fill="none" stroke="#059669" stroke-width="1.5" marker-end="url(#act-arrow-green)"/>
            <text x="760" y="424" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="bold" fill="#047857">[Đã thanh toán VNPay BR-04]</text>

            <!-- Action 6 in Lane 4: VNPay Confirm -->
            <rect x="800" y="445" width="185" height="34" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
            <text x="892" y="459" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">6. Xác nhận GD & Ký Hợp Đồng</text>
            <text x="892" y="471" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#047857" text-anchor="middle">Phát hành Thẻ nội trú & Bàn giao giường</text>

            <!-- Line to End Node in Lane 1 -->
            <path d="M 800 462 L 127 462 L 127 470" fill="none" stroke="#059669" stroke-width="1.5" marker-end="url(#act-arrow-green)"/>
            <circle cx="127" cy="482" r="10" fill="none" stroke="#059669" stroke-width="2"/>
            <circle cx="127" cy="482" r="6" fill="#059669" />
            <text x="155" y="485" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" fill="#047857">Hoàn tất (BF)</text>
        </svg>
    </div>

    <!-- Footer -->
    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đồ án KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) • Nhóm 3</span>
        <span>Trang 2/3: Biểu Đồ Hoạt Động (Activity Diagram)</span>
    </div>
</div>

<!-- ========================================== -->
<!-- TRANG 3: BIỂU ĐỒ THÀNH PHẦN (COMPONENT DIAGRAM) -->
<!-- ========================================== -->
<div class="page">
    <!-- Header -->
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div class="flex items-center gap-3">
            <span class="w-10 h-10 rounded-xl bg-sky-600 text-white flex items-center justify-center font-black text-xl shadow">🧩</span>
            <div>
                <span class="text-[10px] font-mono font-bold text-sky-700 uppercase tracking-wider block">VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) • ĐẠI HỌC ĐÀ NẴNG</span>
                <h1 class="text-xl font-black text-slate-900 leading-tight">3/3: Biểu Đồ Thành Phần (Component Diagram) - Kiến Trúc Phân Tầng UML 2.0</h1>
            </div>
        </div>
        <div class="text-right">
            <span class="text-[10.5px] font-mono font-bold bg-sky-50 text-sky-800 px-3 py-1 rounded-full border border-sky-200 block">
                NHÓM 3 (VNUK): Kiệt • Hiếu • Triệu
            </span>
            <span class="text-[9.5px] text-slate-500 font-mono mt-0.5 block">Học phần: Phân tích & Thiết kế HT</span>
        </div>
    </div>

    <!-- Description strip -->
    <div class="flex items-center justify-between text-[11px] bg-slate-50 border border-slate-200 rounded-lg px-3 py-1.5 my-1">
        <span class="text-slate-700"><strong>Mục tiêu:</strong> Mô hình hóa kiến trúc 5 phân tầng thành phần theo chuẩn UML 2.0 (Component Stereotypes, Ball-and-Socket Interfaces và Phụ thuộc nghiệp vụ).</span>
        <div class="flex gap-2 font-mono text-[10px]">
            <span class="px-2 py-0.5 bg-indigo-100 text-indigo-800 rounded font-bold">―(O― Interface Cung cấp</span>
            <span class="px-2 py-0.5 bg-amber-100 text-amber-800 rounded font-bold">―(― Interface Yêu cầu</span>
            <span class="px-2 py-0.5 bg-slate-200 text-slate-800 rounded font-bold">··> Dependency</span>
        </div>
    </div>

    <!-- Diagram SVG Component Visual Area -->
    <div class="diagram-container">
        <svg viewBox="0 0 1020 500" class="w-full h-full" style="max-height: 480px;">
            <defs>
                <marker id="comp-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
                </marker>
            </defs>

            <!-- ================= TIER 1: PRESENTATION LAYER ================= -->
            <rect x="15" y="10" width="990" height="85" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
            <text x="30" y="26" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#334155">TIER 1: PRESENTATION & CLIENT LAYER (TẦNG GIAO DIỆN NGƯỜI DÙNG)</text>

            <!-- Comp 1: Student Web Portal -->
            <g transform="translate(60, 32)">
                <rect x="0" y="0" width="260" height="52" rx="6" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <!-- UML glyph -->
                <rect x="235" y="6" width="16" height="12" fill="#f1f5f9" stroke="#334155" stroke-width="1"/>
                <rect x="230" y="8" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <rect x="230" y="13" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <text x="12" y="18" font-family="'JetBrains Mono', monospace" font-size="8" fill="#64748b">«component»</text>
                <text x="12" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Student Web Portal UI</text>
                <text x="12" y="44" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#4338ca">Responsive Vue / Tailwind CSS</text>
            </g>

            <!-- Comp 2: Admin Dashboard -->
            <g transform="translate(380, 32)">
                <rect x="0" y="0" width="260" height="52" rx="6" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <!-- UML glyph -->
                <rect x="235" y="6" width="16" height="12" fill="#f1f5f9" stroke="#334155" stroke-width="1"/>
                <rect x="230" y="8" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <rect x="230" y="13" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <text x="12" y="18" font-family="'JetBrains Mono', monospace" font-size="8" fill="#64748b">«component»</text>
                <text x="12" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Staff & Admin Dashboard</text>
                <text x="12" y="44" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#059669">Quản lý quỹ phòng & xét duyệt</text>
            </g>

            <!-- Comp 3: Mobile PWA Portal -->
            <g transform="translate(700, 32)">
                <rect x="0" y="0" width="260" height="52" rx="6" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <!-- UML glyph -->
                <rect x="235" y="6" width="16" height="12" fill="#f1f5f9" stroke="#334155" stroke-width="1"/>
                <rect x="230" y="8" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <rect x="230" y="13" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <text x="12" y="18" font-family="'JetBrains Mono', monospace" font-size="8" fill="#64748b">«component»</text>
                <text x="12" y="32" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Mobile PWA Gateway</text>
                <text x="12" y="44" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#d97706">Tra cứu kết quả & quét QR VNPay</text>
            </g>

            <!-- Connectors Tier 1 -> Tier 2 (Ball and Socket) -->
            <path d="M 190 84 L 190 108" stroke="#334155" stroke-width="1.5"/>
            <path d="M 510 84 L 510 108" stroke="#334155" stroke-width="1.5"/>
            <path d="M 830 84 L 830 108" stroke="#334155" stroke-width="1.5"/>

            <circle cx="190" cy="113" r="5" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
            <circle cx="510" cy="113" r="5" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
            <circle cx="830" cy="113" r="5" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>

            <!-- ================= TIER 2: GATEWAY & SECURITY ================= -->
            <rect x="15" y="125" width="990" height="75" rx="10" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
            <text x="30" y="141" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#1e293b">TIER 2: API GATEWAY & SECURITY LAYER (CỔNG AN NINH & ĐỐI SOÁT)</text>

            <!-- API Gateway -->
            <g transform="translate(100, 146)">
                <rect x="0" y="0" width="360" height="46" rx="6" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <rect x="335" y="6" width="16" height="12" fill="#f1f5f9" stroke="#334155" stroke-width="1"/>
                <rect x="330" y="8" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <rect x="330" y="13" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <text x="12" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#64748b">«component»</text>
                <text x="12" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a">Reverse Proxy & Rate Limiter</text>
                <text x="12" y="40" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#4338ca">Bảo vệ CSRF, Chống Brute Force (NFR-03)</text>
            </g>

            <!-- Auth Guard -->
            <g transform="translate(560, 146)">
                <rect x="0" y="0" width="360" height="46" rx="6" fill="#ffffff" stroke="#334155" stroke-width="1.5"/>
                <rect x="335" y="6" width="16" height="12" fill="#f1f5f9" stroke="#334155" stroke-width="1"/>
                <rect x="330" y="8" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <rect x="330" y="13" width="8" height="3" fill="#ffffff" stroke="#334155" stroke-width="0.8"/>
                <text x="12" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#64748b">«component»</text>
                <text x="12" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="bold" fill="#0f172a">Authentication Guard (JWT & Cookies)</text>
                <text x="12" y="40" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#059669">HttpOnly Session Token, BR-01 Verify</text>
            </g>

            <!-- Connectors Tier 2 -> Tier 3 -->
            <path d="M 280 192 L 280 220" stroke="#334155" stroke-width="1.5"/>
            <path d="M 740 192 L 740 220" stroke="#334155" stroke-width="1.5"/>

            <!-- ================= TIER 3: CORE APPLICATION LOGIC ================= -->
            <rect x="15" y="222" width="990" height="92" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
            <text x="30" y="238" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#065f46">TIER 3: CORE BUSINESS APPLICATION SERVICES (CÁC DỊCH VỤ NGHIỆP VỤ LÕI)</text>

            <!-- Service 1: Application Approval -->
            <g transform="translate(30, 246)">
                <rect x="0" y="0" width="225" height="58" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#059669">«component»</text>
                <text x="10" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Application Service</text>
                <text x="10" y="42" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">BR-01, BR-02 (Cam kết)</text>
                <text x="10" y="52" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">BR-03 (Điểm chính sách)</text>
            </g>

            <!-- Service 2: Gale-Shapley Matching Engine -->
            <g transform="translate(275, 246)">
                <rect x="0" y="0" width="235" height="58" rx="6" fill="#d1fae5" stroke="#047857" stroke-width="2"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#047857">«core component»</text>
                <text x="10" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="extrabold" fill="#064e3b">Gale-Shapley Engine</text>
                <text x="10" y="42" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" fill="#047857">BR-06 (Top 1.5x Trọng số)</text>
                <text x="10" y="52" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" fill="#047857">BR-07 (Blocking Pairs = 0)</text>
            </g>

            <!-- Service 3: Room Allocation Manager -->
            <g transform="translate(530, 246)">
                <rect x="0" y="0" width="220" height="58" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#059669">«component»</text>
                <text x="10" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Room Allocation Mgr</text>
                <text x="10" y="42" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">BR-05 (Lấp đầy 100% giường)</text>
                <text x="10" y="52" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">Phân nhóm gói 2, 4, 6 người</text>
            </g>

            <!-- Service 4: Payment & Contract Manager -->
            <g transform="translate(770, 246)">
                <rect x="0" y="0" width="220" height="58" rx="6" fill="#ffffff" stroke="#059669" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#059669">«component»</text>
                <text x="10" y="30" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#0f172a">Payment & Contract</text>
                <text x="10" y="42" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">BR-04 (Hạn cọc 72 giờ)</text>
                <text x="10" y="52" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569">Sinh hợp đồng số & Thẻ KTX</text>
            </g>

            <!-- Connectors Tier 3 -> Tier 4 & 5 -->
            <path d="M 142 304 L 142 334" stroke="#059669" stroke-width="1.5"/>
            <path d="M 392 304 L 392 334" stroke="#059669" stroke-width="1.5"/>
            <path d="M 640 304 L 640 334" stroke="#059669" stroke-width="1.5"/>
            <path d="M 880 304 L 880 334" stroke="#059669" stroke-width="1.5"/>

            <!-- ================= TIER 4: EXTERNAL INTEGRATION ================= -->
            <rect x="15" y="336" width="485" height="75" rx="10" fill="#fdf4ff" stroke="#a21caf" stroke-width="1.5"/>
            <text x="30" y="352" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#701a75">TIER 4A: EXTERNAL INTEGRATION (TÍCH HỢP NGOÀI)</text>

            <!-- Adapter 1: School A LDAP -->
            <g transform="translate(30, 358)">
                <rect x="0" y="0" width="215" height="45" rx="6" fill="#ffffff" stroke="#86198f" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#86198f">«adapter»</text>
                <text x="10" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a">School A LDAP / REST</text>
                <text x="10" y="39" font-family="'JetBrains Mono', monospace" font-size="7" fill="#701a75">Xác thực MSSV BR-01</text>
            </g>

            <!-- Adapter 2: VNPay IPN -->
            <g transform="translate(265, 358)">
                <rect x="0" y="0" width="220" height="45" rx="6" fill="#ffffff" stroke="#86198f" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#86198f">«adapter»</text>
                <text x="10" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a">VNPay QR / IPN Gateway</text>
                <text x="10" y="39" font-family="'JetBrains Mono', monospace" font-size="7" fill="#701a75">Xác nhận thanh toán 72h BR-04</text>
            </g>

            <!-- ================= TIER 5: DATA PERSISTENCE ================= -->
            <rect x="520" y="336" width="485" height="75" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
            <text x="535" y="352" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" fill="#4c1d95">TIER 4B: PERSISTENCE & DATA STORAGE (LƯU TRỮ)</text>

            <!-- DB 1: Primary DB -->
            <g transform="translate(535, 358)">
                <rect x="0" y="0" width="215" height="45" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#7c3aed">«database»</text>
                <text x="10" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a">KTX Relational DB</text>
                <text x="10" y="39" font-family="'JetBrains Mono', monospace" font-size="7" fill="#4c1d95">PostgreSQL (Users, Rooms, Bills)</text>
            </g>

            <!-- DB 2: Audit & Stability Vault -->
            <g transform="translate(770, 358)">
                <rect x="0" y="0" width="220" height="45" rx="6" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
                <text x="10" y="16" font-family="'JetBrains Mono', monospace" font-size="8" fill="#7c3aed">«audit store»</text>
                <text x="10" y="29" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" font-weight="bold" fill="#0f172a">Matching Stability Audit</text>
                <text x="10" y="39" font-family="'JetBrains Mono', monospace" font-size="7" fill="#4c1d95">Lưu vết BP=0 & Lịch sử đổi phòng</text>
            </g>

            <!-- Cross-Tier Interfaces Legend Bar at Bottom of Diagram -->
            <rect x="15" y="420" width="990" height="65" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
            <text x="30" y="436" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" fill="#334155">BẢNG DANH MỤC INTERFACE KẾT NỐI CHÍNH (UML INTERFACES SPECIFICATION):</text>
            
            <g transform="translate(30, 444)" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569">
                <text x="0" y="12"><tspan font-weight="bold" fill="#4338ca">1. IStudentUI / IAdminUI:</tspan> Cung cấp giao diện Web Portal & Dashboard theo chuẩn RESTful JSON.</text>
                <text x="0" y="24"><tspan font-weight="bold" fill="#059669">2. IMatchingEngine:</tspan> Giao thức thực thi giải thuật Gale-Shapley hai chiều với trọng số ưu tiên 1.5x (BR-06, BR-07).</text>
                <text x="500" y="12"><tspan font-weight="bold" fill="#86198f">3. IPaymentCallback (IPN):</tspan> Webhook đối soát tự động giao dịch 2.000.000đ trong 72 giờ từ VNPay (BR-04).</text>
                <text x="500" y="24"><tspan font-weight="bold" fill="#7c3aed">4. IRepositoryAccess:</tspan> ORM Data Layer đảm bảo tính toàn vẹn ACID khi khóa giường phòng 2, 4, 6 (BR-05).</text>
            </g>
        </svg>
    </div>

    <!-- Footer -->
    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đồ án KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) • Nhóm 3</span>
        <span>Trang 3/3: Biểu Đồ Thành Phần (Component Diagram)</span>
    </div>
</div>

</body>
</html>
"""

def generate_pdf():
    print("1. Writing HTML file...")
    html_dir = os.path.abspath("ui")
    os.makedirs(html_dir, exist_ok=True)
    html_file = os.path.join(html_dir, "three_diagrams_export.html")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print(f"   HTML written to: {html_file}")

    downloads_dir = r"C:\Users\LENOVO\Downloads"
    os.makedirs(downloads_dir, exist_ok=True)
    docs_dir = os.path.abspath("docs")
    os.makedirs(docs_dir, exist_ok=True)

    pdf_target_downloads = os.path.join(downloads_dir, "Bo_3_Diagram_KTX_Smart_Match_VNUK.pdf")
    pdf_target_docs = os.path.join(docs_dir, "Bo_3_Diagram_KTX_Smart_Match_VNUK.pdf")

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
        f"--print-to-pdf={pdf_target_downloads}",
        file_url
    ]

    print("2. Converting to vector PDF using Edge headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("   Edge return code:", res.returncode)

    if os.path.exists(pdf_target_downloads):
        size = os.path.getsize(pdf_target_downloads)
        print(f"3. SUCCESS: Created {pdf_target_downloads} ({size:,} bytes)")

        # Verify page count with pypdf
        reader = pypdf.PdfReader(pdf_target_downloads)
        page_count = len(reader.pages)
        print(f"   Verified PDF page count: {page_count} pages (Expected: exactly 3 pages)")

        try:
            shutil.copyfile(pdf_target_downloads, pdf_target_docs)
            print(f"   Copied to docs: {pdf_target_docs}")
        except Exception as e:
            print(f"   Notice: {e}")
    else:
        print("ERROR: PDF was not created!")
        if res.stderr:
            print("Edge error:", res.stderr)

if __name__ == "__main__":
    generate_pdf()
