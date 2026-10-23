# -*- coding: utf-8 -*-
r"""
build_merged_master_pdf.py
Builds the unified Master Presentation PDF in the exact order requested by user:
1. Bìa & Đặt vấn đề (VNUK, Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều)
2. Business Rules (BR-01 đến BR-07) & Non-Functional Requirements (NFR-01 đến NFR-06)
3. Bộ 3 Diagram bắt buộc (Sequence Diagram, Activity Diagram, Component Diagram) được vẽ trực quan
4. Bảng Đặc tả Use Case chi tiết (1 Dễ + 5 Quan trọng theo chuẩn Rubric của Thầy) + Wireframe UI khớp 1-1
5. Ma trận truy vết 1-to-1 & Nghiệm thu đồ án

Outputs:
  - C:\Users\LENOVO\Downloads\Bao_Cao_Do_An_KTX_Smart_Match_VNUK.pdf
  - docs\Bao_Cao_Do_An_KTX_Smart_Match_VNUK.pdf
  - C:\Users\LENOVO\Downloads\Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf
  - docs\Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf
"""

import os
import subprocess
import shutil
import pypdf

# Common HTML Header & Footer for 16:9 Presentation Deck
HTML_HEADER = r"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Đồ Án KTX Smart Match - VNUK Nhóm 3 (Châu Tuấn Kiệt - Bùi Đình Hiếu - Lê Hoàng Triều)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {
            size: 297mm 167.0625mm; /* 16:9 Widescreen */
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
            padding: 10mm 15mm 8mm 15mm;
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

# ==============================================================================
# SLIDE 1: BÌA BÁO CÁO (COVER)
# ==============================================================================
SLIDE_1_COVER = r"""
<div class="slide bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white justify-between p-12">
    <div class="flex justify-between items-center border-b border-indigo-400/30 pb-4">
        <div class="flex items-center gap-3">
            <span class="w-11 h-11 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-black text-2xl shadow-lg">🎓</span>
            <div>
                <span class="text-xs font-mono font-bold text-indigo-300 uppercase tracking-widest block">VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) • ĐẠI HỌC ĐÀ NẴNG</span>
                <span class="text-sm font-bold text-white">HỌC PHẦN: PHÂN TÍCH & THIẾT KẾ HỆ THỐNG (SYSTEM ENGINEERING)</span>
            </div>
        </div>
        <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs font-mono font-bold">
            BÁO CÁO ĐỒ ÁN 2026
        </span>
    </div>

    <div class="space-y-4 my-auto py-6">
        <div class="inline-block px-3.5 py-1 rounded-lg bg-indigo-500/30 border border-indigo-400 text-indigo-200 text-xs font-mono font-bold uppercase tracking-wider">
            BÁO CÁO TOÀN DIỆN: BUSINESS RULES • NON-FUNCTIONAL • BỘ 3 DIAGRAM • ĐẶC TẢ USE CASE & WIREFRAME
        </div>
        <h1 class="text-4xl md:text-5xl font-black text-white tracking-tight leading-tight">
            HỆ THỐNG QUẢN TRỊ & GHÉP BẠN CÙNG PHÒNG<br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-indigo-300 to-emerald-400">
                KÝ TÚC XÁ THÔNG MINH (KTX SMART MATCH)
            </span>
        </h1>
        <p class="text-slate-300 text-base max-w-3xl leading-relaxed">
            Ứng dụng giải thuật ghép cặp ổn định Gale-Shapley (BP=0), phân tích nếp sống đa tiêu chí với trọng số Top Priority 1.5x, tối ưu lấp đầy 100% giường và quản trị thanh toán bảo mật 72 giờ.
        </p>
    </div>

    <div class="border-t border-indigo-500/30 pt-4 flex justify-between items-center text-sm">
        <div>
            <span class="text-indigo-300 text-xs block font-mono">SINH VIÊN THỰC HIỆN (NHÓM 3 - VNUK):</span>
            <strong class="text-white text-base">Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</strong>
        </div>
        <div class="text-right text-xs font-mono text-slate-300">
            <span>Giảng viên hướng dẫn & chấm điểm</span><br>
            <span class="text-emerald-300 font-bold">ĐẠT CHUẨN 100% RUBRIC BẢNG LỚP</span>
        </div>
    </div>
</div>
"""

