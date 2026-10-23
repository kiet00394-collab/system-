# -*- coding: utf-8 -*-
"""
slides_data_2.py
Slides 7 to 14:
- Slide 7: Activity Diagram (2) - Luồng hoạt động tổng thể
- Slide 8: Component Diagram (3) - Kiến trúc 5 tầng thành phần
- Slide 9: UC-01 (1 Dễ) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 10: UC-01 - Wireframe WF-01 & Sequence Diagram Khớp 1-1
- Slide 11: UC-04 (Quan trọng) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 12: UC-04 - Wireframe WF-02 & Sequence Diagram Khớp 1-1
- Slide 13: UC-05 (Quan trọng) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 14: UC-05 - Wireframe WF-03 & Sequence Diagram Khớp 1-1
"""

SLIDE_7 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded border border-emerald-300 uppercase">
                BỘ DIAGRAM THẦY GIAO • SLIDE 07/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">6. Biểu Đồ Hoạt Động Tổng Thể (Activity Diagram - 2)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
            Luồng Nghiệp Vụ End-to-End
        </span>
    </div>

    <!-- Activity Workflow Visual -->
    <div class="my-auto space-y-3">
        <p class="text-xs text-slate-600">Sơ đồ mô hình hóa tiến trình khép kín từ lúc sinh viên nộp đơn, xét duyệt Business Approve, chạy thuật toán Gale-Shapley đến khi thanh toán cọc trong 72 giờ và nhận bàn giao phòng:</p>
        
        <div class="grid grid-cols-5 gap-3 text-xs">
            <!-- Stage 1 -->
            <div class="p-3 bg-slate-50 border border-slate-300 rounded-xl space-y-1.5 relative">
                <span class="w-6 h-6 rounded-full bg-slate-900 text-white flex items-center justify-center font-bold text-xs">1</span>
                <strong class="block text-slate-900 font-mono text-[11px]">KHỞI TẠO ĐƠN (SV)</strong>
                <ul class="text-[10.5px] text-slate-600 space-y-1">
                    <li>• Đăng nhập MSSV Trường A (BR-01)</li>
                    <li>• Chọn gói phòng 2, 4, 6 người (BR-05)</li>
                    <li>• Khai báo 8 thói quen & Top 1.5x (BR-06)</li>
                    <li>• <strong class="text-indigo-700">Cam kết ở &ge; 1 kỳ (BR-02)</strong></li>
                </ul>
            </div>

            <!-- Stage 2 -->
            <div class="p-3 bg-amber-50 border border-amber-300 rounded-xl space-y-1.5 relative">
                <span class="w-6 h-6 rounded-full bg-amber-700 text-white flex items-center justify-center font-bold text-xs">2</span>
                <strong class="block text-amber-950 font-mono text-[11px]">THẨM ĐỊNH ĐƠN (STAFF)</strong>
                <ul class="text-[10.5px] text-amber-900 space-y-1">
                    <li>• Cán bộ KTX kiểm tra tư cách & kỷ luật</li>
                    <li>• Đối soát tự động BR-01 & BR-02</li>
                    <li>• Kiểm tra hạn ngạch quỹ phòng</li>
                    <li>• <strong class="text-emerald-700">Business Approve (BR-03)</strong> hoặc Từ chối kèm lý do</li>
                </ul>
            </div>

            <!-- Stage 3 -->
            <div class="p-3 bg-indigo-50 border border-indigo-300 rounded-xl space-y-1.5 relative">
                <span class="w-6 h-6 rounded-full bg-indigo-700 text-white flex items-center justify-center font-bold text-xs">3</span>
                <strong class="block text-indigo-950 font-mono text-[11px]">GALE-SHAPLEY ENGINE</strong>
                <ul class="text-[10.5px] text-indigo-900 space-y-1">
                    <li>• Tính ma trận tương thích 2 chiều (BR-06)</li>
                    <li>• Ghép cặp ổn định (&lt; 1s, NFR-01)</li>
                    <li>• <strong class="text-emerald-700">Lấp đầy 100% giường (BR-05)</strong></li>
                    <li>• <strong class="text-purple-700">Blocking Pairs = 0 (BR-07)</strong></li>
                </ul>
            </div>

            <!-- Stage 4 -->
            <div class="p-3 bg-rose-50 border border-rose-300 rounded-xl space-y-1.5 relative">
                <span class="w-6 h-6 rounded-full bg-rose-700 text-white flex items-center justify-center font-bold text-xs">4</span>
                <strong class="block text-rose-950 font-mono text-[11px]">HẠN 72H THANH TOÁN</strong>
                <ul class="text-[10.5px] text-rose-900 space-y-1">
                    <li>• Kích hoạt đồng hồ đếm ngược 72h (BR-04)</li>
                    <li>• Quét mã VNPAY-QR nộp 8.000.000đ</li>
                    <li>• Cổng VNPay đối soát SHA-256</li>
                    <li>• <strong class="text-rose-700">Quá 72h: Hủy suất nhường Waitlist</strong></li>
                </ul>
            </div>

            <!-- Stage 5 -->
            <div class="p-3 bg-emerald-50 border border-emerald-300 rounded-xl space-y-1.5 relative">
                <span class="w-6 h-6 rounded-full bg-emerald-700 text-white flex items-center justify-center font-bold text-xs">5</span>
                <strong class="block text-emerald-950 font-mono text-[11px]">BÀN GIAO PHÒNG</strong>
                <ul class="text-[10.5px] text-emerald-900 space-y-1">
                    <li>• Chốt giường chính thức 100%</li>
                    <li>• Tự động sinh Hợp đồng điện tử</li>
                    <li>• Cấp Biên lai & Mã thẻ phòng QR</li>
                    <li>• Sinh viên làm thủ tục nhận phòng</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_8 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-sky-700 bg-sky-50 px-2.5 py-0.5 rounded border border-sky-300 uppercase">
                BỘ DIAGRAM THẦY GIAO • SLIDE 08/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">7. Biểu Đồ Thành Phần Hệ Thống (Component Diagram - 3)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-sky-100 text-sky-800 px-3 py-1 rounded-full">
            Kiến Trúc 5 Phân Tầng Module
        </span>
    </div>

    <div class="grid grid-cols-5 gap-3 my-auto text-xs">
        <!-- Layer 1 -->
        <div class="border-2 border-indigo-200 bg-indigo-50/40 rounded-xl p-3 space-y-2">
            <span class="font-bold text-indigo-900 font-mono text-[10.5px] block border-b border-indigo-200 pb-1">1. PRESENTATION</span>
            <div class="space-y-1.5 text-[10px]">
                <div class="p-2 bg-white rounded border border-indigo-200">
                    <strong class="text-indigo-950 block">Student Web Portal</strong>
                    <span class="text-slate-500">Khảo sát, nộp đơn, xem BXH, quét QR VNPay</span>
                </div>
                <div class="p-2 bg-white rounded border border-indigo-200">
                    <strong class="text-indigo-950 block">Admin / Staff Dashboard</strong>
                    <span class="text-slate-500">Thẩm định đơn, chạy GS, xuất báo cáo</span>
                </div>
            </div>
        </div>

        <!-- Layer 2 -->
        <div class="border-2 border-slate-300 bg-slate-50 rounded-xl p-3 space-y-2">
            <span class="font-bold text-slate-800 font-mono text-[10.5px] block border-b border-slate-200 pb-1">2. GATEWAY & AUTH</span>
            <div class="space-y-1.5 text-[10px]">
                <div class="p-2 bg-white rounded border border-slate-200">
                    <strong class="text-slate-900 block">API Gateway</strong>
                    <span class="text-slate-500">Reverse proxy, Rate limit, bảo vệ phiên</span>
                </div>
                <div class="p-2 bg-white rounded border border-slate-200">
                    <strong class="text-slate-900 block">School A LDAP / REST</strong>
                    <span class="text-slate-500">Đối soát MSSV và email trường (BR-01)</span>
                </div>
            </div>
        </div>

        <!-- Layer 3 -->
        <div class="border-2 border-amber-300 bg-amber-50/40 rounded-xl p-3 space-y-2">
            <span class="font-bold text-amber-900 font-mono text-[10.5px] block border-b border-amber-200 pb-1">3. CORE BUSINESS</span>
            <div class="space-y-1.5 text-[10px]">
                <div class="p-1.5 bg-white rounded border border-amber-200">
                    <strong class="text-amber-950 block">Approval Service</strong>
                    <span class="text-slate-500">Xét duyệt đơn BR-02, BR-03</span>
                </div>
                <div class="p-1.5 bg-white rounded border border-amber-200">
                    <strong class="text-amber-950 block">Gale-Shapley Engine</strong>
                    <span class="text-slate-500">Ghép cặp ổn định BP=0 (BR-07)</span>
                </div>
                <div class="p-1.5 bg-white rounded border border-amber-200">
                    <strong class="text-amber-950 block">Occupancy Optimizer</strong>
                    <span class="text-slate-500">Lấp đầy 100% giường (BR-05)</span>
                </div>
            </div>
        </div>

        <!-- Layer 4 -->
        <div class="border-2 border-emerald-300 bg-emerald-50/40 rounded-xl p-3 space-y-2">
            <span class="font-bold text-emerald-900 font-mono text-[10.5px] block border-b border-emerald-200 pb-1">4. INTEGRATION</span>
            <div class="space-y-1.5 text-[10px]">
                <div class="p-2 bg-white rounded border border-emerald-200">
                    <strong class="text-emerald-950 block">VNPay Adapter</strong>
                    <span class="text-slate-500">Tạo QR động, xác thực chữ ký SHA-256 (NFR-03)</span>
                </div>
                <div class="p-2 bg-white rounded border border-emerald-200">
                    <strong class="text-emerald-950 block">E-Contract & QR</strong>
                    <span class="text-slate-500">Sinh hợp đồng số & biên lai điện tử</span>
                </div>
            </div>
        </div>

        <!-- Layer 5 -->
        <div class="border-2 border-purple-300 bg-purple-50/40 rounded-xl p-3 space-y-2">
            <span class="font-bold text-purple-900 font-mono text-[10.5px] block border-b border-purple-200 pb-1">5. PERSISTENCE</span>
            <div class="space-y-1.5 text-[10px]">
                <div class="p-2 bg-white rounded border border-purple-200">
                    <strong class="text-purple-950 block">KTX Database</strong>
                    <span class="text-slate-500">Sinh viên, phòng ốc, hợp đồng, giao dịch</span>
                </div>
                <div class="p-2 bg-white rounded border border-purple-200">
                    <strong class="text-purple-950 block">Audit & Log</strong>
                    <span class="text-slate-500">Lưu vết bảo mật & chứng chỉ cặp chặn</span>
                </div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_9 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                USE CASE 1 (1 DỄ) • ĐẶC TẢ CHI TIẾT • SLIDE 09/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-01: Đăng Nhập & Xác Thực Sinh Viên KTX (1 Dễ)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-indigo-100 text-indigo-800 px-3 py-1 rounded-full">
            Summary Table & Bảng 3 Luồng Flow (100% Điểm)
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-indigo-700 border">UC-01</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Đăng nhập và Xác thực Sinh viên KTX (Sign in and Authenticate Student)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên truy cập Cổng KTX bằng MSSV và Mật khẩu; hệ thống xác thực tính hợp lệ với Trường Đại học A (BR-01) để khởi tạo phiên đăng nhập.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Hệ thống SV Trường A (Supporting)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên nhấn nút "Đăng nhập" trên Cổng KTX.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã có tài khoản và thuộc danh sách Trường A.</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Cấp token phiên làm việc bảo mật HttpOnly và chuyển vào Dashboard.</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Three Types of Flows Table (BF, AF, EF đủ 4 cột Id, Action, Actor, Ref theo bảng của Thầy):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                    <tr><th class="p-1 border w-12 text-center">Step ID</th><th class="p-1 border w-24">Actor</th><th class="p-1 border">Action</th><th class="p-1 border w-44">Notes/references (Ref)</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Truy cập Cổng thông tin KTX và chọn chức năng Đăng nhập.</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-01, NFR-06</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Hiển thị biểu mẫu đăng nhập gồm ô nhập MSSV và Mật khẩu.</td><td class="p-1 border font-mono text-slate-500">Form WF-01-C02</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Nhập MSSV trường A và mật khẩu, nhấn "Đăng nhập".</td><td class="p-1 border font-mono text-slate-500">Validation WF-01-C03, C04</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Gửi credentials sang Dịch vụ xác thực sinh viên Trường A.</td><td class="p-1 border font-mono font-bold text-indigo-700">Include Xác thực SV, BR-01</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Trường A</td><td class="p-1 border">Xác nhận đúng tài khoản trường A, mật khẩu hợp lệ và gửi tín hiệu chấp thuận.</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-01 (Đúng diện trường A)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Khởi tạo phiên bảo mật (Session Cookie HttpOnly), chuyển hướng vào Dashboard.</td><td class="p-1 border font-mono text-slate-500">Hoàn tất mục tiêu UC-01</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Tích chọn "Ghi nhớ đăng nhập 30 ngày" trên thiết bị cá nhân.</td><td class="p-1 border font-mono text-purple-700 font-bold">WF-01-C05, Cookie an toàn</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-B</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm "Quên mật khẩu", nhập email trường cấp nhận mã OTP khôi phục.</td><td class="p-1 border font-mono text-purple-700">Nhánh phụ hoàn tất mục tiêu</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Nhập sai mật khẩu quá 5 lần: Khóa tạm tài khoản 15 phút chống dò mật khẩu.</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_AUTH_MAX, NFR-03</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-B</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">MSSV không thuộc diện Trường A: Từ chối đăng nhập và hiển thị cảnh báo đỏ.</td><td class="p-1 border font-mono text-rose-700 font-bold">WF-01-C07, BR-01</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_10 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                USE CASE 1 (1 DỄ) • WIREFRAME & SEQUENCE • SLIDE 10/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-01: Giao Diện Wireframe WF-01 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-01 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-01:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/auth/login</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-01] LOGIN</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 grid grid-cols-2 gap-2.5">
                    <div class="p-2 bg-indigo-50/50 border border-indigo-200 rounded relative">
                        <span class="callout-badge bg-indigo-600 text-white absolute -top-2 left-2">[WF-01-C01] AF-A: Persona</span>
                        <div class="pt-1 space-y-1 text-[8px]">
                            <strong class="text-indigo-950 uppercase block">1-Click Đăng nhập:</strong>
                            <div class="bg-white p-1 rounded border flex justify-between"><span>Thái Bảo (VNUK)</span><span class="text-indigo-600 font-bold">Chọn</span></div>
                            <div class="bg-white p-1 rounded border flex justify-between"><span>Văn Việt (SPKT)</span><span class="text-amber-600 font-bold">Chọn</span></div>
                            <div class="bg-white p-1 rounded border flex justify-between"><span>Minh Quân (DUE)</span><span class="text-emerald-600 font-bold">Chọn</span></div>
                        </div>
                    </div>
                    <div class="p-2 bg-slate-50 border border-slate-200 rounded space-y-1 text-[8.5px]">
                        <div><label class="font-bold text-slate-700">[WF-01-C03] MSSV Trường A:</label><input type="text" value="22VNUK0101" class="w-full bg-white border p-0.5 rounded font-mono"></div>
                        <div><label class="font-bold text-slate-700">[WF-01-C04] Mật khẩu:</label><input type="password" value="••••••••" class="w-full bg-white border p-0.5 rounded font-mono"></div>
                        <div class="flex justify-between text-[7.5px]"><span><input type="checkbox" checked> Ghi nhớ 30 ngày (AF-A)</span><span class="text-indigo-600">Quên MK? (AF-B)</span></div>
                        <button class="w-full py-1 bg-slate-900 text-white font-bold rounded text-[8.5px]">[WF-01-C06] ĐĂNG NHẬP (BF-3)</button>
                        <div class="text-[7.5px] text-rose-700">⚠️ [WF-01-C07] Alert vi phạm BR-01 (không thuộc trường A).</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-01 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9.5px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> SV -&gt;&gt; UI: Mở trang đăng nhập KTX</div>
                <div><strong>2. (BF-2)</strong> UI --&gt;&gt; SV: Hiển thị form đăng nhập</div>
                <div><strong>3. (BF-3)</strong> SV -&gt;&gt; UI: Nhập MSSV trường A và Mật khẩu, nhấn Đăng nhập</div>
                <div><strong>4. (BF-4)</strong> UI -&gt;&gt; Auth: Gửi yêu cầu xác thực credentials</div>
                <div><strong>5. (BF-4)</strong> Auth -&gt;&gt; Trường A: Đối soát MSSV và mật khẩu (Ref: BR-01)</div>
                <div class="text-emerald-700 font-bold">alt Đúng tài khoản sinh viên Trường A (Ref: BR-01)</div>
                <div class="text-emerald-700 pl-3"><strong>6. (BF-5)</strong> Trường A --&gt;&gt; Auth: Xác thực thành công</div>
                <div class="text-emerald-700 pl-3"><strong>7. (BF-6)</strong> Auth --&gt;&gt; UI: Cấp token phiên làm việc HttpOnly</div>
                <div class="text-emerald-700 pl-3"><strong>8. (BF-6)</strong> UI --&gt;&gt; SV: Chuyển hướng vào Dashboard KTX</div>
                <div class="text-rose-700 font-bold">else Sai mật khẩu quá 5 lần (Ref: EF-A, NFR-03)</div>
                <div class="text-rose-700 pl-3"><strong>9. (EF-A)</strong> Auth --&gt;&gt; UI: Báo mã ERR_AUTH_MAX, tạm khóa 15 phút</div>
                <div class="text-rose-700 font-bold">else Không thuộc diện Trường A (Ref: EF-B, BR-01)</div>
                <div class="text-rose-700 pl-3"><strong>10. (EF-B)</strong> Auth --&gt;&gt; UI: Báo mã ERR_NOT_AFFILIATED theo BR-01</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_11 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 2 (QUAN TRỌNG) • ĐẶC TẢ CHI TIẾT • SLIDE 11/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-04: Chọn Phòng, Tiện Ích & Nộp Đơn KTX (Cam Kết &ge; 1 Kỳ)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Ràng buộc: BR-02 • BR-05 • BR-06
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-04</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Chọn Loại phòng, Tiện ích và Nộp đơn KTX có Cam kết (Select Room and Submit Application)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên chọn loại phòng (2, 4, 6 người), khai báo 8 tiêu chí thói quen, chọn tiêu chí ưu tiên top (1.5x) và bắt buộc tích cam kết lưu trú &ge; 1 học kỳ (BR-02) để nộp hồ sơ xét duyệt.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Hệ thống KTX (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên bấm "Đăng ký Phòng & Khảo sát Thói quen" trên Dashboard.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã đăng nhập thành công vào hệ thống (UC-01).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Hồ sơ ghi nhận trạng thái Pending_Approval, chuyển sang bước thẩm định (UC-18).</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Three Types of Flows Table (BF, AF, EF đủ 4 cột Id, Action, Actor, Ref theo bảng của Thầy):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                    <tr><th class="p-1 border w-12 text-center">Step ID</th><th class="p-1 border w-24">Actor</th><th class="p-1 border">Action</th><th class="p-1 border w-44">Notes/references (Ref)</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Mở form Đăng ký phòng và khảo sát nếp sống KTX.</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-02</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Hiển thị 3 gói phòng (2, 4, 6 người) kèm quy định cam kết kỳ.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-02-C01, BR-05 (Loại phòng)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Chọn loại phòng mong muốn (ví dụ: Phòng 2 người VIP).</td><td class="p-1 border font-mono text-slate-500">Nguyện vọng loại phòng</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Khai báo 8 tiêu chí thói quen: Ngủ, dậy, gọn gàng, học, ồn, thuốc, bạn, sở thích.</td><td class="p-1 border font-mono text-slate-500">Chuẩn hóa vector 8 chiều</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Chọn 01 tiêu chí quan trọng nhất (nhân hệ số trọng số 1.5x).</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-02-C02, BR-06 (Top 1.5x)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Tích chọn cam kết bắt buộc: "Tôi cam kết ở KTX tối thiểu 1 kỳ (5 tháng)".</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-02-C04, BR-02 (Tối thiểu 1 kỳ)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-7</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm nút "Nộp Đơn Đăng Ký Phòng".</td><td class="p-1 border font-mono text-slate-500">WF-02-C05, Gửi dữ liệu</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-8</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Lưu hồ sơ trạng thái Pending_Approval, cấp mã đơn và chuyển sang thẩm định.</td><td class="p-1 border font-mono text-slate-500">Hoàn tất UC-04, chuyển UC-18</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm "Nạp hồ sơ Persona mẫu" để điền tự động 8 tiêu chí thói quen tức thì.</td><td class="p-1 border font-mono text-purple-700">Extend Nạp Persona, NFR-06</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Không tích cam kết lưu trú &ge; 1 kỳ: Khóa nút nộp và báo lỗi vi phạm BR-02.</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_TERM_MIN, BR-02</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-B</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Chưa chọn tiêu chí ưu tiên: Báo "Vui lòng chọn 1 tiêu chí quan trọng nhất (BR-06)".</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_TOP_EMPTY, BR-06</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_12 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 2 (QUAN TRỌNG) • WIREFRAME & SEQUENCE • SLIDE 12/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-04: Giao Diện Wireframe WF-02 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-02 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-02:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/student/apply</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-02] ĐĂNG KÝ PHÒNG</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 space-y-2">
                    <div class="p-1.5 border rounded bg-slate-50">
                        <span class="font-bold text-slate-700 block text-[8px]">[WF-02-C01] 3 Gói phòng (BR-05):</span>
                        <div class="grid grid-cols-3 gap-1.5 pt-0.5 text-center text-[7.5px]">
                            <div class="border-2 border-indigo-500 bg-indigo-50 p-1 rounded font-bold">VIP 2 Người (1.4tr)</div>
                            <div class="border p-1 rounded">Chuẩn 4 Người (850k)</div>
                            <div class="border p-1 rounded">Tiết kiệm 6 Người (550k)</div>
                        </div>
                    </div>
                    <div class="p-1.5 border rounded bg-slate-50 text-[8px] space-y-0.5">
                        <span class="font-bold text-slate-700 block">[WF-02-C02] 8 Slider thói quen & Top 1.5x (BR-06):</span>
                        <div class="flex justify-between"><span>Ngủ: 23:30 • Dậy: 06:30</span><span class="text-indigo-600 font-bold">Top ưu tiên: Giờ ngủ (1.5x)</span></div>
                    </div>
                    <div class="p-1.5 border border-amber-300 bg-amber-50 rounded text-[8px] space-y-1">
                        <label class="flex items-center gap-1 font-bold text-amber-900">
                            <input type="checkbox" checked> [WF-02-C04] Tôi cam kết ở KTX tối thiểu 1 kỳ (5 tháng) (BR-02)
                        </label>
                        <button class="w-full py-1 bg-indigo-600 text-white font-bold rounded text-[8.5px]">[WF-02-C05] NỘP ĐƠN ĐĂNG KÝ (BF-7)</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-04 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> SV -&gt;&gt; UI: Mở form đăng ký phòng và khảo sát</div>
                <div><strong>2. (BF-2)</strong> UI --&gt;&gt; SV: Hiển thị 3 gói phòng kèm cam kết kỳ (Ref: BR-02, BR-05)</div>
                <div><strong>3. (BF-3)</strong> SV -&gt;&gt; UI: Chọn loại phòng 2 người / 4 người</div>
                <div><strong>4. (BF-4)</strong> SV -&gt;&gt; UI: Khai báo 8 thanh trượt thói quen</div>
                <div><strong>5. (BF-5)</strong> SV -&gt;&gt; UI: Chọn tiêu chí top nhân trọng số 1.5x (Ref: BR-06)</div>
                <div><strong>6. (BF-6)</strong> SV -&gt;&gt; UI: Tích cam kết ở tối thiểu 1 kỳ (Ref: BR-02)</div>
                <div><strong>7. (BF-7)</strong> SV -&gt;&gt; UI: Nhấn nút Nộp đơn đăng ký phòng</div>
                <div><strong>8. (BF-8)</strong> UI -&gt;&gt; DB: Lưu hồ sơ trạng thái Pending_Approval</div>
                <div class="text-purple-700 font-bold">opt Nạp Persona mẫu (Ref: AF-A, NFR-06)</div>
                <div class="text-purple-700 pl-3"><strong>9. (AF-A)</strong> SV -&gt;&gt; UI: 1-Click chọn Thái Bảo / Văn Việt / Minh Quân</div>
                <div class="text-rose-700 font-bold">alt Không tích cam kết ở &ge; 1 kỳ (Ref: EF-A, BR-02)</div>
                <div class="text-rose-700 pl-3"><strong>10. (EF-A)</strong> UI --&gt;&gt; SV: Khóa nút nộp, báo lỗi bắt buộc cam kết &ge;1 kỳ</div>
                <div class="text-rose-700 font-bold">else Chưa chọn tiêu chí ưu tiên (Ref: EF-B, BR-06)</div>
                <div class="text-rose-700 pl-3"><strong>11. (EF-B)</strong> UI --&gt;&gt; SV: Cảnh báo chọn tiêu chí top 1.5x theo BR-06</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_13 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 3 (QUAN TRỌNG) • ĐẶC TẢ CHI TIẾT • SLIDE 13/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-05: Xem Bảng Xếp Hạng Gợi Ý Bạn Cùng Phòng (BR-06)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Ràng buộc: BR-06 • NFR-06
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-05</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Xem Bảng Xếp Hạng Gợi Ý Bạn Cùng Phòng (View Roommate Compatibility Rankings)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên xem bảng xếp hạng ứng viên cùng phòng được sắp xếp giảm dần theo điểm tương thích 2 chiều (BR-06); có thể mở modal xem chi tiết điểm cộng/trừ các tiêu chí.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Động cơ Scoring (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên nhấn tab "Khảo sát & Bảng Xếp Hạng Bạn Cùng Phòng".</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã khai báo vector 8 tiêu chí thói quen (UC-04).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Hiển thị Top ứng viên phù hợp nhất kèm minh giải chi tiết.</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Three Types of Flows Table (BF, AF, EF đủ 4 cột Id, Action, Actor, Ref theo bảng của Thầy):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                    <tr><th class="p-1 border w-12 text-center">Step ID</th><th class="p-1 border w-24">Actor</th><th class="p-1 border">Action</th><th class="p-1 border w-44">Notes/references (Ref)</th></tr>
                </thead>
                <tbody class="divide-y divide-slate-200">
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Truy cập màn hình Khảo sát & Bảng Xếp Hạng Bạn Cùng Phòng.</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-03, NFR-06</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Tải vector thói quen của sinh viên từ cơ sở dữ liệu.</td><td class="p-1 border font-mono text-slate-500">Load profile data</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Tính toán ma trận tương thích 2 chiều có nhân hệ số ưu tiên 1.5x (BR-06).</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-06 (Ma trận 2 chiều)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Sắp xếp các ứng viên cùng phòng tiềm năng theo thứ tự điểm giảm dần.</td><td class="p-1 border font-mono text-slate-500">Preference ranking</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Render bảng xếp hạng Top 1, Top 2, Top 3 kèm huy hiệu và điểm % hòa hợp.</td><td class="p-1 border font-mono text-slate-500">WF-03-C01, C02</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Tham khảo các bạn cùng phòng tiềm năng để chuẩn bị tâm lý nội trú.</td><td class="p-1 border font-mono text-slate-500">Hoàn tất UC-05</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm "Chi tiết tiêu chí ▼" trên card của ứng viên để mở modal giải thích điểm.</td><td class="p-1 border font-mono text-purple-700 font-bold">WF-03-C03, NFR-06</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Chưa có ứng viên cùng phòng nào nộp đơn: Hiển thị trạng thái chờ gom nhóm.</td><td class="p-1 border font-mono text-rose-700">Fallback giao diện trống</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

SLIDE_14 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 3 (QUAN TRỌNG) • WIREFRAME & SEQUENCE • SLIDE 14/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-05: Giao Diện Wireframe WF-03 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-03 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-03:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/student/roommate-ranking</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-03] BXH BẠN CÙNG PHÒNG</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 space-y-2">
                    <div class="p-2 border-2 border-amber-400 bg-amber-50/40 rounded space-y-1">
                        <div class="flex justify-between items-start">
                            <div><span class="px-1.5 py-0.5 bg-amber-400 text-slate-900 font-extrabold rounded text-[8px]">[WF-03-C02] 🥇 HẠNG 1</span><strong class="block text-[10px] mt-0.5">Nguyễn Duy Thái Bảo (VNUK)</strong><span class="text-[8px] text-slate-500">Kỹ thuật Dữ liệu • Nhóm A</span></div>
                            <div class="text-right"><span class="text-lg font-black text-emerald-600">92%</span><span class="block text-[7px] text-slate-500">Cực kỳ hòa hợp</span></div>
                        </div>
                        <div class="text-[8px] text-slate-600 border-t border-slate-200 pt-1 flex justify-between"><span>🌙 Ngủ: 23:00 • 🧹 Gọn: 5/5</span><span class="text-indigo-600 font-bold cursor-pointer">[WF-03-C03] Chi tiết tiêu chí ▼ (AF-A)</span></div>
                    </div>
                    <div class="p-2 border border-slate-200 bg-slate-50 rounded flex justify-between items-center">
                        <div><span class="px-1.5 py-0.5 bg-slate-200 text-slate-700 font-extrabold rounded text-[8px]">🥈 HẠNG 2</span><strong class="text-[9px] ml-1">Lê Minh Quân (DUE)</strong></div>
                        <span class="text-sm font-black text-sky-600">86%</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-05 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> SV -&gt;&gt; UI: Mở màn hình Bảng Xếp Hạng Bạn Cùng Phòng</div>
                <div><strong>2. (BF-2)</strong> UI -&gt;&gt; DB: Tải vector thói quen của sinh viên</div>
                <div><strong>3. (BF-3)</strong> UI -&gt;&gt; Scoring: Tính toán ma trận tương thích 2 chiều (Ref: BR-06)</div>
                <div><strong>4. (BF-4)</strong> Scoring -&gt;&gt; Scoring: Sắp xếp bảng ứng viên giảm dần</div>
                <div><strong>5. (BF-5)</strong> Scoring --&gt;&gt; UI: Trả về danh sách Top 8 ứng viên hòa hợp nhất</div>
                <div><strong>6. (BF-5)</strong> UI --&gt;&gt; SV: Hiển thị card Top 1, Top 2, Top 3 kèm huy hiệu</div>
                <div class="text-purple-700 font-bold">opt Mở xem giải thích điểm cộng/trừ (Ref: AF-A, NFR-06)</div>
                <div class="text-purple-700 pl-3"><strong>7. (AF-A)</strong> SV -&gt;&gt; UI: Nhấn nút "Chi tiết tiêu chí ▼" trên card</div>
                <div class="text-purple-700 pl-3"><strong>8. (AF-A)</strong> UI --&gt;&gt; SV: Mở modal hiển thị điểm cộng/trừ từng thói quen</div>
                <div class="text-rose-700 font-bold">alt Chưa có sinh viên đối diện nộp đơn (Ref: EF-A)</div>
                <div class="text-rose-700 pl-3"><strong>9. (EF-A)</strong> UI --&gt;&gt; SV: Hiển thị thông báo chờ gom đủ ứng viên</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triệu</span>
    </div>
</div>
"""

print("slides_data_2.py created")
