# -*- coding: utf-8 -*-
"""
slides_data_3.py
Slides 15 to 22:
- Slide 15: UC-18 (Quan trọng) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 16: UC-18 - Wireframe WF-04 & Sequence Diagram Khớp 1-1
- Slide 17: UC-24 (Quan trọng) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 18: UC-24 - Wireframe WF-05 & Sequence Diagram Khớp 1-1
- Slide 19: UC-13 (Quan trọng) - Bảng Đặc tả Luồng Sự kiện (Summary + BF/AF/EF)
- Slide 20: UC-13 - Wireframe WF-06 & Sequence Diagram Khớp 1-1
- Slide 21: Bảng Ma Trận Truy Vết 1-to-1 Toàn Diện (Traceability Matrix)
- Slide 22: Tổng Kết Nghiệm Thu Đồ Án & Q&A
"""

SLIDE_15 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 4 (QUAN TRỌNG) • ĐẶC TẢ CHI TIẾT • SLIDE 15/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-18: Thẩm Định & Phê Duyệt Hồ Sơ KTX (Business Approve)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Ràng buộc: BR-01 • BR-02 • BR-03
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-18</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Phê duyệt Đơn KTX (Business Approve Dormitory Application)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Cán bộ KTX thẩm định các điều kiện nghiệp vụ: tính hợp lệ MSSV trường A (BR-01), cam kết &ge; 1 kỳ (BR-02), lịch sử kỷ luật (BR-03); chỉ hồ sơ Approved mới được nạp vào Gale-Shapley.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Cán bộ KTX (Staff - Primary), Hệ thống KTX (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Cán bộ KTX mở danh sách hồ sơ trạng thái Pending trên Dashboard.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã nộp đơn đăng ký KTX (UC-04).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Hồ sơ chuyển trạng thái Approved_For_Matching hoặc Rejected kèm lý do.</td></tr>
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
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Đăng nhập Dashboard Quản trị và mở màn hình Thẩm định Đơn KTX.</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-04</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Hiển thị danh sách hồ sơ trạng thái Pending kèm huy hiệu đối soát tự động.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-04-C01, BR-01, BR-02</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Chọn hồ sơ để thẩm định tính kỷ luật và diện chính sách ưu tiên.</td><td class="p-1 border font-mono text-slate-500">Nghiệp vụ xét duyệt</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Kiểm tra quỹ phòng còn chỗ tương ứng với loại phòng sinh viên đăng ký.</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-05 (Quỹ phòng khả dụng)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Nhấn nút "Phê duyệt (Business Approve)".</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-04-C03, BR-03 (Approve)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Cập nhật trạng thái Approved_For_Matching, nạp hồ sơ vào hàng đợi phân phòng.</td><td class="p-1 border font-mono text-slate-500">Hoàn tất UC-18, nạp vào UC-24</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Bấm "Duyệt hàng loạt (Batch Approve)" cho các hồ sơ thỏa mãn 100% điều kiện.</td><td class="p-1 border font-mono text-purple-700">NFR-06 (Thao tác nhanh)</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Từ chối đơn (vi phạm kỷ luật, nợ phí cũ), nhập lý do và gửi email thông báo.</td><td class="p-1 border font-mono text-rose-700 font-bold">WF-04-C04, BR-03 (Reject)</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_16 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 4 (QUAN TRỌNG) • WIREFRAME & SEQUENCE • SLIDE 16/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-18: Giao Diện Wireframe WF-04 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-04 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-04:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/admin/approvals</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-04] THẨM ĐỊNH HỒ SƠ</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 space-y-2">
                    <div class="flex justify-between items-center bg-slate-100 p-1.5 rounded">
                        <strong class="text-[8.5px] text-slate-800">[WF-04-C01] Đơn Pending (42)</strong>
                        <span class="text-[7.5px] bg-emerald-100 text-emerald-800 px-1 rounded font-bold">[WF-04-C02] Tích xanh BR-01/02</span>
                        <button class="bg-indigo-600 text-white px-2 py-0.5 rounded text-[8px] font-bold">Duyệt loạt (AF-A)</button>
                    </div>
                    <div class="p-1.5 border rounded bg-slate-50 space-y-1">
                        <div class="flex justify-between"><strong>Thái Bảo (VNUK)</strong><span class="text-emerald-700 font-bold">1 Kỳ (Đạt BR-02)</span></div>
                        <div class="flex justify-between items-center pt-1 border-t">
                            <span class="text-[7.5px] text-slate-500">Không nợ phí • Đủ chỉ tiêu</span>
                            <div class="space-x-1">
                                <button class="px-2 py-0.5 bg-emerald-600 text-white rounded font-bold text-[8px]">[WF-04-C03] Phê duyệt (BR-03)</button>
                                <button class="px-2 py-0.5 bg-rose-600 text-white rounded font-bold text-[8px]">[WF-04-C04] Từ chối</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-18 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> Admin -&gt;&gt; UI: Mở màn hình Thẩm định hồ sơ KTX</div>
                <div><strong>2. (BF-2)</strong> UI -&gt;&gt; Service: Yêu cầu danh sách hồ sơ trạng thái Pending</div>
                <div><strong>3. (BF-2)</strong> Service -&gt;&gt; DB: Đối soát tự động BR-01 & BR-02</div>
                <div><strong>4. (BF-2)</strong> UI --&gt;&gt; Admin: Hiển thị danh sách hồ sơ kèm tích xanh</div>
                <div><strong>5. (BF-3)</strong> Admin -&gt;&gt; UI: Chọn hồ sơ kiểm tra chi tiết kỷ luật</div>
                <div><strong>6. (BF-4)</strong> UI -&gt;&gt; Service: Kiểm tra quỹ phòng khả dụng (BR-05)</div>
                <div class="text-emerald-700 font-bold">alt Đạt tiêu chuẩn thẩm định nghiệp vụ (Ref: BF-5, BR-03)</div>
                <div class="text-emerald-700 pl-3"><strong>7. (BF-5)</strong> Admin -&gt;&gt; UI: Bấm "Phê duyệt (Business Approve)"</div>
                <div class="text-emerald-700 pl-3"><strong>8. (BF-6)</strong> Service -&gt;&gt; DB: Cập nhật Approved_For_Matching</div>
                <div class="text-emerald-700 pl-3"><strong>9. (BF-6)</strong> UI --&gt;&gt; Admin: Báo thành công, nạp đơn vào Gale-Shapley</div>
                <div class="text-rose-700 font-bold">else Vi phạm kỷ luật / Chưa cam kết kỳ (Ref: EF-A, BR-03)</div>
                <div class="text-rose-700 pl-3"><strong>10. (EF-A)</strong> Admin -&gt;&gt; UI: Nhập lý do từ chối và bấm "Từ chối"</div>
                <div class="text-rose-700 pl-3"><strong>11. (EF-A)</strong> Service -&gt;&gt; DB: Cập nhật Rejected, gửi email cho SV</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_17 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 5 (QUAN TRỌNG) • ĐẶC TẢ CHI TIẾT • SLIDE 17/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-24: Ghép Phòng Tự Động Gale-Shapley & Lấp Đầy 100%</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Ràng buộc: BR-05 • BR-07 • NFR-01, 02
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-24</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Thực hiện Ghép phòng Tự động (Execute Automated Room Matching)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Thuật toán Gale-Shapley tự động phân bổ sinh viên vào phòng theo loại phòng đăng ký, tối ưu lấp đầy 100% giường (BR-05) và triệt tiêu cặp chặn Blocking Pairs = 0 (BR-07, NFR-02).</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Hệ thống Scheduler (Primary), Cán bộ KTX (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Đến hạn khóa sổ đăng ký hoặc Cán bộ KTX bấm nút "Khởi chạy ghép phòng".</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Có danh sách hồ sơ ở trạng thái Approved_For_Matching (UC-18).</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Sinh danh sách phân phòng chính thức, kích hoạt đồng hồ hạn thanh toán 72h (BR-04).</td></tr>
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
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Scheduler</td><td class="p-1 border">Khởi chạy quy trình Phân phòng Tự động Gale-Shapley.</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-05</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Phân nhóm hồ sơ Approved theo loại phòng nguyện vọng (2, 4, 6 người).</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-05 (Loại phòng)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Tính ma trận tương thích 2 chiều có nhân hệ số ưu tiên 1.5x cho tiêu chí top.</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-06 (Top 1.5x)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Thiết lập bảng sở thích (Preference Lists) giảm dần theo điểm tương thích.</td><td class="p-1 border font-mono text-slate-500">Gale-Shapley input</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Thực thi giải thuật ghép cặp ổn định Gale-Shapley trong thời gian &lt; 1.0 giây.</td><td class="p-1 border font-mono font-bold text-indigo-700">NFR-01 (&lt;1s)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Gộp các cặp ổn định vào phòng thực tế theo nguyên tắc lấp đầy 100% giường.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-05-C02, BR-05 (Lấp đầy)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-7</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Kiểm chứng độ ổn định toán học: Đạt số cặp chặn Blocking Pairs = 0.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-05-C01, BR-07, NFR-02</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-8</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Lưu kết quả xếp phòng vào cơ sở dữ liệu và hiển thị bảng phân bổ.</td><td class="p-1 border font-mono text-slate-500">Database commit</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-9</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Công bố danh sách trúng tuyển và kích hoạt đồng hồ hạn nộp tiền 72 giờ.</td><td class="p-1 border font-mono font-bold text-indigo-700">Chuyển sang UC-13, BR-04</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Cán bộ KTX</td><td class="p-1 border">Xuất toàn bộ kết quả phân phòng và số liệu lấp đầy ra file CSV để báo cáo.</td><td class="p-1 border font-mono text-purple-700">NFR-06 (Export CSV)</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Số lượng hồ sơ lẻ (không đủ cặp): Tự động chuyển hồ sơ lẻ vào danh sách chờ.</td><td class="p-1 border font-mono text-rose-700">Xử lý lẻ người, Waitlist</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_18 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 5 (QUAN TRỌNG) • WIREFRAME & SEQUENCE • SLIDE 18/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-24: Giao Diện Wireframe WF-05 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-05 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-05:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/admin/matching</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-05] PHÂN PHÒNG GALE-SHAPLEY</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 space-y-2">
                    <div class="grid grid-cols-3 gap-1.5 text-center">
                        <div class="p-1 border border-emerald-300 bg-emerald-50 rounded">
                            <span class="text-[7.5px] text-emerald-800 font-bold block">[WF-05-C01] ĐỘ ỔN ĐỊNH</span>
                            <span class="text-xs font-black text-emerald-700">BP = 0</span>
                        </div>
                        <div class="p-1 border border-sky-300 bg-sky-50 rounded">
                            <span class="text-[7.5px] text-sky-800 font-bold block">[WF-05-C02] LẤP ĐẦY</span>
                            <span class="text-xs font-black text-sky-700">100% Giường</span>
                        </div>
                        <div class="p-1 border border-indigo-300 bg-indigo-50 rounded">
                            <span class="text-[7.5px] text-indigo-800 font-bold block">[WF-05-C03] HIỆU NĂNG</span>
                            <span class="text-xs font-black text-indigo-700">0.08 Giây</span>
                        </div>
                    </div>
                    <div class="p-1.5 border rounded bg-slate-50 flex justify-between items-center text-[8px]">
                        <strong>Phòng 201 (VIP 2): Thái Bảo + Minh Quân (92%)</strong>
                        <div class="space-x-1">
                            <button class="bg-slate-800 text-white px-2 py-0.5 rounded">Xuất CSV</button>
                            <button class="bg-indigo-600 text-white px-2 py-0.5 rounded font-bold">Công bố 72h (BF-9)</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-24 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> Scheduler -&gt;&gt; UI: Kích hoạt lệnh chạy ghép phòng</div>
                <div><strong>2. (BF-2)</strong> UI -&gt;&gt; GS: Truyền hồ sơ Approved theo loại phòng</div>
                <div><strong>3. (BF-3)</strong> GS -&gt;&gt; GS: Tính ma trận tương thích 2 chiều & Top 1.5x (BR-06)</div>
                <div><strong>4. (BF-4)</strong> GS -&gt;&gt; GS: Xây dựng bảng sở thích giảm dần</div>
                <div><strong>5. (BF-5)</strong> GS -&gt;&gt; GS: Thực thi giải thuật Gale-Shapley (&lt; 1s, NFR-01)</div>
                <div><strong>6. (BF-6)</strong> GS -&gt;&gt; RoomOpt: Chuyển các cặp ổn định để gộp phòng</div>
                <div><strong>7. (BF-6)</strong> RoomOpt -&gt;&gt; RoomOpt: Phân giường lấp đầy 100% (BR-05)</div>
                <div><strong>8. (BF-7)</strong> GS -&gt;&gt; GS: Kiểm chứng Blocking Pairs = 0 (BR-07, NFR-02)</div>
                <div><strong>9. (BF-8)</strong> RoomOpt --&gt;&gt; UI: Trả về kết quả phân phòng & lấp đầy</div>
                <div><strong>10. (BF-8)</strong> UI -&gt;&gt; DB: Lưu kết quả xếp phòng vào cơ sở dữ liệu</div>
                <div><strong>11. (BF-9)</strong> UI -&gt;&gt; DB: Kích hoạt đồng hồ hạn 72h & phát thông báo (BR-04)</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_19 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 6 (QUAN TRỌNG) • ĐẶC TẢ CHI TIẾT • SLIDE 19/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-13: Thanh Toán Tiền Phòng & Cọc Giữ Chỗ Hạn 72 Giờ Qua VNPay</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Ràng buộc: BR-04 • NFR-03
        </span>
    </div>

    <div class="space-y-2.5 my-auto text-xs">
        <!-- Summary Table -->
        <div>
            <span class="font-bold text-slate-800 text-[10px] block uppercase font-mono mb-1">1. Summary Table (Slide Template):</span>
            <table class="w-full text-left border border-slate-200 text-[9.5px]">
                <tbody class="divide-y divide-slate-200">
                    <tr><td class="p-1 font-bold bg-slate-50 w-24 border">ID</td><td class="p-1 font-mono font-bold text-amber-800 border">UC-13</td><td class="p-1 font-bold bg-slate-50 w-28 border">Title</td><td class="p-1 font-semibold border">Thanh toán Tiền phòng và Cọc 72h (Pay Room Fee and Deposit within 72h)</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Description</td><td class="p-1 border" colspan="3">Sinh viên nộp tiền phòng kỳ 1 kèm tiền cọc tài sản (1.000.000 VNĐ) qua mã VNPAY-QR trong vòng 72 giờ để hoàn tất thủ tục nhận phòng; quá 72h tự động thu hồi phòng cho Waitlist (BR-04).</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Actors</td><td class="p-1 border">Sinh viên (Primary), Cổng thanh toán VNPay (Secondary)</td><td class="p-1 font-bold bg-slate-50 border">Trigger</td><td class="p-1 border">Sinh viên nhận thông báo trúng tuyển phòng và mở màn hình thanh toán.</td></tr>
                    <tr><td class="p-1 font-bold bg-slate-50 border">Preconditions</td><td class="p-1 border">Sinh viên đã được ghép phòng chính thức ở UC-24.</td><td class="p-1 font-bold bg-slate-50 border">Post conditions</td><td class="p-1 border">Khóa vị trí giường chính thức, phát hành Hợp đồng số và Biên lai điện tử có mã QR.</td></tr>
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
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-1</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Nhận thông báo xếp phòng và mở màn hình "Thanh toán Tiền phòng & Cọc".</td><td class="p-1 border font-mono text-slate-500">Màn hình WF-06</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-2</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Hiển thị bảng kê: Tiền phòng Kỳ 1 (7tr) + Cọc tài sản (1tr) = 8.000.000 VNĐ.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-06-C02, BR-04 (Cọc 1tr)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-3</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Kích hoạt đồng hồ đếm ngược thời hạn thanh toán chính xác 72 giờ.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-06-C01, BR-04 (Hạn 72h)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-4</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Chọn phương thức: "Cổng thanh toán bảo mật VNPAY-QR".</td><td class="p-1 border font-mono text-slate-500">Phương thức online</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-5</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Sinh mã giao dịch bảo mật và hiển thị mã QR động từ Cổng VNPay.</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-06-C03, NFR-03 (TLS 1.3)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-6</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Dùng Mobile Banking quét mã QR để chuyển số tiền 8.000.000 VNĐ.</td><td class="p-1 border font-mono text-slate-500">Thao tác người dùng</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-7</td><td class="p-1 border">VNPay</td><td class="p-1 border">Xử lý trừ tiền an toàn, gửi webhook phản hồi vnp_ResponseCode == "00" (SUCCESS).</td><td class="p-1 border font-mono font-bold text-indigo-700">NFR-03 (Đối soát SHA-256)</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-8</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Cập nhật trạng thái "Paid", khóa vị trí giường chính thức trong cơ sở dữ liệu.</td><td class="p-1 border font-mono text-slate-500">Chốt giường 100%</td></tr>
                    <tr class="bg-emerald-50/30"><td class="p-1 border font-mono font-bold text-emerald-800 text-center">BF-9</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Tự động phát hành Biên lai điện tử và cấp Hợp đồng lưu trú có mã QR xác thực.</td><td class="p-1 border font-mono text-slate-500">Extend: Tải hợp đồng/biên lai</td></tr>
                    <tr class="bg-purple-50/40"><td class="p-1 border font-mono font-bold text-purple-700 text-center">AF-A</td><td class="p-1 border">Sinh viên</td><td class="p-1 border">Bấm tải bản PDF Biên lai thu tiền và Hợp đồng nội trú về máy.</td><td class="p-1 border font-mono text-purple-700">Lưu trữ văn bản số</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-A</td><td class="p-1 border">Hệ thống</td><td class="p-1 border">Quá 72h không nộp tiền: Tự động hủy kết quả, thu hồi giường nhường cho Waitlist.</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_TIMEOUT, BR-04</td></tr>
                    <tr class="bg-rose-50/40"><td class="p-1 border font-mono font-bold text-rose-700 text-center">EF-B</td><td class="p-1 border">VNPay</td><td class="p-1 border">Tài khoản không đủ số dư: Báo FAILED, giữ nguyên đồng hồ 72h cho SV thử lại.</td><td class="p-1 border font-mono text-rose-700 font-bold">Mã ERR_INSUFFICIENT</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_20 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded border border-amber-300 uppercase">
                USE CASE 6 (QUAN TRỌNG) • WIREFRAME & SEQUENCE • SLIDE 20/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">UC-13: Giao Diện Wireframe WF-06 & Sơ Đồ Sequence Khớp 1-1</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-amber-100 text-amber-800 px-3 py-1 rounded-full">
            Đặc Tả Trước, Design Sau
        </span>
    </div>

    <div class="grid grid-cols-2 gap-4 my-auto">
        <!-- Wireframe WF-06 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">1. Bản Vẽ Giao Diện Wireframe WF-06:</span>
            <div class="blueprint-bg border-2 border-slate-400 rounded-xl p-3 text-[9px] space-y-2">
                <div class="bg-slate-200 px-2 py-1 rounded flex justify-between items-center">
                    <span class="font-mono text-slate-600">https://ktx.udn.vn/payment/checkout</span>
                    <span class="font-bold text-slate-500 font-mono">[WF-06] THANH TOÁN 72H</span>
                </div>
                <div class="bg-white p-3 rounded border border-slate-300 grid grid-cols-2 gap-2 text-[8.5px]">
                    <div class="space-y-1.5">
                        <div class="p-1.5 bg-rose-50 border border-rose-300 rounded text-center">
                            <span class="text-[7.5px] text-rose-800 font-bold block">[WF-06-C01] ĐỒNG HỒ 72H</span>
                            <span class="text-sm font-black text-rose-600 font-mono">68h : 14m : 30s</span>
                        </div>
                        <div class="p-1.5 border rounded bg-slate-50">
                            <span>• Tiền phòng VIP (5th): 7.000.000đ</span><br>
                            <span>• Tiền cọc (BR-04): 1.000.000đ</span><br>
                            <strong class="text-indigo-900">Tổng cộng: 8.000.000 VNĐ</strong>
                        </div>
                    </div>
                    <div class="p-1.5 border border-indigo-200 bg-indigo-50/50 rounded text-center space-y-1">
                        <span class="callout-badge bg-indigo-600 text-white">[WF-06-C03] Mã VNPAY-QR</span>
                        <div class="w-14 h-14 mx-auto bg-slate-900 text-white rounded flex items-center justify-center font-mono text-[7px]">[QR 8tr]</div>
                        <button class="w-full py-0.5 bg-emerald-600 text-white font-bold rounded text-[7.5px]">✓ Đã Nộp Tiền (BF-7)</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Sequence Diagram UC-13 -->
        <div class="space-y-1.5">
            <span class="font-bold text-slate-800 text-[10.5px] uppercase font-mono block">2. Sơ Đồ Tuần Tự (Sequence Diagram Khớp 1-1):</span>
            <div class="p-3 bg-slate-50 border-2 border-slate-300 rounded-xl font-mono text-[9px] space-y-1 text-slate-700 leading-relaxed">
                <div><strong>1. (BF-1)</strong> SV -&gt;&gt; UI: Mở màn hình thanh toán tiền phòng & cọc</div>
                <div><strong>2. (BF-2)</strong> UI -&gt;&gt; Pay: Yêu cầu bảng kê viện phí (7tr phòng + 1tr cọc = 8tr)</div>
                <div><strong>3. (BF-3)</strong> Pay --&gt;&gt; UI: Kích hoạt đồng hồ đếm ngược 72 giờ (BR-04)</div>
                <div><strong>4. (BF-4)</strong> SV -&gt;&gt; UI: Chọn phương thức VNPay-QR</div>
                <div><strong>5. (BF-5)</strong> UI -&gt;&gt; VNPay: Khởi tạo phiên giao dịch (TLS 1.3, NFR-03)</div>
                <div><strong>6. (BF-6)</strong> SV -&gt;&gt; VNPay: Quét mã QR trên Mobile Banking và xác thực</div>
                <div class="text-emerald-700 font-bold">alt Thanh toán thành công trong 72h (Ref: BF-7, BR-04)</div>
                <div class="text-emerald-700 pl-3"><strong>7. (BF-7)</strong> VNPay --&gt;&gt; Pay: Webhook SUCCESS (vnp_ResponseCode = 00)</div>
                <div class="text-emerald-700 pl-3"><strong>8. (BF-8)</strong> Pay -&gt;&gt; DB: Cập nhật Paid, khóa giường chính thức 100%</div>
                <div class="text-emerald-700 pl-3"><strong>9. (BF-9)</strong> Pay --&gt;&gt; SV: Cấp Hợp đồng số & Biên lai điện tử QR</div>
                <div class="text-rose-700 font-bold">else Quá hạn 72h không thanh toán (Ref: EF-A, BR-04)</div>
                <div class="text-rose-700 pl-3"><strong>10. (EF-A)</strong> Pay -&gt;&gt; DB: Hủy kết quả, thu hồi giường nhường cho Waitlist</div>
            </div>
        </div>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_21 = r"""
<div class="slide">
    <div class="flex justify-between items-start border-b border-slate-200 pb-2">
        <div>
            <span class="text-[10px] font-mono font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded border border-indigo-200 uppercase">
                BẢO CHỨNG CHẤT LƯỢNG • SLIDE 21/22
            </span>
            <h2 class="text-xl font-black text-slate-900 mt-0.5">8. Bảng Ma Trận Truy Vết 1-to-1 (Traceability Matrix)</h2>
        </div>
        <span class="text-xs font-mono font-bold bg-emerald-100 text-emerald-800 px-3 py-1 rounded-full">
            Khớp 1-1 Tuyệt Đối: Step ID ↔ Message ↔ Wireframe ↔ BR
        </span>
    </div>

    <div class="overflow-x-auto my-auto text-xs">
        <table class="w-full text-left border border-slate-200 text-[9.5px]">
            <thead class="bg-slate-100 font-bold text-slate-700 uppercase">
                <tr>
                    <th class="p-1.5 border w-12">Mã UC</th>
                    <th class="p-1.5 border w-24">Bước Đặc Tả (Step ID)</th>
                    <th class="p-1.5 border">Message Sequence Diagram (1-1)</th>
                    <th class="p-1.5 border">Mã Thành Phần Wireframe Design</th>
                    <th class="p-1.5 border">Quy Tắc Nghiệp Vụ (BR)</th>
                    <th class="p-1.5 border text-center w-20">Kết Quả</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-200">
                <tr><td class="p-1 border font-mono font-bold text-indigo-700">UC-01</td><td class="p-1 border font-mono">BF-3</td><td class="p-1 border">Message 3 (SV -&gt; UI)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-01-C03, C04</td><td class="p-1 border font-mono">BR-01 (Đúng trường A)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>
                <tr><td class="p-1 border font-mono font-bold text-indigo-700">UC-01</td><td class="p-1 border font-mono">EF-B</td><td class="p-1 border">Message 10 (EF-B)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-01-C07</td><td class="p-1 border font-mono text-rose-600 font-bold">BR-01 (Từ chối sai trường)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>
                
                <tr class="bg-slate-50"><td class="p-1 border font-mono font-bold text-amber-800">UC-04</td><td class="p-1 border font-mono">BF-2, BF-3</td><td class="p-1 border">Message 2, 3 (UI -&gt; SV)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-02-C01</td><td class="p-1 border font-mono">BR-05 (3 Gói phòng)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>
                <tr class="bg-slate-50"><td class="p-1 border font-mono font-bold text-amber-800">UC-04</td><td class="p-1 border font-mono">BF-5, BF-6</td><td class="p-1 border">Message 5, 6 (SV -&gt; UI)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-02-C02, C04</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-06 (Top 1.5x) • BR-02 (Kỳ)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>

                <tr><td class="p-1 border font-mono font-bold text-amber-800">UC-05</td><td class="p-1 border font-mono">BF-3, BF-5</td><td class="p-1 border">Message 3, 5 (Scoring Engine)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-03-C01, C02</td><td class="p-1 border font-mono">BR-06 (Ma trận 2 chiều)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>

                <tr class="bg-slate-50"><td class="p-1 border font-mono font-bold text-amber-800">UC-18</td><td class="p-1 border font-mono">BF-5</td><td class="p-1 border">Message 7, 8 (Admin -&gt; UI)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-04-C03</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-03 (Business Approve)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>

                <tr><td class="p-1 border font-mono font-bold text-amber-800">UC-24</td><td class="p-1 border font-mono">BF-6, BF-7</td><td class="p-1 border">Message 7, 8 (Gale-Shapley)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-05-C01, C02</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-05 (100% Giường) • BR-07 (BP=0)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>

                <tr class="bg-slate-50"><td class="p-1 border font-mono font-bold text-amber-800">UC-13</td><td class="p-1 border font-mono">BF-2, BF-3</td><td class="p-1 border">Message 2, 3 (UI &lt;-&gt; Pay)</td><td class="p-1 border font-mono font-bold text-indigo-700">WF-06-C01, C02</td><td class="p-1 border font-mono font-bold text-indigo-700">BR-04 (Hạn 72h & Cọc 1tr)</td><td class="p-1 border text-center text-emerald-700 font-bold">✓ Khớp 1-1</td></tr>
            </tbody>
        </table>
    </div>

    <div class="p-3 bg-emerald-50 border border-emerald-300 rounded-xl text-[10.5px] text-emerald-950 font-semibold space-y-1">
        <span class="font-bold block text-emerald-900">NGHIỆM THU NGUYÊN TẮC: "ĐẶC TẢ TRƯỚC, DESIGN SAU"</span>
        <p>Mọi yếu tố giao diện wireframe (button, input, checkbox, widget, alert) đều được sinh ra từ các bước sự kiện cụ thể trong bảng đặc tả và message tương ứng trong sơ đồ tuần tự.</p>
    </div>

    <div class="border-t border-slate-200 pt-2 flex justify-between items-center text-xs text-slate-500 font-mono">
        <span>Đề tài KTX Smart Match • Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK)</span>
        <span>Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
    </div>
</div>
"""

