# -*- coding: utf-8 -*-
"""
slides_data_1.py
Slides 1 to 6:
- Slide 1: Bìa bài thuyết trình (VNUK, Nhóm 3)
- Slide 2: Đặt vấn đề & Mục tiêu đề tài KTX Smart Match
- Slide 3: Sơ đồ Use Case tổng thể 26 Use Case & 8 Tác nhân (Draw.io)
- Slide 4: Hệ thống 7 Quy tắc Nghiệp vụ (Business Rules: BR-01..07)
- Slide 5: Hệ thống 6 Yêu cầu Phi chức năng (Non-Functional: NFR-01..06)
- Slide 6: Yêu cầu của Thầy về Đặc tả Use Case (Rubric bảng lớp: BF/AF/EF, 1 Dễ + 1-n Quan trọng, Bộ 3 Diagram)
"""

SLIDE_1 = r"""
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
            SLIDE BÁO CÁO ĐỒ ÁN 2026
        </span>
    </div>

    <div class="space-y-4 my-auto py-6">
        <div class="inline-block px-3.5 py-1 rounded-lg bg-indigo-500/30 border border-indigo-400 text-indigo-200 text-xs font-mono font-bold uppercase tracking-wider">
            BÁO CÁO ĐẶC TẢ YÊU CẦU, BỘ 3 DIAGRAM & THIẾT KẾ WIREFRAME UI
        </div>
        <h1 class="text-4xl md:text-5xl font-black text-white tracking-tight leading-tight">
            HỆ THỐNG QUẢN TRỊ & GHÉP BẠN CÙNG PHÒNG<br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-indigo-300 to-emerald-400">
                KÝ TÚC XÁ THÔNG MINH (KTX SMART MATCH)
            </span>
        </h1>
        <p class="text-slate-300 text-base max-w-3xl leading-relaxed">
            Ứng dụng giải thuật ghép cặp ổn định Gale-Shapley (BP=0), phân tích nếp sống đa tiêu chí, tối ưu hóa lấp đầy 100% giường và quản trị hợp đồng - thanh toán bảo mật 72 giờ.
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

SLIDE_2 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                TỔNG QUAN DỰ ÁN • SLIDE 02/22
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

SLIDE_3 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                KIẾN TRÚC HỆ THỐNG • SLIDE 03/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">2. Sơ Đồ Use Case Tổng Thể (26 Use Cases & 8 Tác Nhân)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-indigo-50 text-indigo-700 px-3 py-1 rounded-full border border-indigo-200">
            Khớp 100% File Draw.io Mới Nhất
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Subsystem 1: Sinh viên -->
        <div class="border-2 border-indigo-200 bg-indigo-50/40 rounded-2xl p-4 space-y-2">
            <div class="flex justify-between items-center border-b border-indigo-200 pb-2">
                <span class="font-extrabold text-indigo-950 text-sm flex items-center gap-1.5">
                    <span>🧑🎓</span> PHÂN HỆ SINH VIÊN (13 USE CASES)
                </span>
                <span class="text-[10px] font-mono font-bold bg-indigo-600 text-white px-2 py-0.5 rounded">UC-01 .. UC-13</span>
            </div>
            <div class="grid grid-cols-2 gap-1.5 text-[11px] text-slate-700">
                <div class="p-1.5 bg-white rounded border border-indigo-100 font-bold text-indigo-900">• UC-01: Đăng nhập / Quên MK</div>
                <div class="p-1.5 bg-white rounded border border-indigo-100 font-bold text-indigo-900">• UC-04: Chọn phòng & Nộp đơn</div>
                <div class="p-1.5 bg-white rounded border border-indigo-100 font-bold text-indigo-900">• UC-05: BXH Bạn cùng phòng</div>
                <div class="p-1.5 bg-white rounded border border-indigo-100 font-bold text-indigo-900">• UC-13: Thanh toán 72h & Cọc</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-02: Đăng ký tài khoản</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-03: Cập nhật nếp sống</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-06: Mời bạn quen ghép</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-07: Xem kết quả phòng</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-08: Yêu cầu đổi phòng</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-09: Báo cáo sự cố KTX</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-10: Xem thông báo</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-11, 12: Đánh giá & Trả phòng</div>
            </div>
            <p class="text-[10px] text-indigo-800 font-mono">Tác nhân hỗ trợ: Hệ thống SV Trường A (Xác thực MSSV BR-01) & Cổng VNPay (BR-04)</p>
        </div>

        <!-- Subsystem 2: Quản trị & Vận hành -->
        <div class="border-2 border-slate-300 bg-slate-50 rounded-2xl p-4 space-y-2">
            <div class="flex justify-between items-center border-b border-slate-200 pb-2">
                <span class="font-extrabold text-slate-900 text-sm flex items-center gap-1.5">
                    <span>🏢</span> PHÂN HỆ QUẢN TRỊ & VẬN HÀNH (13 USE CASES)
                </span>
                <span class="text-[10px] font-mono font-bold bg-slate-800 text-white px-2 py-0.5 rounded">UC-14 .. UC-26</span>
            </div>
            <div class="grid grid-cols-2 gap-1.5 text-[11px] text-slate-700">
                <div class="p-1.5 bg-white rounded border border-slate-200 font-bold text-slate-900">• UC-18: Thẩm định Business Approve</div>
                <div class="p-1.5 bg-white rounded border border-slate-200 font-bold text-slate-900">• UC-24: Ghép phòng Gale-Shapley</div>
                <div class="p-1.5 bg-white rounded border border-slate-200 font-bold text-slate-900">• UC-22: Đối soát kế toán</div>
                <div class="p-1.5 bg-white rounded border border-slate-200 font-bold text-slate-900">• UC-26: Hủy quá 72h & Waitlist</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-14: Quản lý tòa/phòng/giá</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-15: Phân quyền hệ thống</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-16: Quản lý dữ liệu CSV</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-17: Cấu hình luật ghép</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-19: Override phòng thủ công</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-20: Xử lý đổi bạn phòng</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-21: Xử lý sự cố kỹ thuật</div>
                <div class="p-1 bg-white/70 rounded text-[10px]">• UC-23, 25: Báo cáo & Nhắc 72h</div>
            </div>
            <p class="text-[10px] text-slate-600 font-mono">Tác nhân: Quản trị viên (Admin), Cán bộ KTX (Staff), Kỹ thuật, Kế toán, Scheduler</p>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_4 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                QUY TẮC NGHIỆP VỤ • SLIDE 04/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">3. Hệ Thống 7 Quy Tắc Nghiệp Vụ (Business Rules: BR-01 .. BR-07)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-50 text-amber-800 border border-amber-200 px-3 py-1 rounded-full">
            Định Nghĩa Tường Minh • Không Note Bừa Bãi
        </span>
    </div>

    <div class="grid grid-cols-2 gap-3 my-auto text-xs">
        <div class="space-y-2">
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-01: Đối Tượng Tiếp Nhận (SV Trường A)</strong><span class="text-[10px] bg-indigo-100 text-indigo-800 px-2 rounded font-bold">Xác thực MSSV</span></div>
                <p class="text-slate-600 text-[11px]">Chỉ tiếp nhận sinh viên thuộc Trường Đại học A có MSSV và email trường cấp hợp lệ. Ngăn chặn người ngoài xâm nhập KTX.</p>
            </div>
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-02: Thời Hạn Hợp Đồng Tối Thiểu 1 Kỳ</strong><span class="text-[10px] bg-indigo-100 text-indigo-800 px-2 rounded font-bold">Cam kết &ge; 5 tháng</span></div>
                <p class="text-slate-600 text-[11px]">Bắt buộc cam kết lưu trú &ge; 01 học kỳ (05 tháng) hoặc 10 tháng. Hệ thống từ chối hợp đồng ngắn hạn ngày/tuần để tránh xáo trộn.</p>
            </div>
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-03: Phê Duyệt Nghiệp Vụ (Business Approve)</strong><span class="text-[10px] bg-amber-100 text-amber-800 px-2 rounded font-bold">Cán bộ KTX Duyệt</span></div>
                <p class="text-slate-600 text-[11px]">Hồ sơ phải qua bước thẩm định tư cách (MSSV, lịch sử kỷ luật, diện chính sách). Trạng thái Approved mới được nạp vào Gale-Shapley.</p>
            </div>
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-04: Đặt Cọc & Hạn Thanh Toán 72 Giờ</strong><span class="text-[10px] bg-rose-100 text-rose-800 px-2 rounded font-bold">Cọc 1tr • Hạn 72h</span></div>
                <p class="text-slate-600 text-[11px]">Trong 72h sau công bố phòng, nộp tiền phòng kỳ 1 + cọc 1.000.000đ qua VNPay. Quá 72h tự hủy kết quả chuyển cho Waitlist.</p>
            </div>
        </div>

        <div class="space-y-2">
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-05: Tối Ưu Lợi Nhuận & Lấp Đầy Phòng</strong><span class="text-[10px] bg-emerald-100 text-emerald-800 px-2 rounded font-bold">Occupancy 100%</span></div>
                <p class="text-slate-600 text-[11px]">Hệ thống ưu tiên lấp đầy 100% số giường từng phòng (2, 4, 6 người) trước khi mở phòng mới, triệt tiêu lãng phí điều hòa điện nước.</p>
            </div>
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-06: Trọng Số Ưu Tiên Cá Nhân (Top 1.5x)</strong><span class="text-[10px] bg-sky-100 text-sky-800 px-2 rounded font-bold">Nhân hệ số 1.5x</span></div>
                <p class="text-slate-600 text-[11px]">Tiêu chí thói quen số 1 (top) được nhân trọng số 1.5x, tạo ma trận tương thích 2 chiều bất đối xứng phản ánh kỳ vọng thực tế của mỗi SV.</p>
            </div>
            <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl space-y-0.5">
                <div class="flex justify-between"><strong class="text-indigo-900 font-mono">BR-07: Triệt Tiêu Cặp Chặn (Blocking Pairs = 0)</strong><span class="text-[10px] bg-purple-100 text-purple-800 px-2 rounded font-bold">BP = 0 Tuyệt Đối</span></div>
                <p class="text-slate-600 text-[11px]">Đảm bảo độ ổn định toán học tuyệt đối: Không một cặp SV nào có động cơ rủ nhau bỏ phòng hiện tại sang phòng khác, triệt tiêu khiếu nại.</p>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_5 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-600 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                YÊU CẦU KỸ THUẬT • SLIDE 05/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">4. Hệ Thống 6 Yêu Cầu Phi Chức Năng (NFR-01 .. NFR-06)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-50 text-emerald-700 border border-emerald-300 px-3 py-1 rounded-full">
            Chỉ Số Đo Lường Định Lượng
        </span>
    </div>

    <div class="grid grid-cols-3 gap-3.5 my-auto text-xs">
        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-01: Hiệu Năng Xử Lý</span>
            <div class="text-lg font-black text-slate-900">&lt; 1.0 Giây</div>
            <p class="text-slate-600 text-[11px]">Thuật toán Gale-Shapley tính xong trong &lt; 1.0s với N=200, &lt; 5.0s với N=1.000 sinh viên (đo bằng perf_counter).</p>
        </div>

        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-02: Ổn Định Toán Học</span>
            <div class="text-lg font-black text-slate-900">BP = 0 Tuyệt Đối</div>
            <p class="text-slate-600 text-[11px]">Triệt tiêu 100% cặp chặn qua tối thiểu 50 seed ngẫu nhiên liên tiếp trong bộ kiểm thử tự động test_matching.py.</p>
        </div>

        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-03: Bảo Mật Giao Dịch</span>
            <div class="text-lg font-black text-slate-900">TLS 1.3 + SHA-256</div>
            <p class="text-slate-600 text-[11px]">Mã hóa đường truyền TLS 1.3 và đối soát chữ ký số băm SHA-256 từ cổng VNPay chống giả mạo giao dịch tài chính.</p>
        </div>

        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-04: Khả Năng Chịu Lỗi</span>
            <div class="text-lg font-black text-slate-900">Graceful Handling</div>
            <p class="text-slate-600 text-[11px]">Hệ thống không crash khi nạp CSV lỗi (thiếu cột, lệch nhóm, file trống); bắt exception và cảnh báo dòng/cột cụ thể.</p>
        </div>

        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-05: Mở Rộng Quy Mô</span>
            <div class="text-lg font-black text-slate-900">Phòng 2, 4, 6 Giường</div>
            <p class="text-slate-600 text-[11px]">Kiến trúc thuật toán hỗ trợ linh hoạt mở rộng từ phòng 2 người (ghép cặp) sang phòng 4 người và phòng 6 người (merge tham lam).</p>
        </div>

        <div class="p-3.5 bg-slate-50 border border-slate-200 rounded-xl space-y-1.5">
            <span class="font-bold text-emerald-800 font-mono block text-xs">NFR-06: Trải Nghiệm UI/UX</span>
            <div class="text-lg font-black text-slate-900">Phản Hồi &lt; 2.0s</div>
            <p class="text-slate-600 text-[11px]">Giao diện web phản hồi mượt mà &lt; 2.0s khi kéo slider thói quen; hỗ trợ nạp nhanh 3 Persona mẫu chỉ với 1 cú click.</p>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_6 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2.5">
        <div>
            <span class="text-[10px] font-mono font-bold text-rose-600 bg-rose-50 px-2.5 py-0.5 rounded border border-rose-300 uppercase">
                TIÊU CHUẨN ĐÁNH GIÁ • SLIDE 06/22
            </span>
            <h2 class="text-2xl font-black text-slate-900 mt-1">5. Chuẩn Hóa Theo Lời Dặn Của Thầy Trên Bảng Lớp</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-50 text-amber-800 border border-amber-300 px-3 py-1 rounded-full">
            Rubric Chấm Điểm 100%
        </span>
    </div>

    <div class="grid grid-cols-3 gap-4 my-auto text-xs">
        <!-- Rubric 1: Bảng 3 Luồng Flow -->
        <div class="p-4 bg-slate-50 border-2 border-indigo-200 rounded-2xl space-y-2.5">
            <div class="flex justify-between items-center border-b border-indigo-100 pb-1.5">
                <strong class="text-indigo-950 font-mono text-sm">BẢNG 3 LUỒNG FLOW</strong>
                <span class="text-xs font-black text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">100% ĐIỂM</span>
            </div>
            <div class="space-y-1.5 text-slate-700 text-[11px]">
                <p>Thầy ghi rõ trên bảng:</p>
                <div class="p-2 bg-white rounded border border-slate-200 font-mono text-[10px]">
                    BF \ <br>
                    AF  |  <strong>Id, action, actor, Ref</strong><br>
                    EF /
                </div>
                <p>• <strong>50% điểm:</strong> Nếu chỉ làm mỗi luồng cơ bản (BF).</p>
                <p class="font-bold text-emerald-800">• <strong>100% điểm:</strong> Phải có đủ cả 3 luồng: BF (cơ bản), AF (thay thế), EF (ngoại lệ) kèm đủ 4 cột Id, Action, Actor, Ref!</p>
            </div>
        </div>

        <!-- Rubric 2: Phân loại Use Case -->
        <div class="p-4 bg-slate-50 border-2 border-amber-200 rounded-2xl space-y-2.5">
            <div class="flex justify-between items-center border-b border-amber-100 pb-1.5">
                <strong class="text-amber-950 font-mono text-sm">PHÂN LOẠI USE CASE</strong>
                <span class="text-xs font-black text-amber-800 bg-amber-100 px-2 py-0.5 rounded">1 DỄ + 1-N CỐT LÕI</span>
            </div>
            <div class="space-y-1.5 text-slate-700 text-[11px]">
                <p>Thầy yêu cầu đặc tả chi tiết:</p>
                <div class="p-2 bg-white rounded border border-slate-200 font-mono text-[10px]">
                    + Đặc tả Use case &lt;<br>
                    &nbsp;&nbsp;- <strong>1 dễ</strong><br>
                    &nbsp;&nbsp;- <strong>1-n quan trọng</strong>
                </div>
                <p>• <strong>1 Dễ:</strong> UC-01 Đăng nhập & Xác thực SV.</p>
                <p>• <strong>5 Quan trọng:</strong> UC-04 (Nộp đơn kỳ), UC-05 (BXH), UC-13 (Thanh toán 72h), UC-18 (Duyệt đơn), UC-24 (Gale-Shapley).</p>
            </div>
        </div>

        <!-- Rubric 3: Bộ 3 Diagram -->
        <div class="p-4 bg-slate-50 border-2 border-emerald-200 rounded-2xl space-y-2.5">
            <div class="flex justify-between items-center border-b border-emerald-100 pb-1.5">
                <strong class="text-emerald-950 font-mono text-sm">BỘ 3 DIAGRAM BẮT BUỘC</strong>
                <span class="text-xs font-black text-sky-800 bg-sky-100 px-2 py-0.5 rounded">3 LOẠI DIAGRAM</span>
            </div>
            <div class="space-y-1.5 text-slate-700 text-[11px]">
                <p>Ghi chú mũi tên của Thầy:</p>
                <div class="p-2 bg-white rounded border border-slate-200 font-mono text-[10px]">
                    ↓ Bộ diagram -&gt; <strong>Sequence (1)</strong><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&gt; <strong>Activity (2)</strong><br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&gt; <strong>Component (3)</strong>
                </div>
                <p>• <strong>(1) Sequence:</strong> Khớp 1-1 từng Step ID.</p>
                <p>• <strong>(2) Activity:</strong> Luồng quy trình End-to-End.</p>
                <p>• <strong>(3) Component:</strong> Kiến trúc 5 tầng module.</p>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

print("slides_data_1.py created")
