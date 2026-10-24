# -*- coding: utf-8 -*-
"""
build_usecase_spec_html_and_pdf.py
Sinh mã HTML chuẩn giao diện hiện đại và xuất PDF cho Tài liệu Đặc tả Use Case:
- Chuẩn khung bài giảng: SUMMARY, THREE TYPES OF FLOWS (4 cột: Step ID, Actor, Action, Ref), ADDITIONAL INFO
- 5 Use Case tiêu biểu (1 Dễ + 4 Nghiệp vụ cốt lõi)
- Xuất PDF bằng Edge Headless
"""

import os
import subprocess
import shutil

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tài liệu Đặc tả Use Case - KTX Smart Match (VNUK)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #0f172a;
            color: #1e293b;
        }
        .page {
            width: 210mm;
            min-height: 297mm;
            padding: 16mm 18mm;
            margin: 20px auto;
            background: #ffffff;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            page-break-after: always;
            position: relative;
        }
        @media print {
            body { background: transparent; padding: 0; }
            .page {
                width: 100%;
                min-height: 100vh;
                margin: 0;
                padding: 14mm 16mm;
                box-shadow: none;
                page-break-after: always;
            }
            .no-print { display: none !important; }
        }
        .code-font { font-family: 'JetBrains Mono', monospace; }
    </style>