# ==============================================================================
# SLIDE 2: ĐẶT VẤN ĐỀ & GIẢI PHÁP
# ==============================================================================
SLIDE_2_PROBLEM = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                TỔNG QUAN DỰ ÁN • SLIDE 02/23
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">1. Đặt Vấn Đề Thực Tế & Giải Pháp KTX Smart Match</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-slate-100 text-slate-600 px-3 py-1 rounded-full border border-slate-300">
            Problem & Solution
        </span>
    </div>

    <div class="grid grid-cols-2 gap-6 my-auto">
        <!-- Problem -->
        <div class="p-5 bg-rose-50 border-2 border-rose-200 rounded-2xl space-y-3">
            <div class="flex items-center gap-2 text-rose-800 font-extrabold text-base">
                <span class="text-xl">❌</span> THỰC TRẠNG & BẤT CẬP HIỆN NAY
            </div>
            <ul class="space-y-2 text-xs text-rose-950 leading-relaxed">
                <li class="flex items-start gap-1.5">• <strong>Ghép phòng ngẫu nhiên:</strong> Sinh viên bị xếp phòng hoàn toàn dựa theo số thứ tự nộp đơn, không xét nếp sống.</li>
                <li class="flex items-start gap-1.5">• <strong>Xung đột lối sống gay gắt:</strong> Cú đêm ở chung với người ngủ sớm (22h); người ưa yên tĩnh ở chung người thích nghe nhạc to; người hút thuốc ở chung người ghét khói.</li>
                <li class="flex items-start gap-1.5">• <strong>Quá tải khiếu nại:</strong> Cán bộ KTX mệt mỏi xử lý hàng trăm đơn xin đổi phòng mỗi tuần; phòng ốc xáo trộn.</li>
                <li class="flex items-start gap-1.5">• <strong>Lãng phí vận hành:</strong> Nhiều phòng 4 người chỉ có 1-2 người ở dở dang, gây lãng phí điều hòa, điện nước.</li>
            </ul>
        </div>

        <!-- Solution -->
        <div class="p-5 bg-emerald-50 border-2 border-emerald-200 rounded-2xl space-y-3">
            <div class="flex items-center gap-2 text-emerald-800 font-extrabold text-base">
                <span class="text-xl">✅</span> GIẢI PHÁP ĐỘT PHÁ CỦA NHÓM 3 (VNUK)
            </div>
            <ul class="space-y-2 text-xs text-emerald-950 leading-relaxed">
                <li class="flex items-start gap-1.5">• <strong>Khảo sát 8 tiêu chí thói quen:</strong> Giờ ngủ, giờ dậy, độ gọn gàng, thói quen học, mức chịu ồn, hút thuốc, dắt bạn bè, sở thích.</li>
                <li class="flex items-start gap-1.5">• <strong>Trọng số ưu tiên cá nhân (Top 1.5x - BR-06):</strong> Cho phép mỗi sinh viên chọn 1 tiêu chí quan trọng nhất để tính ma trận 2 chiều.</li>
                <li class="flex items-start gap-1.5">• <strong>Thuật toán Gale-Shapley (BP=0 - BR-07):</strong> Ghép cặp ổn định toán học tuyệt đối, triệt tiêu 100% cặp chặn xin đổi phòng.</li>
                <li class="flex items-start gap-1.5">• <strong>Tối ưu lấp đầy 100% giường (BR-05):</strong> Lấp đầy từng phòng trước khi mở phòng mới, tối ưu hóa doanh thu KTX.</li>
            </ul>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

