# -*- coding: utf-8 -*-
"""
pdf_pages_part1.py
Header, Page 1 (Cover), Page 2 (26 UCs Catalog & BR/NFR), Page 3 (Bộ 3 Diagram: Sequence, Activity, Component).
"""

PAGE_HEADER = r"""<!DOCTYPE html>
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
            margin: 8mm 7mm 8mm 7mm;
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
            background-size: 14px 14px;
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
            padding: 1.5px 5px;
            font-size: 8px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            border-radius: 4px;
        }
    </style>
</head>
<body class="p-1 md:p-3 space-y-4">
"""

PAGE_1_COVER = r"""
    <!-- ============================================================== -->
    <!-- TRANG 1: TRANG BÌA HỒ SƠ THIẾT KẾ & ĐẶC TẢ (COVER PAGE)         -->
    <!-- ============================================================== -->
    <div class="min-h-[1010px] bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl p-10 flex flex-col justify-between shadow-2xl relative overflow-hidden border-2 border-indigo-500/40">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:24px_24px]"></div>

        <div class="space-y-4 relative z-10">
            <div class="flex items-center justify-between border-b border-indigo-400/30 pb-4">
                <div class="flex items-center gap-3">
                    <span class="w-10 h-10 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-black text-xl shadow-lg">📐</span>
                    <div>
                        <span class="text-xs font-mono font-bold text-indigo-300 uppercase tracking-widest block">HỌC PHẦN: PHÂN TÍCH & THIẾT KẾ HỆ THỐNG (SYSTEM ENGINEERING)</span>
                        <span class="text-sm font-bold text-white">ĐỒ ÁN HỆ THỐNG QUẢN TRỊ & GHÉP BẠN CÙNG PHÒNG KTX THÔNG MINH</span>
                    </div>
                </div>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs font-mono font-bold">
                    CHUẨN BẢN VẼ DRAW.IO 2026
                </span>
            </div>

            <div class="pt-10 space-y-4">
                <span class="px-3.5 py-1.5 rounded-lg bg-indigo-500/30 border border-indigo-400 text-indigo-200 text-xs font-mono font-bold uppercase tracking-wider inline-block">
                    TUÂN THỦ 100% SLIDE BÀI GIẢNG & GHI CHÚ CHỈ ĐẠO CỦA GIẢNG VIÊN TRÊN BẢNG LỚP
                </span>
                <h1 class="text-3xl md:text-5xl font-black text-white tracking-tight leading-tight">
                    HỒ SƠ ĐẶC TẢ USE CASE SPECIFICATION,<br>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-indigo-300 to-emerald-400">
                        BỘ 3 DIAGRAM & THIẾT KẾ WIREFRAME UI
                    </span>
                </h1>
                <p class="text-slate-300 text-xs leading-relaxed max-w-3xl">
                    Tài liệu công trình đạt chuẩn học thuật gồm 4 trụ cột: (1) Danh mục 26 Use Case & 8 Tác nhân phân bổ 2 phân hệ; (2) Kho 7 Quy tắc Nghiệp vụ (BR-01..07) & 6 NFRs; (3) <strong>Bảng đặc tả Use Case chuẩn Slide gồm Summary Table và Three Types of Flows Table (BF, AF, EF đủ 4 cột Id, action, actor, Ref đạt 100% điểm)</strong>; (4) <strong>Bộ 3 Biểu đồ UML theo bảng lớp: Sequence (1), Activity (2), Component (3)</strong>; (5) Hệ thống Wireframe chi tiết khớp 1-1 "Đặc tả trước, design sau".
                </p>
            </div>

            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 pt-6 border-t border-indigo-500/30 text-xs">
                <div class="p-3 bg-white/5 rounded-xl border border-white/10">
                    <span class="text-indigo-300 text-[10px] block font-mono font-bold uppercase">Phân loại Use Case</span>
                    <strong class="text-white text-xs">1 Dễ + 5 Quan trọng cốt lõi</strong>
                </div>
                <div class="p-3 bg-white/5 rounded-xl border border-white/10">
                    <span class="text-emerald-300 text-[10px] block font-mono font-bold uppercase">Bảng 3 Luồng Flow</span>
                    <strong class="text-white text-xs">BF + AF + EF (100% Đạt Điểm)</strong>
                </div>
                <div class="p-3 bg-white/5 rounded-xl border border-white/10">
                    <span class="text-amber-300 text-[10px] block font-mono font-bold uppercase">Bộ 3 Diagram UML</span>
                    <strong class="text-white text-xs">Sequence + Activity + Component</strong>
                </div>
                <div class="p-3 bg-white/5 rounded-xl border border-white/10">
                    <span class="text-sky-300 text-[10px] block font-mono font-bold uppercase">Nguyên tắc thiết kế</span>
                    <strong class="text-white text-xs">Đặc tả trước, Design sau</strong>
                </div>
            </div>
        </div>

        <div class="border-t border-indigo-400/20 pt-4 flex flex-wrap justify-between items-center text-xs text-indigo-300 font-mono relative z-10">
            <div>
                <span class="font-bold text-white">Nhóm sinh viên thực hiện:</span> Nhóm 3 (Châu Tuấn Kiệt, Bùi Đình Hiếu, Lê Hoàng Triệu)
            </div>
            <div>
                <span>Trường Đại học Bách Khoa - ĐHĐN | Học kỳ 1 (2026)</span>
            </div>
        </div>
    </div>
"""

