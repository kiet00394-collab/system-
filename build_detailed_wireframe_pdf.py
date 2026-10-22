# -*- coding: utf-8 -*-
"""
build_detailed_wireframe_pdf.py
Generates an ultra-detailed, comprehensive Wireframe Specification document
and exports it directly to a print-ready vector PDF in C:\\Users\\LENOVO\\Downloads\\
"""

import os
import subprocess
import shutil

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hồ Sơ Thiết Kế Wireframe Chi Tiết - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {
            size: A4 portrait;
            margin: 12mm 10mm 12mm 10mm;
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
            font-size: 9.5px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            border-radius: 4px;
        }
    </style>
</head>
<body class="p-2 md:p-6 space-y-8">

    <!-- ============================================================== -->
    <!-- TRANG 1: TRANG BÌA HỒ SƠ THIẾT KẾ (COVER PAGE)                -->
    <!-- ============================================================== -->
    <div class="min-h-[960px] bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl p-10 md:p-14 flex flex-col justify-between shadow-2xl relative overflow-hidden border-2 border-indigo-500/40">
        <!-- Background Grid Pattern -->
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:24px_24px]"></div>

        <div class="space-y-4 relative z-10">
            <div class="flex items-center justify-between border-b border-indigo-400/30 pb-4">
                <div class="flex items-center gap-3">
                    <span class="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-black text-xl shadow-lg">📐</span>
                    <div>
                        <span class="text-xs font-mono font-bold text-indigo-300 uppercase tracking-widest block">HỆ THỐNG KỸ THUẬT & PHÂN TÍCH THIẾT KẾ (SYSTEM ENGINEERING)</span>
                        <span class="text-sm font-bold text-white">ĐỒ ÁN PHÂN TÍCH THIẾT KẾ HỆ THỐNG GHÉP PHÒNG KTX</span>
                    </div>
                </div>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs font-mono font-bold">
                    PHIÊN BẢN CHÍNH THỨC 2026
                </span>
            </div>

            <div class="pt-16 space-y-4">
                <span class="px-3.5 py-1.5 rounded-lg bg-indigo-500/30 border border-indigo-400 text-indigo-200 text-xs font-mono font-bold uppercase tracking-wider inline-block">
                    TÀI LIỆU KỸ THUẬT GIAO DIỆN & TRUY VẾT NGHIỆP VỤ (1-TO-1 TRACEABILITY)
                </span>
                <h1 class="text-3xl md:text-5xl font-black text-white tracking-tight leading-tight">
                    HỒ SƠ THIẾT KẾ WIREFRAME CHI TIẾT<br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-indigo-300 to-emerald-400">
                        HỆ THỐNG GHÉP BẠN CÙNG PHÒNG KTX
                    </span>
                </h1>
                <p class="text-slate-300 text-sm max-w-2xl leading-relaxed">
                    Tài liệu bản vẽ kiến trúc giao diện tương tác (High-Fidelity Wireframes), từ điển thành phần (Component Data Dictionary) và bảng ma trận truy vết 1-1 với Bảng Đặc Tả Use Case (BF/AF/EF), Hệ thống Quy tắc Nghiệp vụ (BR-01 đến BR-07) và Sơ đồ Tuần tự (Sequence Diagrams).
                </p>
            </div>
        </div>

        <div class="space-y-6 relative z-10 pt-10">
            <!-- 3 Nguyên tắc thiết kế -->
            <div class="grid grid-cols-3 gap-4 pt-4 border-t border-indigo-400/30 text-xs">
                <div class="bg-white/5 border border-white/10 p-3.5 rounded-xl">
                    <span class="text-amber-300 font-bold block mb-1">1. ĐẶC TẢ TRƯỚC, DESIGN SAU</span>
                    <p class="text-slate-400 text-[11px]">Mọi nút bấm, input, alert trên wireframe đều có bước đặc tả và sequence tương ứng.</p>
                </div>
                <div class="bg-white/5 border border-white/10 p-3.5 rounded-xl">
                    <span class="text-sky-300 font-bold block mb-1">2. TRUY VẾT 1-TO-1</span>
                    <p class="text-slate-400 text-[11px]">Đánh mã Callout [WF-xx-Cyy] nối trực tiếp vào BF, AF, EF và BR trong tài liệu.</p>
                </div>
                <div class="bg-white/5 border border-white/10 p-3.5 rounded-xl">
                    <span class="text-emerald-300 font-bold block mb-1">3. CHUẨN MỰC HỌC THUẬT</span>
                    <p class="text-slate-400 text-[11px]">Đầy đủ 1 Use Case dễ (UC-01) + 4 Use Case nghiệp vụ cốt lõi (UC-02, 03, 04, 05).</p>
                </div>
            </div>

            <!-- Footer Meta -->
            <div class="flex items-center justify-between text-xs text-slate-400 pt-4 border-t border-indigo-400/20">
                <div>
                    <span class="text-slate-300 font-bold">Nhóm thực hiện:</span> Nhóm 3 (Châu Tuấn Kiệt, Bùi Đình Hiếu, Lê Hoàng Triệu)
                </div>
                <div class="font-mono text-slate-300">
                    Cập nhật: Học kỳ 1 (2026) • ĐH Đà Nẵng
                </div>
            </div>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 2: TỔNG QUAN KIẾN TRÚC WIREFRAME & BẢNG ÁNH XẠ 1-1       -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-4 flex justify-between items-center">
            <div>
                <span class="text-xs font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase">
                    PHẦN I: MA TRẬN ÁNH XẠ KIẾN TRÚC GIAO DIỆN
                </span>
                <h2 class="text-xl font-extrabold text-slate-900 mt-1">Bảng Tổng Hợp Ánh Xạ Giữa Use Case & Màn Hình Wireframe</h2>
            </div>
            <span class="text-xs font-mono font-bold bg-slate-100 text-slate-600 px-3 py-1 rounded-full">
                Tổng cộng: 5 Màn hình chuẩn
            </span>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
            Tuân thủ nghiêm ngặt chỉ đạo của Giảng viên: <em>"Làm design có gì thì đặc tả phải có cái nớ. Đặc tả trước, design sau."</em> Toàn bộ 5 màn hình wireframe dưới đây được thiết kế đồng bộ với từng bước luồng cơ bản (BF), luồng thay thế (AF) và luồng ngoại lệ (EF):
        </p>

        <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                    <tr>
                        <th class="p-3 border">Mã Màn Hình</th>
                        <th class="p-3 border">Tên Giao Diện Wireframe</th>
                        <th class="p-3 border">Use Case Tương Ứng</th>
                        <th class="p-3 border">Tác Nhân (Actor)</th>
                        <th class="p-3 border">Quy Tắc Nghiệp Vụ (BR) & NFR</th>
                        <th class="p-3 border">Trạng Thái Tương Tác / Callout</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    <tr class="hover:bg-slate-50">
                        <td class="p-3 font-mono font-bold text-indigo-700">WF-01</td>
                        <td class="p-3 font-bold text-slate-900">Cổng Đăng Nhập & Xác Thực Sinh Viên</td>
                        <td class="p-3 font-mono font-semibold">UC-01 (1 dễ)</td>
                        <td class="p-3">Sinh viên nội trú</td>
                        <td class="p-3 font-mono text-slate-600"><span class="font-bold text-indigo-700">BR-01</span> (Trường A), NFR-03, NFR-06</td>
                        <td class="p-3 text-[11px] text-slate-600">Form MSSV + Pass, 3 Persona mẫu 1-click, Checkbox 30 ngày, Modal báo lỗi sai trường.</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                        <td class="p-3 font-mono font-bold text-indigo-700">WF-02</td>
                        <td class="p-3 font-bold text-slate-900">Đăng Ký Loại Phòng & Khảo Sát Thói Quen</td>
                        <td class="p-3 font-mono font-semibold">UC-02 (Nghiệp vụ)</td>
                        <td class="p-3">Sinh viên nội trú</td>
                        <td class="p-3 font-mono text-slate-600"><span class="font-bold text-indigo-700">BR-02</span> (&ge;1 kỳ), <span class="font-bold text-indigo-700">BR-06</span> (Top 1.5x), BR-05</td>
                        <td class="p-3 text-[11px] text-slate-600">3 Thẻ loại phòng kèm giá, 8 Slider thói quen, Dropdown tiêu chí ưu tiên 1.5x, Checkbox cam kết &ge;1 kỳ.</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                        <td class="p-3 font-mono font-bold text-indigo-700">WF-03</td>
                        <td class="p-3 font-bold text-slate-900">Dashboard Thẩm Định Hồ Sơ KTX (Business Approve)</td>
                        <td class="p-3 font-mono font-semibold">UC-03 (Nghiệp vụ)</td>
                        <td class="p-3">Cán bộ KTX / Hệ thống</td>
                        <td class="p-3 font-mono text-slate-600"><span class="font-bold text-indigo-700">BR-01</span>, <span class="font-bold text-indigo-700">BR-02</span>, <span class="font-bold text-indigo-700">BR-03</span> (Approve), BR-05</td>
                        <td class="p-3 text-[11px] text-slate-600">Bảng đơn Pending, Huy hiệu đối soát tự động BR-01/02, Quỹ giường trống, Nút Duyệt, Nút Từ chối nhập lý do.</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                        <td class="p-3 font-mono font-bold text-indigo-700">WF-04</td>
                        <td class="p-3 font-bold text-slate-900">Phân Phòng Gale-Shapley & Tối Ưu Lợi Nhuận</td>
                        <td class="p-3 font-mono font-semibold">UC-04 (Nghiệp vụ)</td>
                        <td class="p-3">Cán bộ KTX / Hệ thống</td>
                        <td class="p-3 font-mono text-slate-600"><span class="font-bold text-indigo-700">BR-05</span> (Occupancy 100%), <span class="font-bold text-indigo-700">BR-07</span> (BP=0), NFR-01, 02</td>
                        <td class="p-3 text-[11px] text-slate-600">Nút chạy GS, Widget BP=0, Widget lấp đầy 100%, Sơ đồ tầng/phòng thực tế, Nút công bố kích hoạt 72h.</td>
                    </tr>
                    <tr class="hover:bg-slate-50">
                        <td class="p-3 font-mono font-bold text-indigo-700">WF-05</td>
                        <td class="p-3 font-bold text-slate-900">Thanh Toán Tiền Phòng & Đặt Cọc Hạn 72 Giờ</td>
                        <td class="p-3 font-mono font-semibold">UC-05 (Nghiệp vụ)</td>
                        <td class="p-3">Sinh viên nội trú</td>
                        <td class="p-3 font-mono text-slate-600"><span class="font-bold text-indigo-700">BR-04</span> (Hạn 72h & cọc 1tr), NFR-03 (TLS 1.3)</td>
                        <td class="p-3 text-[11px] text-slate-600">Đồng hồ đếm ngược 72h, Bảng kê 7tr phòng + 1tr cọc = 8tr, Mã VNPay-QR động, E-Receipt & Thẻ phòng điện tử.</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Callout Quy định nghiệp vụ -->
        <div class="bg-indigo-50 border border-indigo-200 rounded-2xl p-4 text-xs space-y-1.5">
            <span class="font-bold text-indigo-950 uppercase block font-mono">Ý Nghĩa Hệ Thống Quy Tắc Nghiệp Vụ Cốt Lõi (BR):</span>
            <p class="text-slate-700 leading-relaxed">
                • <strong>BR-01 (Đối tượng tiếp nhận):</strong> KTX A chỉ phục vụ sinh viên thuộc Trường ĐH A. Sai trường hệ thống từ chối.<br>
                • <strong>BR-02 (Thời hạn hợp đồng tối thiểu 1 kỳ):</strong> Sinh viên phải cam kết ở $\ge 1$ học kỳ (05 tháng), không hỗ trợ hợp đồng ngắn ngày.<br>
                • <strong>BR-03 (Phê duyệt nghiệp vụ Business Approve):</strong> Đơn đăng ký phải được Cán bộ KTX duyệt thì mới được đưa vào thuật toán phân phòng.<br>
                • <strong>BR-04 (Hạn nộp tiền & Cọc 72h):</strong> Phải hoàn tất nộp tiền phòng + cọc 1tr trong 72h; quá 72h tự động thu hồi phòng cho Waitlist.<br>
                • <strong>BR-05 (Tối ưu lấp đầy phòng):</strong> Lấp đầy 100% giường từng phòng trước khi mở phòng mới để tiết kiệm điện nước & tối đa hóa lợi nhuận.<br>
                • <strong>BR-06 (Trọng số 1.5x):</strong> Tiêu chí thói quen số 1 nhân hệ số 1.5x.<br>
                • <strong>BR-07 (Triệt tiêu cặp chặn):</strong> Số cặp chặn phải bằng 0 (Blocking Pairs = 0).
            </p>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 3: WIREFRAME CHI TIẾT WF-01 (LOGIN & AUTH)               -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-start">
            <div>
                <div class="flex items-center gap-2">
                    <span class="callout-badge bg-indigo-100 text-indigo-800 border border-indigo-300">MÀN HÌNH WF-01</span>
                    <span class="text-xs font-mono font-bold text-slate-500">Ánh xạ UC-01 (Use Case Đơn giản - 1 dễ)</span>
                </div>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Cổng Đăng Nhập & Xác Thực Sinh Viên KTX</h2>
                <p class="text-xs text-slate-500">Cửa ngõ xác thực danh tính sinh viên trường liên kết trước khi vào hệ thống</p>
            </div>
            <div class="text-right text-xs font-mono text-slate-500">
                <span>Ràng buộc: <strong>BR-01</strong>, <strong>NFR-03</strong></span>
            </div>
        </div>

        <!-- Blueprint Mockup -->
        <div class="blueprint-bg border-2 border-slate-400 rounded-2xl p-5 relative overflow-hidden">
            <!-- Browser Header -->
            <div class="bg-slate-200 border border-slate-300 rounded-t-xl px-3 py-1.5 flex items-center justify-between text-xs">
                <div class="flex items-center gap-1.5">
                    <span class="w-2.5 h-2.5 rounded-full bg-rose-400 inline-block"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-amber-400 inline-block"></span>
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block"></span>
                    <span class="ml-2 font-mono text-[10px] text-slate-600 bg-white px-2 py-0.5 rounded border border-slate-300">
                        https://ktx.udn.vn/auth/login
                    </span>
                </div>
                <span class="text-[10px] font-bold text-slate-500 font-mono">PORTAL: STUDENT_AUTH</span>
            </div>

            <!-- Wireframe Canvas Content -->
            <div class="bg-white border-x border-b border-slate-300 p-6 rounded-b-xl space-y-5">
                <!-- Branding -->
                <div class="text-center space-y-1">
                    <div class="w-10 h-10 mx-auto rounded-xl bg-slate-900 text-white flex items-center justify-center font-bold text-lg">🏢</div>
                    <h3 class="text-sm font-extrabold text-slate-900 uppercase">CỔNG DỊCH VỤ NỘI TRÚ KÝ TÚC XÁ ĐẠI HỌC ĐÀ NẴNG</h3>
                    <p class="text-[11px] text-slate-500">Hệ thống ghép bạn cùng phòng thông minh & quản lý hợp đồng lưu trú</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-5 pt-2">
                    <!-- Left: 1-Click Persona Box -->
                    <div class="border-2 border-dashed border-indigo-300 bg-indigo-50/40 rounded-xl p-4 space-y-3 relative">
                        <span class="callout-badge bg-indigo-600 text-white absolute -top-2.5 left-3">
                            [WF-01-C01] AF-01: Persona Nhanh (1-Click)
                        </span>
                        <div class="pt-1">
                            <h4 class="text-xs font-bold text-indigo-950 uppercase">Tài khoản Persona Trải Nghiệm Mẫu</h4>
                            <p class="text-[10px] text-indigo-700">Dành cho sinh viên demo nhanh hoặc chạy thử nghiệm</p>
                        </div>

                        <div class="space-y-2 text-xs">
                            <!-- Persona 1 -->
                            <div class="border border-slate-300 bg-white p-2.5 rounded-lg flex items-center justify-between shadow-sm hover:border-indigo-500">
                                <div class="flex items-center gap-2">
                                    <span class="w-7 h-7 rounded-lg bg-indigo-100 text-indigo-800 flex items-center justify-center font-bold text-[10px]">TB</span>
                                    <div>
                                        <p class="font-bold text-slate-900 text-[11px]">Nguyễn Duy Thái Bảo</p>
                                        <p class="text-[9.5px] text-slate-500">VNUK • Ngủ 22:00 • Học thư viện</p>
                                    </div>
                                </div>
                                <span class="px-2 py-0.5 bg-indigo-600 text-white rounded text-[10px] font-bold">Chọn →</span>
                            </div>

                            <!-- Persona 2 -->
                            <div class="border border-slate-300 bg-white p-2.5 rounded-lg flex items-center justify-between shadow-sm hover:border-amber-500">
                                <div class="flex items-center gap-2">
                                    <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-[10px]">VV</span>
                                    <div>
                                        <p class="font-bold text-slate-900 text-[11px]">Lê Văn Việt</p>
                                        <p class="text-[9.5px] text-slate-500">SPKT • Cú đêm 02:00 • Cơ điện tử</p>
                                    </div>
                                </div>
                                <span class="px-2 py-0.5 bg-amber-600 text-white rounded text-[10px] font-bold">Chọn →</span>
                            </div>

                            <!-- Persona 3 -->
                            <div class="border border-slate-300 bg-white p-2.5 rounded-lg flex items-center justify-between shadow-sm hover:border-emerald-500">
                                <div class="flex items-center gap-2">
                                    <span class="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-[10px]">MQ</span>
                                    <div>
                                        <p class="font-bold text-slate-900 text-[11px]">Lê Minh Quân</p>
                                        <p class="text-[9.5px] text-slate-500">DUE • Healthy • Không hút thuốc</p>
                                    </div>
                                </div>
                                <span class="px-2 py-0.5 bg-emerald-600 text-white rounded text-[10px] font-bold">Chọn →</span>
                            </div>
                        </div>
                    </div>

                    <!-- Right: Form Login Standard -->
                    <div class="border border-slate-300 bg-slate-50 rounded-xl p-4 space-y-3 relative">
                        <span class="callout-badge bg-slate-800 text-white absolute -top-2.5 left-3">
                            [WF-01-C02] BF-02, BF-03: Form Đăng Nhập
                        </span>
                        
                        <div class="space-y-2.5 text-xs pt-1">
                            <div>
                                <label class="block font-bold text-slate-700 mb-0.5 text-[11px]">
                                    [WF-01-C03] Mã sinh viên (MSSV Trường A):
                                </label>
                                <input type="text" value="22VNUK0101" class="w-full bg-white border border-slate-300 rounded px-2.5 py-1 text-slate-800 font-mono text-xs">
                            </div>

                            <div>
                                <label class="block font-bold text-slate-700 mb-0.5 text-[11px]">
                                    [WF-01-C04] Mật khẩu xác thực:
                                </label>
                                <input type="password" value="••••••••••••" class="w-full bg-white border border-slate-300 rounded px-2.5 py-1 text-slate-800 font-mono text-xs">
                            </div>

                            <div class="flex items-center justify-between pt-1">
                                <label class="flex items-center gap-1.5 cursor-pointer text-[11px] text-slate-600">
                                    <input type="checkbox" checked class="rounded text-indigo-600">
                                    <span>[WF-01-C05] Ghi nhớ 30 ngày (AF-01)</span>
                                </label>
                                <span class="text-[10px] text-indigo-600 hover:underline cursor-pointer">Quên mật khẩu?</span>
                            </div>

                            <button class="w-full py-2 bg-slate-900 hover:bg-slate-800 text-white font-extrabold rounded-lg text-xs shadow">
                                [WF-01-C06] ĐĂNG NHẬP VÀO HỆ THỐNG (BF-03)
                            </button>
                        </div>

                        <!-- EF Alerts -->
                        <div class="space-y-1.5 pt-2 border-t border-slate-200">
                            <div class="p-2 bg-rose-50 border border-rose-300 rounded text-[10px] text-rose-800 flex items-start gap-1.5">
                                <span>⚠️</span>
                                <div>
                                    <span class="font-bold">[WF-01-C07] Alert EF-02 (BR-01):</span> Sinh viên không thuộc Trường Đại học A sẽ bị hệ thống từ chối đăng nhập.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Component Dictionary Table -->
        <div class="overflow-x-auto avoid-break">
            <span class="font-bold text-slate-800 text-xs block mb-1 uppercase font-mono">Từ Điển Thành Phần Giao Diện Màn Hình WF-01:</span>
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[11px] uppercase">
                    <tr>
                        <th class="p-2 border">Mã Callout</th>
                        <th class="p-2 border">Kiểu Thành Phần</th>
                        <th class="p-2 border">Tên Phần Tử</th>
                        <th class="p-2 border">Mô Tả & Ràng Buộc Nghiệp Vụ</th>
                        <th class="p-2 border">Tham Chiếu Bước</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">WF-01-C01</td><td class="p-2">Persona Cards</td><td class="p-2 font-semibold">Bộ 3 tài khoản mẫu</td><td class="p-2">Nạp nhanh dữ liệu sinh viên mẫu, không cần nhập thủ công.</td><td class="p-2 font-mono text-indigo-700">AF-01, NFR-06</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C02</td><td class="p-2">Form Container</td><td class="p-2 font-semibold">Khung đăng nhập chính</td><td class="p-2">Chứa các trường thông tin đăng nhập bắt buộc.</td><td class="p-2 font-mono text-indigo-700">BF-02</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C03</td><td class="p-2">Text Input</td><td class="p-2 font-semibold">Ô nhập MSSV</td><td class="p-2">Bắt buộc định dạng MSSV trường A. Kiểm tra theo BR-01.</td><td class="p-2 font-mono text-indigo-700">BF-03, BR-01</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C04</td><td class="p-2">Password Input</td><td class="p-2 font-semibold">Ô nhập Mật khẩu</td><td class="p-2">Bảo mật ký tự, kiểm tra hash mật khẩu trong DB.</td><td class="p-2 font-mono text-indigo-700">BF-03, NFR-03</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C05</td><td class="p-2">Checkbox</td><td class="p-2 font-semibold">Ghi nhớ đăng nhập</td><td class="p-2">Gia hạn thời gian lưu phiên HttpOnly lên 30 ngày thay vì 2h.</td><td class="p-2 font-mono text-indigo-700">AF-01, AF-02</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C06</td><td class="p-2">Submit Button</td><td class="p-2 font-semibold">Nút Đăng nhập</td><td class="p-2">Gửi credentials sang Auth Service để xác thực danh tính.</td><td class="p-2 font-mono text-indigo-700">BF-04</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-01-C07</td><td class="p-2">Alert Modal</td><td class="p-2 font-semibold">Cảnh báo lỗi vi phạm BR-01</td><td class="p-2">Xuất thông báo từ chối khi MSSV không thuộc trường liên kết.</td><td class="p-2 font-mono text-rose-700 font-bold">EF-02, BR-01</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 4: WIREFRAME CHI TIẾT WF-02 (SURVEY & PREFERENCES)       -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-start">
            <div>
                <div class="flex items-center gap-2">
                    <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">MÀN HÌNH WF-02</span>
                    <span class="text-xs font-mono font-bold text-slate-500">Ánh xạ UC-02 (Use Case Nghiệp vụ Quan trọng)</span>
                </div>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Đăng Ký Loại Phòng, Khảo Sát Thói Quen & Cam Kết Lưu Trú</h2>
                <p class="text-xs text-slate-500">Thu thập vector 8 tiêu chí thói quen sinh hoạt và cam kết hợp đồng tối thiểu 1 kỳ</p>
            </div>
            <div class="text-right text-xs font-mono text-slate-500">
                <span>Ràng buộc: <strong>BR-02</strong>, <strong>BR-06</strong></span>
            </div>
        </div>

        <!-- Blueprint Mockup -->
        <div class="blueprint-bg border-2 border-slate-400 rounded-2xl p-5 relative overflow-hidden">
            <div class="bg-white border border-slate-300 p-5 rounded-xl space-y-5">
                
                <!-- Stepper -->
                <div class="flex items-center justify-between max-w-xl mx-auto text-xs pb-2 border-b border-slate-200">
                    <div class="flex items-center gap-1.5 text-indigo-600 font-bold">
                        <span class="w-5 h-5 rounded-full bg-indigo-600 text-white flex items-center justify-center text-[10px]">1</span>
                        <span>Chọn Phòng</span>
                    </div>
                    <span class="w-8 h-0.5 bg-indigo-600"></span>
                    <div class="flex items-center gap-1.5 text-indigo-600 font-bold">
                        <span class="w-5 h-5 rounded-full bg-indigo-600 text-white flex items-center justify-center text-[10px]">2</span>
                        <span>8 Tiêu Chí</span>
                    </div>
                    <span class="w-8 h-0.5 bg-slate-300"></span>
                    <div class="flex items-center gap-1.5 text-slate-400 font-bold">
                        <span class="w-5 h-5 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center text-[10px]">3</span>
                        <span>Cam Kết BR-02</span>
                    </div>
                </div>

                <!-- 1. Chọn loại phòng (BF-02, BF-03, BR-05) -->
                <div class="space-y-2">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-800 uppercase font-mono">
                            [WF-02-C01] BF-02, BF-03: Chọn Gói Phòng Nguyện Vọng (BR-05)
                        </label>
                        <span class="text-[10px] text-slate-500">Đơn vị: VNĐ / Sinh viên / Tháng</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                        <!-- VIP 2 -->
                        <div class="border-2 border-indigo-600 bg-indigo-50/60 p-3 rounded-xl space-y-1 relative">
                            <span class="callout-badge bg-indigo-600 text-white absolute -top-2 right-2">LỰA CHỌN</span>
                            <div class="flex justify-between items-center">
                                <span class="font-bold text-indigo-950">Phòng 2 Người (VIP)</span>
                                <input type="radio" checked name="wf2-room" class="text-indigo-600">
                            </div>
                            <p class="text-indigo-700 font-mono font-black text-sm">1.400.000 đ/tháng</p>
                            <p class="text-[10px] text-slate-500 leading-tight">Điều hòa Inverter, WC khép kín, 2 bàn học riêng biệt.</p>
                        </div>

                        <!-- 4 người -->
                        <div class="border border-slate-300 bg-slate-50 p-3 rounded-xl space-y-1">
                            <div class="flex justify-between items-center">
                                <span class="font-bold text-slate-800">Phòng 4 Người (Chuẩn)</span>
                                <input type="radio" name="wf2-room" class="text-indigo-600">
                            </div>
                            <p class="text-slate-700 font-mono font-bold text-sm">850.000 đ/tháng</p>
                            <p class="text-[10px] text-slate-500 leading-tight">Giường tầng cao cấp, tủ đồ khóa từ cá nhân.</p>
                        </div>

                        <!-- 6 người -->
                        <div class="border border-slate-300 bg-slate-50 p-3 rounded-xl space-y-1">
                            <div class="flex justify-between items-center">
                                <span class="font-bold text-slate-800">Phòng 6 Người (Tiết kiệm)</span>
                                <input type="radio" name="wf2-room" class="text-indigo-600">
                            </div>
                            <p class="text-slate-700 font-mono font-bold text-sm">550.000 đ/tháng</p>
                            <p class="text-[10px] text-slate-500 leading-tight">Phù hợp tân sinh viên, khu học tập cộng đồng.</p>
                        </div>
                    </div>
                </div>

                <!-- 2. Tiêu chí số 1 nhân hệ số 1.5x (BF-05, BR-06) -->
                <div class="bg-amber-50/80 border border-amber-300 p-3.5 rounded-xl space-y-1.5">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-amber-950">
                            [WF-02-C02] BF-05: Tiêu Chí Ưu Tiên Số 1 Của Bạn (Quy định BR-06 - Hệ số 1.5x):
                        </label>
                        <span class="callout-badge bg-amber-200 text-amber-900 border border-amber-400">TRỌNG SỐ x1.5</span>
                    </div>
                    <select class="w-full bg-white border border-amber-400 rounded px-2.5 py-1 text-xs text-amber-950 font-bold">
                        <option selected>Giờ đi ngủ (sleep) - Ưu tiên hàng đầu phòng ngủ sớm và yên tĩnh</option>
                        <option>Độ gọn gàng ngăn nắp (tidy) - Tuyệt đối không để đồ bừa bộn</option>
                        <option>Không hút thuốc lá (smoke) - Dị ứng khói thuốc</option>
                        <option>Mức chịu tiếng ồn (noise) - Cần không gian tĩnh lặng</option>
                    </select>
                </div>

                <!-- 3. Form 8 Tiêu chí thói quen (BF-04) -->
                <div class="border border-slate-300 rounded-xl p-4 bg-slate-50 space-y-3 text-xs">
                    <span class="font-bold text-slate-800 block uppercase font-mono text-[11px]">
                        [WF-02-C03] BF-04: Khảo Sát Nếp Sống Sinh Hoạt (8 Tiêu Chí Chuẩn Hóa):
                    </span>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <!-- Tiêu chí 1: Giờ ngủ -->
                        <div class="bg-white p-2.5 rounded-lg border border-slate-200 space-y-1">
                            <div class="flex justify-between font-bold text-slate-700 text-[11px]">
                                <span>🌙 Giờ đi ngủ (sleep):</span>
                                <span class="text-indigo-600 font-mono">22:00 (10:00 PM)</span>
                            </div>
                            <input type="range" class="w-full accent-indigo-600" value="22" min="20" max="28">
                        </div>

                        <!-- Tiêu chí 2: Giờ dậy -->
                        <div class="bg-white p-2.5 rounded-lg border border-slate-200 space-y-1">
                            <div class="flex justify-between font-bold text-slate-700 text-[11px]">
                                <span>⏰ Giờ thức dậy (wake):</span>
                                <span class="text-indigo-600 font-mono">06:00 (AM)</span>
                            </div>
                            <input type="range" class="w-full accent-indigo-600" value="6" min="5" max="11">
                        </div>

                        <!-- Tiêu chí 3: Gọn gàng -->
                        <div class="bg-white p-2.5 rounded-lg border border-slate-200 space-y-1">
                            <div class="flex justify-between font-bold text-slate-700 text-[11px]">
                                <span>🧹 Độ gọn gàng (tidy):</span>
                                <span class="text-indigo-600 font-mono">5/5 (Rất ngăn nắp)</span>
                            </div>
                            <input type="range" class="w-full accent-indigo-600" value="5" min="1" max="5">
                        </div>

                        <!-- Tiêu chí 4: Tiếng ồn -->
                        <div class="bg-white p-2.5 rounded-lg border border-slate-200 space-y-1">
                            <div class="flex justify-between font-bold text-slate-700 text-[11px]">
                                <span>🔊 Chịu tiếng ồn (noise):</span>
                                <span class="text-indigo-600 font-mono">1/5 (Cần tĩnh lặng)</span>
                            </div>
                            <input type="range" class="w-full accent-indigo-600" value="1" min="1" max="5">
                        </div>
                    </div>
                </div>

                <!-- 4. Cam kết hợp đồng KTX >= 1 kỳ (BF-06, BR-02) -->
                <div class="bg-indigo-50 border-2 border-indigo-400 p-3.5 rounded-xl space-y-2">
                    <span class="callout-badge bg-indigo-700 text-white">
                        [WF-02-C04] BF-06: Cam Kết Thời Hạn Lưu Trú Bắt Buộc (BR-02)
                    </span>
                    <label class="flex items-start gap-2 cursor-pointer">
                        <input type="checkbox" checked class="mt-0.5 rounded text-indigo-600 w-4 h-4">
                        <span class="text-[11px] text-indigo-950 font-bold leading-relaxed">
                            Tôi cam kết đăng ký lưu trú tại KTX tối thiểu 01 học kỳ (05 tháng) theo Quy tắc nghiệp vụ BR-02. Nếu đơn phương hủy hợp đồng trước hạn 1 kỳ, tôi chấp nhận mất toàn bộ tiền đặt cọc giữ chỗ.
                        </span>
                    </label>
                </div>

                <button class="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold rounded-xl text-xs shadow-lg">
                    [WF-02-C05] NỘP HỒ SƠ ĐĂNG KÝ PHÒNG & THÓI QUEN (BF-07)
                </button>
            </div>
        </div>

        <!-- Component Dictionary Table -->
        <div class="overflow-x-auto avoid-break">
            <span class="font-bold text-slate-800 text-xs block mb-1 uppercase font-mono">Từ Điển Thành Phần Giao Diện Màn Hình WF-02:</span>
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[11px] uppercase">
                    <tr>
                        <th class="p-2 border">Mã Callout</th>
                        <th class="p-2 border">Kiểu Thành Phần</th>
                        <th class="p-2 border">Tên Phần Tử</th>
                        <th class="p-2 border">Mô Tả & Ràng Buộc Nghiệp Vụ</th>
                        <th class="p-2 border">Tham Chiếu Bước</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">WF-02-C01</td><td class="p-2">Radio Cards</td><td class="p-2 font-semibold">Gói phòng 2/4/6 người</td><td class="p-2">Phân loại đối tượng theo nhu cầu tài chính và loại phòng.</td><td class="p-2 font-mono text-indigo-700">BF-02, BR-05</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-02-C02</td><td class="p-2">Select Dropdown</td><td class="p-2 font-semibold">Tiêu chí quan trọng nhất</td><td class="p-2">Nhân trọng số 1.5x cho tiêu chí được chọn để tạo ma trận tương thích.</td><td class="p-2 font-mono text-indigo-700">BF-05, BR-06</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-02-C03</td><td class="p-2">Sliders Group</td><td class="p-2 font-semibold">8 Thanh trượt thói quen</td><td class="p-2">Chuẩn hóa điểm số thói quen về vector số học đầu vào.</td><td class="p-2 font-mono text-indigo-700">BF-04</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-02-C04</td><td class="p-2">Checkbox Cam Kết</td><td class="p-2 font-semibold">Cam kết ở tối thiểu 1 kỳ</td><td class="p-2">Bắt buộc phải tích chọn. Nếu không tích, khóa nút nộp theo EF-01.</td><td class="p-2 font-mono text-rose-700 font-bold">BF-06, BR-02, EF-01</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-02-C05</td><td class="p-2">Action Button</td><td class="p-2 font-semibold">Nút Nộp Hồ Sơ Đăng Ký</td><td class="p-2">Gửi hồ sơ vào trạng thái Pending_Approval để chuyển sang UC-03.</td><td class="p-2 font-mono text-indigo-700">BF-07</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 5: WIREFRAME CHI TIẾT WF-03 (BUSINESS APPROVE)           -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-start">
            <div>
                <div class="flex items-center gap-2">
                    <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">MÀN HÌNH WF-03</span>
                    <span class="text-xs font-mono font-bold text-slate-500">Ánh xạ UC-03 (Use Case Nghiệp vụ Quan trọng)</span>
                </div>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Dashboard Thẩm Định Hồ Sơ KTX (Business Approve)</h2>
                <p class="text-xs text-slate-500">Cổng thẩm định nghiệp vụ dành cho Cán bộ Quản trị KTX trước khi xếp phòng</p>
            </div>
            <div class="text-right text-xs font-mono text-slate-500">
                <span>Ràng buộc: <strong>BR-01</strong>, <strong>BR-02</strong>, <strong>BR-03</strong></span>
            </div>
        </div>

        <!-- Blueprint Mockup -->
        <div class="blueprint-bg border-2 border-slate-400 rounded-2xl p-5 relative overflow-hidden">
            <div class="bg-white border border-slate-300 p-5 rounded-xl space-y-4">
                
                <!-- KPI Bar -->
                <div class="grid grid-cols-1 md:grid-cols-4 gap-3 text-xs">
                    <div class="bg-slate-50 p-3 rounded-xl border border-slate-300">
                        <span class="text-slate-500 block text-[10px]">Tổng đơn đăng ký:</span>
                        <span class="text-lg font-bold text-slate-900 font-mono">148 Đơn</span>
                    </div>
                    <div class="bg-amber-50 p-3 rounded-xl border border-amber-300">
                        <span class="text-amber-800 block text-[10px]">Chờ duyệt (Pending):</span>
                        <span class="text-lg font-bold text-amber-900 font-mono">24 Đơn</span>
                    </div>
                    <div class="bg-emerald-50 p-3 rounded-xl border border-emerald-300">
                        <span class="text-emerald-800 block text-[10px]">Quỹ giường trống:</span>
                        <span class="text-lg font-bold text-emerald-900 font-mono">120 Giường (BR-05)</span>
                    </div>
                    <div class="flex items-center">
                        <button class="w-full py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl text-xs shadow">
                            [WF-03-C01] Duyệt Hàng Loạt (AF-01)
                        </button>
                    </div>
                </div>

                <!-- Bảng danh sách thẩm định -->
                <div class="border border-slate-300 rounded-xl overflow-hidden text-xs">
                    <div class="bg-slate-100 px-4 py-2 font-bold text-slate-800 flex justify-between items-center">
                        <span class="font-mono uppercase text-[11px]">[WF-03-C02] BF-02: Danh Sách Hồ Sơ Chờ Phê Duyệt Nghiệp Vụ</span>
                        <span class="text-[10px] text-slate-500">Đối soát tự động hệ thống API</span>
                    </div>
                    <table class="w-full text-left">
                        <thead class="bg-slate-50 border-b border-slate-200 text-slate-500 text-[10px] uppercase font-bold">
                            <tr>
                                <th class="p-2.5">Mã SV & Tên</th>
                                <th class="p-2.5">Trường (BR-01)</th>
                                <th class="p-2.5">Loại Phòng</th>
                                <th class="p-2.5">Cam Kết (BR-02)</th>
                                <th class="p-2.5">Kỷ Luật / Nợ Phí</th>
                                <th class="p-2.5 text-right">Thao Tác Thẩm Định (BR-03)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 text-[11px]">
                            <!-- Row 1 -->
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5">
                                    <p class="font-bold text-slate-900">Nguyễn Duy Thái Bảo</p>
                                    <p class="text-[9.5px] text-slate-500 font-mono">22VNUK0101</p>
                                </td>
                                <td class="p-2.5"><span class="px-1.5 py-0.5 bg-emerald-100 text-emerald-800 rounded font-bold text-[9.5px]">VNUK (Hợp lệ)</span></td>
                                <td class="p-2.5 font-semibold">Phòng 2 Người</td>
                                <td class="p-2.5 text-emerald-700 font-bold">✓ Đủ 1 Kỳ (5T)</td>
                                <td class="p-2.5 text-emerald-700 font-bold">✓ Tốt (0 vi phạm)</td>
                                <td class="p-2.5 text-right space-x-1">
                                    <button class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded shadow-sm text-[10px]">
                                        [WF-03-C03] Duyệt (BR-03)
                                    </button>
                                    <button class="px-2 py-1 bg-rose-100 text-rose-700 font-bold rounded text-[10px]">
                                        Từ chối
                                    </button>
                                </td>
                            </tr>

                            <!-- Row 2 -->
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5">
                                    <p class="font-bold text-slate-900">Lê Văn Việt</p>
                                    <p class="text-[9.5px] text-slate-500 font-mono">21SPKT0205</p>
                                </td>
                                <td class="p-2.5"><span class="px-1.5 py-0.5 bg-emerald-100 text-emerald-800 rounded font-bold text-[9.5px]">SPKT (Hợp lệ)</span></td>
                                <td class="p-2.5 font-semibold">Phòng 2 Người</td>
                                <td class="p-2.5 text-emerald-700 font-bold">✓ Đủ 1 Kỳ (5T)</td>
                                <td class="p-2.5 text-emerald-700 font-bold">✓ Tốt (0 vi phạm)</td>
                                <td class="p-2.5 text-right space-x-1">
                                    <button class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded shadow-sm text-[10px]">
                                        [WF-03-C03] Duyệt (BR-03)
                                    </button>
                                    <button class="px-2 py-1 bg-rose-100 text-rose-700 font-bold rounded text-[10px]">
                                        Từ chối
                                    </button>
                                </td>
                            </tr>

                            <!-- Row 3: Vi phạm -->
                            <tr class="bg-rose-50/40">
                                <td class="p-2.5">
                                    <p class="font-bold text-slate-900">Trần Văn C</p>
                                    <p class="text-[9.5px] text-slate-500 font-mono">23OTHER99</p>
                                </td>
                                <td class="p-2.5"><span class="px-1.5 py-0.5 bg-rose-100 text-rose-800 rounded font-bold text-[9.5px]">Trường Ngoài (Sai)</span></td>
                                <td class="p-2.5 font-semibold">Phòng 4 Người</td>
                                <td class="p-2.5 text-rose-600 font-bold">✗ Chưa cam kết</td>
                                <td class="p-2.5 text-rose-600 font-bold">✗ Vi phạm BR-01</td>
                                <td class="p-2.5 text-right">
                                    <button class="px-2.5 py-1 bg-rose-600 hover:bg-rose-700 text-white font-bold rounded shadow-sm text-[10px]">
                                        [WF-03-C04] Từ Chối (EF-01)
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Component Dictionary Table -->
        <div class="overflow-x-auto avoid-break">
            <span class="font-bold text-slate-800 text-xs block mb-1 uppercase font-mono">Từ Điển Thành Phần Giao Diện Màn Hình WF-03:</span>
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[11px] uppercase">
                    <tr>
                        <th class="p-2 border">Mã Callout</th>
                        <th class="p-2 border">Kiểu Thành Phần</th>
                        <th class="p-2 border">Tên Phần Tử</th>
                        <th class="p-2 border">Mô Tả & Ràng Buộc Nghiệp Vụ</th>
                        <th class="p-2 border">Tham Chiếu Bước</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">WF-03-C01</td><td class="p-2">Batch Action Button</td><td class="p-2 font-semibold">Nút Duyệt hàng loạt</td><td class="p-2">Tự động duyệt tất cả hồ sơ đã có tích xanh BR-01 và BR-02.</td><td class="p-2 font-mono text-indigo-700">AF-01, NFR-06</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-03-C02</td><td class="p-2">Data Table</td><td class="p-2 font-semibold">Bảng hồ sơ thẩm định</td><td class="p-2">Hiển thị danh sách hồ sơ trạng thái Pending kèm kết quả đối soát.</td><td class="p-2 font-mono text-indigo-700">BF-02</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-03-C03</td><td class="p-2">Approve Button</td><td class="p-2 font-semibold">Nút Phê duyệt (Approve)</td><td class="p-2">Chuyển trạng thái sang Approved_For_Matching theo BR-03.</td><td class="p-2 font-mono text-emerald-700 font-bold">BF-05, BR-03</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-03-C04</td><td class="p-2">Reject Button</td><td class="p-2 font-semibold">Nút Từ chối (Reject)</td><td class="p-2">Mở modal nhập lý do vi phạm (BR-01, kỷ luật) và gửi email từ chối.</td><td class="p-2 font-mono text-rose-700 font-bold">EF-01, BR-03</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 6: WIREFRAME CHI TIẾT WF-04 (GALE-SHAPLEY & OCCUPANCY)   -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-start">
            <div>
                <div class="flex items-center gap-2">
                    <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">MÀN HÌNH WF-04</span>
                    <span class="text-xs font-mono font-bold text-slate-500">Ánh xạ UC-04 (Use Case Nghiệp vụ Quan trọng)</span>
                </div>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Bảng Điều Khiển Gale-Shapley & Tối Ưu Lấp Đầy Phòng (Occupancy)</h2>
                <p class="text-xs text-slate-500">Thuật toán ghép cặp ổn định triệt tiêu cặp chặn = 0 và tối đa hóa biên lợi nhuận KTX</p>
            </div>
            <div class="text-right text-xs font-mono text-slate-500">
                <span>Ràng buộc: <strong>BR-05</strong>, <strong>BR-07</strong></span>
            </div>
        </div>

        <!-- Blueprint Mockup -->
        <div class="blueprint-bg border-2 border-slate-400 rounded-2xl p-5 relative overflow-hidden">
            <div class="space-y-4">
                
                <!-- 3 Metric Widgets Đỉnh Cao -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                    <div class="bg-white border border-slate-300 rounded-xl p-3.5 space-y-1.5">
                        <span class="font-bold text-slate-700 block uppercase font-mono text-[10px]">[WF-04-C01] Động Cơ Thuật Toán:</span>
                        <button class="w-full py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold rounded-lg shadow text-xs">
                            ▶ KHỞI CHẠY GALE-SHAPLEY (BF-01)
                        </button>
                        <span class="text-[9.5px] text-slate-500 block text-center font-mono">Thời gian chạy: 0.12s (NFR-01 &lt; 1.0s)</span>
                    </div>

                    <div class="bg-emerald-50 border-2 border-emerald-400 rounded-xl p-3 text-center space-y-0.5">
                        <span class="callout-badge bg-emerald-200 text-emerald-900">
                            [WF-04-C02] BF-07: ỔN ĐỊNH TOÁN HỌC (BR-07)
                        </span>
                        <div class="text-2xl font-black text-emerald-700 font-mono">0 CẶP CHẶN</div>
                        <span class="text-[10px] text-emerald-600 font-bold">Blocking Pairs = 0 (Tuyệt đối ổn định)</span>
                    </div>

                    <div class="bg-sky-50 border-2 border-sky-400 rounded-xl p-3 text-center space-y-0.5">
                        <span class="callout-badge bg-sky-200 text-sky-900">
                            [WF-04-C03] BF-08: LẤP ĐẦY PHÒNG (BR-05)
                        </span>
                        <div class="text-2xl font-black text-sky-700 font-mono">100% LẤP ĐẦY</div>
                        <span class="text-[10px] text-sky-600 font-bold">Triệt tiêu phòng trống dở dang</span>
                    </div>
                </div>

                <!-- Bảng Danh Sách Phân Phòng Thực Tế -->
                <div class="bg-white border border-slate-300 rounded-xl overflow-hidden text-xs">
                    <div class="bg-slate-100 px-4 py-2.5 flex justify-between items-center border-b border-slate-200">
                        <span class="font-mono uppercase font-bold text-[11px] text-slate-800">
                            [WF-04-C04] BF-06, BF-08: Kết Quả Xếp Phòng Chính Thức (Tầng 2 & Tầng 3)
                        </span>
                        <div class="flex gap-2">
                            <button class="px-2.5 py-1 bg-slate-800 text-white rounded text-[10px] font-bold">
                                📥 Xuất CSV (BF-09)
                            </button>
                            <button class="px-2.5 py-1 bg-emerald-600 text-white rounded text-[10px] font-bold">
                                📢 Công Bố 72h (BF-09)
                            </button>
                        </div>
                    </div>

                    <div class="p-3.5 space-y-2.5">
                        <!-- Phòng P.201 -->
                        <div class="border border-slate-200 rounded-xl p-3 bg-slate-50 flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <span class="px-2.5 py-1 bg-indigo-600 text-white font-mono font-bold rounded-lg text-xs">Phòng P.201 (VIP)</span>
                                <div>
                                    <p class="font-bold text-slate-900 text-xs">Nguyễn Duy Thái Bảo (VNUK) + Lê Minh Quân (DUE)</p>
                                    <p class="text-[10.5px] text-slate-500">Điểm chung: Cùng ngủ trước 23:00, phòng yên tĩnh, không khói thuốc.</p>
                                </div>
                            </div>
                            <div class="text-right">
                                <span class="text-xs font-black text-emerald-600 font-mono">88.5% HÒA HỢP</span>
                                <span class="block text-[9.5px] text-slate-400">Trạng thái: Đã chốt</span>
                            </div>
                        </div>

                        <!-- Phòng P.202 -->
                        <div class="border border-slate-200 rounded-xl p-3 bg-slate-50 flex items-center justify-between">
                            <div class="flex items-center gap-3">
                                <span class="px-2.5 py-1 bg-indigo-600 text-white font-mono font-bold rounded-lg text-xs">Phòng P.202 (VIP)</span>
                                <div>
                                    <p class="font-bold text-slate-900 text-xs">Lê Văn Việt (SPKT) + Trần Minh Đăng (Bách Khoa)</p>
                                    <p class="text-[10.5px] text-slate-500">Điểm chung: Cú đêm làm đồ án cơ điện tử & mạch kỹ thuật.</p>
                                </div>
                            </div>
                            <div class="text-right">
                                <span class="text-xs font-black text-emerald-600 font-mono">82.1% HÒA HỢP</span>
                                <span class="block text-[9.5px] text-slate-400">Trạng thái: Đã chốt</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Component Dictionary Table -->
        <div class="overflow-x-auto avoid-break">
            <span class="font-bold text-slate-800 text-xs block mb-1 uppercase font-mono">Từ Điển Thành Phần Giao Diện Màn Hình WF-04:</span>
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[11px] uppercase">
                    <tr>
                        <th class="p-2 border">Mã Callout</th>
                        <th class="p-2 border">Kiểu Thành Phần</th>
                        <th class="p-2 border">Tên Phần Tử</th>
                        <th class="p-2 border">Mô Tả & Ràng Buộc Nghiệp Vụ</th>
                        <th class="p-2 border">Tham Chiếu Bước</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">WF-04-C01</td><td class="p-2">Trigger Button</td><td class="p-2 font-semibold">Khởi chạy Gale-Shapley</td><td class="p-2">Kích hoạt engine tính toán điểm và ghép cặp tự động.</td><td class="p-2 font-mono text-indigo-700">BF-01, NFR-01</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-04-C02</td><td class="p-2">Metric Card</td><td class="p-2 font-semibold">Huy hiệu 0 Cặp Chặn</td><td class="p-2">Kiểm chứng số cặp chặn = 0, đảm bảo tính ổn định toán học.</td><td class="p-2 font-mono text-emerald-700 font-bold">BF-07, BR-07, NFR-02</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-04-C03</td><td class="p-2">Metric Card</td><td class="p-2 font-semibold">Widget Lấp Đầy 100%</td><td class="p-2">Ưu tiên lấp đầy 100% số giường phòng trước khi mở phòng mới.</td><td class="p-2 font-mono text-sky-700 font-bold">BF-08, BR-05</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-04-C04</td><td class="p-2">Room Layout List</td><td class="p-2 font-semibold">Danh sách phân phòng</td><td class="p-2">Hiển thị các cặp sinh viên kèm điểm tương thích và nút xuất báo cáo.</td><td class="p-2 font-mono text-indigo-700">BF-06, BF-09</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 7: WIREFRAME CHI TIẾT WF-05 (PAYMENT & 72H DEPOSIT)      -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-start">
            <div>
                <div class="flex items-center gap-2">
                    <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">MÀN HÌNH WF-05</span>
                    <span class="text-xs font-mono font-bold text-slate-500">Ánh xạ UC-05 (Use Case Nghiệp vụ Quan trọng)</span>
                </div>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Cổng Thanh Toán Tiền Phòng & Đặt Cọc Giữ Chỗ (Hạn 72 Giờ)</h2>
                <p class="text-xs text-slate-500">Thanh toán bảo mật tiền phòng học kỳ 1 và tiền cọc cơ sở vật chất qua Cổng VNPay</p>
            </div>
            <div class="text-right text-xs font-mono text-slate-500">
                <span>Ràng buộc: <strong>BR-04</strong>, <strong>NFR-03</strong></span>
            </div>
        </div>

        <!-- Blueprint Mockup -->
        <div class="blueprint-bg border-2 border-slate-400 rounded-2xl p-5 relative overflow-hidden">
            <div class="bg-white border border-slate-300 rounded-xl overflow-hidden space-y-4">
                
                <!-- Top Header With 72h Countdown -->
                <div class="bg-slate-900 text-white p-4 flex justify-between items-center text-xs">
                    <div>
                        <span class="text-[9.5px] font-mono font-bold px-2 py-0.5 rounded bg-amber-400 text-slate-950 uppercase">
                            XÁC NHẬN GIỮ CHỖ PHÒNG KTX
                        </span>
                        <h3 class="text-sm font-extrabold mt-0.5">Cổng Thanh Toán Tiền Phòng Học Kỳ 1 & Cọc Cơ Sở Vật Chất</h3>
                    </div>

                    <!-- Countdown -->
                    <div class="bg-rose-600 border border-rose-400 px-3 py-1.5 rounded-xl text-center">
                        <span class="text-[9px] uppercase font-bold block text-rose-100">[WF-05-C01] HẠN CHÓT 72H (BR-04):</span>
                        <span class="text-base font-mono font-black tracking-wider">71:48:22</span>
                    </div>
                </div>

                <div class="p-5 space-y-4 text-xs">
                    <!-- Phòng đã trúng tuyển -->
                    <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-3 flex justify-between items-center">
                        <div>
                            <span class="font-bold text-indigo-950 block text-xs">KẾT QUẢ PHÂN PHÒNG CHÍNH THỨC:</span>
                            <p class="text-slate-600 mt-0.5 text-[11px]">Phòng: <strong>P.201 - Tòa Nhà A</strong> (Phòng 2 Người VIP)</p>
                            <p class="text-slate-600 text-[11px]">Bạn cùng phòng: <strong>Lê Minh Quân (DUE)</strong> • Độ hòa hợp: <strong>88.5%</strong></p>
                        </div>
                        <span class="px-2.5 py-1 bg-indigo-600 text-white rounded font-mono font-bold text-xs">Giường 01</span>
                    </div>

                    <!-- Bảng kê viện phí nội trú (BF-02, BR-04) -->
                    <div class="border border-slate-300 rounded-xl overflow-hidden">
                        <div class="bg-slate-100 px-3.5 py-1.5 font-bold text-slate-800 text-[11px]">
                            [WF-05-C02] BF-02: Bảng Kê Chi Phí Học Kỳ 1 (Quy định BR-04)
                        </div>
                        <div class="p-3.5 space-y-2 text-[11px]">
                            <div class="flex justify-between border-b border-slate-100 pb-1.5">
                                <span class="text-slate-600">1. Tiền phòng Học kỳ 1 (05 tháng x 1.400.000 đ):</span>
                                <span class="font-mono font-bold text-slate-900">7.000.000 VNĐ</span>
                            </div>
                            <div class="flex justify-between border-b border-slate-100 pb-1.5">
                                <div>
                                    <span class="text-slate-600">2. Tiền đặt cọc bảo đảm tài sản cơ sở vật chất (BR-04):</span>
                                    <span class="block text-[9.5px] text-slate-400">Hoàn trả khi kết thúc hợp đồng nếu không có hư hỏng tài sản</span>
                                </div>
                                <span class="font-mono font-bold text-amber-700">1.000.000 VNĐ</span>
                            </div>
                            <div class="flex justify-between pt-1 text-xs font-extrabold">
                                <span class="text-slate-900">TỔNG CỘNG THANH TOÁN:</span>
                                <span class="font-mono text-indigo-600 text-sm">8.000.000 VNĐ</span>
                            </div>
                        </div>
                    </div>

                    <!-- Phương thức thanh toán VNPAY-QR (BF-04, BF-05, NFR-03) -->
                    <div class="border border-slate-300 rounded-xl p-4 bg-slate-50 space-y-3">
                        <span class="font-bold text-slate-800 block uppercase font-mono text-[10px]">
                            [WF-05-C03] BF-04, BF-05: Quét Mã VNPAY-QR Thanh Toán Bảo Mật (TLS 1.3):
                        </span>

                        <div class="flex flex-col md:flex-row items-center justify-around gap-4 bg-white p-3.5 rounded-xl border border-slate-200">
                            <!-- QR Mockup -->
                            <div class="text-center space-y-1.5">
                                <div class="w-32 h-32 mx-auto bg-slate-100 border-2 border-dashed border-indigo-400 rounded-xl p-2 flex items-center justify-center">
                                    <div class="w-24 h-24 bg-slate-900 rounded-lg flex items-center justify-center text-white text-[10px] font-mono text-center p-1 leading-tight">
                                        [VNPAY-QR 8.000.000đ]
                                    </div>
                                </div>
                                <span class="text-[9.5px] text-slate-500 font-semibold block">Hỗ trợ 40+ Ngân hàng & Ví điện tử</span>
                            </div>

                            <!-- Payment Steps -->
                            <div class="space-y-2 max-w-sm text-[10.5px]">
                                <p class="text-slate-600">1. Mở ứng dụng Mobile Banking (Vietcombank, BIDV, MBBank...) hoặc Ví VNPay.</p>
                                <p class="text-slate-600">2. Quét mã QR và kiểm tra số tiền đúng 8.000.000 VNĐ.</p>
                                <p class="text-slate-600">3. Hệ thống kích hoạt trạng thái "Paid" và cấp hợp đồng điện tử có mã QR.</p>
                                <button class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-lg shadow text-xs">
                                    [WF-05-C04] Giả Lập Thanh Toán Thành Công (BF-07)
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Component Dictionary Table -->
        <div class="overflow-x-auto avoid-break">
            <span class="font-bold text-slate-800 text-xs block mb-1 uppercase font-mono">Từ Điển Thành Phần Giao Diện Màn Hình WF-05:</span>
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[11px] uppercase">
                    <tr>
                        <th class="p-2 border">Mã Callout</th>
                        <th class="p-2 border">Kiểu Thành Phần</th>
                        <th class="p-2 border">Tên Phần Tử</th>
                        <th class="p-2 border">Mô Tả & Ràng Buộc Nghiệp Vụ</th>
                        <th class="p-2 border">Tham Chiếu Bước</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">WF-05-C01</td><td class="p-2">Countdown Timer</td><td class="p-2 font-semibold">Đồng hồ đếm ngược 72h</td><td class="p-2">Thời hạn thanh toán giữ chỗ. Quá 72h tự hủy kết quả theo EF-01.</td><td class="p-2 font-mono text-rose-700 font-bold">BF-03, BR-04, EF-01</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-05-C02</td><td class="p-2">Invoice Table</td><td class="p-2 font-semibold">Bảng kê viện phí nội trú</td><td class="p-2">Minh bạch 7tr tiền phòng kỳ 1 + 1tr cọc cơ sở vật chất = 8tr.</td><td class="p-2 font-mono text-indigo-700">BF-02, BR-04</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-05-C03</td><td class="p-2">Dynamic QR Box</td><td class="p-2 font-semibold">Khung mã VNPAY-QR</td><td class="p-2">Mã hóa thanh toán TLS 1.3 và đối soát băm SHA-256.</td><td class="p-2 font-mono text-indigo-700">BF-05, NFR-03</td></tr>
                    <tr><td class="p-2 font-mono font-bold">WF-05-C04</td><td class="p-2">Callback Action</td><td class="p-2 font-semibold">Xác nhận thanh toán</td><td class="p-2">Chuyển trạng thái Paid, khóa giường chính thức và cấp Hợp đồng KTX.</td><td class="p-2 font-mono text-emerald-700 font-bold">BF-08, BF-09</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- ============================================================== -->
    <!-- TRANG 8: BẢNG MA TRẬN TRUY VẾT 1-TO-1 TOÀN DIỆN                -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-8 shadow-sm space-y-6">
        <div class="border-b border-slate-200 pb-3 flex justify-between items-center">
            <div>
                <span class="text-xs font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase">
                    PHẦN II: BẢO CHỨNG CHẤT LƯỢNG HỌC THUẬT
                </span>
                <h2 class="text-lg font-extrabold text-slate-900 mt-1">Bảng Ma Trận Truy Vết 1-to-1 Toàn Diện (Traceability Matrix)</h2>
            </div>
            <span class="text-xs font-mono font-bold bg-emerald-50 text-emerald-700 border border-emerald-300 px-3 py-1 rounded-full">
                Khớp 100% 4 Thành Phần
            </span>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed">
            Bảng ma trận truy vết chứng minh sự liên kết tuyệt đối và nhất quán giữa <strong>Bảng Đặc Tả Use Case</strong> &harr; <strong>Sequence Diagram Message</strong> &harr; <strong>Wireframe Component Callout</strong> &harr; <strong>Quy Tắc Nghiệp Vụ (BR) / NFR</strong>:
        </p>

        <div class="overflow-x-auto">
            <table class="w-full text-xs text-left border border-slate-200">
                <thead class="bg-slate-100 font-bold text-slate-700 text-[10.5px] uppercase">
                    <tr>
                        <th class="p-2.5 border">Use Case ID</th>
                        <th class="p-2.5 border">Bước Đặc Tả (Flow ID)</th>
                        <th class="p-2.5 border">Message Sequence Diagram</th>
                        <th class="p-2.5 border">Mã Thành Phần Wireframe</th>
                        <th class="p-2.5 border">Quy Tắc Nghiệp Vụ / NFR</th>
                        <th class="p-2.5 border text-center">Kết Quả Khớp</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200 text-[11px]">
                    <tr><td class="p-2 font-mono font-bold">UC-01</td><td class="p-2 font-mono">BF-03</td><td class="p-2">Message 3 (SV -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-01-C03, C04</td><td class="p-2 font-mono">BR-01</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-01</td><td class="p-2 font-mono">AF-01</td><td class="p-2">Message opt AF-01</td><td class="p-2 font-mono font-bold text-indigo-700">WF-01-C01, C05</td><td class="p-2 font-mono">NFR-06</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-01</td><td class="p-2 font-mono">EF-02</td><td class="p-2">Message 11, 12 (alt 3)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-01-C07</td><td class="p-2 font-mono font-bold text-rose-600">BR-01 (Sai trường A)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-02</td><td class="p-2 font-mono">BF-02, BF-03</td><td class="p-2">Message 2, 3 (UI -> SV)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-02-C01</td><td class="p-2 font-mono">BR-05 (Loại phòng)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-02</td><td class="p-2 font-mono">BF-04</td><td class="p-2">Message 4 (SV -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-02-C03</td><td class="p-2 font-mono">8 Tiêu chí</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-02</td><td class="p-2 font-mono">BF-05</td><td class="p-2">Message 5 (SV -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-02-C02</td><td class="p-2 font-mono font-bold text-indigo-700">BR-06 (Top 1.5x)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-02</td><td class="p-2 font-mono">BF-06</td><td class="p-2">Message 6, 7 (SV -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-02-C04</td><td class="p-2 font-mono font-bold text-indigo-700">BR-02 (&ge;1 kỳ)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>

                    <tr><td class="p-2 font-mono font-bold">UC-03</td><td class="p-2 font-mono">BF-02</td><td class="p-2">Message 2, 5 (UI <-> Service)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-03-C02</td><td class="p-2 font-mono">BR-01, BR-02</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-03</td><td class="p-2 font-mono">BF-05</td><td class="p-2">Message 9, 10 (Admin -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-03-C03</td><td class="p-2 font-mono font-bold text-indigo-700">BR-03 (Approve)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-03</td><td class="p-2 font-mono">EF-01</td><td class="p-2">Message 14, 15 (alt Reject)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-03-C04</td><td class="p-2 font-mono font-bold text-rose-600">BR-03 (Từ chối)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>

                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-04</td><td class="p-2 font-mono">BF-01</td><td class="p-2">Message 1 (Admin -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-04-C01</td><td class="p-2 font-mono">NFR-01 (&lt;1s)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-04</td><td class="p-2 font-mono">BF-07</td><td class="p-2">Message 8 (GS -> GS)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-04-C02</td><td class="p-2 font-mono font-bold text-indigo-700">BR-07, NFR-02 (BP=0)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr class="bg-slate-50"><td class="p-2 font-mono font-bold">UC-04</td><td class="p-2 font-mono">BF-08</td><td class="p-2">Message 9, 10 (RoomOpt -> UI)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-04-C03, C04</td><td class="p-2 font-mono font-bold text-indigo-700">BR-05 (100% Lấp đầy)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>

                    <tr><td class="p-2 font-mono font-bold">UC-05</td><td class="p-2 font-mono">BF-02</td><td class="p-2">Message 2, 3 (UI <-> PayService)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-05-C02</td><td class="p-2 font-mono font-bold text-indigo-700">BR-04 (7tr+1tr=8tr)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-05</td><td class="p-2 font-mono">BF-03</td><td class="p-2">Message 3 (Đồng hồ 72h)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-05-C01</td><td class="p-2 font-mono font-bold text-indigo-700">BR-04 (Hạn 72h)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-05</td><td class="p-2 font-mono">BF-05</td><td class="p-2">Message 7 (VNPay -> UI QR)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-05-C03</td><td class="p-2 font-mono">NFR-03 (TLS 1.3)</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                    <tr><td class="p-2 font-mono font-bold">UC-05</td><td class="p-2 font-mono">BF-07, BF-08</td><td class="p-2">Message 9, 10 (SUCCESS)</td><td class="p-2 font-mono font-bold text-indigo-700">WF-05-C04</td><td class="p-2 font-mono">Khóa giường chính thức</td><td class="p-2 text-center text-emerald-600 font-bold">✅ Khớp 1-1</td></tr>
                </tbody>
            </table>
        </div>

        <div class="p-4 bg-emerald-50 border border-emerald-300 rounded-2xl text-xs text-emerald-950 font-semibold space-y-1">
            <span class="font-bold block text-emerald-900">KẾT LUẬN NGHIỆM THU:</span>
            <p>Hồ sơ thiết kế Wireframe này đạt độ chính xác và đồng bộ 100% với tài liệu đặc tả hệ thống. Mọi yếu tố giao diện đều có cơ sở nghiệp vụ vững chắc, không một chi tiết nào được thiết kế ngẫu nhiên hay thiếu tham chiếu.</p>
        </div>
    </div>

</body>
</html>
"""

# 1. Write HTML file to ui/wireframe_detail_export.html
export_html_path = os.path.abspath("ui/wireframe_detail_export.html")
with open(export_html_path, "w", encoding="utf-8") as f:
    f.write(html_template)
print("1. Written HTML to:", export_html_path)

# 2. Convert to PDF using Edge / Chrome headless
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

print("2. Running browser PDF export command...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("Exit code:", res.returncode)

if os.path.exists(pdf_downloads):
    size = os.path.getsize(pdf_downloads)
    print(f"3. Successfully created PDF at: {pdf_downloads} ({size} bytes)")
    # Copy to docs/
    shutil.copy2(pdf_downloads, pdf_docs)
    print(f"4. Successfully copied PDF to: {pdf_docs}")
else:
    print("FAILED: PDF not found in Downloads!")