# ==============================================================================
# SLIDE 3: BUSINESS RULES (BR-01 ĐẾN BR-04)
# ==============================================================================
SLIDE_3_BR_PART1 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                QUY TẮC NGHIỆP VỤ • PHẦN 1/2 • SLIDE 03/23
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-1">2. Hệ Thống Quy Tắc Nghiệp Vụ Cốt Lõi (BR-01 đến BR-04)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full">
            Core Business Rules
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto text-xs">
        <!-- BR-01 -->
        <div class="p-3.5 bg-slate-50 border-2 border-indigo-200 rounded-xl space-y-1.5">
            <div class="flex justify-between items-center">
                <span class="px-2 py-0.5 bg-indigo-600 text-white text-[10px] font-mono font-bold rounded">BR-01</span>
                <span class="text-[10px] font-mono font-bold text-rose-700">Hard Rule (Cưỡng chế)</span>
            </div>
            <strong class="text-slate-900 block text-xs">Đối tượng Sinh viên Hợp lệ (Trường Đại học A)</strong>
            <p class="text-[10.5px] text-slate-600 leading-relaxed">
                Chỉ cho phép sinh viên chính quy thuộc Trường A đăng nhập bằng MSSV và email trường cấp (<code>@udn.vn</code>). Sinh viên trường khác bị từ chối truy cập (Mã lỗi <code>ERR_NOT_SCHOOL_A</code>).
            </p>
            <div class="text-[9.5px] font-mono text-indigo-700 pt-1 border-t border-indigo-100 flex justify-between">
                <span>Áp dụng: UC-01, UC-04</span>
                <span>Wireframe: WF-01-C07</span>
            </div>
        </div>

        <!-- BR-02 -->
        <div class="p-3.5 bg-slate-50 border-2 border-sky-200 rounded-xl space-y-1.5">
            <div class="flex justify-between items-center">
                <span class="px-2 py-0.5 bg-sky-600 text-white text-[10px] font-mono font-bold rounded">BR-02</span>
                <span class="text-[10px] font-mono font-bold text-sky-800">Cam kết Hợp đồng</span>
            </div>
            <strong class="text-slate-900 block text-xs">Thời hạn Cam kết Lưu trú Tối thiểu (&ge; 1 Học kỳ)</strong>
            <p class="text-[10.5px] text-slate-600 leading-relaxed">
                Sinh viên nộp đơn bắt buộc cam kết ở tối thiểu 1 học kỳ (5 tháng) nhằm ổn định phòng ốc. Rút lui trước hạn đơn phương sẽ <strong>mất 100% tiền cọc 2.000.000đ</strong>.
            </p>
            <div class="text-[9.5px] font-mono text-sky-700 pt-1 border-t border-sky-100 flex justify-between">
                <span>Áp dụng: UC-04, UC-24</span>
                <span>Wireframe: WF-02-C06</span>
            </div>
        </div>

        <!-- BR-03 -->
        <div class="p-3.5 bg-slate-50 border-2 border-amber-200 rounded-xl space-y-1.5">
            <div class="flex justify-between items-center">
                <span class="px-2 py-0.5 bg-amber-600 text-white text-[10px] font-mono font-bold rounded">BR-03</span>
                <span class="text-[10px] font-mono font-bold text-amber-800">Chính sách Xã hội</span>
            </div>
            <strong class="text-slate-900 block text-xs">Ưu tiên Đối tượng Chính sách (+15 Điểm Xét Tuyển)</strong>
            <p class="text-[10.5px] text-slate-600 leading-relaxed">
                Con thương binh, hộ nghèo, dân tộc thiểu số hoặc khuyết tật có minh chứng hợp lệ được <strong>cộng 15 điểm ưu tiên</strong>, xếp đợt 1 và bố trí phòng tầng thấp thuận tiện.
            </p>
            <div class="text-[9.5px] font-mono text-amber-700 pt-1 border-t border-amber-100 flex justify-between">
                <span>Áp dụng: UC-04, UC-05</span>
                <span>Wireframe: WF-03-C03</span>
            </div>
        </div>

        <!-- BR-04 -->
        <div class="p-3.5 bg-slate-50 border-2 border-rose-200 rounded-xl space-y-1.5">
            <div class="flex justify-between items-center">
                <span class="px-2 py-0.5 bg-rose-600 text-white text-[10px] font-mono font-bold rounded">BR-04</span>
                <span class="text-[10px] font-mono font-bold text-rose-800">Đếm ngược Tự động</span>
            </div>
            <strong class="text-slate-900 block text-xs">Hạn Chót Thanh Toán Cọc 72 Giờ (72-Hour Deposit Lock)</strong>
            <p class="text-[10.5px] text-slate-600 leading-relaxed">
                Sau khi có kết quả ghép phòng, sinh viên có <strong>chính xác 72 giờ</strong> nộp cọc 2.000.000đ qua VNPay. Quá 72h tự động hủy giữ chỗ, chuyển giường cho sinh viên dự bị.
            </p>
            <div class="text-[9.5px] font-mono text-rose-700 pt-1 border-t border-rose-100 flex justify-between">
                <span>Áp dụng: UC-18, UC-24</span>
                <span>Wireframe: WF-04-C03 (Đồng hồ 72h)</span>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

