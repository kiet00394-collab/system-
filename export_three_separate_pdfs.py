# -*- coding: utf-8 -*-
"""
export_three_separate_pdfs.py
Tạo 3 file HTML riêng và xuất thành 3 file PDF riêng biệt cho người dùng:
1. BR_KTX_Smart_Match_VNUK.pdf
2. Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.pdf
3. Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.pdf
"""

import os
import subprocess
import shutil

EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = os.path.dirname(__file__)

# -------------------------------------------------------------
# 1. HTML CHO BUSINESS RULES RIÊNG
# -------------------------------------------------------------
HTML_BR = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Quy tắc Nghiệp vụ - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #1e293b; }
        .page { width: 210mm; min-height: 297mm; padding: 16mm 18mm; margin: 20px auto; background: #fff; box-shadow: 0 10px 25px rgba(0,0,0,0.3); page-break-after: always; }
        @media print { body { background: transparent; padding: 0; } .page { width: 100%; min-height: 100vh; margin: 0; padding: 14mm 16mm; box-shadow: none; page-break-after: always; } }
    </style>
</head>
<body class="py-6">
    <div class="page flex flex-col justify-between">
        <div>
            <div class="border-b-2 border-indigo-900 pb-2.5 mb-4 flex justify-between items-start">
                <div>
                    <div class="text-[11px] font-extrabold uppercase tracking-wider text-indigo-950">Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng</div>
                    <div class="text-[10px] font-bold text-slate-500 uppercase tracking-wide">Khoa Công nghệ Thông tin & Trí tuệ Nhân tạo • System Engineering</div>
                </div>
                <div class="text-right">
                    <span class="text-[10px] font-mono font-bold bg-indigo-50 text-indigo-700 border border-indigo-200 px-2 py-0.5 rounded">SLIDE P125 STANDARD</span>
                </div>
            </div>

            <div class="text-center my-3">
                <span class="text-[10px] font-mono font-extrabold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300 uppercase tracking-widest">TÀI LIỆU QUY TẮC NGHIỆP VỤ RIÊNG BIỆT</span>
                <h1 class="text-xl font-black text-slate-900 mt-2 mb-1 tracking-tight uppercase">Hệ Thống Quy Tắc Nghiệp Vụ KTX</h1>
                <p class="text-xs italic text-slate-600">Đề tài: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)</p>
            </div>

            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 mb-4 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Nhóm sinh viên thực hiện</span>
                        <span class="font-black text-slate-900 text-sm">Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
                        <span class="text-slate-500 block text-[11px] mt-0.5">Nhóm 3 – Lớp Kỹ thuật Phần mềm (VNUK)</span>
                    </div>
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Bản chất tài liệu</span>
                        <span class="font-extrabold text-indigo-700 block">• Định dạng chuẩn 3 cột: Rule ID | Name | Description</span>
                        <span class="font-extrabold text-slate-600 block">• Tập trung 100% Ràng buộc nghiệp vụ (Business Constraints)</span>
                    </div>
                </div>
            </div>

            <div class="mb-3">
                <h2 class="text-xs font-extrabold text-slate-900 uppercase mb-1.5 flex items-center gap-1.5">
                    <span>⚖️</span> Danh mục 09 Quy tắc Nghiệp vụ Cốt lõi (Business Rules)
                </h2>
                <table class="w-full text-[9px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-indigo-950 text-white font-bold text-center">
                            <th class="p-1.5 border border-slate-700 w-16">Rule ID</th>
                            <th class="p-1.5 border border-slate-700 w-44 text-left">Tên Quy tắc (Name)</th>
                            <th class="p-1.5 border border-slate-700 text-left">Ràng buộc Nghiệp vụ Cụ thể (Description)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-01</td>
                            <td class="p-1 font-bold text-slate-800">Mã SV duy nhất & Đối tượng hợp lệ</td>
                            <td class="p-1 text-slate-600">Mỗi sinh viên có duy nhất một Mã số sinh viên (MSSV) không trùng lặp trong toàn bộ hệ thống, đóng vai trò khóa chính định danh tài khoản. KTX chỉ tiếp nhận sinh viên chính quy thuộc khối liên kết VNUK có trạng thái đào tạo hợp lệ và sử dụng email trường cấp (@vnuk.edu.vn). Tài khoản ngoài hệ thống hoặc MSSV không hợp lệ bị từ chối đăng ký.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-02</td>
                            <td class="p-1 font-bold text-slate-800">Cam kết thời hạn tối thiểu 1 kỳ</td>
                            <td class="p-1 text-slate-600">Mỗi hồ sơ đăng ký KTX bắt buộc phải có cam kết thời hạn cư trú tối thiểu 01 học kỳ (05 tháng) hoặc trọn năm học (10 tháng). Hệ thống kiên quyết không thụ lý hợp đồng ngắn hạn theo ngày/tuần nhằm bảo toàn nếp sống văn hóa ổn định và kế hoạch vận hành tài chính của KTX.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-03</td>
                            <td class="p-1 font-bold text-slate-800">Phê duyệt nghiệp vụ (Approve)</td>
                            <td class="p-1 text-slate-600">Mọi hồ sơ đăng ký phòng của sinh viên sau khi nộp trực tuyến bắt buộc phải trải qua bước thẩm định và phê duyệt nghiệp vụ của Cán bộ KTX (rà soát lịch sử kỷ luật, đối soát diện ưu tiên chính sách, kiểm tra nợ cũ) trước khi được đưa vào hàng đợi chạy thuật toán phân bổ phòng.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-04</td>
                            <td class="p-1 font-bold text-slate-800">Đặt cọc giữ chỗ và hạn 72 giờ</td>
                            <td class="p-1 text-slate-600">Trong vòng chính xác 72 giờ kể từ thời điểm công bố kết quả phân phòng, sinh viên phải hoàn tất thanh toán tiền phòng kỳ 1 kèm tiền đặt cọc tài sản (2.000.000 VNĐ) qua cổng VNPay. Quá thời hạn 72 giờ không thanh toán, hệ thống tự động hủy kết quả giữ chỗ và chuyển suất cho sinh viên trong danh sách chờ (Waitlist).</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-05</td>
                            <td class="p-1 font-bold text-slate-800">Ghép bạn theo Request hai chiều</td>
                            <td class="p-1 text-slate-600">Việc ghép bạn cùng phòng giữa hai cá nhân bắt buộc phải dựa trên sự đồng thuận tự nguyện của cả hai bên: Một bên gửi yêu cầu (Matching Request), bên còn lại phải nhận thông tin, xem xét hồ sơ nếp sống và chủ động bấm 'Đồng ý' thì quan hệ ghép cặp mới được xác lập hợp lệ. Thời hạn phản hồi tối đa là 48 giờ.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-06</td>
                            <td class="p-1 font-bold text-slate-800">Tối ưu lấp đầy 100% phòng</td>
                            <td class="p-1 text-slate-600">Thuật toán phân bổ phòng ưu tiên lấp đầy 100% số giường của từng phòng (2, 4, 6 người) trước khi mở phòng mới nhằm tối ưu hóa chi phí điện nước chung, khấu hao điều hòa và bảo toàn biên lợi nhuận vận hành cho KTX.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-07</td>
                            <td class="p-1 font-bold text-slate-800">Quyết toán và hoàn cọc khi trả phòng</td>
                            <td class="p-1 text-slate-600">Khi làm thủ tục trả phòng, tiền đặt cọc chỉ được hoàn trả sau khi Cán bộ KTX nghiệm thu hiện trạng cơ sở vật chất. Số tiền cọc hoàn lại = 2.000.000đ − (Công nợ dịch vụ phát sinh + Chi phí bồi thường hư hỏng tài sản nếu có). Nếu sinh viên đơn phương phá vỡ hợp đồng trước 1 học kỳ, toàn bộ tiền cọc không được hoàn lại.</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-08</td>
                            <td class="p-1 font-bold text-slate-800">Ràng buộc đổi phòng / đổi bạn</td>
                            <td class="p-1 text-slate-600">Mỗi sinh viên chỉ được phép có tối đa 01 yêu cầu đổi phòng đang trong trạng thái xử lý; yêu cầu bắt buộc phải có lý do cụ thể và chỉ được Cán bộ KTX phê duyệt khi phòng đích còn chỗ trống khả dụng và phù hợp về giới tính, loại phòng.</td>
                        </tr>
                        <tr class="bg-white">
                            <td class="p-1 text-center font-bold font-mono text-indigo-700">BR-09</td>
                            <td class="p-1 font-bold text-slate-800">Trọng số ưu tiên cá nhân 1.5x</td>
                            <td class="p-1 text-slate-600">Điểm hòa hợp nếp sống giữa hai sinh viên được tính toán trên vector 8 tiêu chí thói quen; tiêu chí mà mỗi sinh viên đánh dấu là quan trọng nhất (Top Criterion) sẽ được nhân hệ số trọng số 1.5x khi tính toán ma trận tương thích hai chiều bất đối xứng.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Tài liệu Business Rules riêng biệt</span>
        </div>
    </div>