</head>
<body class="py-8">

    <!-- Top Floating Toolbar -->
    <div class="no-print fixed top-4 right-6 z-50 flex items-center gap-2 bg-slate-900/90 backdrop-blur-md px-4 py-2.5 rounded-xl border border-slate-700 shadow-2xl">
        <span class="text-xs font-bold text-slate-300">Nhóm 3 • VNUK</span>
        <button onclick="window.print()" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            🖨️ In / Xuất PDF
        </button>
        <a href="/download-usecase-spec-docx" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            📄 Tải Word (.docx)
        </a>
        <a href="/download-usecase-spec-pdf" class="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            📥 Tải PDF Sẵn
        </a>
        <a href="/wireframes" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold transition">
            ← Trở lại App
        </a>
    </div>

    <!-- ==================== TRANG 1: BÌA BÁO CÁO & PHẦN I ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <!-- Header School -->
            <div class="border-b-2 border-indigo-900 pb-3 mb-5 flex justify-between items-start">
                <div>
                    <div class="text-[11px] font-extrabold uppercase tracking-wider text-indigo-950">
                        Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng
                    </div>
                    <div class="text-[10px] font-bold text-slate-500 uppercase tracking-wide">
                        Khoa Công nghệ Thông tin & Trí tuệ Nhân tạo • Học phần Phân tích Thiết kế Hệ thống
                    </div>
                </div>
                <div class="text-right">
                    <span class="text-[10px] font-mono font-bold bg-indigo-50 text-indigo-700 border border-indigo-200 px-2.5 py-1 rounded-md">
                        SLIDE TEMPLATE 100%
                    </span>
                </div>
            </div>

            <!-- Title -->
            <div class="text-center my-6">
                <span class="text-[10px] font-mono font-extrabold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300 uppercase tracking-widest">
                    USE CASE SPECIFICATION • CHUẨN RUBRIC BÀI GIẢNG
                </span>
                <h1 class="text-2xl font-black text-slate-900 mt-2 mb-1 tracking-tight uppercase">
                    Tài Liệu Đặc Tả Use Case Hệ Thống KTX
                </h1>
                <p class="text-xs italic text-slate-600">
                    Đề tài: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)
                </p>
            </div>

            <!-- Team Metadata Box -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 mb-6 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Nhóm sinh viên thực hiện</span>
                        <span class="font-black text-slate-900 text-sm">Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
                        <span class="text-slate-500 block text-[11px] mt-0.5">Nhóm 3 – Lớp Kỹ thuật Phần mềm (VNUK)</span>
                    </div>
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Cấu trúc đặc tả tuân thủ</span>
                        <span class="font-extrabold text-indigo-700 block">1. Summary Table (Bảng tóm tắt)</span>
                        <span class="font-extrabold text-emerald-700 block">2. Three Types of Flows (BF, AF, EF)</span>
                        <span class="font-extrabold text-amber-700 block">3. Additional Information (BR, NFR, UI)</span>
                    </div>
                </div>
            </div>

            <!-- Section 1 -->
            <div class="mb-4">
                <h2 class="text-sm font-extrabold text-slate-900 border-l-4 border-indigo-600 pl-2 uppercase mb-2">
                    PHẦN I: KHUNG CHUẨN BÀI GIẢNG USE CASE SPECIFICATION
                </h2>
                <p class="text-[11px] text-slate-600 leading-relaxed text-justify mb-2">
                    Theo đúng slide bài giảng của Giảng viên, chỉ vẽ sơ đồ Use Case Diagram trong UML là chưa đủ. Mỗi Use Case cần có văn bản đặc tả đi kèm mô tả mục đích, phạm vi, kịch bản sự kiện và các ràng buộc nghiệp vụ.
                </p>

                <div class="grid grid-cols-3 gap-2.5 text-[10.5px]">
                    <div class="p-2.5 bg-indigo-50/60 border border-indigo-100 rounded-lg">
                        <div class="font-bold text-indigo-900 text-[11px] mb-1">1. SUMMARY</div>
                        <ul class="text-slate-600 space-y-0.5 list-disc list-inside">
                            <li><strong>ID:</strong> UC-NUMBER (UC-01, UC-04...)</li>
                            <li><strong>Title:</strong> Verb + Noun Phrase</li>
                            <li><strong>Description:</strong> Mục đích & kết quả</li>
                            <li><strong>Actors:</strong> Primary & Secondary</li>
                            <li><strong>Pre & Post Conditions</strong></li>
                            <li><strong>Trigger:</strong> Sự kiện kích hoạt</li>
                        </ul>
                    </div>

                    <div class="p-2.5 bg-emerald-50/60 border border-emerald-100 rounded-lg">
                        <div class="font-bold text-emerald-900 text-[11px] mb-1">2. THREE FLOWS</div>
                        <ul class="text-slate-600 space-y-0.5 list-disc list-inside">
                            <li><strong>Basic Flow (BF):</strong> Con đường chính lý tưởng (Meet goal)</li>
                            <li><strong>Alternate Flows (AF):</strong> Tùy chọn rẽ nhánh khác (Meet goal)</li>
                            <li><strong>Exception Flows (EF):</strong> Xử lý lỗi / vi phạm (Not meet)</li>
                            <li><strong>4 Cột:</strong> Step ID, Actor, Action, Notes/references</li>
                        </ul>
                    </div>

                    <div class="p-2.5 bg-amber-50/60 border border-amber-100 rounded-lg">
                        <div class="font-bold text-amber-900 text-[11px] mb-1">3. ADDITIONAL INFO</div>
                        <ul class="text-slate-600 space-y-0.5 list-disc list-inside">
                            <li><strong>Business Rules (BR):</strong> BR-01..07</li>
                            <li><strong>Non-functional (NFR):</strong> NFR-01..06</li>
                            <li><strong>Wireframe UI:</strong> Màn hình tương ứng</li>
                            <li><strong>Sequence Link:</strong> Đánh số khớp 1-1 với Bảng luồng sự kiện</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Bảng BR tóm tắt -->
            <div>
                <h3 class="text-xs font-bold text-slate-800 mb-1.5 flex items-center gap-1.5">
                    <span>📌</span> Hệ thống 7 Quy tắc Nghiệp vụ tham chiếu (Business Rules Repository)
                </h3>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-16">Mã BR</th>
                            <th class="p-1.5 border border-slate-700 w-48 text-left">Tên Quy tắc</th>
                            <th class="p-1.5 border border-slate-700 text-left">Nội dung chi tiết & Ràng buộc nghiệp vụ</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-01</td>
                            <td class="p-1 font-bold text-slate-800">Đối tượng tiếp nhận</td>
                            <td class="p-1 text-slate-600">Dành riêng sinh viên Trường Đại học A (liên kết VNUK), email @vnuk.edu.vn hợp lệ.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-02</td>
                            <td class="p-1 font-bold text-slate-800">Thời hạn hợp đồng tối thiểu 1 kỳ</td>
                            <td class="p-1 text-slate-600">Bắt buộc cam kết lưu trú ≥ 01 học kỳ (05 tháng), không tiếp nhận thuê theo ngày/tuần.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-03</td>
                            <td class="p-1 font-bold text-slate-800">Phê duyệt nghiệp vụ (Approve)</td>
                            <td class="p-1 text-slate-600">Cán bộ KTX rà soát kỷ luật & diện ưu tiên trước khi đưa vào thuật toán ghép phòng.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-04</td>
                            <td class="p-1 font-bold text-slate-800">Đặt cọc giữ chỗ hạn 72h</td>
                            <td class="p-1 text-slate-600">Nộp tiền phòng kỳ 1 + Cọc 2.000.000đ qua VNPay trong 72h. Quá hạn tự động hủy đơn.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-05</td>
                            <td class="p-1 font-bold text-slate-800">Tối ưu lấp đầy phòng</td>
                            <td class="p-1 text-slate-600">Phân nhóm loại phòng (2, 4, 6 người), ưu tiên lấp đầy 100% giường trước khi mở phòng mới.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-06</td>
                            <td class="p-1 font-bold text-slate-800">Trọng số ưu tiên cá nhân 1.5x</td>
                            <td class="p-1 text-slate-600">Tiêu chí thói quen số 1 (Top criterion) của sinh viên được nhân hệ số trọng số 1.5x.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-07</td>
                            <td class="p-1 font-bold text-slate-800">Triệt tiêu cặp chặn (BP = 0)</td>
                            <td class="p-1 text-slate-600">Đảm bảo độ ổn định Gale-Shapley, không ai có động cơ đổi phòng tự phát.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Footer -->
        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 01 / 06</span>
        </div>
    </div>

    <!-- ==================== TRANG 2: UC-01 (1 DỄ) ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-300">
                    USE CASE 1: ĐƠN GIẢN (1 DỄ - BẮT BUỘC THEO RUBRIC)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">MODULE: XÁC THỰC BẢO MẬT</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-1">
                UC-01: Đăng nhập & Xác thực Sinh viên KTX (Sign in and Authenticate Student)
            </h2>
            <p class="text-[11px] text-slate-500 italic mb-3">
                Tuân thủ chuẩn Slide bài giảng: Bảng tóm tắt (Summary) và Bảng luồng sự kiện (Three Types of Flows: BF, AF, EF)
            </p>

            <!-- A. SUMMARY TABLE -->
            <div class="mb-4">
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    A. Bảng Tóm Tắt (Summary Table)
                </div>
                <table class="w-full text-[10.5px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 w-28 border border-slate-200">ID</td>
                            <td class="p-1.5 font-mono font-bold text-indigo-700 border border-slate-200">UC-01</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Title</td>
                            <td class="p-1.5 font-bold text-slate-900 border border-slate-200">Sign in and Authenticate Student (Đăng nhập và Xác thực Sinh viên KTX)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Description</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Mô tả cách sinh viên đăng nhập vào Cổng dịch vụ KTX bằng Mã sinh viên trường VNUK và Mật khẩu, hệ thống xác thực danh tính và cấp phiên làm việc bảo mật (JWT).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1.5 text-slate-800 border border-slate-200">Sinh viên (Primary Actor), Hệ thống Xác thực SV Trường A (Secondary Supporting Actor).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên đã có tài khoản và thuộc danh sách trường VNUK hợp lệ.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Post conditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên đăng nhập thành công, nhận JWT Token và được chuyển hướng vào Dashboard.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên truy cập Cổng KTX và nhấn 'Đăng nhập'.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- B. THREE TYPES OF FLOWS -->
            <div>
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    B. Bảng Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table - 4 Cột Chuẩn)
                </div>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-14">Step ID</th>
                            <th class="p-1.5 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1.5 border border-slate-700 text-left">Action</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Notes/references (Ref)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Truy cập vào trang Đăng nhập của Cổng dịch vụ KTX.</td>
                            <td class="p-1 text-slate-500 italic">Màn hình WF-01, NFR-06</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Hiển thị form đăng nhập gồm ô nhập MSSV/Email và Mật khẩu.</td>
                            <td class="p-1 text-slate-500 italic">Kiểm tra cú pháp email</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Nhập email trường (@vnuk.edu.vn) và mật khẩu cá nhân, bấm 'Đăng nhập'.</td>
                            <td class="p-1 text-slate-500 italic">BR-01 (Đúng email trường)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Gửi thông tin xác thực đến Dịch vụ xác thực trung tâm trường A.</td>
                            <td class="p-1 text-slate-500 italic">Mã hóa TLS 1.3, NFR-03</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống Trường A</td>
                            <td class="p-1 text-slate-700">Đối soát MSSV, xác nhận sinh viên chính quy trường A và mật khẩu chính xác.</td>
                            <td class="p-1 text-slate-500 italic">BR-01 (Đối tượng hợp lệ)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Khởi tạo Session/Token bảo mật, chuyển hướng sinh viên vào Dashboard chính.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">Hoàn thành mục tiêu UC-01</td>
                        </tr>
                        <!-- Alternate Flows -->
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-A</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Tại bước BF-2, sinh viên chọn 'Đăng nhập nhanh bằng Google SSO (@vnuk.edu.vn)'.</td>
                            <td class="p-1 text-emerald-700 italic">Nhánh phụ đạt mục tiêu (Meet goal)</td>
                        </tr>
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-B</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Tại bước BF-2, sinh viên tích chọn 'Ghi nhớ đăng nhập trong 30 ngày'.</td>
                            <td class="p-1 text-emerald-700 italic">Lưu token thiết bị an toàn</td>
                        </tr>
                        <!-- Exception Flows -->
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-A</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tại bước BF-4, sinh viên nhập sai mật khẩu quá 5 lần: Khóa tài khoản 15 phút.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_AUTH_MAX, NFR-03</td>
                        </tr>
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-B</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tại bước BF-5, tài khoản không thuộc danh sách trường A: Báo lỗi từ chối tiếp nhận.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_NOT_AFFILIATED, BR-01</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- C. ADDITIONAL INFO -->
            <div class="mt-3 p-2 bg-slate-50 border border-slate-200 rounded text-[10px]">
                <span class="font-bold text-slate-800 uppercase">C. Thông tin bổ sung:</span>
                <span class="text-slate-600"> Áp dụng quy tắc <strong>BR-01</strong> (Đối tượng sinh viên Trường A liên kết), <strong>NFR-03</strong> (Bảo mật phiên JWT, TLS 1.3), Giao diện Wireframe tương ứng <strong>WF-01</strong>.</span>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 02 / 06</span>
        </div>
    </div>

    <!-- ==================== TRANG 3: UC-04 (NGHIỆP VỤ SINH VIÊN) ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800 border border-blue-300">
                    USE CASE 2: NGHIỆP VỤ SINH VIÊN (CORE BUSINESS)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">MODULE: KHẢO SÁT & ĐĂNG KÝ PHÒNG</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-1">
                UC-04: Khảo sát 8 Thói quen & Nộp hồ sơ KTX (Survey Lifestyle and Submit Application)
            </h2>
            <p class="text-[11px] text-slate-500 italic mb-3">
                Quy trình sinh viên khai báo nếp sống, chọn trọng số 1.5x và ký cam kết lưu trú tối thiểu 1 kỳ (BR-02)
            </p>

            <!-- A. SUMMARY TABLE -->
            <div class="mb-4">
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    A. Bảng Tóm Tắt (Summary Table)
                </div>
                <table class="w-full text-[10.5px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 w-28 border border-slate-200">ID</td>
                            <td class="p-1.5 font-mono font-bold text-indigo-700 border border-slate-200">UC-04</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Title</td>
                            <td class="p-1.5 font-bold text-slate-900 border border-slate-200">Survey Lifestyle and Submit Dormitory Application (Khảo sát nếp sống & Nộp hồ sơ KTX)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Description</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Mô tả quy trình sinh viên lựa chọn loại phòng (2, 4, 6 người), điền 8 tiêu chí thói quen, chọn tiêu chí quan trọng nhất (nhân 1.5x) và tích cam kết ở tối thiểu 1 học kỳ để nộp đơn.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1.5 text-slate-800 border border-slate-200">Sinh viên (Primary Actor), Hệ thống KTX (Secondary Actor).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên đã đăng nhập thành công vào hệ thống (UC-01).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Post conditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Hồ sơ được tạo ở trạng thái Pending_Approval, chuyển sang Cán bộ KTX thẩm định (UC-18).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên chọn chức năng 'Khảo sát thói quen & Đăng ký phòng' trên Dashboard.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- B. THREE TYPES OF FLOWS -->
            <div>
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    B. Bảng Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table)
                </div>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-14">Step ID</th>
                            <th class="p-1.5 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1.5 border border-slate-700 text-left">Action</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Notes/references (Ref)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Mở biểu mẫu khảo sát nếp sống và đăng ký loại phòng KTX.</td>
                            <td class="p-1 text-slate-500 italic">Màn hình WF-02</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Hiển thị 3 loại phòng (VIP 2, Chuẩn 4, Tiết kiệm 6) và bảng 8 tiêu chí thói quen.</td>
                            <td class="p-1 text-slate-500 italic">BR-05 (Danh mục phòng)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Chọn gói phòng nguyện vọng (ví dụ: Phòng 4 người Chuẩn).</td>
                            <td class="p-1 text-slate-500 italic">Thu thập nguyện vọng</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Điều chỉnh 8 thanh trượt thói quen (Giờ ngủ, Giờ dậy, Ngăn nắp, Chịu ồn, Hút thuốc...).</td>
                            <td class="p-1 text-slate-500 italic">Chuẩn hóa vector 8 chiều</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Chọn 01 tiêu chí quan trọng nhất (Top Criterion) để nhân hệ số ưu tiên 1.5x.</td>
                            <td class="p-1 text-slate-500 italic">BR-06 (Trọng số 1.5x)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Tích chọn ô cam kết bắt buộc: 'Tôi cam kết ở KTX tối thiểu 01 học kỳ (05 tháng)'.</td>
                            <td class="p-1 text-slate-500 italic">BR-02 (Thời hạn tối thiểu)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-7</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Bấm nút 'Nộp hồ sơ đăng ký KTX'.</td>
                            <td class="p-1 text-slate-500 italic">Gửi payload dữ liệu</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-8</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Kiểm tra tính hợp lệ dữ liệu, lưu hồ sơ vào Database ở trạng thái Pending_Approval.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">Hoàn thành mục tiêu UC-04</td>
                        </tr>
                        <!-- Alternate Flows -->
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-A</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Tại bước BF-4, sinh viên bấm 'Nạp hồ sơ mẫu Persona' để tự động điền nhanh 8 thói quen.</td>
                            <td class="p-1 text-emerald-700 italic">NFR-06 (Trải nghiệm UI 1-click)</td>
                        </tr>
                        <!-- Exception Flows -->
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-A</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tại bước BF-6, không tích cam kết ở tối thiểu 1 kỳ: Khóa nút nộp, báo lỗi đỏ vi phạm BR-02.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_TERM_MIN, BR-02</td>
                        </tr>
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-B</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tại bước BF-5, bỏ trống tiêu chí ưu tiên: Nhắc nhở chọn 1 tiêu chí top theo BR-06.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_TOP_EMPTY, BR-06</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- C. ADDITIONAL INFO -->
            <div class="mt-3 p-2 bg-slate-50 border border-slate-200 rounded text-[10px]">
                <span class="font-bold text-slate-800 uppercase">C. Thông tin bổ sung:</span>
                <span class="text-slate-600"> Áp dụng quy tắc <strong>BR-02</strong> (Cam kết thời hạn tối thiểu 1 kỳ), <strong>BR-05</strong> (Cấu hình loại phòng), <strong>BR-06</strong> (Trọng số ưu tiên 1.5x), Giao diện Wireframe <strong>WF-02</strong>.</span>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 03 / 06</span>
        </div>
    </div>

    <!-- ==================== TRANG 4: UC-18 (QUẢN TRỊ BUSINESS APPROVE) ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-amber-100 text-amber-800 border border-amber-300">
                    USE CASE 3: QUẢN TRỊ KTX (BUSINESS APPROVE)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">MODULE: THẨM ĐỊNH HỒ SƠ</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-1">
                UC-18: Thẩm định & Phê duyệt Nghiệp vụ Hồ sơ KTX (Review and Approve Application)
            </h2>
            <p class="text-[11px] text-slate-500 italic mb-3">
                Đáp ứng phản biện của thầy: "Cần business approve trước khi phân phòng, không cho chạy tự do"
            </p>

            <!-- A. SUMMARY TABLE -->
            <div class="mb-4">
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    A. Bảng Tóm Tắt (Summary Table)
                </div>
                <table class="w-full text-[10.5px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 w-28 border border-slate-200">ID</td>
                            <td class="p-1.5 font-mono font-bold text-indigo-700 border border-slate-200">UC-18</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Title</td>
                            <td class="p-1.5 font-bold text-slate-900 border border-slate-200">Review and Approve Dormitory Application (Thẩm định & Phê duyệt đơn KTX)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Description</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Cán bộ KTX rà soát điều kiện nội trú (tính hợp lệ MSSV trường A, điểm rèn luyện, lịch sử kỷ luật, cam kết 1 kỳ) và ra quyết định phê duyệt đơn để nạp vào thuật toán Gale-Shapley.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1.5 text-slate-800 border border-slate-200">Cán bộ Quản lý KTX (Staff - Primary Actor), Hệ thống KTX (Secondary Actor).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Hồ sơ sinh viên nộp đang ở trạng thái chờ duyệt (Pending_Approval).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Post conditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Hồ sơ chuyển sang trạng thái Approved_For_Matching hoặc Rejected kèm lý do.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Cán bộ KTX mở module 'Thẩm định Đơn Đăng ký KTX' trên Dashboard Quản trị.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- B. THREE TYPES OF FLOWS -->
            <div>
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    B. Bảng Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table)
                </div>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-14">Step ID</th>
                            <th class="p-1.5 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1.5 border border-slate-700 text-left">Action</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Notes/references (Ref)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Mở danh sách các hồ sơ đăng ký KTX đang chờ thẩm định.</td>
                            <td class="p-1 text-slate-500 italic">Màn hình WF-03</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Hiển thị bảng hồ sơ kèm kết quả đối soát tự động: Đúng trường A (BR-01), Đủ cam kết 1 kỳ (BR-02).</td>
                            <td class="p-1 text-slate-500 italic">BR-01, BR-02</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Chọn hồ sơ sinh viên để kiểm tra chi tiết diện chính sách, hạnh kiểm và quỹ phòng trống.</td>
                            <td class="p-1 text-slate-500 italic">BR-05 (Kiểm tra quỹ phòng)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Bấm nút 'Phê duyệt hồ sơ (Business Approve)'.</td>
                            <td class="p-1 text-slate-500 italic">Quyết định thẩm định BR-03</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Cập nhật trạng thái hồ sơ thành Approved_For_Matching và gửi thông báo cho sinh viên.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">Hoàn thành mục tiêu UC-18</td>
                        </tr>
                        <!-- Alternate Flows -->
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-A</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Tại bước BF-2, Cán bộ bấm 'Duyệt hàng loạt (Batch Approve)' cho các đơn đã qua kiểm tra tự động.</td>
                            <td class="p-1 text-emerald-700 italic">Tối ưu hiệu suất quản trị</td>
                        </tr>
                        <!-- Exception Flows -->
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-A</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Tại bước BF-3, phát hiện sinh viên vi phạm kỷ luật năm trước: Bấm 'Từ chối (Reject)' kèm lý do.</td>
                            <td class="p-1 text-rose-700 italic">BR-03 (Loại bỏ vi phạm)</td>
                        </tr>
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-B</td>
                            <td class="p-1 font-bold text-slate-800">Cán bộ KTX</td>
                            <td class="p-1 text-slate-700">Hồ sơ thiếu minh chứng gia đình chính sách: Bấm 'Yêu cầu bổ sung tài liệu'.</td>
                            <td class="p-1 text-rose-700 italic">Trạng thái Incomplete</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- C. ADDITIONAL INFO -->
            <div class="mt-3 p-2 bg-slate-50 border border-slate-200 rounded text-[10px]">
                <span class="font-bold text-slate-800 uppercase">C. Thông tin bổ sung:</span>
                <span class="text-slate-600"> Áp dụng quy tắc <strong>BR-01</strong> (Đối tượng SV), <strong>BR-03</strong> (Phê duyệt nghiệp vụ Business Approve), <strong>BR-05</strong> (Kiểm soát hạn ngạch quỹ phòng), Giao diện <strong>WF-03</strong>.</span>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 04 / 06</span>
        </div>
    </div>

    <!-- ==================== TRANG 5: UC-24 (THUẬT TOÁN GALE-SHAPLEY) ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-purple-100 text-purple-800 border border-purple-300">
                    USE CASE 4: THUẬT TOÁN CỐT LÕI (CORE ALGORITHM)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">MODULE: GALE-SHAPLEY & LẤP ĐẦY</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-1">
                UC-24: Khởi chạy Phân bổ Phòng Ổn định (Execute Stable Room Matching)
            </h2>
            <p class="text-[11px] text-slate-500 italic mb-3">
                Thuật toán Gale-Shapley ghép cặp triệt tiêu cặp chặn (BP=0) kết hợp chiến lược lấp đầy 100% giường (BR-05, BR-07)
            </p>

            <!-- A. SUMMARY TABLE -->
            <div class="mb-4">
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    A. Bảng Tóm Tắt (Summary Table)
                </div>
                <table class="w-full text-[10.5px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 w-28 border border-slate-200">ID</td>
                            <td class="p-1.5 font-mono font-bold text-indigo-700 border border-slate-200">UC-24</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Title</td>
                            <td class="p-1.5 font-bold text-slate-900 border border-slate-200">Execute Stable Room Matching and Optimization (Khởi chạy Ghép phòng ổn định & Tối ưu)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Description</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Hệ thống tự động thực thi thuật toán Gale-Shapley kết hợp thuật toán gộp phòng tham lam để phân bổ sinh viên vào phòng theo đúng loại phòng đã chọn, đảm bảo không có cặp chặn (BP=0).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1.5 text-slate-800 border border-slate-200">Hệ thống KTX (System / Scheduler - Primary Actor), Quản trị viên KTX (Admin - Observer).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Đợt tiếp nhận đã đóng, các hồ sơ tham gia đã được Cán bộ KTX duyệt (Approved_For_Matching).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Post conditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Bảng phân phòng chính thức được sinh ra, kích hoạt hạn thanh toán cọc 72 giờ cho sinh viên.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Đến lịch tự động (Cron job) hoặc Quản trị viên bấm 'Khởi chạy Ghép phòng' trên Dashboard.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- B. THREE TYPES OF FLOWS -->
            <div>
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    B. Bảng Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table)
                </div>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-14">Step ID</th>
                            <th class="p-1.5 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1.5 border border-slate-700 text-left">Action</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Notes/references (Ref)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Kích hoạt tiến trình phân phòng tự động cho đợt tiếp nhận mới.</td>
                            <td class="p-1 text-slate-500 italic">Màn hình WF-04, NFR-01</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Phân nhóm hồ sơ theo cùng nguyện vọng loại phòng (2, 4, 6 người) và theo giới tính.</td>
                            <td class="p-1 text-slate-500 italic">BR-05 (Phân nhóm phòng)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tính toán ma trận tương thích 2 chiều, nhân trọng số 1.5x cho tiêu chí ưu tiên của từng bạn.</td>
                            <td class="p-1 text-slate-500 italic">BR-06 (scoring.py)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Chạy thuật toán Gale-Shapley tìm cặp ghép ổn định cho từng nhóm sinh viên.</td>
                            <td class="p-1 text-slate-500 italic">BR-07 (Blocking Pairs = 0)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Áp dụng thuật toán gộp phòng (merge_pairs) để lấp đầy 100% số giường phòng 4 và phòng 6.</td>
                            <td class="p-1 text-slate-500 italic">BR-05 (Tối ưu lấp đầy phòng)</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Lưu kết quả phân phòng vào Database, kích hoạt đồng hồ đếm ngược thanh toán cọc 72 giờ.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">BR-04, Hoàn thành UC-24</td>
                        </tr>
                        <!-- Alternate Flows -->
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-A</td>
                            <td class="p-1 font-bold text-slate-800">Quản trị viên</td>
                            <td class="p-1 text-slate-700">Sau bước BF-6, Admin có thể điều chỉnh thủ công (Manual Override) một số ca đặc biệt.</td>
                            <td class="p-1 text-emerald-700 italic">Can thiệp quản trị an toàn</td>
                        </tr>
                        <!-- Exception Flows -->
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-A</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Số lượng sinh viên nhóm A và B bị lệch lẻ: Đưa sinh viên nộp muộn nhất vào danh sách chờ.</td>
                            <td class="p-1 text-rose-700 italic">Waitlist xếp hàng sau</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- C. ADDITIONAL INFO -->
            <div class="mt-3 p-2 bg-slate-50 border border-slate-200 rounded text-[10px]">
                <span class="font-bold text-slate-800 uppercase">C. Thông tin bổ sung:</span>
                <span class="text-slate-600"> Áp dụng quy tắc <strong>BR-05</strong> (Lấp đầy giường 100%), <strong>BR-06</strong> (Trọng số 1.5x), <strong>BR-07</strong> (Triệt tiêu cặp chặn BP=0), <strong>NFR-01</strong> (Thời gian xử lý &lt; 1 giây cho 200 sinh viên), Giao diện <strong>WF-04</strong>.</span>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 05 / 06</span>
        </div>
    </div>

    <!-- ==================== TRANG 6: UC-13 (THANH TOÁN 72H) ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-2 mb-3">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-300">
                    USE CASE 5: GIAO DỊCH TÀI CHÍNH (FINANCIAL WORKFLOW)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">MODULE: THANH TOÁN VNPAY & CỌC 72H</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-1">
                UC-13: Thanh toán Tiền phòng & Đặt cọc 72h (Pay Dorm Fee and Deposit)
            </h2>
            <p class="text-[11px] text-slate-500 italic mb-3">
                Quy trình thanh toán tiền phòng kỳ 1 + Đặt cọc giữ chỗ 2.000.000đ qua cổng VNPay trong hạn chót 72 giờ (BR-04)
            </p>

            <!-- A. SUMMARY TABLE -->
            <div class="mb-4">
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    A. Bảng Tóm Tắt (Summary Table)
                </div>
                <table class="w-full text-[10.5px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 w-28 border border-slate-200">ID</td>
                            <td class="p-1.5 font-mono font-bold text-indigo-700 border border-slate-200">UC-13</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Title</td>
                            <td class="p-1.5 font-bold text-slate-900 border border-slate-200">Pay Dormitory Fee and Security Deposit (Thanh toán tiền phòng & Đặt cọc KTX)</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Description</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Mô tả quy trình sinh viên thực hiện thanh toán tiền phòng học kỳ 1 kèm tiền đặt cọc giữ chỗ trong hạn 72 giờ qua cổng VNPay để xác nhận vị trí phòng chính thức.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1.5 text-slate-800 border border-slate-200">Sinh viên (Primary Actor), Cổng VNPay (External Actor), Hệ thống KTX (Secondary Actor).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên đã có kết quả phân phòng và thời hạn 72 giờ đang có hiệu lực (BR-04).</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Post conditions</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Phòng được khóa chính thức (Paid), hệ thống xuất Biên lai thu tiền điện tử và Hợp đồng lưu trú mã QR.</td>
                        </tr>
                        <tr>
                            <td class="p-1.5 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1.5 text-slate-600 border border-slate-200">Sinh viên nhận thông báo trúng tuyển phòng và truy cập vào mục 'Thanh toán & Đặt cọc'.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- B. THREE TYPES OF FLOWS -->
            <div>
                <div class="text-[11px] font-bold text-indigo-900 bg-indigo-50 px-2.5 py-1 rounded border border-indigo-200 uppercase mb-1.5">
                    B. Bảng Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table)
                </div>
                <table class="w-full text-[10px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-14">Step ID</th>
                            <th class="p-1.5 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1.5 border border-slate-700 text-left">Action</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Notes/references (Ref)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Mở màn hình 'Thanh toán & Đặt cọc KTX' từ thông báo trúng tuyển.</td>
                            <td class="p-1 text-slate-500 italic">Màn hình WF-05</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Hiển thị bảng kê: Tiền phòng Kỳ 1 + Tiền đặt cọc giữ chỗ (2.000.000đ) và đồng hồ 72h.</td>
                            <td class="p-1 text-slate-500 italic">BR-04 (Hạn cọc 72h)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Chọn phương thức thanh toán 'Cổng thanh toán điện tử VNPay (VNPAY-QR)'.</td>
                            <td class="p-1 text-slate-500 italic">Tích hợp cổng VNPay</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Khởi tạo giao dịch bảo mật (TLS 1.3), sinh mã đơn hàng và mã QR thanh toán động.</td>
                            <td class="p-1 text-slate-500 italic">NFR-03 (Toàn vẹn giao dịch)</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Mở App Ngân hàng quét mã QR để thanh toán toàn bộ số tiền phòng và tiền cọc.</td>
                            <td class="p-1 text-slate-500 italic">Mobile Banking scan QR</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-1 font-bold text-slate-800">Cổng VNPay</td>
                            <td class="p-1 text-slate-700">Xác thực trừ tiền thành công, gửi mã callback vnp_ResponseCode = 00 về máy chủ KTX.</td>
                            <td class="p-1 text-slate-500 italic">Đối soát giao dịch thành công</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-7</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Cập nhật trạng thái hợp đồng thành Paid, khóa chính thức chỗ ở và sinh Biên lai điện tử.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">Hoàn thành mục tiêu UC-13</td>
                        </tr>
                        <!-- Alternate Flows -->
                        <tr class="bg-emerald-50/50">
                            <td class="p-1 text-center font-bold font-mono text-emerald-800">AF-A</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên</td>
                            <td class="p-1 text-slate-700">Tại bước BF-7, sinh viên bấm 'Tải biên lai điện tử' và 'Tải hợp đồng số KTX' có mã QR xác thực.</td>
                            <td class="p-1 text-emerald-700 italic">Lưu trữ chứng từ kế toán</td>
                        </tr>
                        <!-- Exception Flows -->
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-A</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Sau 72 giờ không hoàn tất nộp tiền: Tự động hủy kết quả phòng, nhường suất cho Waitlist.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_PAYMENT_TIMEOUT, BR-04</td>
                        </tr>
                        <tr class="bg-rose-50/60">
                            <td class="p-1 text-center font-bold font-mono text-rose-700">EF-B</td>
                            <td class="p-1 font-bold text-slate-800">Cổng VNPay</td>
                            <td class="p-1 text-slate-700">Giao dịch bị từ chối do tài khoản không đủ số dư hoặc lỗi thẻ: Cho phép quét lại mã QR.</td>
                            <td class="p-1 text-rose-700 italic">Mã lỗi ERR_INSUFFICIENT_FUNDS</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- C. ADDITIONAL INFO -->
            <div class="mt-3 p-2 bg-slate-50 border border-slate-200 rounded text-[10px]">
                <span class="font-bold text-slate-800 uppercase">C. Thông tin bổ sung:</span>
                <span class="text-slate-600"> Áp dụng quy tắc <strong>BR-04</strong> (Đặt cọc giữ chỗ hạn 72h), <strong>NFR-03</strong> (Bảo mật chữ ký số SHA-256 đối soát cổng VNPay), Giao diện <strong>WF-05</strong>.</span>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-[10px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 06 / 06</span>
        </div>
    </div>

</body>
</html>
"""

def generate_html_and_pdf():
    html_path = os.path.join(os.path.dirname(__file__), "ui", "usecase_spec_export.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)
    print(f"[HTML SUCCESS] Created {html_path}")

    # Export to PDF via Edge Headless
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    edge_exe = next((p for p in edge_paths if os.path.exists(p)), None)
    if not edge_exe:
        print("[PDF ERROR] Edge executable not found.")
        return

    pdf_out_docs = os.path.join(os.path.dirname(__file__), "docs", "Dac_Ta_Use_Case_Chuan_Slide_Thay_KTX_VNUK.pdf")
    pdf_out_dl = os.path.join(r"C:\Users\LENOVO\Downloads", "Dac_Ta_Use_Case_Chuan_Slide_Thay_KTX_VNUK.pdf")

    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_out_docs}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_out_docs):
        print(f"[PDF SUCCESS] Generated {pdf_out_docs} ({os.path.getsize(pdf_out_docs)} bytes)")
        try:
            shutil.copy2(pdf_out_docs, pdf_out_dl)
            print(f"[PDF SUCCESS] Copied to {pdf_out_dl}")
        except Exception as e:
            print(f"[PDF WARNING] Could not copy to Downloads: {e}")
    else:
        print(f"[PDF ERROR] Edge print failed: {res.stderr}")

if __name__ == "__main__":
    generate_html_and_pdf()