# ==============================================================================
# SLIDE 4: BUSINESS RULES (BR-05 ĐẾN BR-07 & GALE-SHAPLEY)
# ==============================================================================
SLIDE_4_BR_PART2 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                QUY TẮC NGHIỆP VỤ • PHẦN 2/2 • SLIDE 04/23
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-1">3. Thuật Toán Gale-Shapley & Tối Ưu Lấp Đầy (BR-05 đến BR-07)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
            Mathematical Engine
        </span>
    </div>

    <div class="grid grid-cols-3 gap-4 my-auto text-xs">
        <!-- BR-05 -->
        <div class="p-3.5 bg-slate-50 border-2 border-emerald-200 rounded-xl space-y-1.5 flex flex-col justify-between">
            <div class="space-y-1">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 bg-emerald-600 text-white text-[10px] font-mono font-bold rounded">BR-05</span>
                    <span class="text-[9px] font-mono font-bold text-emerald-800">Tối ưu vận hành</span>
                </div>
                <strong class="text-slate-900 block text-xs">Lấp Đầy 100% Giường</strong>
                <p class="text-[10px] text-slate-600 leading-relaxed">
                    Lấp đầy trọn vẹn số giường của từng phòng (2, 4, 6 người) trước khi mở phòng mới cùng dãy. Tuyệt đối không để phòng dở dang 1 người trong phòng 4 người để tiết kiệm điện điều hòa.
                </p>
            </div>
            <div class="text-[9px] font-mono text-emerald-700 pt-1 border-t border-emerald-100">
                Áp dụng: UC-04, UC-05 (WF-03-C04)
            </div>
        </div>

        <!-- BR-06 -->
        <div class="p-3.5 bg-slate-50 border-2 border-purple-200 rounded-xl space-y-1.5 flex flex-col justify-between">
            <div class="space-y-1">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 bg-purple-600 text-white text-[10px] font-mono font-bold rounded">BR-06</span>
                    <span class="text-[9px] font-mono font-bold text-purple-800">Cá nhân hóa</span>
                </div>
                <strong class="text-slate-900 block text-xs">Top Priority Trọng Số 1.5x</strong>
                <p class="text-[10px] text-slate-600 leading-relaxed">
                    Trong 8 tiêu chí thói quen (Giờ ngủ, giờ dậy, gọn gàng, ồn ào, học đêm, hút thuốc, dắt bạn, sở thích), sinh viên được chọn 1 tiêu chí quan trọng nhất để <strong>nhân hệ số 1.5x</strong> tính ma trận tương đồng.
                </p>
            </div>
            <div class="text-[9px] font-mono text-purple-700 pt-1 border-t border-purple-100">
                Áp dụng: UC-04 (WF-02-C04)
            </div>
        </div>

        <!-- BR-07 -->
        <div class="p-3.5 bg-slate-50 border-2 border-indigo-200 rounded-xl space-y-1.5 flex flex-col justify-between">
            <div class="space-y-1">
                <div class="flex justify-between items-center">
                    <span class="px-2 py-0.5 bg-indigo-700 text-white text-[10px] font-mono font-bold rounded">BR-07</span>
                    <span class="text-[9px] font-mono font-bold text-indigo-900">Cốt lõi toán học</span>
                </div>
                <strong class="text-slate-900 block text-xs">Gale-Shapley (BP = 0)</strong>
                <p class="text-[10px] text-slate-600 leading-relaxed">
                    Khử triệt để 100% cặp chặn (Blocking Pairs = 0). Đảm bảo không tồn tại bất kỳ cặp sinh viên nào thích ở cùng nhau hơn bạn cùng phòng hiện tại mà cả hai đều muốn đổi $\rightarrow$ <strong>0% khiếu nại</strong>.
                </p>
            </div>
            <div class="text-[9px] font-mono text-indigo-700 pt-1 border-t border-indigo-100">
                Áp dụng: Matching Engine (Audit BP=0)
            </div>
        </div>
    </div>

    <!-- Formula Strip -->
    <div class="p-3 bg-indigo-50 border border-indigo-200 rounded-xl flex justify-between items-center text-xs">
        <div>
            <strong class="text-indigo-950 font-mono block text-[11px]">CÔNG THỨC TÍNH ĐỘ TƯƠNG ĐỒNG HAI CHIỀU:</strong>
            <span class="text-slate-600 text-[10.5px]">Similarity(A, B) = [ &Sigma; (w_i &times; &delta;(A_i, B_i)) / &Sigma; w_i ] &times; 100% (với w_top = 1.5)</span>
        </div>
        <span class="px-3 py-1 bg-indigo-600 text-white font-mono text-xs font-bold rounded-lg shadow">
            STABLE MATCHING BP=0
        </span>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

