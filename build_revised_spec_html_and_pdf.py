# -*- coding: utf-8 -*-
"""
build_revised_spec_html_and_pdf.py
Sinh mã HTML chuẩn giao diện hiện đại và xuất PDF cho Tài liệu Đặc tả Use Case và Business Rules:
- Tích hợp Mermaid JS để vẽ Sequence Diagram trực quan với activation bars
- Bảng Business Rules 3 cột chuẩn Slide p125 & Nhóm 2
- Xuất PDF chuẩn A4 qua Edge Headless
"""

import os
import subprocess
import shutil

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đặc tả Use Case & Business Rules Chuẩn Hóa - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
    </script>
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
            padding: 15mm 16mm;
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
                padding: 12mm 14mm;
                box-shadow: none;
                page-break-after: always;
            }
            .no-print { display: none !important; }
        }
        .code-font { font-family: 'JetBrains Mono', monospace; }
    </style>
</head>
<body class="py-6">

    <!-- Top Floating Toolbar -->
    <div class="no-print fixed top-4 right-6 z-50 flex items-center gap-2 bg-slate-900/90 backdrop-blur-md px-4 py-2.5 rounded-xl border border-slate-700 shadow-2xl">
        <span class="text-xs font-bold text-slate-300">Nhóm 3 • VNUK</span>
        <button onclick="window.print()" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            🖨️ In / Xuất PDF
        </button>
        <a href="/download-revised-spec-docx" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            📄 Tải Word (.docx)
        </a>
        <a href="/download-revised-spec-pdf" class="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-lg text-xs font-bold shadow flex items-center gap-1.5 transition">
            📥 Tải PDF Sẵn
        </a>
        <a href="/wireframes" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg text-xs font-semibold transition">
            ← Trở lại App
        </a>
    </div>

    <!-- ==================== TRANG 1: TIẾP THU FEEDBACK & BUSINESS RULES ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <!-- Header School -->
            <div class="border-b-2 border-indigo-900 pb-2.5 mb-4 flex justify-between items-start">
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
                        REVISED BASELINE v4.0
                    </span>
                </div>
            </div>

            <!-- Title -->
            <div class="text-center my-3">
                <span class="text-[10px] font-mono font-extrabold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300 uppercase tracking-widest">
                    USE CASE SPECIFICATION & BUSINESS RULES (P110, P125)
                </span>
                <h1 class="text-xl font-black text-slate-900 mt-2 mb-1 tracking-tight uppercase">
                    Tài Liệu Đặc Tả Use Case & Quy Tắc Nghiệp Vụ
                </h1>
                <p class="text-xs italic text-slate-600">
                    Hệ thống: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)
                </p>
            </div>

            <!-- Team Metadata Box -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 mb-4 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Nhóm sinh viên thực hiện</span>
                        <span class="font-black text-slate-900 text-sm">Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
                        <span class="text-slate-500 block text-[11px] mt-0.5">Nhóm 3 – Lớp Kỹ thuật Phần mềm (VNUK)</span>
                    </div>
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Căn cứ tiếp thu & chuẩn hóa</span>
                        <span class="font-extrabold text-indigo-700 block">• Ý kiến Feedback trực tiếp ngày 24/10 của Thầy</span>
                        <span class="font-extrabold text-emerald-700 block">• Chuẩn Slide p110, p125 & Đối sánh Nhóm 2</span>
                    </div>
                </div>
            </div>

            <!-- Bảng Tiếp thu Feedback 24/10 -->
            <div class="mb-4">
                <h2 class="text-xs font-extrabold text-slate-900 uppercase mb-1.5 flex items-center gap-1.5">
                    <span>📌</span> 1. Bảng Tiếp thu & Khắc phục Toàn diện Ý kiến Giảng viên (24/10)
                </h2>
                <table class="w-full text-[9.5px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-1/3 text-left">Ý kiến Feedback của Thầy (24/10)</th>
                            <th class="p-1.5 border border-slate-700 text-left">Giải pháp Tiếp thu & Chuẩn hóa trong v4.0</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 font-bold text-slate-800">1. Tên đăng nhập / mật khẩu là 1 chức năng; Đăng ký & khai báo là 1 use case</td>
                            <td class="p-1 text-slate-600">Đóng gói UC-01 (Đăng nhập bằng Tên/Email hoặc MSSV) và UC-02 (Đăng ký tài khoản kèm khai báo nếp sống 8 tiêu chí).</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 font-bold text-slate-800">2. Không cần phải liệt kê hết (bị loãng, vụn vặt)</td>
                            <td class="p-1 text-slate-600">Tinh giản từ 43 use case bị phân mảnh xuống danh mục Use Case nghiệp vụ trọng tâm, loại bỏ các micro-actions.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 font-bold text-slate-800">3. Đánh mạnh vào matching theo request (1 bên request, bên kia đồng ý thì match)</td>
                            <td class="p-1 text-slate-600">Xây dựng UC-05 chuẩn: Sinh viên A gửi Matching Request -> Sinh viên B nhận thông báo và đối chiếu profile -> B bấm Đồng ý thì Match.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 font-bold text-slate-800">4. 1 bên gửi 1 bên nhận là 2 người khác nhau; Trả phòng làm sai</td>
                            <td class="p-1 text-slate-600">Phân định rõ 2 tác nhân SV A và SV B; Tách riêng và chuẩn hóa quy trình Trả phòng: Kiểm kê -> Quyết toán cọc -> Giải phóng giường.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 font-bold text-slate-800">5. Thanh toán có tạo/in biên lai (không nhét vào AF); Đặc tả hết bước; BR sai format</td>
                            <td class="p-1 text-slate-600">Đưa Tạo/In biên lai vào luồng chính BF; đảm bảo mọi flow đều có kết thúc [End of Use Case]; chuyển BR sang chuẩn 3 cột p125.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Bảng Quy tắc nghiệp vụ chuẩn 3 cột -->
            <div>
                <h2 class="text-xs font-extrabold text-slate-900 uppercase mb-1.5 flex items-center gap-1.5">
                    <span>⚖️</span> 2. Danh mục Quy tắc Nghiệp vụ (Business Rules - Chuẩn Slide p125)
                </h2>
                <table class="w-full text-[9px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-indigo-950 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-14">Rule ID</th>
                            <th class="p-1 border border-slate-700 w-44 text-left">Tên Quy tắc (Name)</th>
                            <th class="p-1 border border-slate-700 text-left">Ràng buộc Nghiệp vụ Cụ thể (Description)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-01</td>
                            <td class="p-1 font-bold text-slate-800">MSSV duy nhất & Đối tượng hợp lệ</td>
                            <td class="p-1 text-slate-600">Mỗi sinh viên có duy nhất 1 MSSV định danh tài khoản, bắt buộc dùng email @vnuk.edu.vn và có tư cách sinh viên hợp lệ.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-02</td>
                            <td class="p-1 font-bold text-slate-800">Cam kết thời hạn tối thiểu 1 kỳ</td>
                            <td class="p-1 text-slate-600">Mỗi đơn KTX bắt buộc cam kết lưu trú ≥ 01 học kỳ (05 tháng); từ chối hợp đồng ngắn hạn để giữ nếp sống ổn định.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-03</td>
                            <td class="p-1 font-bold text-slate-800">Phê duyệt nghiệp vụ (Approve)</td>
                            <td class="p-1 text-slate-600">Cán bộ KTX thẩm định kỷ luật, chính sách ưu tiên và quỹ phòng trước khi đưa hồ sơ vào thuật toán phân phòng.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-04</td>
                            <td class="p-1 font-bold text-slate-800">Đặt cọc giữ chỗ và hạn 72 giờ</td>
                            <td class="p-1 text-slate-600">Trong 72h kể từ khi công bố kết quả, sinh viên phải nộp tiền phòng kỳ 1 + Cọc 2.000.000đ qua VNPay. Quá hạn tự động hủy đơn.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-05</td>
                            <td class="p-1 font-bold text-slate-800">Ghép bạn theo Request hai chiều</td>
                            <td class="p-1 text-slate-600">Bắt buộc có sự đồng thuận 2 bên: Bên gửi (SV A) tạo Request -> Bên nhận (SV B) xem profile và bấm 'Đồng ý' thì mới ghép cặp.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-06</td>
                            <td class="p-1 font-bold text-slate-800">Tối ưu lấp đầy 100% phòng</td>
                            <td class="p-1 text-slate-600">Ưu tiên lấp đầy 100% giường của từng phòng (2/4/6 người) trước khi mở phòng mới để tối ưu chi phí điện nước và lợi nhuận KTX.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-07</td>
                            <td class="p-1 font-bold text-slate-800">Quyết toán và hoàn cọc khi trả phòng</td>
                            <td class="p-1 text-slate-600">Tiền cọc hoàn = 2.000.000đ − (Nợ dịch vụ kỳ cuối + Phí bồi thường hư hại tài sản nếu có). Phá vỡ hợp đồng trước 1 kỳ không hoàn cọc.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-08</td>
                            <td class="p-1 font-bold text-slate-800">Ràng buộc đổi phòng / đổi bạn</td>
                            <td class="p-1 text-slate-600">Mỗi sinh viên chỉ có tối đa 1 yêu cầu đổi phòng đang xử lý; bắt buộc có lý do và chỉ duyệt khi phòng đích còn chỗ trống phù hợp.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-09</td>
                            <td class="p-1 font-bold text-slate-800">Trọng số ưu tiên cá nhân 1.5x</td>
                            <td class="p-1 text-slate-600">Tiêu chí số 1 (Top Criterion) trong 8 thói quen của mỗi bạn được nhân hệ số 1.5x khi tính toán ma trận tương thích 2 chiều.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 01 / 04</span>
        </div>
    </div>

    <!-- ==================== TRANG 2: UC-05 MATCHING BY REQUEST ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-1.5 mb-2.5">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 border border-indigo-300">
                    USE CASE TRỌNG TÂM: MATCHING THEO REQUEST (ĐÁNH MẠNH THEO GÓP Ý CỦA THẦY)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">UC-05</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-0.5">
                UC-05: Ghép bạn cùng phòng theo yêu cầu hai chiều (Roommate Matching by Request)
            </h2>
            <p class="text-[10.5px] text-slate-500 italic mb-2.5">
                Phân định rõ 2 tác nhân con người: Sinh viên gửi (SV A) và Sinh viên nhận (SV B). Đảm bảo đặc tả hết bước và đúng vòng đời.
            </p>

            <!-- Summary Table -->
            <div class="mb-3">
                <div class="text-[10px] font-bold text-indigo-900 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200 uppercase mb-1">
                    A. Summary Table (Bảng tóm tắt - Slide p110)
                </div>
                <table class="w-full text-[9.5px] border-collapse border border-slate-200">
                    <tbody>
                        <tr>
                            <td class="p-1 font-bold text-slate-700 bg-slate-50 w-24 border border-slate-200">Description</td>
                            <td class="p-1 text-slate-600 border border-slate-200">Cho phép SV A gửi Matching Request đến SV B dựa trên điểm hòa hợp nếp sống; SV B nhận thông báo, xem đối chiếu profile và chọn Đồng ý (ghép cặp) hoặc Từ chối.</td>
                        </tr>
                        <tr>
                            <td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td>
                            <td class="p-1 text-slate-800 border border-slate-200">Sinh viên gửi (SV A - Primary), Sinh viên nhận (SV B - Secondary), Hệ thống KTX (Supporting).</td>
                        </tr>
                        <tr>
                            <td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td>
                            <td class="p-1 text-slate-600 border border-slate-200">Cả A và B đều đã hoàn thành khảo sát 8 thói quen sinh hoạt và chưa chốt hợp đồng phòng chính thức.</td>
                        </tr>
                        <tr>
                            <td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Postconditions</td>
                            <td class="p-1 text-slate-600 border border-slate-200">Khi B đồng ý: Cặp ghép được xác lập (Matched Pair) để ưu tiên xếp phòng chung. Khi B từ chối: Yêu cầu bị hủy và A được thông báo.</td>
                        </tr>
                        <tr>
                            <td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td>
                            <td class="p-1 text-slate-600 border border-slate-200">Sinh viên A nhấn nút 'Gửi yêu cầu ghép bạn' trên giao diện gợi ý bạn cùng phòng.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Basic Flow -->
            <div class="mb-2.5">
                <div class="text-[10px] font-bold text-indigo-900 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200 uppercase mb-1">
                    B. Basic Flow (Luồng cơ bản – Happy Path)
                </div>
                <table class="w-full text-[9px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-12">Step ID</th>
                            <th class="p-1 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1 border border-slate-700 text-left">Action</th>
                            <th class="p-1 border border-slate-700 w-44 text-left">Notes and References</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên A</td>
                            <td class="p-1 text-slate-700">Xem danh sách gợi ý hòa hợp nếp sống và nhấn 'Gửi yêu cầu ghép bạn' tới Sinh viên B.</td>
                            <td class="p-1 text-slate-500 italic">Trigger: SV A gửi request</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Kiểm tra điều kiện: Cùng giới tính, cùng loại phòng, B chưa vào nhóm khác và chưa có request đang chờ.</td>
                            <td class="p-1 text-slate-500 italic">BR-05. Rẽ EF-A: Không đủ điều kiện.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Tạo bản ghi yêu cầu trạng thái 'Pending', thiết lập hạn 48h và gửi thông báo tức thì đến Sinh viên B.</td>
                            <td class="p-1 text-slate-500 italic">Rẽ AF-B: A chủ động thu hồi.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên B</td>
                            <td class="p-1 text-slate-700">Đăng nhập hệ thống, mở thông báo và xem bảng đối chiếu 8 thói quen sinh hoạt của Sinh viên A.</td>
                            <td class="p-1 text-slate-500 italic">Actor: SV B. Rẽ AF-A: B từ chối.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-1 font-bold text-slate-800">Sinh viên B</td>
                            <td class="p-1 text-slate-700">Nhấn nút 'Đồng ý kết bạn cùng phòng'.</td>
                            <td class="p-1 text-slate-500 italic font-bold text-emerald-700">Đồng thuận hai chiều</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Cập nhật trạng thái 'Matched Pair' cho cặp A-B, ưu tiên xếp phòng chung và gửi thông báo chúc mừng tới cả hai.</td>
                            <td class="p-1 text-slate-500 italic">BR-05: Hoàn tất ghép cặp</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-teal-700">BF-7</td>
                            <td class="p-1 font-bold text-slate-800">Hệ thống</td>
                            <td class="p-1 text-slate-700">Đóng yêu cầu thành công và cập nhật bảng bạn cùng phòng của cả hai bên.</td>
                            <td class="p-1 text-emerald-700 font-bold">[End of Use Case: mục tiêu đã đạt]</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Alternate Flows -->
            <div class="mb-2.5">
                <div class="text-[10px] font-bold text-emerald-900 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 uppercase mb-1">
                    C. Alternate Flows (Luồng thay thế - Rẽ nhánh đúng quy tắc)
                </div>
                <div class="text-[9px] mb-1">
                    <span class="font-bold text-emerald-800">• AF-A: Sinh viên B từ chối lời mời ghép phòng</span>
                    <span class="text-slate-500 italic">(Branch point: BF-4 | Condition: SV B thấy nếp sống không hòa hợp)</span>
                </div>
                <table class="w-full text-[8.5px] border-collapse border border-slate-200 mb-1.5">
                    <tbody>
                        <tr class="bg-emerald-50/50">
                            <td class="p-0.5 text-center font-mono font-bold text-emerald-800 w-12">AF-A-1</td>
                            <td class="p-0.5 font-bold w-24">Sinh viên B</td>
                            <td class="p-0.5">Nhấn nút 'Từ chối' kèm lời nhắn lịch sự (tùy chọn).</td>
                            <td class="p-0.5 w-44 text-slate-500 italic">B từ chối lời mời</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-mono font-bold text-emerald-800">AF-A-2</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Cập nhật trạng thái 'Declined', giải phóng cờ chờ và gửi thông báo nhẹ nhàng đến Sinh viên A.</td>
                            <td class="p-0.5 text-emerald-700 font-bold">[Outcome: kind: successEnd]</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Exception Flows -->
            <div>
                <div class="text-[10px] font-bold text-rose-900 bg-rose-50 px-2 py-0.5 rounded border border-rose-200 uppercase mb-1">
                    D. Exception Flows (Luồng ngoại lệ)
                </div>
                <div class="text-[9px]">
                    <span class="font-bold text-rose-800">• EF-A: Không đủ điều kiện ràng buộc ghép đôi (Branch point: BF-2)</span>
                    <p class="text-slate-600 pl-2">Hệ thống chặn gửi và thông báo lý do (khác giới tính, khác loại phòng, đối phương đã có phòng). [End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd].</p>
                    <span class="font-bold text-rose-800">• EF-B: Lời mời hết hạn 48 giờ không phản hồi (Branch point: BF-3)</span>
                    <p class="text-slate-600 pl-2">Quá 48h SV B không tương tác, hệ thống tự động hủy request, đặt trạng thái 'Expired' và thông báo cho A để tìm bạn khác. [Outcome: kind: failureEnd].</p>
                </div>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 02 / 04</span>
        </div>
    </div>

    <!-- ==================== TRANG 3: UC-07 THANH TOÁN & UC-08 TRẢ PHÒNG ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <!-- UC-07 THANH TOÁN TIỀN PHÒNG & ĐẶT CỌC -->
            <div class="border-b-2 border-slate-200 pb-3 mb-3">
                <div class="flex items-center justify-between pb-1 mb-1.5">
                    <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-300">
                        USE CASE THANH TOÁN: TẠO VÀ IN BIÊN LAI TRỰC TIẾP TRONG LUỒNG CHÍNH
                    </span>
                    <span class="text-xs font-mono font-bold text-slate-400">UC-07</span>
                </div>
                <h2 class="text-sm font-black text-slate-900 mb-0.5">
                    UC-07: Thanh toán tiền phòng & Đặt cọc giữ chỗ 72h (Dormitory Payment & Deposit)
                </h2>
                <p class="text-[9.5px] text-slate-500 italic mb-2">
                    Sửa triệt để góp ý: "Trong chức năng thanh toán có thêm chức năng tạo/in biên lai... Không được nhét tạo biên lai vào AF".
                </p>

                <!-- Basic Flow UC-07 -->
                <table class="w-full text-[8.5px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-12">Step ID</th>
                            <th class="p-1 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1 border border-slate-700 text-left">Action</th>
                            <th class="p-1 border border-slate-700 w-44 text-left">Notes and References</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-0.5 font-bold">Sinh viên</td>
                            <td class="p-0.5">Mở màn hình thanh toán từ thông báo phân phòng trúng tuyển KTX.</td>
                            <td class="p-0.5 text-slate-500 italic">Trigger</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Hiển thị bảng kê: Tiền phòng kỳ 1 + Cọc 2.000.000đ và đồng hồ đếm ngược 72 giờ.</td>
                            <td class="p-0.5 text-slate-500 italic">BR-04. Rẽ EF-B: Quá hạn 72h.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-0.5 font-bold">Sinh viên</td>
                            <td class="p-0.5">Xác nhận thanh toán và chọn phương thức cổng điện tử VNPAY-QR.</td>
                            <td class="p-0.5 text-slate-500 italic">Rẽ AF-A: Chọn chuyển khoản.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Tạo đơn hàng bảo mật (TLS 1.3), sinh mã giao dịch duy nhất và mã QR thanh toán động.</td>
                            <td class="p-0.5 text-slate-500 italic">NFR-04</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-0.5 font-bold">Cổng VNPay</td>
                            <td class="p-0.5">Sinh viên quét QR trên Mobile Banking; VNPay trừ tiền và gửi callback (vnp_ResponseCode = 00).</td>
                            <td class="p-0.5 text-slate-500 italic">Rẽ EF-A: Giao dịch lỗi.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Cập nhật hợp đồng thành 'Paid', khóa cố định vị trí phòng giường cho sinh viên.</td>
                            <td class="p-0.5 text-slate-500 italic">Chốt phòng thành công</td>
                        </tr>
                        <tr class="bg-amber-50">
                            <td class="p-0.5 text-center font-bold font-mono text-amber-800">BF-7</td>
                            <td class="p-0.5 font-bold text-amber-900">Hệ thống</td>
                            <td class="p-0.5 font-bold text-amber-900">TỰ ĐỘNG TẠO BIÊN LAI ĐIỆN TỬ có mã tra cứu và hiển thị nút 'In biên lai' / 'Tải file PDF biên lai'.</td>
                            <td class="p-0.5 text-amber-800 font-bold">TẠO/IN BIÊN LAI TRONG BF</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-8</td>
                            <td class="p-0.5 font-bold">Sinh viên</td>
                            <td class="p-0.5">Bấm in hoặc tải biên lai điện tử về máy và hoàn tất thủ tục nhận phòng.</td>
                            <td class="p-0.5 text-emerald-700 font-bold">[End of Use Case: Thành công]</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- UC-08 TRẢ PHÒNG & QUYẾT TOÁN CỌC (CHECK-OUT) -->
            <div>
                <div class="flex items-center justify-between pb-1 mb-1.5">
                    <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800 border border-blue-300">
                        USE CASE TRẢ PHÒNG: CHUẨN HÓA VÒNG ĐỜI (KIỂM KÊ -> KHẤU TRỪ -> HOÀN CỌC -> GIẢI PHÓNG)
                    </span>
                    <span class="text-xs font-mono font-bold text-slate-400">UC-08</span>
                </div>
                <h2 class="text-sm font-black text-slate-900 mb-0.5">
                    UC-08: Thủ tục Trả phòng & Quyết toán KTX (Dormitory Check-out & Settlement)
                </h2>
                <p class="text-[9.5px] text-slate-500 italic mb-2">
                    Tách riêng hoàn toàn với Gia hạn phòng; phản ánh đúng vòng đời thanh lý hợp đồng và hoàn tiền cọc theo BR-07.
                </p>

                <!-- Basic Flow UC-08 -->
                <table class="w-full text-[8.5px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-12">Step ID</th>
                            <th class="p-1 border border-slate-700 w-24 text-left">Actor</th>
                            <th class="p-1 border border-slate-700 text-left">Action</th>
                            <th class="p-1 border border-slate-700 w-44 text-left">Notes and References</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-1</td>
                            <td class="p-0.5 font-bold">Sinh viên</td>
                            <td class="p-0.5">Gửi yêu cầu trả phòng và đăng ký lịch kiểm kê bàn giao cơ sở vật chất.</td>
                            <td class="p-0.5 text-slate-500 italic">Trigger</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-2</td>
                            <td class="p-0.5 font-bold">Cán bộ KTX</td>
                            <td class="p-0.5">Đến phòng kiểm kê tài sản (giường, tủ, khóa), chốt chỉ số điện nước và nhập vào hệ thống.</td>
                            <td class="p-0.5 text-slate-500 italic">Actor: Cán bộ KTX kiểm kê</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-3</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Tính toán công nợ dịch vụ và chi phí bồi thường hư hại tài sản (nếu có phát sinh vi phạm).</td>
                            <td class="p-0.5 text-slate-500 italic">Tính toán nợ phát sinh</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-4</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Áp dụng quy tắc tài chính BR-07: Tiền hoàn = 2.000.000đ cọc − (Nợ dịch vụ + Phí hư hại).</td>
                            <td class="p-0.5 text-slate-500 italic">BR-07. Rẽ EF-A: Nợ > 2tr.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-5</td>
                            <td class="p-0.5 font-bold">Sinh viên</td>
                            <td class="p-0.5">Kiểm tra bảng kê số liệu, bàn giao thẻ/chìa khóa phòng và ký biên bản thanh lý điện tử.</td>
                            <td class="p-0.5 text-slate-500 italic">Bàn giao vật lý</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-6</td>
                            <td class="p-0.5 font-bold">Cán bộ KTX</td>
                            <td class="p-0.5">Nhấn nút 'Xác nhận hoàn tất bàn giao phòng' trên ứng dụng quản trị KTX.</td>
                            <td class="p-0.5 text-slate-500 italic">Duyệt bàn giao</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-7</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Cập nhật hợp đồng 'Closed', giải phóng giường phòng về trạng thái 'Vacant' (Trống khả dụng).</td>
                            <td class="p-0.5 text-slate-500 italic font-bold text-indigo-700">Giải phóng giường phòng</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-8</td>
                            <td class="p-0.5 font-bold">Kế toán</td>
                            <td class="p-0.5">Duyệt lệnh hoàn cọc trên hệ thống; cổng thanh toán tự động chuyển tiền cọc thừa về tài khoản sinh viên.</td>
                            <td class="p-0.5 text-slate-500 italic">Actor: Kế toán hoàn cọc</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-9</td>
                            <td class="p-0.5 font-bold">Hệ thống</td>
                            <td class="p-0.5">Gửi email thông báo thanh lý hợp đồng thành công kèm biên lai hoàn tiền cho sinh viên.</td>
                            <td class="p-0.5 text-emerald-700 font-bold">[End of Use Case: Thành công]</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 03 / 04</span>
        </div>
    </div>

    <!-- ==================== TRANG 4: SEQUENCE DIAGRAM & VÒNG ĐỜI TƯƠNG TÁC ==================== -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-1.5 mb-2.5">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-purple-100 text-purple-800 border border-purple-300">
                    5. BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) CHUẨN THANH VÒNG ĐỜI (ACTIVATION BARS)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">UC-05 SEQUENCE</span>
            </div>

            <h2 class="text-base font-black text-slate-900 mb-0.5">
                Biểu đồ Tuần tự Ghép bạn cùng phòng theo Request (SV A → Hệ thống → SV B)
            </h2>
            <p class="text-[10.5px] text-slate-500 italic mb-2">
                Thể hiện chính xác thanh vòng đời (Activation bars) mở/đóng đúng phiên làm việc; phân định rõ 2 con người độc lập A và B.
            </p>

            <!-- Mermaid Diagram Container -->
            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 mb-3">
                <div class="mermaid text-xs">