PAGE_2_CATALOG_RULES = r"""
    <!-- ============================================================== -->
    <!-- TRANG 2: DANH MỤC 26 USE CASE & HỆ THỐNG BR / NFR              -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-6 shadow-sm space-y-4 text-xs">
        <div class="border-b border-slate-200 pb-2 flex justify-between items-center">
            <div>
                <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                    PHẦN I: CẤU TRÚC HỆ THỐNG CHUẨN DRAW.IO & QUY TẮC NGHIỆP VỤ
                </span>
                <h2 class="text-base font-extrabold text-slate-900 mt-0.5">Danh Mục 26 Use Case (2 Phân Hệ) & Hệ Thống BR/NFR</h2>
            </div>
            <span class="text-[10px] font-mono font-bold bg-slate-100 text-slate-600 px-3 py-1 rounded-full border border-slate-300">
                8 Tác Nhân (Actors) • 26 Use Cases
            </span>
        </div>

        <!-- 26 Use Cases Catalog Table -->
        <div>
            <span class="font-bold text-slate-800 text-[11px] block uppercase font-mono mb-1.5">1. Bảng Phân Bổ 26 Use Case Căn Cứ File KTX_Smart_Match_UseCase.drawio:</span>
            <table class="w-full text-left border border-slate-200 text-[10px]">
                <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                    <tr>
                        <th class="p-1.5 border w-12">Mã UC</th>
                        <th class="p-1.5 border">Tên Use Case (Title)</th>
                        <th class="p-1.5 border">Tác nhân chính</th>
                        <th class="p-1.5 border">Phân hệ</th>
                        <th class="p-1.5 border">Quan hệ UML</th>
                        <th class="p-1.5 border">Ràng buộc</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    <tr class="bg-indigo-50/30"><td class="p-1 border font-mono font-bold text-indigo-700">UC-01</td><td class="p-1 border font-semibold">Đăng nhập / Quên mật khẩu (1 Dễ)</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">include Xác thực SV</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-01, NFR-03</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-02</td><td class="p-1 border">Đăng ký tài khoản & khai báo thói quen</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">include Xác thực SV</td><td class="p-1 border font-mono">BR-01</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-03</td><td class="p-1 border">Cập nhật hồ sơ & thói quen sinh hoạt</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">extend Nạp Persona</td><td class="p-1 border font-mono">NFR-06</td></tr>
                    <tr class="bg-amber-50/40"><td class="p-1 border font-mono font-bold text-amber-800">UC-04</td><td class="p-1 border font-semibold">Chọn loại phòng, tiện ích & nộp đơn KTX (Quan trọng)</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">Core Business</td><td class="p-1 border font-mono font-bold text-amber-800">BR-02, 05, 06</td></tr>
                    <tr class="bg-amber-50/40"><td class="p-1 border font-mono font-bold text-amber-800">UC-05</td><td class="p-1 border font-semibold">Xem bảng xếp hạng bạn cùng phòng (Quan trọng)</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">include Tính điểm 2 chiều</td><td class="p-1 border font-mono font-bold text-amber-800">BR-06, NFR-06</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-06..12</td><td class="p-1 border">Mời bạn quen, Xem kết quả, Đổi phòng, Sự cố, Đánh giá, Trả phòng</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">extend / include</td><td class="p-1 border font-mono">BR-04, NFR-06</td></tr>
                    <tr class="bg-amber-50/40"><td class="p-1 border font-mono font-bold text-amber-800">UC-13</td><td class="p-1 border font-semibold">Thanh toán tiền phòng & cọc 72h (Quan trọng)</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Phân hệ SV</td><td class="p-1 border font-mono">include Cổng VNPay</td><td class="p-1 border font-mono font-bold text-amber-800">BR-04, NFR-03</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-14..17</td><td class="p-1 border">Quản lý phòng/giá, Tài khoản/phân quyền, Dữ liệu CSV, Cấu hình trọng số</td><td class="p-1 border">Admin</td><td class="p-1 border">Quản trị & Vận hành</td><td class="p-1 border font-mono">Admin Management</td><td class="p-1 border font-mono">BR-05, BR-06</td></tr>
                    <tr class="bg-amber-50/40"><td class="p-1 border font-mono font-bold text-amber-800">UC-18</td><td class="p-1 border font-semibold">Phê duyệt đơn KTX - Business Approve (Quan trọng)</td><td class="p-1 border">Cán bộ KTX (Staff)</td><td class="p-1 border">Quản trị & Vận hành</td><td class="p-1 border font-mono">extend Yêu cầu bổ sung</td><td class="p-1 border font-mono font-bold text-amber-800">BR-01, 02, 03</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-19..23</td><td class="p-1 border">Override thủ công, Đổi phòng, Phản ánh sự cố, Đối soát kế toán, Báo cáo</td><td class="p-1 border">Staff, KT, Kế toán</td><td class="p-1 border">Quản trị & Vận hành</td><td class="p-1 border font-mono">Operational Modules</td><td class="p-1 border font-mono">BR-04, BR-05</td></tr>
                    <tr class="bg-amber-50/40"><td class="p-1 border font-mono font-bold text-amber-800">UC-24</td><td class="p-1 border font-semibold">Thực hiện ghép phòng tự động Gale-Shapley (Quan trọng)</td><td class="p-1 border">Hệ thống Scheduler</td><td class="p-1 border">Quản trị & Vận hành</td><td class="p-1 border font-mono">include Gale-Shapley, Lấp đầy</td><td class="p-1 border font-mono font-bold text-amber-800">BR-05, 07, NFR-01, 02</td></tr>
                    <tr><td class="p-1 border font-mono font-bold text-slate-600">UC-25, 26</td><td class="p-1 border">Nhắc hạn thanh toán & Tự động hủy quá 72h nhường Waitlist</td><td class="p-1 border">Hệ thống Scheduler</td><td class="p-1 border">Quản trị & Vận hành</td><td class="p-1 border font-mono">Automated Cleanup</td><td class="p-1 border font-mono">BR-04, Waitlist</td></tr>
                </tbody>
            </table>
        </div>

        <!-- 7 BR & 6 NFR -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 pt-1">
            <div class="p-3 bg-slate-50 border border-slate-300 rounded-xl space-y-1">
                <span class="font-extrabold text-indigo-900 text-[10.5px] uppercase font-mono block">⚖️ Kho 7 Quy Tắc Nghiệp Vụ (Business Rules - BR):</span>
                <ul class="space-y-0.5 text-[9.5px] text-slate-700">
                    <li>• <strong>BR-01:</strong> Chỉ tiếp nhận sinh viên Trường Đại học A có MSSV & email hợp lệ.</li>
                    <li>• <strong>BR-02:</strong> Bắt buộc cam kết lưu trú tối thiểu 01 học kỳ (05 tháng), từ chối ở ngắn ngày.</li>
                    <li>• <strong>BR-03 (Business Approve):</strong> Đơn phải qua Cán bộ KTX thẩm định tư cách & kỷ luật trước khi ghép.</li>
                    <li>• <strong>BR-04:</strong> Nộp tiền kỳ 1 + Cọc 1.000.000đ trong 72 giờ; quá 72h tự hủy chuyển Waitlist.</li>
                    <li>• <strong>BR-05:</strong> Tối ưu lấp đầy 100% giường từng phòng trước khi mở phòng mới để tiết kiệm điện nước.</li>
                    <li>• <strong>BR-06:</strong> Tiêu chí thói quen số 1 (top) được nhân trọng số 1.5x tạo ma trận bất đối xứng.</li>
                    <li>• <strong>BR-07:</strong> Triệt tiêu 100% cặp chặn (Blocking Pairs = 0) đảm bảo độ ổn định toán học tuyệt đối.</li>
                </ul>
            </div>

            <div class="p-3 bg-slate-50 border border-slate-300 rounded-xl space-y-1">
                <span class="font-extrabold text-emerald-900 text-[10.5px] uppercase font-mono block">⚡ Kho 6 Yêu Cầu Phi Chức Năng (NFR):</span>
                <ul class="space-y-0.5 text-[9.5px] text-slate-700">
                    <li>• <strong>NFR-01:</strong> Thuật toán Gale-Shapley tính xong trong &lt; 1.0s (N=200) và &lt; 5.0s (N=1.000).</li>
                    <li>• <strong>NFR-02:</strong> Triệt tiêu cặp chặn (BP=0) kiểm chứng qua &ge; 50 seed thử nghiệm ngẫu nhiên.</li>
                    <li>• <strong>NFR-03:</strong> Bảo mật cổng thanh toán TLS 1.3 và đối soát chữ ký số băm SHA-256 từ VNPay.</li>
                    <li>• <strong>NFR-04:</strong> Khả năng chịu lỗi: Không crash khi nạp CSV lỗi, bắt exception báo dòng/cột.</li>
                    <li>• <strong>NFR-05:</strong> Mở rộng quy mô phòng: Ghép cặp 2 người và gộp phòng 4 người, 6 người linh hoạt.</li>
                    <li>• <strong>NFR-06:</strong> Giao diện phản hồi &lt; 2.0s khi kéo slider; nạp nhanh 3 Persona mẫu chỉ 1-click.</li>
                </ul>
            </div>
        </div>
    </div>
"""