# ==============================================================================
# SLIDE 5: NON-FUNCTIONAL REQUIREMENTS (NFR-01 ĐẾN NFR-06)
# ==============================================================================
SLIDE_5_NFR = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded border border-emerald-200 uppercase">
                YÊU CẦU PHI CHỨC NĂNG • SLIDE 05/23
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-1">4. Hệ Thống 6 Yêu Cầu Phi Chức Năng (NFR-01 đến NFR-06)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
            ISO/IEC 25010 Standard
        </span>
    </div>

    <div class="grid grid-cols-3 gap-3.5 my-auto text-xs">
        <!-- NFR-01 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-emerald-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-emerald-700 block">NFR-01: PERFORMANCE</span>
            <strong class="text-slate-900 block text-[11px]">Tốc Độ Ghép & Phản Hồi API</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Thuật toán Gale-Shapley ghép 1.000 SV trong <strong>&lt; 500ms</strong>; 95% request API phản hồi <strong>&le; 200ms (p95)</strong> qua Redis caching.
            </p>
        </div>

        <!-- NFR-02 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-sky-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-sky-700 block">NFR-02: SCALABILITY</span>
            <strong class="text-slate-900 block text-[11px]">Chịu Tải Mùa Tuyển Sinh</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Hệ thống chịu tải đồng thời tối thiểu <strong>2.000 SV trực tuyến</strong> nộp đơn và tra cứu cùng lúc trong tuần cao điểm; tỷ lệ lỗi 5xx &lt; 0.01%.
            </p>
        </div>

        <!-- NFR-03 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-rose-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-rose-700 block">NFR-03: SECURITY</span>
            <strong class="text-slate-900 block text-[11px]">Bảo Vệ Dữ Liệu & Phiên</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Mật khẩu băm <strong>bcrypt (cost 12)</strong>; Session lưu <strong>HttpOnly Secure Cookie</strong> chống XSS; khóa 15p sau 5 lần nhập sai MK.
            </p>
        </div>

        <!-- NFR-04 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-indigo-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-indigo-700 block">NFR-04: AVAILABILITY</span>
            <strong class="text-slate-900 block text-[11px]">Sẵn Sàng & CronJob 5 Phút</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Uptime cam kết <strong>&ge; 99.9%</strong>; CronJob quét tự động hạn nộp cọc 72h <strong>mỗi 5 phút một lần</strong>; tự động backup CSDL mỗi 6 giờ.
            </p>
        </div>

        <!-- NFR-05 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-amber-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-amber-700 block">NFR-05: USABILITY</span>
            <strong class="text-slate-900 block text-[11px]">Giao Diện Responsive & Đơn &lt; 3p</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Sinh viên hoàn tất nộp đơn và 8 câu khảo sát trong <strong>&le; 3 phút</strong>; giao diện mượt mà trên cả Mobile, Tablet và Desktop.
            </p>
        </div>

        <!-- NFR-06 -->
        <div class="p-3 bg-slate-50 border-t-4 border-t-purple-600 rounded-xl space-y-1 border border-slate-200">
            <span class="text-[9.5px] font-mono font-bold text-purple-700 block">NFR-06: AUDIT TRAIL</span>
            <strong class="text-slate-900 block text-[11px]">Truy Vết Toàn Vẹn & Kiến Trúc 5 Lớp</strong>
            <p class="text-[10px] text-slate-600 leading-relaxed">
                Ghi log kiểm toán 100% giao dịch VNPay và lịch sử ghép phòng; kiến trúc phân tầng Clean Multi-tier dễ bảo trì và mở rộng.
            </p>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