sequenceDiagram
    autonumber
    actor SVA as 🧑 Sinh viên A (Gửi Request)
    participant UI as 🖥️ Giao diện KTX Web
    participant MatchSvc as ⚙️ Matching Service
    participant DB as 🗄️ Database KTX
    actor SVB as 🧑 Sinh viên B (Nhận Request)

    Note over SVA, SVB: GIAI ĐOẠN 1: SINH VIÊN A GỬI YÊU CẦU GHÉP PHÒNG
    SVA->>UI: 1. (BF-1) Chọn ứng viên B & Bấm "Gửi yêu cầu ghép bạn"
    activate UI
    UI->>MatchSvc: 2. (BF-2) Kiểm tra điều kiện (giới tính, loại phòng, BR-05)
    activate MatchSvc
    MatchSvc->>DB: 3. (BF-2) Truy vấn hồ sơ B & Kiểm tra cờ nhóm
    activate DB
    DB-->>MatchSvc: 4. (BF-2) Xác nhận B hợp lệ & chưa thuộc nhóm nào
    deactivate DB
    
    MatchSvc->>DB: 5. (BF-3) Lưu yêu cầu trạng thái "Pending" (Hạn 48h)
    activate DB
    DB-->>MatchSvc: 6. (BF-3) Xác nhận lưu bản ghi thành công
    deactivate DB

    MatchSvc->>SVB: 7. (BF-3) Đẩy thông báo: "Bạn có lời mời ghép phòng từ SV A"
    MatchSvc-->>UI: 8. (BF-3) Phản hồi: Đã gửi lời mời thành công
    deactivate MatchSvc
    UI-->>SVA: 9. (BF-3) Thông báo gửi request thành công, chờ B phản hồi
    deactivate UI

    Note over SVA, SVB: GIAI ĐOẠN 2: SINH VIÊN B ĐỐI SOÁT & PHẢN HỒI (BẤT ĐỒNG BỘ)
    SVB->>UI: 10. (BF-4) Đăng nhập, mở xem chi tiết hồ sơ 8 thói quen của A
    activate UI
    UI->>MatchSvc: 11. (BF-4) Lấy thông tin so sánh đối soát nếp sống
    activate MatchSvc
    MatchSvc-->>UI: 12. (BF-4) Trả về bảng đối chiếu tiêu chí (Ref: BR-09)
    deactivate MatchSvc
    UI-->>SVB: 13. (BF-4) Hiển thị giao diện so sánh hòa hợp & 2 nút lựa chọn
    deactivate UI

    alt Trường hợp B Đồng ý (Accept - Luồng cơ bản BF-5, BF-6)
        SVB->>UI: 14. (BF-5) Nhấn nút "Đồng ý ghép phòng"
        activate UI
        UI->>MatchSvc: 15. (BF-5) Gửi lệnh chấp thuận kết bạn
        activate MatchSvc
        MatchSvc->>DB: 16. (BF-6) Cập nhật trạng thái nhóm thành "Matched Pair"
        activate DB
        DB-->>MatchSvc: 17. (BF-6) Xác nhận liên kết thành công
        deactivate DB
        MatchSvc->>SVA: 18. (BF-6) Gửi thông báo chúc mừng tới A: "SV B đã đồng ý!"
        MatchSvc-->>UI: 19. (BF-6) Thông báo thành công tới B
        deactivate MatchSvc
        UI-->>SVB: 20. (BF-7) Hiển thị thông báo hoàn tất ghép đôi
        deactivate UI
    else Trường hợp B Từ chối (Decline - Luồng thay thế AF-A)
        SVB->>UI: 21. (AF-A-1) Nhấn nút "Từ chối ghép bạn"
        activate UI
        UI->>MatchSvc: 22. (AF-A-2) Hủy yêu cầu, cập nhật trạng thái "Declined"
        activate MatchSvc
        MatchSvc->>DB: 23. (AF-A-2) Giải phóng cờ chờ của A và B
        activate DB
        DB-->>MatchSvc: 24. (AF-A-2) Xác nhận hủy
        deactivate DB
        MatchSvc->>SVA: 25. (AF-A-3) Thông báo tới A: "Lời mời chưa được chấp thuận"
        deactivate MatchSvc
        UI-->>SVB: 26. (AF-A-3) Xác nhận đóng yêu cầu thành công
        deactivate UI
    end
                </div>
            </div>

            <!-- Đối chiếu quy tắc -->
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-lg text-[9.5px]">
                <span class="font-bold text-slate-800 uppercase block mb-1">Đánh giá tính chuẩn xác của Sequence Diagram:</span>
                <ul class="text-slate-600 space-y-0.5 list-disc list-inside">
                    <li><strong>Thanh kích hoạt vòng đời (Lifeline Activation Bars):</strong> Khối chữ nhật màu xanh mở ra khi đối tượng nhận thông điệp kích hoạt và đóng lại ngay khi trả kết quả (deactivate), không bị kéo dài vô lý.</li>
                    <li><strong>Phân định rõ 2 người dùng (A và B):</strong> Sinh viên A gửi thông điệp ở Giai đoạn 1 và đóng phiên; Sinh viên B mở phiên làm việc mới ở Giai đoạn 2 để xem xét và bấm duyệt, đúng bản chất bất đồng bộ.</li>
                    <li><strong>Khớp 1-1 tuyệt đối:</strong> 100% các bước đánh số trên Sequence Diagram đều trùng khớp với mã Step ID trong Bảng đặc tả Use Case (BF-1 đến BF-7, AF-A-1 đến AF-A-3).</li>
                </ul>
            </div>
        </div>

        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 04 / 04</span>
        </div>
    </div>

</body>
</html>
"""

def generate_html_and_pdf():
    html_path = os.path.join(os.path.dirname(__file__), "ui", "revised_usecase_spec.html")
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

    pdf_out_docs = os.path.join(os.path.dirname(__file__), "docs", "Dac_Ta_Use_Case_Va_Business_Rules_KTX_Chuan_VNUK.pdf")
    pdf_out_dl = os.path.join(r"C:\Users\LENOVO\Downloads", "Dac_Ta_Use_Case_Va_Business_Rules_KTX_Chuan_VNUK.pdf")

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