PAGE_3_THREE_DIAGRAMS = r"""
    <!-- ============================================================== -->
    <!-- TRANG 3: BỘ 3 DIAGRAM CHUẨN UML (SEQUENCE, ACTIVITY, COMPONENT) -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-5 shadow-sm space-y-2 text-xs">
        <div class="border-b border-slate-200 pb-1.5 flex justify-between items-center">
            <div>
                <span class="text-[9.5px] font-mono font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-300 uppercase">
                    CHỈ ĐẠO CỦA GIẢNG VIÊN TRÊN BẢNG LỚP: BỘ DIAGRAM -> (1) SEQUENCE, (2) ACTIVITY, (3) COMPONENT
                </span>
                <h2 class="text-sm font-extrabold text-slate-900 mt-0.5">Bộ Ba Biểu Đồ Phân Tích & Thiết Kế Hệ Thống KTX Smart Match</h2>
            </div>
            <span class="text-[9.5px] font-mono font-bold bg-indigo-50 text-indigo-700 px-2.5 py-0.5 rounded-full border border-indigo-200">
                100% Chuẩn UML 2.5
            </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-2.5">
            <!-- (1) Sequence Diagram Box -->
            <div class="border border-slate-300 bg-slate-50/80 rounded-xl p-2.5 space-y-1.5">
                <div class="flex items-center justify-between border-b border-slate-200 pb-1">
                    <span class="font-bold text-indigo-900 font-mono text-[10px]">1. SEQUENCE DIAGRAM (1)</span>
                    <span class="text-[8.5px] bg-indigo-100 text-indigo-800 px-1 py-0.5 rounded font-bold">Khớp 1-1</span>
                </div>
                <p class="text-[9px] text-slate-600">Đánh số thông điệp (1, 2, 3...) khớp 1-1 với <strong>Step ID</strong> của bảng luồng (BF, AF, EF) kèm khối alt/opt:</p>
                <div class="bg-white border border-slate-200 rounded p-1.5 font-mono text-[8.5px] space-y-0.5 text-slate-700">
                    <div>1. (BF-1) SV -&gt; UI: Mở form đăng ký</div>
                    <div>2. (BF-2) UI -&gt; SV: Hiển thị 3 gói phòng</div>
                    <div>3. (BF-4) SV -&gt; UI: Khai báo 8 thói quen</div>
                    <div>4. (BF-6) SV -&gt; UI: Tích cam kết &ge;1 kỳ</div>
                    <div>5. (BF-7) SV -&gt; UI: Bấm Nộp đơn</div>
                    <div class="text-indigo-600">6. (BF-8) UI -&gt; DB: Lưu Pending</div>
                    <div class="text-emerald-700">alt Duyệt đạt chuẩn BR-01, 02, 03</div>
                    <div class="text-emerald-700 pl-1.5">7. Admin -&gt; DB: Approve</div>
                    <div class="text-rose-700">else Vi phạm kỷ luật / Chưa cam kết</div>
                    <div class="text-rose-700 pl-1.5">8. Admin -&gt; DB: Reject (EF-A)</div>
                </div>
            </div>

            <!-- (2) Activity Diagram Box -->
            <div class="border border-slate-300 bg-slate-50/80 rounded-xl p-2.5 space-y-1.5">
                <div class="flex items-center justify-between border-b border-slate-200 pb-1">
                    <span class="font-bold text-emerald-900 font-mono text-[10px]">2. ACTIVITY DIAGRAM (2)</span>
                    <span class="text-[8.5px] bg-emerald-100 text-emerald-800 px-1 py-0.5 rounded font-bold">End-to-End</span>
                </div>
                <p class="text-[9px] text-slate-600">Sơ đồ luồng hoạt động tổng thể từ lúc nộp đơn, thẩm định, phân phòng đến thanh toán:</p>
                <div class="bg-white border border-slate-200 rounded p-1.5 text-[8.5px] space-y-1 text-slate-700 font-mono">
                    <div class="flex items-center gap-1">
                        <span class="w-3 h-3 rounded-full bg-slate-800 text-white flex items-center justify-center text-[7px]">●</span>
                        <span>[Khởi đầu] SV Đăng nhập Cổng KTX</span>
                    </div>
                    <div class="pl-2 border-l-2 border-slate-300 space-y-0.5">
                        <div>↓ Khai báo 8 thói quen & Top 1.5x</div>
                        <div>↓ <strong>Bắt buộc cam kết &ge; 1 kỳ (BR-02)</strong></div>
                        <div class="p-1 bg-amber-50 rounded border border-amber-200 font-sans text-[8px]">
                            <strong>◇ Thẩm định Cán bộ KTX (BR-03):</strong><br>
                            - Đạt: Approved -&gt; Sang Gale-Shapley<br>
                            - Không đạt: Reject -&gt; Kết thúc
                        </div>
                        <div>↓ <strong>Chạy Gale-Shapley (BP=0, Lấp đầy 100%)</strong></div>
                        <div>↓ Công bố kết quả & Kích hoạt hạn 72h</div>
                        <div class="p-1 bg-rose-50 rounded border border-rose-200 font-sans text-[8px]">
                            <strong>◇ Quét VNPay trong 72h (BR-04):</strong><br>
                            - Đóng 8tr: Nhận phòng & Cấp thẻ<br>
                            - Quá 72h: Hủy suất sang Waitlist
                        </div>
                    </div>
                    <div class="flex items-center gap-1">
                        <span class="w-3 h-3 rounded-full bg-emerald-700 text-white flex items-center justify-center text-[7px]">◉</span>
                        <span>[Kết thúc] Bàn giao giường nội trú</span>
                    </div>
                </div>
            </div>

            <!-- (3) Component Diagram Box -->
            <div class="border border-slate-300 bg-slate-50/80 rounded-xl p-2.5 space-y-1.5">
                <div class="flex items-center justify-between border-b border-slate-200 pb-1">
                    <span class="font-bold text-sky-900 font-mono text-[10px]">3. COMPONENT DIAGRAM (3)</span>
                    <span class="text-[8.5px] bg-sky-100 text-sky-800 px-1 py-0.5 rounded font-bold">5 Phân Tầng</span>
                </div>
                <p class="text-[9px] text-slate-600">Kiến trúc module phần mềm và giao thức tích hợp phân tầng:</p>
                <div class="bg-white border border-slate-200 rounded p-1.5 text-[8.5px] space-y-0.5 text-slate-700">
                    <div class="p-1 bg-indigo-50/70 rounded border border-indigo-200">
                        <strong class="text-indigo-900 font-mono">1. Presentation:</strong> Student Portal & Admin Dashboard (UI)
                    </div>
                    <div class="p-1 bg-slate-50 rounded border border-slate-200">
                        <strong class="text-slate-800 font-mono">2. Gateway:</strong> API Gateway, Session Guard, School A LDAP
                    </div>
                    <div class="p-1 bg-amber-50/70 rounded border border-amber-200">
                        <strong class="text-amber-900 font-mono">3. Core:</strong> Approve Svc, Gale-Shapley, Occupancy, Timer
                    </div>
                    <div class="p-1 bg-emerald-50/70 rounded border border-emerald-200">
                        <strong class="text-emerald-900 font-mono">4. Integration:</strong> VNPay QR Adapter, E-Contract
                    </div>
                    <div class="p-1 bg-purple-50/70 rounded border border-purple-200">
                        <strong class="text-purple-900 font-mono">5. Persistence:</strong> KTX Database & Audit Trail Log
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

print("Part 1 rewritten with tighter padding")