def generate_unified_deck():
    # Import the remaining slides from existing data files
    from slides_data_1 import SLIDE_3 as SLIDE_USECASE_OVERVIEW
    from slides_data_1 import SLIDE_6 as SLIDE_RUBRIC_SPEC
    from slides_data_2 import SLIDE_7 as SLIDE_ACT_DIAGRAM
    from slides_data_2 import SLIDE_8 as SLIDE_COMP_DIAGRAM
    from slides_data_2 import (
        SLIDE_9, SLIDE_10, SLIDE_11, SLIDE_12, SLIDE_13, SLIDE_14
    )
    from slides_data_3 import (
        SLIDE_15, SLIDE_16, SLIDE_17, SLIDE_18, SLIDE_19, SLIDE_20, SLIDE_21, SLIDE_22
    )

    # Let's inspect the Sequence Diagram drawing from generate_3_diagrams_pdf
    # We create a dedicated slide for Sequence Diagram (Biểu đồ 1)
    SLIDE_6_SEQ_DIAGRAM = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-1.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                BỘ 3 DIAGRAM BẮT BUỘC • SƠ ĐỒ 1/3 • SLIDE 06/23
            </span>
            <h2 class="text-lg font-black text-slate-900 mt-0.5">5. Biểu Đồ Tuần Tự (Sequence Diagram) - Quy Trình Ghép Phòng & Cọc 72 Giờ</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full">
            Tương Tác 6 Lifelines & Khung Alt
        </span>
    </div>

    <div class="border border-slate-300 rounded-xl p-2 bg-white my-auto shadow-sm" style="height: 120mm;">
        <svg viewBox="0 0 1020 480" class="w-full h-full">
            <defs>
                <marker id="arrow-master" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b" />
                </marker>
                <marker id="arrow-green-m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                </marker>
                <marker id="arrow-red-m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#e11d48" />
                </marker>
            </defs>

            <!-- Lifeline Headers -->
            <g transform="translate(60, 10)">
                <rect x="-45" y="0" width="90" height="28" rx="5" fill="#e0e7ff" stroke="#4338ca" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#312e81" text-anchor="middle">Sinh viên</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#4338ca" text-anchor="middle">:SinhVien</text>
            </g>
            <g transform="translate(230, 10)">
                <rect x="-55" y="0" width="110" height="28" rx="5" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Student Portal</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569" text-anchor="middle">:WebUI</text>
            </g>
            <g transform="translate(410, 10)">
                <rect x="-55" y="0" width="110" height="28" rx="5" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">API Gateway</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#475569" text-anchor="middle">:Auth Guard</text>
            </g>
            <g transform="translate(590, 10)">
                <rect x="-65" y="0" width="130" height="28" rx="5" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#064e3b" text-anchor="middle">Matching Engine</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#059669" text-anchor="middle">:GaleShapley (BP=0)</text>
            </g>
            <g transform="translate(770, 10)">
                <rect x="-55" y="0" width="110" height="28" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">VNPay Gateway</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#b45309" text-anchor="middle">:Payment QR</text>
            </g>
            <g transform="translate(940, 10)">
                <rect x="-50" y="0" width="100" height="28" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
                <text x="0" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="bold" fill="#4c1d95" text-anchor="middle">KTX Database</text>
                <text x="0" y="24" font-family="'JetBrains Mono', monospace" font-size="7.5" fill="#7c3aed" text-anchor="middle">:PostgreSQL</text>
            </g>

            <!-- Dashed Lifelines -->
            <line x1="60" y1="38" x2="60" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />
            <line x1="230" y1="38" x2="230" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />
            <line x1="410" y1="38" x2="410" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />
            <line x1="590" y1="38" x2="590" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />
            <line x1="770" y1="38" x2="770" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />
            <line x1="940" y1="38" x2="940" y2="470" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="4 4" />

            <!-- Activation Bars -->
            <rect x="56" y="55" width="8" height="400" fill="#c7d2fe" stroke="#4338ca" stroke-width="1"/>
            <rect x="226" y="60" width="8" height="390" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
            <rect x="406" y="65" width="8" height="380" fill="#e2e8f0" stroke="#475569" stroke-width="1"/>
            <rect x="586" y="130" width="8" height="110" fill="#a7f3d0" stroke="#059669" stroke-width="1"/>
            <rect x="766" y="235" width="8" height="85" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
            <rect x="936" y="80" width="8" height="360" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>

            <!-- Sequence Steps -->
            <line x1="64" y1="65" x2="226" y2="65" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow-master)"/>
            <text x="145" y="60" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">1: Nộp đơn 8 thói quen & Top 1.5x (BR-06)</text>

            <line x1="234" y1="80" x2="406" y2="80" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow-master)"/>
            <text x="320" y="75" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">2: POST /api/roommate-match/submit</text>

            <line x1="414" y1="95" x2="936" y2="95" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow-master)"/>
            <text x="675" y="90" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#4338ca" text-anchor="middle">3: Đối soát MSSV Trường A & Đơn cam kết >= 1 kỳ (BR-01, BR-02)</text>

            <line x1="936" y1="110" x2="414" y2="110" stroke="#475569" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#arrow-master)"/>
            <text x="675" y="106" font-family="'JetBrains Mono', monospace" font-size="8" fill="#475569" text-anchor="middle">4: return Verified (Status: APPROVED)</text>

            <line x1="414" y1="130" x2="586" y2="130" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="500" y="125" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">5: triggerMatching(CandidatesPool)</text>

            <line x1="594" y1="148" x2="936" y2="148" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="765" y="143" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">6: SELECT available_beds (BR-05 Lấp đầy 100%)</text>

            <!-- Self-call GS -->
            <path d="M 594 165 L 635 165 L 635 190 L 594 190" fill="none" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="642" y="180" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#047857">7: Run Gale-Shapley (BP=0, BR-07)</text>

            <line x1="594" y1="205" x2="936" y2="205" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="765" y="200" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">8: INSERT RoomMatch (Status: PENDING_PAYMENT, 72h)</text>

            <line x1="586" y1="220" x2="414" y2="220" stroke="#059669" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#arrow-green-m)"/>
            <text x="500" y="216" font-family="'JetBrains Mono', monospace" font-size="8" fill="#065f46" text-anchor="middle">9: MatchResult(RoomId, Roommates, 72h)</text>

            <line x1="414" y1="240" x2="766" y2="240" stroke="#d97706" stroke-width="1.2" marker-end="url(#arrow-master)"/>
            <text x="590" y="235" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#92400e" text-anchor="middle">10: createPaymentOrder(2.000.000đ, Timeout: 72h)</text>

            <line x1="766" y1="255" x2="414" y2="255" stroke="#d97706" stroke-width="1.2" stroke-dasharray="3 3" marker-end="url(#arrow-master)"/>
            <text x="590" y="251" font-family="'JetBrains Mono', monospace" font-size="8" fill="#92400e" text-anchor="middle">11: return QRCodeURL + TransId</text>

            <line x1="406" y1="270" x2="64" y2="270" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow-master)"/>
            <text x="235" y="265" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#0f172a" text-anchor="middle">12: Hiển thị thông báo trúng tuyển & Mã QR cọc 72h (WF-04)</text>

            <!-- Alt Box -->
            <rect x="40" y="280" width="940" height="185" rx="5" fill="#f8fafc" stroke="#64748b" stroke-width="1.2" fill-opacity="0.4"/>
            <rect x="40" y="280" width="40" height="16" rx="2" fill="#334155"/>
            <text x="60" y="291" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">alt</text>

            <text x="90" y="293" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#059669">[Thanh toán cọc trong 72h (BR-04, BF-Luồng chuẩn)]</text>
            <line x1="64" y1="305" x2="766" y2="305" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="415" y="300" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#047857" text-anchor="middle">13a: Sinh viên quét mã QR thanh toán 2.000.000đ</text>

            <line x1="774" y1="320" x2="414" y2="320" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="595" y="316" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#047857" text-anchor="middle">14a: VNPay Webhook IPN -> verifySuccess()</text>

            <line x1="414" y1="335" x2="936" y2="335" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="675" y="331" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#047857" text-anchor="middle">15a: UPDATE Status='CONFIRMED', LockBed=1 (BR-05)</text>

            <line x1="406" y1="350" x2="64" y2="350" stroke="#059669" stroke-width="1.2" marker-end="url(#arrow-green-m)"/>
            <text x="235" y="346" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#047857" text-anchor="middle">16a: Phát hành Thẻ nội trú & Hợp đồng KTX (WF-05)</text>

            <!-- Dash separator -->
            <line x1="40" y1="362" x2="980" y2="362" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 3"/>

            <text x="90" y="375" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#e11d48">[else Quá hạn 72h không đóng cọc (BR-04, EF-Luồng Ngoại lệ)]</text>
            <line x1="414" y1="392" x2="936" y2="392" stroke="#e11d48" stroke-width="1.2" marker-end="url(#arrow-red-m)"/>
            <text x="675" y="387" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#be123c" text-anchor="middle">13b: CronJob phát hiện quá 72h -> UPDATE Status='EXPIRED_REVOKED'</text>

            <line x1="936" y1="410" x2="586" y2="410" stroke="#e11d48" stroke-width="1.2" marker-end="url(#arrow-red-m)"/>
            <text x="765" y="405" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" fill="#be123c" text-anchor="middle">14b: Thu hồi giữ chỗ, gán giường cho Sinh viên danh sách chờ</text>

            <line x1="406" y1="428" x2="64" y2="428" stroke="#e11d48" stroke-width="1.2" marker-end="url(#arrow-red-m)"/>
            <text x="235" y="423" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" fill="#be123c" text-anchor="middle">15b: Gửi Email hủy kết quả & Mở đăng ký đợt bổ sung</text>
        </svg>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

    # Assemble all slides in exact requested sequence:
    # 1. Bìa & Đặt vấn đề
    # 2. Business Rules (BR-01..07) & Non-Functional (NFR-01..06)
    # 3. Bộ 3 Diagram (Sequence, Activity, Component)
    # 4. Use Case Specifications & Wireframes (UC-01, 04, 05, 18, 24, 13)
    # 5. Traceability Matrix & Nghiệm thu
    all_slides = [
        SLIDE_1_COVER,          # Slide 1: Bìa (VNUK, Kiệt, Hiếu, Triều)
        SLIDE_2_PROBLEM,        # Slide 2: Đặt vấn đề & Giải pháp
        SLIDE_USECASE_OVERVIEW, # Slide 3: Sơ đồ 26 Use Case & 8 Tác nhân
        SLIDE_3_BR_PART1,       # Slide 4: BR-01 đến BR-04
        SLIDE_4_BR_PART2,       # Slide 5: BR-05 đến BR-07 (Gale-Shapley BP=0)
        SLIDE_5_NFR,            # Slide 6: NFR-01 đến NFR-06
        SLIDE_6_SEQ_DIAGRAM,    # Slide 7: Biểu đồ Tuần tự (Sequence Diagram - 1)
        SLIDE_ACT_DIAGRAM,      # Slide 8: Biểu đồ Hoạt động (Activity Diagram - 2)
        SLIDE_COMP_DIAGRAM,     # Slide 9: Biểu đồ Thành phần (Component Diagram - 3)
        SLIDE_RUBRIC_SPEC,      # Slide 10: Chuẩn Rubric Đặc tả của Thầy (BF/AF/EF)
        SLIDE_9,                # Slide 11: UC-01 (Dễ) - Bảng Đặc tả
        SLIDE_10,               # Slide 12: UC-01 - Wireframe WF-01 & Sequence
        SLIDE_11,               # Slide 13: UC-04 (Quan trọng) - Bảng Đặc tả
        SLIDE_12,               # Slide 14: UC-04 - Wireframe WF-02 & Sequence
        SLIDE_13,               # Slide 15: UC-05 (Quan trọng) - Bảng Đặc tả
        SLIDE_14,               # Slide 16: UC-05 - Wireframe WF-03 & Sequence
        SLIDE_15,               # Slide 17: UC-18 (Quan trọng) - Bảng Đặc tả
        SLIDE_16,               # Slide 18: UC-18 - Wireframe WF-04 & Sequence
        SLIDE_17,               # Slide 19: UC-24 (Quan trọng) - Bảng Đặc tả
        SLIDE_18,               # Slide 20: UC-24 - Wireframe WF-05 & Sequence
        SLIDE_19,               # Slide 21: UC-13 (Quan trọng) - Bảng Đặc tả
        SLIDE_20,               # Slide 22: UC-13 - Wireframe WF-06 & Sequence
        SLIDE_21,               # Slide 23: Ma trận truy vết 1-to-1 Toàn diện
        SLIDE_22                # Slide 24: Nghiệm thu đồ án & Lời cảm ơn
    ]

    print(f"Loaded {len(all_slides)} merged master slides in requested order.")

    full_html = HTML_HEADER + "\n".join(all_slides) + HTML_FOOTER

    html_dir = os.path.abspath("ui")
    os.makedirs(html_dir, exist_ok=True)
    html_file = os.path.join(html_dir, "master_presentation_deck.html")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"1. Saved unified presentation HTML to: {html_file}")

    downloads_dir = r"C:\Users\LENOVO\Downloads"
    os.makedirs(downloads_dir, exist_ok=True)
    docs_dir = os.path.abspath("docs")
    os.makedirs(docs_dir, exist_ok=True)

    pdf_main_target = os.path.join(downloads_dir, "Bao_Cao_Do_An_KTX_Smart_Match_VNUK.pdf")
    pdf_main_docs = os.path.join(docs_dir, "Bao_Cao_Do_An_KTX_Smart_Match_VNUK.pdf")
    pdf_slide_target = os.path.join(downloads_dir, "Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf")
    pdf_slide_docs = os.path.join(docs_dir, "Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf")

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
        f"--print-to-pdf={pdf_main_target}",
        file_url
    ]

    print("2. Converting to unified vector PDF presentation using Edge headless...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("   Edge return code:", res.returncode)

    if os.path.exists(pdf_main_target):
        size = os.path.getsize(pdf_main_target)
        print(f"3. SUCCESS: Created {pdf_main_target} ({size:,} bytes)")

        reader = pypdf.PdfReader(pdf_main_target)
        page_count = len(reader.pages)
        print(f"   Verified PDF page count: {page_count} slides")

        # Copy to docs/
        try:
            shutil.copyfile(pdf_main_target, pdf_main_docs)
            print(f"   Copied to docs: {pdf_main_docs}")
        except Exception as e:
            print(f"   Notice (docs copy): {e}")

        # Also update Slide_Thuyet_Trinh_KTX_Smart_Match_VNUK.pdf
        try:
            shutil.copyfile(pdf_main_target, pdf_slide_target)
            print(f"   Updated: {pdf_slide_target}")
        except Exception as e:
            print(f"   Notice (downloads slide): {e}")

        try:
            shutil.copyfile(pdf_main_target, pdf_slide_docs)
            print(f"   Updated: {pdf_slide_docs}")
        except Exception as e:
            print(f"   Notice (docs slide): {e}")
    else:
        print("ERROR: PDF was not created!")
        if res.stderr:
            print("Edge error:", res.stderr)

if __name__ == "__main__":
    generate_unified_deck()
