# -*- coding: utf-8 -*-
"""
pdf_pages_part2.py
Page 4 (UC-01 - 1 Dễ), Page 5 (UC-04 - Quan trọng), Page 6 (UC-05 - Bảng xếp hạng bạn cùng phòng).
Each page includes: Summary Table + Blueprint Wireframe Mockup + 3 Types of Flows Table (BF, AF, EF).
"""

PAGE_4_UC01 = r"""
    <!-- ============================================================== -->
    <!-- TRANG 4: USE CASE 1 (1 DỄ) - UC-01: ĐĂNG NHẬP / QUÊN MẬT KHẨU  -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-6 shadow-sm space-y-3.5 text-xs">
        <div class="border-b border-slate-200 pb-2 flex justify-between items-center">
            <div>
                <span class="callout-badge bg-indigo-100 text-indigo-800 border border-indigo-300">USE CASE ĐƠN GIẢN (1 DỄ) • WF-01</span>
                <h2 class="text-base font-extrabold text-slate-900 mt-0.5">UC-01: Đăng Nhập & Xác Thực Sinh Viên KTX Trường A</h2>
            </div>
            <span class="text-[10px] font-mono font-bold bg-slate-100 text-slate-600 px-2.5 py-0.5 rounded border border-slate-300">
                Ràng buộc: BR-01 • NFR-03
            </span>
        </div>

        <!-- 1. Summary Table According to Slide -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Bảng Tóm Tắt Đặc Tả (Summary Table - Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-indigo-700 border">UC-01</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Đăng nhập và Xác thực Sinh viên KTX (Sign in and Authenticate Student)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên truy cập Cổng KTX bằng MSSV và Mật khẩu; hệ thống đối soát dữ liệu với Trường Đại học A (BR-01) để khởi tạo phiên đăng nhập bảo mật.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Hệ thống SV Trường A (Supporting)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên nhấn nút "Đăng nhập" trên Cổng KTX.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã có tài khoản và thuộc danh sách Trường A.</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Cấp token phiên làm việc bảo mật HttpOnly và chuyển vào Dashboard.</td></tr>
                </tbody>
            </table>
        </div>

        <!-- 2. Blueprint Wireframe Mockup -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Thiết Kế Giao Diện Wireframe (WF-01):</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 relative overflow-hidden">
                <div class="bg-slate-200 border border-slate-300 rounded-t-lg px-2.5 py-1 flex items-center justify-between text-[10px]">
                    <div class="flex items-center gap-1">
                        <span class="w-2 h-2 rounded-full bg-rose-400 inline-block"></span>
                        <span class="w-2 h-2 rounded-full bg-amber-400 inline-block"></span>
                        <span class="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
                        <span class="ml-2 font-mono text-[9px] text-slate-600 bg-white px-2 py-0.5 rounded border border-slate-300">https://ktx.udn.vn/login</span>
                    </div>
                    <span class="text-[9px] font-bold text-slate-500 font-mono">PORTAL: STUDENT_AUTH</span>
                </div>
                <div class="bg-white border-x border-b border-slate-300 p-3 rounded-b-lg grid grid-cols-2 gap-3">
                    <div class="border border-indigo-200 bg-indigo-50/40 rounded-lg p-2.5 space-y-1.5 relative">
                        <span class="callout-badge bg-indigo-600 text-white absolute -top-2 left-2">[WF-01-C01] AF-A: 1-Click Persona</span>
                        <div class="text-[9px] pt-1">
                            <strong class="text-indigo-950 uppercase">Tài khoản Persona mẫu:</strong>
                            <div class="mt-1 space-y-1">
                                <div class="bg-white p-1 rounded border border-slate-200 flex justify-between items-center text-[8.5px]"><span>Thái Bảo (VNUK - Thư viện)</span><span class="bg-indigo-600 text-white px-1 rounded font-bold">Chọn</span></div>
                                <div class="bg-white p-1 rounded border border-slate-200 flex justify-between items-center text-[8.5px]"><span>Văn Việt (SPKT - Cú đêm)</span><span class="bg-amber-600 text-white px-1 rounded font-bold">Chọn</span></div>
                                <div class="bg-white p-1 rounded border border-slate-200 flex justify-between items-center text-[8.5px]"><span>Minh Quân (DUE - Healthy)</span><span class="bg-emerald-600 text-white px-1 rounded font-bold">Chọn</span></div>
                            </div>
                        </div>
                    </div>
                    <div class="border border-slate-300 bg-slate-50 rounded-lg p-2.5 space-y-1.5 relative text-[9px]">
                        <span class="callout-badge bg-slate-800 text-white absolute -top-2 left-2">[WF-01-C02] BF-2, 3: Form Credentials</span>
                        <div class="pt-1 space-y-1">
                            <div><label class="block font-bold text-slate-700 text-[8.5px]">[WF-01-C03] Mã sinh viên Trường A (MSSV):</label><input type="text" value="22VNUK0101" class="w-full bg-white border border-slate-300 rounded px-1.5 py-0.5 font-mono text-[9px]"></div>
                            <div><label class="block font-bold text-slate-700 text-[8.5px]">[WF-01-C04] Mật khẩu:</label><input type="password" value="••••••••" class="w-full bg-white border border-slate-300 rounded px-1.5 py-0.5 font-mono text-[9px]"></div>
                            <div class="flex items-center justify-between text-[8px] text-slate-600"><span><input type="checkbox" checked> [WF-01-C05] Ghi nhớ 30 ngày (AF-A)</span><span class="text-indigo-600">Quên mật khẩu? (AF-B)</span></div>
                            <button class="w-full py-1 bg-slate-900 text-white font-bold rounded text-[9px]">[WF-01-C06] ĐĂNG NHẬP HỆ THỐNG (BF-3)</button>
                            <div class="p-1 bg-rose-50 border border-rose-300 rounded text-[8px] text-rose-800">⚠️ [WF-01-C07] EF-B (BR-01): Sinh viên không thuộc Trường A sẽ bị từ chối đăng nhập.</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3. Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">3. Bảng 3 Loại Luồng (Three Types of Flows Table - Đủ 4 Cột Id, Actor, Action, Ref Đạt 100%):</span>
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
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Khởi tạo phiên bảo mật (Session Cookie HttpOnly), chuyển hướng vào Dashboard.</td><td class="p-1 border font-mono text-slate-500">Hoàn tất UC-01, NFR-03</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Tích chọn "Ghi nhớ đăng nhập 30 ngày" trên thiết bị cá nhân.</td><td class="p-1 border font-mono text-purple-700 font-bold">WF-01-C05, Gia hạn Cookie</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-B</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm "Quên mật khẩu", nhập email trường cấp nhận OTP khôi phục.</td><td class="p-1 border font-mono text-purple-700">Nhánh phụ hoàn tất mục tiêu</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Nhập sai mật khẩu quá 5 lần: Khóa tạm tài khoản 15 phút chống Brute-force.</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_AUTH_MAX, NFR-03</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-B</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">MSSV không thuộc diện Trường A: Từ chối đăng nhập và hiển thị cảnh báo đỏ.</td><td class="p-1 border font-mono text-rose-700 font-bold">WF-01-C07, BR-01</td></tr>
                </tbody>
            </table>
        </div>
    </div>
"""