</body>
</html>
"""

# -------------------------------------------------------------
# 2. HTML CHO ĐẶC TẢ USE CASE RIÊNG
# -------------------------------------------------------------
HTML_SPEC = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đặc tả Use Case - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #1e293b; }
        .page { width: 210mm; min-height: 297mm; padding: 14mm 16mm; margin: 20px auto; background: #fff; box-shadow: 0 10px 25px rgba(0,0,0,0.3); page-break-after: always; }
        @media print { body { background: transparent; padding: 0; } .page { width: 100%; min-height: 100vh; margin: 0; padding: 12mm 14mm; box-shadow: none; page-break-after: always; } }
    </style>
</head>
<body class="py-6">

    <!-- Trang 1: Mục lục use case vẽ lại -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="border-b-2 border-indigo-900 pb-2 mb-3 flex justify-between items-start">
                <div>
                    <div class="text-[11px] font-extrabold uppercase tracking-wider text-indigo-950">Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng</div>
                    <div class="text-[10px] font-bold text-slate-500 uppercase tracking-wide">Khoa Công nghệ Thông tin & Trí tuệ Nhân tạo • Phân tích Thiết kế Hệ thống</div>
                </div>
                <div class="text-right">
                    <span class="text-[10px] font-mono font-bold bg-indigo-50 text-indigo-700 border border-indigo-200 px-2 py-0.5 rounded">SLIDE P110 SPECIFICATION</span>
                </div>
            </div>

            <div class="text-center my-3">
                <span class="text-[10px] font-mono font-extrabold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300 uppercase tracking-widest">TÀI LIỆU ĐẶC TẢ USE CASE RIÊNG BIỆT</span>
                <h1 class="text-xl font-black text-slate-900 mt-2 mb-1 tracking-tight uppercase">Đặc Tả Use Case Hệ Thống KTX</h1>
                <p class="text-xs italic text-slate-600">Đề tài: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)</p>
            </div>

            <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 mb-4 text-xs">
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Nhóm sinh viên thực hiện</span>
                        <span class="font-black text-slate-900 text-sm">Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều</span>
                        <span class="text-slate-500 block text-[11px] mt-0.5">Nhóm 3 – Lớp Kỹ thuật Phần mềm (VNUK)</span>
                    </div>
                    <div>
                        <span class="font-bold text-slate-500 uppercase text-[10px] block">Đặc điểm tài liệu đặc tả</span>
                        <span class="font-extrabold text-indigo-700 block">• Tinh giản danh mục Use Case cốt lõi (vẽ lại chuẩn)</span>
                        <span class="font-extrabold text-emerald-700 block">• Đầy đủ 3 luồng: Basic (BF), Alternate (AF), Exception (EF)</span>
                    </div>
                </div>
            </div>

            <div class="mb-3">
                <h2 class="text-xs font-extrabold text-slate-900 uppercase mb-1.5 flex items-center gap-1.5">
                    <span>📋</span> 1. Danh mục Use Case Hệ Thống (Vẽ lại Tinh gọn & Chuẩn hóa)
                </h2>
                <table class="w-full text-[8.5px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-12">Mã UC</th>
                            <th class="p-1 border border-slate-700 w-44 text-left">Tên Use Case</th>
                            <th class="p-1 border border-slate-700 w-32 text-left">Tác nhân chính</th>
                            <th class="p-1 border border-slate-700 text-left">Phạm vi chức năng cốt lõi</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-01</td><td class="p-0.5 font-bold">Đăng nhập & Xác thực hệ thống</td><td class="p-0.5">Sinh viên, Cán bộ KTX</td><td class="p-0.5">Lựa chọn đăng nhập bằng Tên/Email (@vnuk.edu.vn) hoặc MSSV + Mật khẩu là 1 chức năng duy nhất.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-02</td><td class="p-0.5 font-bold">Đăng ký & Khai báo nếp sống</td><td class="p-0.5">Sinh viên</td><td class="p-0.5">Đăng ký tài khoản bằng MSSV duy nhất và khai báo hồ sơ nếp sống sinh hoạt 8 tiêu chí.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-03</td><td class="p-0.5 font-bold">Cập nhật hồ sơ & thói quen</td><td class="p-0.5">Sinh viên</td><td class="p-0.5">Chỉnh sửa thông tin cá nhân và 8 thói quen sinh hoạt; hỗ trợ nạp Persona mẫu.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-04</td><td class="p-0.5 font-bold">Chọn phòng & Nộp đơn KTX</td><td class="p-0.5">Sinh viên</td><td class="p-0.5">Chọn loại phòng (2/4/6), tiện ích, ký cam kết ở tối thiểu 1 kỳ và nộp hồ sơ chờ duyệt.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-05</td><td class="p-0.5 font-bold">Ghép bạn theo yêu cầu (Matching)</td><td class="p-0.5">SV gửi A, SV nhận B</td><td class="p-0.5">SV A gửi Matching Request -> SV B nhận thông báo, xem profile và chọn Đồng ý/Từ chối.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-06</td><td class="p-0.5 font-bold">Xem kết quả phân phòng</td><td class="p-0.5">Sinh viên</td><td class="p-0.5">Tra cứu phòng được phân, danh sách bạn cùng phòng, viện phí và hạn chót thanh toán 72h.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-07</td><td class="p-0.5 font-bold">Thanh toán & Đặt cọc 72h</td><td class="p-0.5">Sinh viên, VNPay</td><td class="p-0.5">Thanh toán viện phí và cọc 2tr; hệ thống tự động tạo và in/tải biên lai trong luồng chính.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-08</td><td class="p-0.5 font-bold">Thủ tục Trả phòng (Check-out)</td><td class="p-0.5">SV, Cán bộ, Kế toán</td><td class="p-0.5">Quy trình trả phòng: Kiểm kê tài sản -> Khấu trừ hư hại -> Hoàn trả cọc -> Giải phóng chỗ.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-09</td><td class="p-0.5 font-bold">Yêu cầu chuyển phòng / đổi bạn</td><td class="p-0.5">Sinh viên, Cán bộ KTX</td><td class="p-0.5">Gửi yêu cầu đổi phòng kèm lý do/minh chứng khi có xung đột nếp sống phát sinh.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-10</td><td class="p-0.5 font-bold">Báo hỏng cơ sở vật chất</td><td class="p-0.5">Sinh viên, Kỹ thuật</td><td class="p-0.5">Khai báo sự cố điện nước, thiết bị hư hỏng trong phòng và theo dõi tiến độ sửa chữa.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-11</td><td class="p-0.5 font-bold">Quản lý tòa, phòng & bảng giá</td><td class="p-0.5">Quản trị viên (Admin)</td><td class="p-0.5">Thêm, cập nhật, cấu hình danh mục tòa nhà, phòng ở, định mức giá và chỉ tiêu tiếp nhận.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-12</td><td class="p-0.5 font-bold">Phê duyệt đơn Business Approve</td><td class="p-0.5">Cán bộ quản lý KTX</td><td class="p-0.5">Kiểm tra điều kiện lưu trú, xét duyệt hồ sơ hợp lệ để đưa vào thuật toán phân phòng.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-13</td><td class="p-0.5 font-bold">Phân bổ phòng Gale-Shapley</td><td class="p-0.5">Hệ thống (Scheduler)</td><td class="p-0.5">Chạy thuật toán Gale-Shapley kết hợp lấp đầy 100% giường, triệt tiêu cặp chặn BP=0.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-14</td><td class="p-0.5 font-bold">Đối soát thanh toán & Hoàn cọc</td><td class="p-0.5">Kế toán, VNPay</td><td class="p-0.5">Quản lý dòng tiền thu cọc/viện phí, đối soát tự động với VNPay và thực thi lệnh hoàn cọc.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-15</td><td class="p-0.5 font-bold">Tự động hủy đơn quá 72h</td><td class="p-0.5">Hệ thống (Scheduler)</td><td class="p-0.5">Quét định kỳ các đơn quá hạn thanh toán 72h, tự động thu hồi phòng và phân bổ cho Waitlist.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-indigo-700">UC-16</td><td class="p-0.5 font-bold">Báo cáo doanh thu & lấp đầy</td><td class="p-0.5">Kế toán, Admin</td><td class="p-0.5">Xuất báo cáo thống kê tỷ lệ lấp đầy, doanh thu viện phí, công nợ và hiệu quả vận hành.</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 01 / 03 - Danh mục Use Case tinh gọn</span>
        </div>
    </div>

    <!-- Trang 2: Chi tiết UC-05 Matching by Request -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between border-b border-slate-200 pb-1.5 mb-2">
                <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 border border-indigo-300">
                    USE CASE TRỌNG TÂM: MATCHING THEO REQUEST (ĐỒNG THUẬN 2 BÊN)
                </span>
                <span class="text-xs font-mono font-bold text-slate-400">UC-05</span>
            </div>

            <h2 class="text-sm font-black text-slate-900 mb-0.5">
                UC-05: Ghép bạn cùng phòng theo yêu cầu hai chiều (Roommate Matching by Request)
            </h2>
            <p class="text-[10px] text-slate-500 italic mb-2">
                Phân định rõ 2 tác nhân độc lập: Sinh viên gửi (SV A) và Sinh viên nhận (SV B). Đặc tả đầy đủ kết thúc.
            </p>

            <div class="mb-2.5">
                <table class="w-full text-[9px] border-collapse border border-slate-200">
                    <tbody>
                        <tr><td class="p-1 font-bold text-slate-700 bg-slate-50 w-24 border border-slate-200">Description</td><td class="p-1 text-slate-600 border border-slate-200">SV A gửi Matching Request đến SV B; SV B nhận thông báo, xem đối chiếu profile và chọn Đồng ý (ghép cặp) hoặc Từ chối.</td></tr>
                        <tr><td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Actors</td><td class="p-1 text-slate-800 border border-slate-200">Sinh viên gửi (SV A - Primary), Sinh viên nhận (SV B - Secondary), Hệ thống KTX (Supporting).</td></tr>
                        <tr><td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Preconditions</td><td class="p-1 text-slate-600 border border-slate-200">Cả A và B đều đã hoàn thành khảo sát 8 thói quen sinh hoạt và chưa chốt hợp đồng phòng chính thức.</td></tr>
                        <tr><td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Postconditions</td><td class="p-1 text-slate-600 border border-slate-200">Khi B đồng ý: Cặp ghép được xác lập (Matched Pair) để ưu tiên xếp phòng chung. Khi B từ chối: Yêu cầu bị hủy và A được thông báo.</td></tr>
                        <tr><td class="p-1 font-bold text-slate-700 bg-slate-50 border border-slate-200">Trigger</td><td class="p-1 text-slate-600 border border-slate-200">Sinh viên A nhấn nút 'Gửi yêu cầu ghép bạn' trên danh sách gợi ý bạn cùng phòng.</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- Basic Flow -->
            <div class="mb-2">
                <div class="text-[9.5px] font-bold text-indigo-900 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200 uppercase mb-1">Luồng cơ bản (Basic Flow)</div>
                <table class="w-full text-[8.5px] border-collapse border border-slate-200">
                    <thead>
                        <tr class="bg-slate-900 text-white font-bold text-center">
                            <th class="p-1 border border-slate-700 w-12">Step ID</th><th class="p-1 border border-slate-700 w-24 text-left">Actor</th><th class="p-1 border border-slate-700 text-left">Action</th><th class="p-1 border border-slate-700 w-44 text-left">Notes and References</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-1</td><td class="p-0.5 font-bold">Sinh viên A</td><td class="p-0.5">Xem gợi ý mức độ hòa hợp nếp sống và nhấn 'Gửi yêu cầu ghép bạn' tới Sinh viên B.</td><td class="p-0.5 text-slate-500 italic">Trigger: SV A gửi request</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-2</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Kiểm tra điều kiện: Cùng giới tính, cùng loại phòng, B chưa vào nhóm khác và chưa có request đang chờ.</td><td class="p-0.5 text-slate-500 italic">BR-05. Rẽ EF-A: Không đủ điều kiện.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-3</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Tạo bản ghi yêu cầu trạng thái 'Pending', thiết lập hạn 48h và gửi thông báo tức thì đến Sinh viên B.</td><td class="p-0.5 text-slate-500 italic">Rẽ AF-B: A chủ động thu hồi.</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-4</td><td class="p-0.5 font-bold">Sinh viên B</td><td class="p-0.5">Đăng nhập hệ thống, mở thông báo và xem bảng đối chiếu 8 thói quen sinh hoạt của Sinh viên A.</td><td class="p-0.5 text-slate-500 italic">Actor: SV B. Rẽ AF-A: B từ chối.</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-5</td><td class="p-0.5 font-bold">Sinh viên B</td><td class="p-0.5">Nhấn nút 'Đồng ý kết bạn cùng phòng'.</td><td class="p-0.5 text-slate-500 italic font-bold text-emerald-700">Đồng thuận hai chiều</td></tr>
                        <tr class="bg-slate-50"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-6</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Cập nhật trạng thái 'Matched Pair' cho cặp A-B, ưu tiên xếp phòng chung và gửi thông báo chúc mừng tới cả hai.</td><td class="p-0.5 text-slate-500 italic">BR-05: Hoàn tất ghép cặp</td></tr>
                        <tr class="bg-white"><td class="p-0.5 text-center font-bold font-mono text-teal-700">BF-7</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Đóng yêu cầu thành công và cập nhật bảng danh sách bạn cùng phòng của cả hai bên.</td><td class="p-0.5 text-emerald-700 font-bold">[End of Use Case: mục tiêu đã đạt]</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- AF & EF -->
            <div class="grid grid-cols-2 gap-2 text-[8px]">
                <div class="p-1.5 bg-emerald-50/60 border border-emerald-200 rounded">
                    <span class="font-bold text-emerald-800 uppercase block mb-0.5">Alternate Flows (AF)</span>
                    <p><strong>AF-A: B từ chối (tại BF-4):</strong> B nhấn 'Từ chối' -> Hệ thống chuyển trạng thái 'Declined', giải phóng cờ chờ và gửi thông báo nhẹ nhàng cho A để tìm bạn khác. [Outcome: kind: successEnd].</p>
                    <p class="mt-1"><strong>AF-B: A thu hồi (tại BF-3):</strong> A mở danh sách đã gửi, bấm 'Thu hồi yêu cầu' -> Hệ thống hủy Pending, thu hồi thông báo phía B. [Outcome: kind: successEnd].</p>
                </div>
                <div class="p-1.5 bg-rose-50/60 border border-rose-200 rounded">
                    <span class="font-bold text-rose-800 uppercase block mb-0.5">Exception Flows (EF)</span>
                    <p><strong>EF-A: Không đủ điều kiện (tại BF-2):</strong> Khác giới tính, khác loại phòng hoặc B đã có nhóm -> Hệ thống chặn gửi và báo lý do. [Outcome: kind: failureEnd].</p>
                    <p class="mt-1"><strong>EF-B: Quá hạn 48 giờ (tại BF-3):</strong> B không phản hồi sau 48h -> Hệ thống tự động chuyển trạng thái 'Expired' và thông báo cho A. [Outcome: kind: failureEnd].</p>
                </div>
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 02 / 03 - Đặc tả UC Matching Request</span>
        </div>
    </div>

    <!-- Trang 3: Chi tiết UC-07 Thanh toán & UC-08 Trả phòng -->
    <div class="page flex flex-col justify-between">
        <div>
            <!-- UC-07 -->
            <div class="border-b border-slate-200 pb-2 mb-2">
                <div class="flex items-center justify-between pb-1 mb-1">
                    <span class="text-[9.5px] font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 border border-emerald-300">
                        UC-07: THANH TOÁN TIỀN PHÒNG & ĐẶT CỌC 72H (TẠO/IN BIÊN LAI TRỰC TIẾP TRONG BF)
                    </span>
                </div>
                <table class="w-full text-[8px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700 w-10">BF-1</td><td class="p-0.5 font-bold w-20">Sinh viên</td><td class="p-0.5">Mở màn hình thanh toán từ thông báo phân phòng trúng tuyển KTX.</td><td class="p-0.5 w-40 text-slate-500 italic">Trigger</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-2</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Hiển thị bảng kê: Tiền phòng kỳ 1 + Cọc 2.000.000đ và đồng hồ đếm ngược 72 giờ.</td><td class="p-0.5 text-slate-500 italic">BR-04. Rẽ EF-B: Quá hạn 72h.</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-3</td><td class="p-0.5 font-bold">Sinh viên</td><td class="p-0.5">Xác nhận thanh toán và chọn phương thức cổng điện tử VNPAY-QR.</td><td class="p-0.5 text-slate-500 italic">Rẽ AF-A: Chọn chuyển khoản.</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-4</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Tạo đơn hàng bảo mật (TLS 1.3), sinh mã giao dịch duy nhất và mã QR thanh toán động.</td><td class="p-0.5 text-slate-500 italic">NFR-04</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-5</td><td class="p-0.5 font-bold">Cổng VNPay</td><td class="p-0.5">Sinh viên quét QR trên Mobile Banking; VNPay trừ tiền và gửi callback (vnp_ResponseCode = 00).</td><td class="p-0.5 text-slate-500 italic">Rẽ EF-A: Giao dịch lỗi.</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-6</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Cập nhật hợp đồng thành 'Paid', khóa cố định vị trí phòng giường cho sinh viên.</td><td class="p-0.5 text-slate-500 italic">Chốt phòng thành công</td></tr>
                        <tr class="bg-amber-50"><td class="p-0.5 font-mono font-bold text-amber-800">BF-7</td><td class="p-0.5 font-bold text-amber-900">Hệ thống</td><td class="p-0.5 font-bold text-amber-900">TỰ ĐỘNG TẠO BIÊN LAI ĐIỆN TỬ có mã tra cứu và hiển thị nút 'In biên lai' / 'Tải file PDF biên lai'.</td><td class="p-0.5 text-amber-800 font-bold">TẠO/IN BIÊN LAI TRONG BF</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-8</td><td class="p-0.5 font-bold">Sinh viên</td><td class="p-0.5">Bấm in hoặc tải biên lai điện tử về máy và hoàn tất thủ tục nhận phòng.</td><td class="p-0.5 text-emerald-700 font-bold">[End of Use Case: Thành công]</td></tr>
                    </tbody>
                </table>
            </div>

            <!-- UC-08 -->
            <div>
                <div class="flex items-center justify-between pb-1 mb-1">
                    <span class="text-[9.5px] font-mono font-bold px-2 py-0.5 rounded bg-blue-100 text-blue-800 border border-blue-300">
                        UC-08: THỦ TỤC TRẢ PHÒNG & QUYẾT TOÁN CỌC (CHECK-OUT - VÒNG ĐỜI CHUẨN)
                    </span>
                </div>
                <table class="w-full text-[8px] border-collapse border border-slate-200">
                    <tbody class="divide-y divide-slate-200">
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700 w-10">BF-1</td><td class="p-0.5 font-bold w-20">Sinh viên</td><td class="p-0.5">Gửi yêu cầu trả phòng và đăng ký lịch kiểm kê bàn giao cơ sở vật chất.</td><td class="p-0.5 w-40 text-slate-500 italic">Trigger</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-2</td><td class="p-0.5 font-bold">Cán bộ KTX</td><td class="p-0.5">Đến phòng kiểm kê tài sản (giường, tủ, khóa), chốt chỉ số điện nước và nhập vào hệ thống.</td><td class="p-0.5 text-slate-500 italic">Actor: Cán bộ KTX kiểm kê</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-3</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Tính toán công nợ dịch vụ và chi phí bồi thường hư hại tài sản (nếu có phát sinh vi phạm).</td><td class="p-0.5 text-slate-500 italic">Tính toán nợ phát sinh</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-4</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Áp dụng quy tắc tài chính BR-07: Tiền hoàn = 2.000.000đ cọc − (Nợ dịch vụ + Phí hư hại).</td><td class="p-0.5 text-slate-500 italic">BR-07. Rẽ EF-A: Nợ > 2tr.</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-5</td><td class="p-0.5 font-bold">Sinh viên</td><td class="p-0.5">Kiểm tra bảng kê số liệu, bàn giao thẻ/chìa khóa phòng và ký biên bản thanh lý điện tử.</td><td class="p-0.5 text-slate-500 italic">Bàn giao vật lý</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-6</td><td class="p-0.5 font-bold">Cán bộ KTX</td><td class="p-0.5">Nhấn nút 'Xác nhận hoàn tất bàn giao phòng' trên ứng dụng quản trị KTX.</td><td class="p-0.5 text-slate-500 italic">Duyệt bàn giao</td></tr>
                        <tr class="bg-indigo-50"><td class="p-0.5 font-mono font-bold text-indigo-700">BF-7</td><td class="p-0.5 font-bold text-indigo-900">Hệ thống</td><td class="p-0.5 font-bold text-indigo-900">Cập nhật hợp đồng 'Closed', giải phóng giường phòng về trạng thái 'Vacant' (Trống khả dụng).</td><td class="p-0.5 text-indigo-700 font-bold">Giải phóng giường phòng</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-8</td><td class="p-0.5 font-bold">Kế toán</td><td class="p-0.5">Duyệt lệnh hoàn cọc trên hệ thống; cổng thanh toán tự động chuyển tiền cọc thừa về tài khoản sinh viên.</td><td class="p-0.5 text-slate-500 italic">Actor: Kế toán hoàn cọc</td></tr>
                        <tr><td class="p-0.5 font-mono font-bold text-teal-700">BF-9</td><td class="p-0.5 font-bold">Hệ thống</td><td class="p-0.5">Gửi email thông báo thanh lý hợp đồng thành công kèm biên lai hoàn tiền cho sinh viên.</td><td class="p-0.5 text-emerald-700 font-bold">[End of Use Case: Thành công]</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 03 / 03 - Đặc tả Thanh toán & Trả phòng</span>
        </div>
    </div>

</body>
</html>
"""