SLIDE_22 = r"""
<div class="slide bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white justify-between p-12">
    <div class="flex justify-between items-center border-b border-indigo-400/30 pb-4">
        <span class="text-xs font-mono font-bold text-indigo-300 uppercase tracking-widest block">TỔNG KẾT BÁO CÁO • SLIDE 22/22</span>
        <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs font-mono font-bold">
            HOÀN TẤT BẢO VỆ ĐỒ ÁN
        </span>
    </div>

    <div class="space-y-4 my-auto py-6 text-center">
        <span class="text-5xl block mb-2">🎉</span>
        <h2 class="text-3xl md:text-4xl font-black text-white tracking-tight">
            CẢM ƠN THẦY VÀ CÁC BẠN ĐÃ LẮNG NGHE!
        </h2>
        <p class="text-slate-300 text-sm max-w-2xl mx-auto leading-relaxed">
            Hồ sơ đồ án Hệ Thống KTX Smart Match đã hoàn thành 100% các tiêu chuẩn học thuật khắt khe nhất: Chuẩn bản vẽ Draw.io 26 Use Case, Bảng luồng BF/AF/EF (100% điểm), Bộ 3 Diagram (Sequence, Activity, Component) và Thiết kế Wireframe UI đồng bộ 1-1.
        </p>
        <div class="pt-4">
            <span class="px-5 py-2 rounded-xl bg-indigo-600/80 border border-indigo-400 text-white font-mono font-bold text-sm inline-block shadow-lg">
                NHÓM 3 (VNUK) SẴN SÀNG CHO PHẦN HỎI ĐÁP (Q&A)
            </span>
        </div>
    </div>

    <div class="border-t border-indigo-500/30 pt-4 flex justify-between items-center text-xs text-slate-300 font-mono">
        <div>
            <span>Thành viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
        </div>
        <div>
            <span>Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) • Đại học Đà Nẵng (2026)</span>
        </div>
    </div>
</div>
"""

print("slides_data_3.py created")