PAGE_5_UC04 = r"""
    <!-- ============================================================== -->
    <!-- TRANG 5: USE CASE 2 (QUAN TRỌNG) - UC-04: ĐĂNG KÝ PHÒNG & THÓI QUEN -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-6 shadow-sm space-y-3.5 text-xs">
        <div class="border-b border-slate-200 pb-2 flex justify-between items-center">
            <div>
                <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">USE CASE QUAN TRỌNG • WF-02</span>
                <h2 class="text-base font-extrabold text-slate-900 mt-0.5">UC-04: Chọn Loại Phòng, Tiện Ích & Nộp Đơn KTX (Cam Kết &ge; 1 Kỳ)</h2>
            </div>
            <span class="text-[10px] font-mono font-bold bg-slate-100 text-slate-600 px-2.5 py-0.5 rounded border border-slate-300">
                Ràng buộc: BR-02 • BR-05 • BR-06
            </span>
        </div>

        <!-- 1. Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Bảng Tóm Tắt Đặc Tả (Summary Table - Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-04</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Chọn Loại phòng, Tiện ích và Nộp đơn KTX có Cam kết (Select Room and Submit Application)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên chọn loại phòng (2, 4, 6 người), khai báo 8 tiêu chí thói quen, chọn tiêu chí ưu tiên top (1.5x) và bắt buộc tích cam kết lưu trú &ge; 1 học kỳ (BR-02) để nộp hồ sơ xét duyệt.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Hệ thống KTX (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên bấm "Đăng ký Phòng & Khảo sát Thói quen" trên Dashboard.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã đăng nhập thành công vào hệ thống (UC-01).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Hồ sơ ghi nhận trạng thái Pending_Approval, chuyển sang bước thẩm định (UC-18).</td></tr>
                </tbody>
            </table>
        </div>

        <!-- 2. Blueprint Wireframe Mockup -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Thiết Kế Giao Diện Wireframe (WF-02):</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 relative overflow-hidden">
                <div class="bg-slate-200 border border-slate-300 rounded-t-lg px-2.5 py-1 flex items-center justify-between text-[10px]">
                    <span class="font-mono text-[9px] text-slate-600">https://ktx.udn.vn/student/apply</span>
                    <span class="text-[9px] font-bold text-slate-500 font-mono">[WF-02] ĐƠN ĐĂNG KÝ NỘI TRÚ</span>
                </div>
                <div class="bg-white border-x border-b border-slate-300 p-3 rounded-b-lg space-y-2 text-[9px]">
                    <div class="p-2 border border-slate-200 rounded bg-slate-50 space-y-1 relative">
                        <span class="callout-badge bg-indigo-700 text-white absolute -top-2 left-2">[WF-02-C01] BF-2, 3: Chọn Nguyện Vọng Gói Phòng (BR-05)</span>
                        <div class="grid grid-cols-3 gap-2 pt-1">
                            <div class="p-1.5 border-2 border-indigo-500 bg-indigo-50 rounded text-center"><strong>VIP 2 Người</strong><br><span class="text-indigo-700 font-bold">1.400.000đ/th</span></div>
                            <div class="p-1.5 border border-slate-300 bg-white rounded text-center"><strong>Chuẩn 4 Người</strong><br><span class="text-slate-600">850.000đ/th</span></div>
                            <div class="p-1.5 border border-slate-300 bg-white rounded text-center"><strong>Tiết kiệm 6 Người</strong><br><span class="text-slate-600">550.000đ/th</span></div>
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div class="p-2 border border-slate-200 rounded bg-slate-50 space-y-1 relative">
                            <span class="callout-badge bg-slate-800 text-white absolute -top-2 left-2">[WF-02-C02] BF-4, 5: 8 Thói Quen & Top 1.5x</span>
                            <div class="pt-1 space-y-0.5 text-[8.5px]">
                                <div class="flex justify-between"><span>Giờ ngủ: 23:30</span><span>Độ ngăn nắp: 4/5</span></div>
                                <div class="flex justify-between"><span>Giờ dậy: 06:30</span><span>Mức độ ồn: 2/5</span></div>
                                <div class="mt-1 pt-1 border-t border-slate-200"><span class="font-bold text-indigo-700">Tiêu chí Top ưu tiên: [Giờ ngủ - Trọng số 1.5x (BR-06)]</span></div>
                            </div>
                        </div>
                        <div class="p-2 border border-slate-200 rounded bg-slate-50 space-y-1.5 relative">
                            <span class="callout-badge bg-rose-700 text-white absolute -top-2 left-2">[WF-02-C03] BF-6, 7: Cam Kết Kỳ & Nộp Đơn (BR-02)</span>
                            <div class="pt-1 space-y-1 text-[8.5px]">
                                <label class="flex items-start gap-1 p-1 bg-amber-50 rounded border border-amber-200 font-bold text-amber-900">
                                    <input type="checkbox" checked class="mt-0.5">
                                    <span>[WF-02-C04] Tôi cam kết ở KTX tối thiểu 1 kỳ (5 tháng) theo quy định BR-02</span>
                                </label>
                                <button class="w-full py-1.5 bg-indigo-600 text-white font-bold rounded shadow text-[9px]">[WF-02-C05] NỘP ĐƠN ĐĂNG KÝ PHÒNG (BF-7)</button>
                                <div class="text-[7.5px] text-rose-700">⚠️ EF-A: Khóa nút nộp nếu chưa tích cam kết &ge;1 kỳ theo BR-02.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3. Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">3. Bảng 3 Loại Luồng (Three Types of Flows Table - Đủ 4 Cột Id, Actor, Action, Ref Đạt 100%):</span>
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
"""