# -------------------------------------------------------------
# 3. HTML CHO DIAGRAM & SEQUENCE RIÊNG
# -------------------------------------------------------------
HTML_DIAGRAM = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Biểu đồ Use Case & Sequence Diagrams - KTX Smart Match</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #1e293b; }
        .page { width: 210mm; min-height: 297mm; padding: 14mm 16mm; margin: 20px auto; background: #fff; box-shadow: 0 10px 25px rgba(0,0,0,0.3); page-break-after: always; }
        @media print { body { background: transparent; padding: 0; } .page { width: 100%; min-height: 100vh; margin: 0; padding: 12mm 14mm; box-shadow: none; page-break-after: always; } }
    </style>
</head>
<body class="py-6">

    <!-- Trang 1: Sơ đồ Use Case tổng thể vẽ lại & Sequence Diagram 1 -->
    <div class="page flex flex-col justify-between">
        <div>
            <div class="border-b-2 border-indigo-900 pb-2 mb-3 flex justify-between items-start">
                <div>
                    <div class="text-[11px] font-extrabold uppercase tracking-wider text-indigo-950">Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng</div>
                    <div class="text-[10px] font-bold text-slate-500 uppercase tracking-wide">Khoa Công nghệ Thông tin & Trí tuệ Nhân tạo • System Engineering</div>
                </div>
                <div class="text-right">
                    <span class="text-[10px] font-mono font-bold bg-purple-50 text-purple-700 border border-purple-200 px-2 py-0.5 rounded">DIAGRAM SPECIFICATION</span>
                </div>
            </div>

            <div class="text-center my-2">
                <span class="text-[10px] font-mono font-extrabold px-3 py-1 rounded-full bg-slate-100 text-slate-800 border border-slate-300 uppercase tracking-widest">TÀI LIỆU BIỂU ĐỒ RIÊNG BIỆT</span>
                <h1 class="text-xl font-black text-slate-900 mt-1.5 mb-1 tracking-tight uppercase">Sơ Đồ Use Case & Sequence Diagram Chuẩn Vòng Đời</h1>
                <p class="text-xs italic text-slate-600">Chuẩn hóa thanh kích hoạt vòng đời (Activation Bars) & Khớp 1-1 với Bảng đặc tả</p>
            </div>

            <!-- Sequence Diagram UC-05 Matching by Request -->
            <div class="mb-2">
                <h2 class="text-xs font-black text-slate-900 uppercase mb-1 flex items-center gap-1.5">
                    <span>📐</span> Sequence Diagram: Ghép bạn cùng phòng theo yêu cầu (UC-05: Matching by Request)
                </h2>
                <p class="text-[9.5px] text-slate-500 italic mb-1.5">
                    Phân định 2 tác nhân con người SV A và SV B; thanh kích hoạt (Activation Bars) mở khi nhận thông điệp và đóng khi trả kết quả (deactivate).
                </p>
                <div class="bg-slate-50 border border-slate-200 rounded-lg p-2">
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

    MatchSvc->>SVB: 7. (BF-3) Đẩy thông báo Push: "Bạn có lời mời ghép phòng từ SV A"
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
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 01 / 02 - Sequence Diagram UC-05</span>
        </div>
    </div>

    <!-- Trang 2: Sequence Diagrams UC-07 Thanh toán & UC-08 Trả phòng -->
    <div class="page flex flex-col justify-between">
        <div>
            <!-- Sequence Diagram UC-07 -->
            <div class="border-b border-slate-200 pb-2 mb-2">
                <h2 class="text-xs font-black text-slate-900 uppercase mb-0.5 flex items-center gap-1.5">
                    <span>💳</span> Sequence Diagram: Thanh toán viện phí & Tạo/In biên lai trực tiếp (UC-07)
                </h2>
                <div class="bg-slate-50 border border-slate-200 rounded-lg p-1.5">
                    <div class="mermaid text-xs">
sequenceDiagram
    autonumber
    actor SV as 🧑 Sinh viên
    participant UI as 🖥️ Màn hình Thanh toán
    participant PaySvc as 💳 Payment Service
    participant VNPay as 🏦 Cổng VNPay
    participant DB as 🗄️ Database KTX

    SV->>UI: 1. (BF-1) Mở màn hình thanh toán tiền phòng & cọc 72h
    activate UI
    UI->>PaySvc: 2. (BF-2) Lấy bảng kê viện phí & đồng hồ đếm ngược 72h (BR-04)
    activate PaySvc
    PaySvc-->>UI: 3. (BF-2) Trả về bảng kê chi tiết (Tiền phòng + Cọc 2tr)
    deactivate PaySvc

    SV->>UI: 4. (BF-3) Xác nhận thanh toán qua VNPAY-QR
    UI->>PaySvc: 5. (BF-4) Khởi tạo phiên giao dịch bảo mật (TLS 1.3)
    activate PaySvc
    PaySvc->>VNPay: 6. (BF-4) Tạo đơn hàng thanh toán & yêu cầu mã QR
    activate VNPay
    VNPay-->>UI: 7. (BF-4) Hiển thị mã VNPAY-QR động trên màn hình
    deactivate VNPay
    deactivate PaySvc

    SV->>VNPay: 8. (BF-5) Quét mã QR trên App Mobile Banking & Nhập OTP trừ tiền
    activate VNPay
    VNPay-->>PaySvc: 9. (BF-5) Gửi webhook callback thanh toán thành công (vnp_ResponseCode = 00)
    deactivate VNPay
    activate PaySvc
    
    PaySvc->>DB: 10. (BF-6) Cập nhật trạng thái hợp đồng thành "Paid" & Khóa giường
    activate DB
    DB-->>PaySvc: 11. (BF-6) Xác nhận khóa chỗ thành công
    deactivate DB

    Note over PaySvc, UI: TẠO VÀ IN BIÊN LAI ĐIỆN TỬ TRỰC TIẾP TRONG LUỒNG CHÍNH (BF-7)
    PaySvc->>PaySvc: 12. (BF-7) Sinh mã hóa đơn điện tử & Tạo file PDF Biên lai thu tiền
    PaySvc-->>UI: 13. (BF-7) Trả về dữ liệu biên lai kèm nút "In biên lai" / "Tải PDF"
    deactivate PaySvc

    UI-->>SV: 14. (BF-8) Hiển thị thông báo nhận phòng thành công & cho phép In/Tải biên lai
    deactivate UI
                    </div>
                </div>
            </div>

            <!-- Sequence Diagram UC-08 -->
            <div>
                <h2 class="text-xs font-black text-slate-900 uppercase mb-0.5 flex items-center gap-1.5">
                    <span>🚪</span> Sequence Diagram: Thủ tục Trả phòng & Quyết toán cọc Check-out (UC-08)
                </h2>
                <div class="bg-slate-50 border border-slate-200 rounded-lg p-1.5">
                    <div class="mermaid text-xs">
sequenceDiagram
    autonumber
    actor SV as 🧑 Sinh viên
    actor Staff as 👨‍💼 Cán bộ KTX
    participant UI as 🖥️ Cổng Quản trị / App KTX
    participant CheckOutSvc as 📋 Check-out Service
    participant DB as 🗄️ Database KTX
    actor Fin as 👩‍💼 Kế toán KTX

    SV->>UI: 1. (BF-1) Đăng ký lịch kiểm kê trả phòng trên cổng dịch vụ
    activate UI
    UI->>DB: 2. (BF-1) Lưu lịch hẹn kiểm tra phòng
    deactivate UI

    Staff->>UI: 3. (BF-2) Kiểm kê hiện trạng tài sản, nhập chỉ số điện nước & chi phí hư hại
    activate UI
    UI->>CheckOutSvc: 4. (BF-3, BF-4) Tính toán công nợ & Quyết toán hoàn cọc (Ref: BR-07)
    activate CheckOutSvc
    CheckOutSvc->>CheckOutSvc: 5. (BF-4) Tiền cọc hoàn = 2.000.000đ - (Nợ dịch vụ + Phí hư hại)
    CheckOutSvc-->>UI: 6. (BF-5) Xuất bảng kê thanh lý hợp đồng điện tử
    deactivate CheckOutSvc

    UI-->>SV: 7. (BF-5) Hiển thị bảng kê số liệu quyết toán cọc
    deactivate UI

    SV->>Staff: 8. (BF-6) Bàn giao chìa khóa/thẻ từ phòng & Ký xác nhận thanh lý
    Staff->>UI: 9. (BF-7) Nhấn "Xác nhận hoàn tất bàn giao phòng"
    activate UI
    UI->>DB: 10. (BF-8) Cập nhật hợp đồng "Closed" & Chuyển trạng thái giường thành "Vacant" (Trống)
    activate DB
    DB-->>UI: 11. (BF-8) Xác nhận giải phóng phòng thành công
    deactivate DB
    deactivate UI

    Fin->>UI: 12. (BF-9) Duyệt lệnh chuyển tiền hoàn cọc về tài khoản ngân hàng của sinh viên
    activate UI
    UI-->>SV: 13. (BF-10) Gửi thông báo & email biên lai hoàn tiền cọc thành công
    deactivate UI
                    </div>
                </div>
            </div>
        </div>
        <div class="border-t border-slate-200 pt-1.5 flex justify-between items-center text-[9px] text-slate-400 font-mono">
            <span>Dự án KTX Smart Match • Viện VNUK</span>
            <span>Trang 02 / 02 - Sequence Diagram UC-07 & UC-08</span>
        </div>
    </div>

</body>
</html>
"""

def export_pdfs():
    tasks = [
        ("ui/br_export_single.html", HTML_BR, "docs/BR_KTX_Smart_Match_VNUK.pdf", r"C:\Users\LENOVO\Downloads\BR_KTX_Smart_Match_VNUK.pdf"),
        ("ui/spec_export_single.html", HTML_SPEC, "docs/Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.pdf", r"C:\Users\LENOVO\Downloads\Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.pdf"),
        ("ui/diagram_export_single.html", HTML_DIAGRAM, "docs/Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.pdf", r"C:\Users\LENOVO\Downloads\Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.pdf")
    ]

    for html_rel, content, pdf_rel, dl_target in tasks:
        html_path = os.path.join(BASE_DIR, html_rel)
        pdf_path = os.path.join(BASE_DIR, pdf_rel)
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created {html_path}")

        cmd = [
            EDGE_EXE,
            "--headless",
            "--disable-gpu",
            "--run-all-compositor-stages-before-draw",
            "--print-to-pdf-no-header",
            f"--print-to-pdf={pdf_path}",
            html_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(pdf_path):
            shutil.copy2(pdf_path, dl_target)
            print(f"[SUCCESS] Exported {pdf_rel} -> {dl_target}")
        else:
            print(f"[ERROR] Failed {pdf_rel}: {res.stderr}")

if __name__ == "__main__":
    export_pdfs()