PAGE_6_UC05 = r"""
    <!-- ============================================================== -->
    <!-- TRANG 6: USE CASE 3 (QUAN TRỌNG) - UC-05: BẢNG XẾP HẠNG BẠN     -->
    <!-- ============================================================== -->
    <div class="page-break bg-white border border-slate-300 rounded-3xl p-6 shadow-sm space-y-3.5 text-xs">
        <div class="border-b border-slate-200 pb-2 flex justify-between items-center">
            <div>
                <span class="callout-badge bg-amber-100 text-amber-800 border border-amber-300">USE CASE QUAN TRỌNG • WF-03</span>
                <h2 class="text-base font-extrabold text-slate-900 mt-0.5">UC-05: Bảng Xếp Hạng Gợi Ý & Khảo Sát Tính Điểm Tương Thích</h2>
            </div>
            <span class="text-[10px] font-mono font-bold bg-slate-100 text-slate-600 px-2.5 py-0.5 rounded border border-slate-300">
                Ràng buộc: BR-06 • NFR-06
            </span>
        </div>

        <!-- 1. Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Bảng Tóm Tắt Đặc Tả (Summary Table - Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-05</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Xem Bảng Xếp Hạng Gợi Ý Bạn Cùng Phòng (View Roommate Compatibility Rankings)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên xem bảng xếp hạng ứng viên cùng phòng được sắp xếp giảm dần theo điểm tương thích 2 chiều (BR-06); có thể mở modal xem chi tiết điểm cộng/trừ các tiêu chí.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Động cơ Scoring (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên nhấn tab "Khảo sát & Bảng Xếp Hạng Bạn Cùng Phòng".</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã khai báo vector 8 tiêu chí thói quen (UC-04).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Hiển thị Top ứng viên phù hợp nhất kèm minh giải chi tiết.</td></tr>
                </tbody>
            </table>
        </div>

        <!-- 2. Blueprint Wireframe Mockup -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">2. Thiết Kế Giao Diện Wireframe (WF-03):</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 relative overflow-hidden">
                <div class="bg-slate-200 border border-slate-300 rounded-t-lg px-2.5 py-1 flex items-center justify-between text-[10px]">
                    <span class="font-mono text-[9px] text-slate-600">https://ktx.udn.vn/student/roommate-ranking</span>
                    <span class="text-[9px] font-bold text-slate-500 font-mono">[WF-03] BẢNG XẾP HẠNG BẠN CÙNG PHÒNG</span>
                </div>
                <div class="bg-white border-x border-b border-slate-300 p-3 rounded-b-lg space-y-2 text-[9px]">
                    <div class="flex justify-between items-center bg-slate-900 text-white p-2 rounded">
                        <div><strong class="text-[10px]">[WF-03-C01] Bảng Gợi Ý Bạn Cùng Phòng Tương Thích</strong><p class="text-[8px] text-slate-400">Đối chiếu vector thói quen có trọng số top 1.5x (BR-06)</p></div>
                        <span class="bg-indigo-600 text-white px-2 py-0.5 rounded text-[8.5px] font-bold">Top 8 Ứng Viên</span>
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        <div class="p-2 border-2 border-amber-400 bg-amber-50/30 rounded space-y-1">
                            <div class="flex justify-between items-start">
                                <div><span class="px-1.5 py-0.5 bg-amber-400 text-slate-900 font-extrabold rounded text-[8px]">[WF-03-C02] 🥇 HẠNG 1</span><strong class="block text-[10px] mt-0.5">Nguyễn Duy Thái Bảo</strong><span class="text-[8px] text-slate-500">VNUK • Kỹ thuật Dữ liệu</span></div>
                                <div class="text-right"><span class="text-lg font-black text-emerald-600">92%</span><span class="block text-[7.5px] text-slate-500">Cực kỳ hòa hợp</span></div>
                            </div>
                            <div class="text-[8px] text-slate-600 border-t border-slate-200 pt-1 flex justify-between"><span>🌙 Ngủ: 23:00 • 🧹 Gọn: 5/5</span><span class="text-indigo-600 font-bold cursor-pointer">[WF-03-C03] Chi tiết ▼ (AF-A)</span></div>
                        </div>
                        <div class="p-2 border border-slate-300 bg-white rounded space-y-1">
                            <div class="flex justify-between items-start">
                                <div><span class="px-1.5 py-0.5 bg-slate-200 text-slate-700 font-extrabold rounded text-[8px]">🥈 HẠNG 2</span><strong class="block text-[10px] mt-0.5">Lê Minh Quân</strong><span class="text-[8px] text-slate-500">DUE • Quản trị Kinh doanh</span></div>
                                <div class="text-right"><span class="text-lg font-black text-sky-600">86%</span><span class="block text-[7.5px] text-slate-500">Rất hòa hợp</span></div>
                            </div>
                            <div class="text-[8px] text-slate-600 border-t border-slate-200 pt-1 flex justify-between"><span>🌙 Ngủ: 23:30 • 🚭 Không thuốc</span><span class="text-indigo-600 font-bold cursor-pointer">Chi tiết ▼</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3. Three Types of Flows Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">3. Bảng 3 Loại Luồng (Three Types of Flows Table - Đủ 4 Cột Id, Actor, Action, Ref Đạt 100%):</span>
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
"""

print("Part 2 defined successfully")
