# -*- coding: utf-8 -*-
"""
build_revised_spec_master.py
Biên soạn tài liệu Đặc tả Use Case và Business Rules chuẩn hóa:
- Tiếp thu 100% Feedback ngày 24/10 của Giảng viên hướng dẫn
- Tham khảo chuẩn mực kiến trúc và quy ước của Nhóm 2 (Slide p110, p125)
- Định dạng chuẩn 3 cột cho Business Rules (Rule ID | Name | Description)
- Tinh gọn Use Case Catalog từ 43 use case rời rạc thành danh mục chuẩn
- Đặc tả chi tiết matching theo request (SV A -> Hệ thống -> SV B)
- Quy trình Trả phòng chuẩn hóa (Kiểm kê -> Khấu trừ -> Hoàn cọc -> Giải phóng giường)
- Thanh toán tích hợp tạo và in biên lai trong luồng chính, AF là luồng rẽ nhánh chuẩn
- Đảm bảo "đặc tả hết bước" và thể hiện đúng thanh vòng đời (lifeline activation bars)
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import shutil
import subprocess

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = OxmlElement(tag)
            element.set(qn('w:val'), edge_data.get('val', 'single'))
            element.set(qn('w:sz'), str(edge_data.get('sz', 4)))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), edge_data.get('color', 'E2E8F0'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def add_styled_p(doc, text="", style='Normal', space_before=0, space_after=4, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph(text, style=style)
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    return p

def add_h1(doc, text):
    p = add_styled_p(doc, space_before=16, space_after=6)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Slate 900
    return p

def add_h2(doc, text):
    p = add_styled_p(doc, space_before=12, space_after=4)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A) # Blue 900
    return p

def add_h3(doc, text):
    p = add_styled_p(doc, space_before=8, space_after=3)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55) # Slate 700
    return p

def add_body(doc, text, bold=False, italic=False, color_rgb=(0x33, 0x41, 0x55)):
    p = add_styled_p(doc, space_before=0, space_after=4, line_spacing=1.15)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor(*color_rgb)
    return p

def build_docx():
    doc = docx.Document()
    
    # Page setup: A4 Normal Margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    # Header School
    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r_inst = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(10)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=4)
    r_title = p_title.add_run("TÀI LIỆU ĐẶC TẢ USE CASE & QUY TẮC NGHIỆP VỤ\n(USE CASE SPECIFICATION & BUSINESS RULES BASELINE)")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    r_sub = p_sub.add_run("Hệ thống: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nBản cập nhật tiếp thu toàn diện Feedback ngày 24/10 & Chuẩn hóa theo tài liệu đối sánh Nhóm 2")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(10)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Info table
    tbl_info = doc.add_table(rows=4, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Học phần:", "System Engineering / Phân tích & Thiết kế Hệ thống"),
        ("Nhóm sinh viên:", "Nhóm 3: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều (Lớp Kỹ thuật Phần mềm VNUK)"),
        ("Căn cứ hiệu chỉnh:", "Feedback trực tiếp ngày 24/10 từ Giảng viên hướng dẫn + Template chuẩn Slide p110, p125"),
        ("Phiên bản cập nhật:", "Version 4.0 - Chuẩn hóa BR, Tinh gọn Use Case, Sửa luồng Matching Request & Trả phòng")
    ]
    for idx, (label, val) in enumerate(info_data):
        row = tbl_info.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.0), Inches(4.5)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 50, 50, 80, 80)
        set_cell_margins(c1, 50, 50, 80, 80)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9.5), True
        r0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(9.5)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=8)

    # ==================== PHẦN 1: BẢNG TIẾP THU FEEDBACK ====================
    add_h1(doc, "1. BẢNG TIẾP THU VÀ ĐỐI CHIẾU SỬA ĐỔI THEO FEEDBACK 24/10")
    add_body(doc, "Dưới đây là bảng giải trình chi tiết từng nội dung mà Giảng viên hướng dẫn đã góp ý trong buổi thông qua ngày 24/10, kèm theo giải pháp chuẩn hóa tương ứng được áp dụng trong tài liệu này:")

    fb_items = [
        ("1. 'lựa chọn tên đăng nhập. tên - mật khẩu là 1 chức năng'",
         "Tích hợp chức năng Đăng nhập cho phép người dùng lựa chọn linh hoạt giữa Tên đăng nhập / Email trường cấp (@vnuk.edu.vn) hoặc MSSV kết hợp với Mật khẩu cá nhân, đóng gói thành 1 Use Case chuẩn (UC-01: Đăng nhập & Xác thực)."),
        ("2. 'dky tài khoản: khai báo thông tin là 1 use case'",
         "Hợp nhất việc tạo tài khoản sinh viên với bước khai báo thông tin nhân thân và hồ sơ nếp sống sinh hoạt thành một tiến trình hoàn chỉnh trong 1 Use Case duy nhất (UC-02: Đăng ký tài khoản & Khai báo thông tin)."),
        ("3. 'ko cần phải liệt kê hết'",
         "Tinh giản toàn diện hệ thống từ 43 use case bị phân mảnh (nhiều use case con thực chất chỉ là 1 nút bấm hoặc hàm tính toán nội bộ) xuống còn danh mục Use Case trọng tâm, đúng bản chất chức năng nghiệp vụ hướng người dùng."),
        ("4. 'cần đánh mạnh vào việc matching giữa các bạn, giữa các phòng' & 'match theo kiểu request: 1 bên bấm request, bên kia nhận thông báo, thông tin, đồng ý thì match'",
         "Xây dựng trọng tâm Use Case Matching hai chiều: Sinh viên A xem thông tin hòa hợp nếp sống và gửi Matching Request -> Hệ thống chuyển thông báo đến Sinh viên B -> Sinh viên B xem profile và quyết định Đồng ý hoặc Từ chối -> Xác nhận tạo cặp ghép thành công."),
        ("5. '1 bên gởi bên kia nhận/phản hồi, là 2 người khác nhau ko đặc tả ... cái đc'",
         "Đặc tả phân định tường minh 2 tác nhân con người độc lập: 'Sinh viên gửi (SV A)' và 'Sinh viên nhận (SV B)', đảm bảo tính bất đồng bộ và phản ánh đúng luồng tương tác thực tế giữa 2 người dùng khác nhau."),
        ("6. 'trả phòng làm sai'",
         "Tách biệt hoàn toàn thủ tục Trả phòng (Check-out) khỏi Gia hạn; chuẩn hóa đầy đủ vòng đời: Sinh viên yêu cầu -> Cán bộ KTX kiểm kê tài sản -> Hệ thống tính toán khấu trừ và hoàn cọc (BR-07) -> Kế toán hoàn tiền -> Bàn giao và giải phóng giường."),
        ("7. 'trong chức năng thanh toán, có thêm chức năng tạo/in biên lai... Còn AF là luồng thay thế khi các bước gặp vấn đề'",
         "Đưa bước 'Tạo và In/Tải biên lai điện tử' vào trực tiếp Luồng cơ bản (Basic Flow) của chức năng Thanh toán tiền phòng & đặt cọc; AF chỉ dành cho các kịch bản rẽ nhánh nghiệp vụ (như chọn phương thức thanh toán thay thế)."),
        ("8. 'đặc tả lúc nào cũng phải hết bước, đặc tả sai -> vẽ sai' & 'thanh thể hiện vòng đời'",
         "Mọi bước trong Basic Flow đều có kết thúc tường minh [End of Use Case: mục tiêu đã đạt]; các luồng AF/EF đều có điểm rẽ nhánh (Branch point), điều kiện (Condition) và điểm kết thúc/quay lại (Outcome) xác định; thể hiện đúng thanh vòng đời (activation bars)."),
        ("9. 'mỗi sv có 1 mã sv duy nhất'",
         "Bổ sung quy tắc nghiệp vụ định danh BR-01: Mỗi sinh viên có duy nhất 1 Mã số sinh viên (MSSV) không trùng lặp, dùng làm khóa chính định danh xuyên suốt hệ thống."),
        ("10. 'br sai format'",
         "Chuyển toàn bộ Business Rules sang cấu trúc chuẩn 3 cột theo Slide p125 & Nhóm 2: Rule ID | Name | Description. Diễn đạt đúng bản chất ràng buộc/luật nghiệp vụ, không viết dạng chức năng phần mềm.")
    ]

    tbl_fb = doc.add_table(rows=len(fb_items)+1, cols=2)
    tbl_fb.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_fb.rows[0].cells[0].width = Inches(2.3)
    tbl_fb.rows[0].cells[1].width = Inches(4.2)
    set_cell_background(tbl_fb.rows[0].cells[0], "1E3A8A")
    set_cell_background(tbl_fb.rows[0].cells[1], "1E3A8A")
    set_cell_margins(tbl_fb.rows[0].cells[0], 60, 60, 80, 80)
    set_cell_margins(tbl_fb.rows[0].cells[1], 60, 60, 80, 80)
    
    r00 = tbl_fb.rows[0].cells[0].paragraphs[0].add_run("Ý kiến Feedback của Thầy (24/10)")
    r00.font.name, r00.font.size, r00.font.bold = 'Times New Roman', Pt(9.5), True
    r00.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    r01 = tbl_fb.rows[0].cells[1].paragraphs[0].add_run("Giải pháp Tiếp thu & Chuẩn hóa trong Tài liệu v4.0")
    r01.font.name, r01.font.size, r01.font.bold = 'Times New Roman', Pt(9.5), True
    r01.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (f_txt, sol_txt) in enumerate(fb_items):
        row = tbl_fb.rows[i+1]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.3), Inches(4.2)
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for c in (c0, c1):
            set_cell_background(c, bg)
            set_cell_margins(c, 50, 50, 80, 80)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(f_txt)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9), True
        r0.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(sol_txt)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(9)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=8)

    # ==================== PHẦN 2: BUSINESS RULES (CHUẨN SLIDE P125) ====================
    add_h1(doc, "2. HỆ THỐNG QUY TẮC NGHIỆP VỤ (BUSINESS RULES - CHUẨN FORMAT SLIDE P125)")
    add_body(doc, "Quy ước chuẩn mực (Slide System Engineering p125 & Nhóm 2): Business Rule là các RÀNG BUỘC NGHIỆP VỤ, ĐIỀU KIỆN TIÊN QUYẾT hoặc CHÍNH SÁCH QUY ĐỊNH của Ký túc xá, không phải là Business Requirement hay các bước thao tác trong Use Case.")
    add_body(doc, "Format chuẩn gồm 3 cột: Rule ID | Name | Description:")

    br_list = [
        ("BR-01", "Mã số sinh viên duy nhất & Thuộc đối tượng tiếp nhận",
         "Mỗi sinh viên có duy nhất một Mã số sinh viên (MSSV) không trùng lặp trong toàn bộ hệ thống, đóng vai trò khóa chính định danh tài khoản. KTX chỉ tiếp nhận sinh viên chính quy thuộc khối liên kết VNUK có trạng thái đào tạo hợp lệ và sử dụng email trường cấp (@vnuk.edu.vn). Người ngoài hoặc tài khoản không hợp lệ bị từ chối đăng ký."),
        ("BR-02", "Cam kết thời hạn lưu trú tối thiểu 01 học kỳ",
         "Mỗi hồ sơ đăng ký KTX bắt buộc phải có cam kết thời hạn cư trú tối thiểu 01 học kỳ (05 tháng) hoặc trọn năm học (10 tháng). Hệ thống kiên quyết không thụ lý hợp đồng ngắn hạn theo ngày/tuần nhằm bảo toàn nếp sống văn hóa ổn định và kế hoạch vận hành của KTX."),
        ("BR-03", "Phê duyệt nghiệp vụ bắt buộc (Business Approve)",
         "Mọi hồ sơ đăng ký phòng của sinh viên sau khi nộp trực tuyến phải trải qua bước thẩm định và phê duyệt nghiệp vụ của Cán bộ KTX (kiểm tra kỷ luật, lịch sử công nợ, đối soát chính sách ưu tiên) trước khi được đưa vào hàng đợi chạy thuật toán phân bổ phòng."),
        ("BR-04", "Đặt cọc giữ chỗ và thời hạn thanh toán 72 giờ",
         "Trong vòng chính xác 72 giờ kể từ thời điểm công bố kết quả phân phòng, sinh viên phải hoàn tất thanh toán tiền phòng kỳ 1 kèm tiền đặt cọc tài sản (2.000.000 VNĐ) qua cổng VNPay. Quá thời hạn 72 giờ không thanh toán, hệ thống tự động hủy kết quả giữ chỗ và chuyển suất cho sinh viên trong danh sách chờ (Waitlist)."),
        ("BR-05", "Ghép bạn cùng phòng theo cơ chế Request hai chiều",
         "Việc ghép bạn cùng phòng giữa hai cá nhân bắt buộc phải dựa trên sự đồng thuận tự nguyện của cả hai bên: Một bên gửi yêu cầu (Matching Request), bên còn lại phải nhận thông tin, xem xét hồ sơ nếp sống và chủ động bấm 'Đồng ý' thì quan hệ ghép cặp mới được xác lập hợp lệ."),
        ("BR-06", "Tối ưu hóa tỷ lệ lấp đầy phòng (Occupancy Rate)",
         "Thuật toán phân bổ phòng ưu tiên lấp đầy 100% số giường của từng phòng (2, 4, 6 người) trước khi mở phòng mới nhằm tối ưu hóa chi phí điện nước chung, khấu hao điều hòa và bảo toàn biên lợi nhuận vận hành cho KTX."),
        ("BR-07", "Quy tắc quyết toán và hoàn cọc khi trả phòng",
         "Khi làm thủ tục trả phòng (Check-out), tiền đặt cọc chỉ được hoàn trả sau khi Cán bộ KTX nghiệm thu hiện trạng cơ sở vật chất. Số tiền cọc hoàn lại = 2.000.000đ − (Công nợ dịch vụ phát sinh + Chi phí bồi thường hư hỏng tài sản nếu có). Nếu sinh viên đơn phương phá vỡ hợp đồng trước 1 kỳ, tiền cọc không được hoàn lại."),
        ("BR-08", "Ràng buộc yêu cầu đổi phòng / đổi bạn",
         "Mỗi sinh viên chỉ được phép có tối đa 01 yêu cầu đổi phòng đang trong trạng thái xử lý; yêu cầu bắt buộc phải có lý do cụ thể và chỉ được Cán bộ KTX phê duyệt khi phòng đích còn chỗ trống khả dụng và phù hợp về giới tính, loại phòng."),
        ("BR-09", "Tính điểm tương thích hai chiều và trọng số ưu tiên 1.5x",
         "Điểm hòa hợp nếp sống giữa hai sinh viên được tính toán trên vector 8 tiêu chí thói quen; tiêu chí mà mỗi sinh viên đánh dấu là quan trọng nhất (Top Criterion) sẽ được nhân hệ số trọng số 1.5x khi tính toán ma trận tương thích hai chiều bất đối xứng.")
    ]

    tbl_br = doc.add_table(rows=len(br_list)+1, cols=3)
    tbl_br.alignment = WD_TABLE_ALIGNMENT.CENTER
    br_w = [Inches(1.0), Inches(2.2), Inches(3.4)]
    for j, h in enumerate(["Rule ID", "Name", "Description"]):
        c = tbl_br.rows[0].cells[j]
        c.width = br_w[j]
        set_cell_background(c, "0F172A")
        set_cell_margins(c, 60, 60, 80, 80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9.5), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (rid, rname, rdesc) in enumerate(br_list):
        row = tbl_br.rows[i+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = br_w[0], br_w[1], br_w[2]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, 50, 50, 80, 80)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(rid)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9), True
        r0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(rname)
        r1.font.name, r1.font.size, r1.font.bold = 'Times New Roman', Pt(9), True
        r1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(rdesc)
        r2.font.name, r2.font.size = 'Times New Roman', Pt(9)
        r2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=8)

    # ==================== PHẦN 3: USE CASE CATALOG TINH GỌN ====================
    add_h1(doc, "3. DANH MỤC USE CASE TINH GỌN & CHUẨN HÓA (USE CASE CATALOG)")
    add_body(doc, "Tiếp thu trực tiếp nhận xét 'ko cần phải liệt kê hết', hệ thống được tinh giản từ 43 use case bị phân mảnh xuống còn danh mục Use Case nghiệp vụ cốt lõi, loại bỏ hoàn toàn các micro-actions và phân định rõ ràng vai trò của từng tác nhân:")

    uc_catalog = [
        ("UC-01", "Đăng nhập & Xác thực hệ thống", "Sinh viên, Cán bộ KTX", "Hỗ trợ đăng nhập bằng tên/email hoặc MSSV + Mật khẩu, lưu phiên JWT và khôi phục mật khẩu.", "BR-01, NFR-01"),
        ("UC-02", "Đăng ký tài khoản & Khai báo thông tin/thói quen", "Sinh viên", "Đăng ký tài khoản bằng MSSV duy nhất và khai báo hồ sơ nếp sống sinh hoạt 8 tiêu chí.", "BR-01, BR-09"),
        ("UC-03", "Cập nhật hồ sơ & nếp sống sinh hoạt", "Sinh viên", "Chỉnh sửa thông tin cá nhân và 8 thói quen; hỗ trợ nạp Persona mẫu khi chưa chốt đợt ghép.", "BR-09, NFR-05"),
        ("UC-04", "Chọn loại phòng & Nộp đơn đăng ký KTX", "Sinh viên", "Chọn loại phòng (2/4/6), tiện ích, ký cam kết ở tối thiểu 1 kỳ và nộp hồ sơ chờ duyệt.", "BR-02, BR-06"),
        ("UC-05", "Ghép bạn cùng phòng theo yêu cầu (Matching by Request)", "Sinh viên gửi (SV A), Sinh viên nhận (SV B)", "SV A gửi Matching Request -> SV B nhận thông báo, xem profile và chọn Đồng ý/Từ chối.", "BR-05, BR-09"),
        ("UC-06", "Xem kết quả phân phòng & thông tin phòng ở", "Sinh viên", "Tra cứu phòng được phân, danh sách bạn cùng phòng, viện phí và hạn chót thanh toán 72h.", "BR-04, BR-06"),
        ("UC-07", "Thanh toán tiền phòng & Đặt cọc giữ chỗ 72h", "Sinh viên, Cổng VNPay", "Thanh toán viện phí và cọc 2tr qua VNPay; hệ thống tự động tạo và in/tải biên lai điện tử.", "BR-04, NFR-04"),
        ("UC-08", "Thủ tục Trả phòng & Quyết toán KTX (Check-out)", "Sinh viên, Cán bộ KTX, Kế toán", "Quy trình trả phòng: Kiểm kê tài sản -> Khấu trừ hư hại -> Hoàn trả cọc -> Giải phóng chỗ.", "BR-07, NFR-06"),
        ("UC-09", "Yêu cầu chuyển phòng / chuyển bạn cùng phòng", "Sinh viên, Cán bộ KTX", "Gửi yêu cầu đổi phòng kèm lý do/minh chứng khi có xung đột nếp sống phát sinh.", "BR-08, NFR-05"),
        ("UC-10", "Gửi phản ánh dịch vụ & Báo hỏng cơ sở vật chất", "Sinh viên, Kỹ thuật", "Khai báo sự cố điện nước, thiết bị hư hỏng trong phòng và theo dõi tiến độ sửa chữa.", "NFR-05, NFR-08"),
        ("UC-11", "Quản lý danh mục tòa, phòng & bảng giá", "Quản trị viên (Admin)", "Thêm, cập nhật, cấu hình danh mục tòa nhà, phòng ở, định mức giá và chỉ tiêu tiếp nhận.", "BR-06, NFR-06"),
        ("UC-12", "Thẩm định & Phê duyệt đơn KTX (Business Approve)", "Cán bộ quản lý KTX", "Kiểm tra điều kiện lưu trú, xét duyệt hồ sơ hợp lệ để đưa vào thuật toán phân phòng.", "BR-01, BR-02, BR-03"),
        ("UC-13", "Khởi chạy Phân bổ phòng tự động & Tối ưu lấp đầy", "Hệ thống (Scheduler), Admin", "Chạy thuật toán Gale-Shapley kết hợp lấp đầy 100% giường, triệt tiêu cặp chặn BP=0.", "BR-04, BR-06, BR-09"),
        ("UC-14", "Theo dõi, đối soát thanh toán & Hoàn cọc", "Kế toán, Cổng VNPay", "Quản lý dòng tiền thu cọc/viện phí, đối soát tự động với VNPay và thực thi lệnh hoàn cọc.", "BR-04, BR-07, NFR-04"),
        ("UC-15", "Tự động hủy đơn quá 72h & Xếp phòng danh sách chờ", "Hệ thống (Scheduler)", "Quét định kỳ các đơn quá hạn thanh toán 72h, tự động thu hồi phòng và phân bổ cho Waitlist.", "BR-04, BR-06"),
        ("UC-16", "Báo cáo doanh thu, chi phí & Công suất phòng KTX", "Kế toán, Ban Giám hiệu", "Xuất báo cáo thống kê tỷ lệ lấp đầy, doanh thu viện phí, công nợ và hiệu quả vận hành.", "BR-06, NFR-03")
    ]

    tbl_cat = doc.add_table(rows=len(uc_catalog)+1, cols=5)
    tbl_cat.alignment = WD_TABLE_ALIGNMENT.CENTER
    cat_w = [Inches(0.8), Inches(2.0), Inches(1.5), Inches(1.6), Inches(0.8)]
    for j, h in enumerate(["Mã UC", "Tên Use Case (Verb + Noun)", "Tác nhân chính", "Phạm vi chức năng cốt lõi", "Ref BR"]):
        c = tbl_cat.rows[0].cells[j]
        c.width = cat_w[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 60, 60, 60, 60)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 4) else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (ucid, ucname, ucact, ucdesc, ucbr) in enumerate(uc_catalog):
        row = tbl_cat.rows[i+1]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for j, val in enumerate([ucid, ucname, ucact, ucdesc, ucbr]):
            c = row.cells[j]
            c.width = cat_w[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 40, 40, 60, 60)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 4) else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name, r.font.size = 'Times New Roman', Pt(8.5)
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
            elif j == 1:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
            else:
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=8)

    # ==================== PHẦN 4: ĐẶC TẢ CHI TIẾT CÁC USE CASE TRỌNG TÂM ====================
    add_h1(doc, "4. ĐẶC TẢ CHI TIẾT CÁC USE CASE TRỌNG TÂM (CHUẨN SLIDE P110 & NHÓM 2)")
    add_body(doc, "Dưới đây là nội dung đặc tả chi tiết các Use Case quan trọng nhất, được viết lại hoàn toàn nhằm sửa chữa các điểm sai vòng đời, bổ sung đủ bước kết thúc và phân định rõ ràng tác nhân theo đúng nhận xét của Giảng viên:")

    # Detailed Use Cases
    detailed_ucs = [
        {
            "id": "UC-01",
            "title": "Đăng nhập & Xác thực hệ thống (Sign in and Authenticate)",
            "desc": "Cho phép người dùng truy cập vào hệ thống KTX bằng việc lựa chọn đăng nhập linh hoạt giữa Tên đăng nhập / Email trường cấp (@vnuk.edu.vn) hoặc MSSV kết hợp với Mật khẩu cá nhân, hệ thống kiểm tra quyền hạn và cấp phiên làm việc bảo mật (JWT).",
            "actors": "Sinh viên, Cán bộ KTX (Primary Actors); Dịch vụ xác thực trung tâm Trường A (Secondary Actor).",
            "precond": "Người dùng đã có tài khoản hợp lệ trên hệ thống KTX.",
            "postcond": "Phiên làm việc bảo mật được thiết lập, người dùng được chuyển hướng vào giao diện tương ứng theo vai trò.",
            "trigger": "Người dùng mở trang đăng nhập KTX và chọn 'Đăng nhập'.",
            "bf": [
                ("BF-1", "Người dùng", "Truy cập cổng đăng nhập của hệ thống KTX.", "Trigger: Mở màn hình Login"),
                ("BF-2", "Hệ thống", "Hiển thị biểu mẫu đăng nhập với ô nhập danh tính (cho phép nhập MSSV hoặc Email @vnuk.edu.vn) và Mật khẩu.", "Hỗ trợ đăng nhập đa kênh"),
                ("BF-3", "Người dùng", "Nhập thông tin định danh (MSSV hoặc Email) và mật khẩu, nhấn nút 'Đăng nhập'.", "Kiểm tra cú pháp đầu vào"),
                ("BF-4", "Hệ thống", "Kiểm tra tính hợp lệ của tài khoản, đối soát dữ liệu với cơ sở dữ liệu trường và băm mật khẩu để so khớp.", "Rẽ AF-A: Đăng nhập bằng Google SSO. Rẽ EF-A: Sai mật khẩu quá số lần. Rẽ EF-B: Tài khoản không tồn tại."),
                ("BF-5", "Hệ thống", "Khởi tạo phiên làm việc bảo mật (JWT Token), ghi nhật ký đăng nhập và chuyển hướng người dùng vào Dashboard.", "[End of Use Case: mục tiêu đã đạt thành công].")
            ],
            "af": [
                {
                    "name": "AF-A – Đăng nhập nhanh qua Google SSO trường cấp",
                    "point": "BF-2",
                    "cond": "Người dùng chọn phương thức đăng nhập bằng Google Workspace VNUK",
                    "steps": [
                        ("AF-A-1", "Người dùng", "Nhấn nút 'Đăng nhập với Google (@vnuk.edu.vn)'.", "Chuyển hướng OAuth 2.0"),
                        ("AF-A-2", "Hệ thống", "Chuyển hướng sang trang xác thực Google và nhận mã ủy quyền hợp lệ.", "Kiểm tra tên miền @vnuk.edu.vn"),
                        ("AF-A-3", "Hệ thống", "Đối khớp email trường với hồ sơ sinh viên, cấp token và đưa vào Dashboard.", "Quay lại BF-5; [Outcome: kind: return, stepId: BF-5]")
                    ]
                },
                {
                    "name": "AF-B – Quên mật khẩu và khôi phục trực tuyến",
                    "point": "BF-2",
                    "cond": "Người dùng không nhớ mật khẩu đăng nhập",
                    "steps": [
                        ("AF-B-1", "Người dùng", "Chọn 'Quên mật khẩu' và nhập email trường cấp.", "Yêu cầu khôi phục"),
                        ("AF-B-2", "Hệ thống", "Kiểm tra email, sinh mã OTP xác thực có hạn 15 phút và gửi về hộp thư.", "Bảo mật NFR-01"),
                        ("AF-B-3", "Người dùng", "Nhập mã OTP và đặt mật khẩu mới đạt độ phức tạp (BR-01).", "Cập nhật mật khẩu"),
                        ("AF-B-4", "Hệ thống", "Cập nhật mật khẩu đã băm, thông báo thành công và chuyển về trang đăng nhập.", "[Outcome: kind: return, stepId: BF-2]")
                    ]
                }
            ],
            "ef": [
                {
                    "name": "EF-A – Nhập sai mật khẩu quá 5 lần liên tiếp",
                    "point": "BF-4",
                    "cond": "Người dùng nhập sai thông tin xác thực quá số lần quy định",
                    "steps": [
                        ("EF-A-1", "Hệ thống", "Phát hiện sai mật khẩu 5 lần, kích hoạt cơ chế khóa tạm thời tài khoản trong 15 phút.", "Chống Brute-force NFR-01"),
                        ("EF-A-2", "Hệ thống", "Hiển thị thông báo tài khoản bị tạm khóa kèm thời gian mở lại và ghi nhật ký cảnh báo an ninh.", "[End of Use Case: chưa đạt mục tiêu trong lần thực hiện này. Outcome: kind: failureEnd]")
                    ]
                },
                {
                    "name": "EF-B – Tài khoản không thuộc đối tượng tiếp nhận",
                    "point": "BF-4",
                    "cond": "MSSV không tồn tại trong danh sách sinh viên hợp lệ của trường",
                    "steps": [
                        ("EF-B-1", "Hệ thống", "Hiển thị cảnh báo: 'Tài khoản không thuộc diện được tiếp nhận tại KTX theo quy định BR-01'.", "Từ chối truy cập"),
                        ("EF-B-2", "Hệ thống", "Chặn phiên làm việc và hướng dẫn sinh viên liên hệ Phòng Đào tạo.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                    ]
                }
            ],
            "add_info": "Business Rules áp dụng: BR-01 (Mã SV duy nhất & đối tượng hợp lệ). Non-functional: NFR-01 (Bảo mật mật khẩu, JWT), NFR-08 (Thời gian phản hồi < 2s)."
        },
        {
            "id": "UC-05",
            "title": "Ghép bạn cùng phòng theo yêu cầu (Roommate Matching by Request)",
            "desc": "Cho phép hai sinh viên chủ động kết nối để trở thành bạn cùng phòng theo cơ chế Request hai chiều: Sinh viên A gửi yêu cầu ghép đôi, Sinh viên B nhận thông báo, xem hồ sơ thói quen của A và quyết định Đồng ý hoặc Từ chối.",
            "actors": "Sinh viên gửi (SV A - Primary Actor), Sinh viên nhận (SV B - Secondary Actor), Hệ thống KTX (Supporting System).",
            "precond": "Cả SV A và SV B đều đã hoàn thành khảo sát 8 thói quen sinh hoạt và chưa chốt hợp đồng phòng chính thức.",
            "postcond": "Khi B đồng ý: Cặp ghép được xác lập ở trạng thái Matched, sẵn sàng để xếp phòng chung. Khi B từ chối: Yêu cầu bị hủy và A được thông báo.",
            "trigger": "Sinh viên A nhấn nút 'Gửi yêu cầu ghép bạn' trên danh sách gợi ý bạn cùng phòng.",
            "bf": [
                ("BF-1", "Sinh viên A", "Xem danh sách gợi ý mức độ hòa hợp nếp sống và nhấn 'Gửi yêu cầu ghép bạn' tới Sinh viên B.", "Trigger: SV A chủ động request"),
                ("BF-2", "Hệ thống", "Kiểm tra điều kiện nghiệp vụ: Cùng giới tính, cùng loại phòng mong muốn, SV B chưa vào nhóm khác và chưa có request đang chờ giữa hai người.", "Ràng buộc BR-05. Rẽ EF-A: Không đủ điều kiện ghép đôi."),
                ("BF-3", "Hệ thống", "Tạo bản ghi yêu cầu ghép phòng ở trạng thái 'Pending', thiết lập thời hạn phản hồi 48 giờ và gửi thông báo tức thì đến Sinh viên B.", "Tạo thông báo thời gian thực"),
                ("BF-4", "Sinh viên B", "Đăng nhập hệ thống, mở thông báo nhận được và xem chi tiết hồ sơ đối chiếu 8 thói quen của Sinh viên A.", "Actor: Sinh viên B phản hồi. Rẽ AF-A: SV B từ chối yêu cầu."),
                ("BF-5", "Sinh viên B", "Nhấn nút 'Đồng ý kết bạn cùng phòng'.", "Xác nhận đồng thuận hai chiều"),
                ("BF-6", "Hệ thống", "Xác lập liên kết nhóm giữa SV A và SV B, cập nhật trạng thái 'Matched' ưu tiên xếp chung phòng và gửi thông báo chúc mừng tới cả hai sinh viên.", "BR-05: Hoàn tất ghép cặp"),
                ("BF-7", "Hệ thống", "Đóng yêu cầu thành công và cập nhật bảng danh sách bạn cùng phòng của cả hai bên.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                {
                    "name": "AF-A – Sinh viên B từ chối lời mời ghép phòng",
                    "point": "BF-4",
                    "cond": "Sinh viên B sau khi xem xét thấy không phù hợp về thói quen sinh hoạt",
                    "steps": [
                        ("AF-A-1", "Sinh viên B", "Nhấn nút 'Từ chối' kèm lời nhắn lịch sự (tùy chọn).", "B từ chối lời mời"),
                        ("AF-A-2", "Hệ thống", "Cập nhật trạng thái yêu cầu thành 'Declined', giải phóng cờ chờ cho cả hai bên.", "Hủy trạng thái Pending"),
                        ("AF-A-3", "Hệ thống", "Gửi thông báo nhẹ nhàng đến Sinh viên A để A tiếp tục tìm kiếm ứng viên khác trên hệ thống.", "[End of Use Case: kết thúc với trạng thái không ghép. Outcome: kind: successEnd]")
                    ]
                },
                {
                    "name": "AF-B – Sinh viên A chủ động thu hồi lời mời trước khi B phản hồi",
                    "point": "BF-3",
                    "cond": "Sinh viên A đổi ý muốn kết nối với bạn khác khi B chưa bấm duyệt",
                    "steps": [
                        ("AF-B-1", "Sinh viên A", "Mở danh sách lời mời đã gửi và nhấn 'Thu hồi yêu cầu'.", "A chủ động hủy"),
                        ("AF-B-2", "Hệ thống", "Hủy bản ghi yêu cầu Pending, thu hồi thông báo hiển thị phía B và cập nhật lại trạng thái khả dụng cho A.", "[Outcome: kind: successEnd]")
                    ]
                }
            ],
            "ef": [
                {
                    "name": "EF-A – Không đủ điều kiện ràng buộc ghép đôi",
                    "point": "BF-2",
                    "cond": "Hai sinh viên khác giới tính, khác loại phòng đăng ký hoặc đối phương đã chốt nhóm",
                    "steps": [
                        ("EF-A-1", "Hệ thống", "Chặn gửi yêu cầu và thông báo lý do cụ thể (Ví dụ: 'Bạn và ứng viên không đăng ký cùng loại phòng' hoặc 'Ứng viên đã có phòng chính thức').", "Kiểm soát an toàn"),
                        ("EF-A-2", "Hệ thống", "Giữ nguyên trạng thái và hướng dẫn SV A chọn bạn khác phù hợp với tiêu chí.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                    ]
                },
                {
                    "name": "EF-B – Yêu cầu hết hạn 48 giờ không phản hồi",
                    "point": "BF-3",
                    "cond": "Quá 48 giờ kể từ khi gửi nhưng Sinh viên B không thực hiện chấp nhận hay từ chối",
                    "steps": [
                        ("EF-B-1", "Hệ thống", "Bộ lập lịch quét quá hạn, tự động chuyển trạng thái yêu cầu sang 'Expired' (Hết hạn).", "Tự động dọn dẹp"),
                        ("EF-B-2", "Hệ thống", "Gửi thông báo cho SV A về việc yêu cầu đã hết hạn để SV A chủ động gửi lời mời tới người khác.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                    ]
                }
            ],
            "add_info": "Business Rules áp dụng: BR-05 (Cơ chế Request hai chiều), BR-06 (Quy tắc phòng), BR-09 (Điểm hòa hợp 1.5x). Non-functional: NFR-05 (Giao diện trực quan), NFR-07 (Thông báo thời gian thực)."
        },
        {
            "id": "UC-07",
            "title": "Thanh toán tiền phòng & Đặt cọc giữ chỗ 72h (Dormitory Payment & Deposit)",
            "desc": "Sinh viên thực hiện thanh toán trực tuyến tiền phòng kỳ 1 kèm tiền đặt cọc giữ chỗ 2.000.000đ qua cổng VNPay trong hạn chót 72 giờ; hệ thống tự động xác thực, chốt phòng và tạo/in biên lai thu tiền điện tử.",
            "actors": "Sinh viên (Primary Actor), Cổng thanh toán điện tử VNPay (External Actor), Hệ thống KTX (Supporting).",
            "precond": "Sinh viên đã có kết quả phân bổ phòng chính thức và thời hạn thanh toán 72 giờ đang có hiệu lực.",
            "postcond": "Giao dịch được đối soát thành công, chỗ phòng được khóa cố định, biên lai điện tử được tạo và sẵn sàng để in/tải.",
            "trigger": "Sinh viên nhấn nút 'Thanh toán ngay' từ thông báo phân phòng hoặc bảng kết quả KTX.",
            "bf": [
                ("BF-1", "Sinh viên", "Mở màn hình thanh toán từ thông báo phân phòng trúng tuyển KTX.", "Trigger: Bắt đầu thanh toán"),
                ("BF-2", "Hệ thống", "Hiển thị bảng kê chi tiết viện phí gồm: Tiền phòng Kỳ 1 (theo loại phòng) + Tiền đặt cọc tài sản (2.000.000đ) và đồng hồ đếm ngược thời hạn 72 giờ.", "Ràng buộc BR-04. Rẽ EF-B: Đã quá hạn 72 giờ."),
                ("BF-3", "Sinh viên", "Xác nhận số tiền thanh toán và chọn phương thức 'Thanh toán qua cổng VNPAY-QR'.", "Xác nhận khoản thu. Rẽ AF-A: Chọn chuyển khoản đối soát."),
                ("BF-4", "Hệ thống", "Khởi tạo đơn hàng bảo mật, sinh mã giao dịch duy nhất và chuyển hướng sang cổng thanh toán VNPay kèm mã QR động.", "Mã hóa TLS 1.3, NFR-04"),
                ("BF-5", "Cổng VNPay", "Sinh viên quét mã QR trên ứng dụng Mobile Banking; Cổng VNPay xử lý trừ tiền an toàn và gửi mã callback xác nhận (vnp_ResponseCode = 00) về máy chủ KTX.", "Đối soát tự động. Rẽ EF-A: Giao dịch ngân hàng thất bại."),
                ("BF-6", "Hệ thống", "Cập nhật trạng thái hợp đồng thành 'Paid' (Đã thanh toán), khóa chính thức vị trí giường phòng cho sinh viên.", "Chốt phòng thành công"),
                ("BF-7", "Hệ thống", "Tự động tạo Biên lai thu tiền điện tử có mã tra cứu và hiển thị nút 'In biên lai' / 'Tải file PDF biên lai' trực tiếp trên màn hình kết quả.", "TẠO VÀ IN BIÊN LAI TRONG LUỒNG CHÍNH"),
                ("BF-8", "Sinh viên", "Xem biên lai, bấm in hoặc tải file biên lai về máy và nhận phòng thành công.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                {
                    "name": "AF-A – Thanh toán qua Chuyển khoản ngân hàng có mã định danh (Virtual Account)",
                    "point": "BF-3",
                    "cond": "Sinh viên không sử dụng ví quét QR mà muốn chuyển khoản qua tài khoản ngân hàng",
                    "steps": [
                        ("AF-A-1", "Sinh viên", "Chọn 'Chuyển khoản theo số tài khoản định danh KTX'.", "Phương thức thanh toán thay thế"),
                        ("AF-A-2", "Hệ thống", "Cung cấp số tài khoản ảo duy nhất kèm cú pháp nội dung chuyển khoản tự động khớp lệnh.", "Tích hợp Open Banking"),
                        ("AF-A-3", "Hệ thống", "Nhận tín hiệu báo có từ ngân hàng, tự động gạch nợ và chuyển sang bước BF-6 để tạo biên lai.", "[Outcome: kind: return, stepId: BF-6]")
                    ]
                }
            ],
            "ef": [
                {
                    "name": "EF-A – Giao dịch ngân hàng bị từ chối hoặc tài khoản không đủ số dư",
                    "point": "BF-5",
                    "cond": "Số dư thẻ không đủ, thẻ hết hạn hoặc sinh viên hủy thao tác trên App ngân hàng",
                    "steps": [
                        ("EF-A-1", "Cổng VNPay", "Gửi thông báo mã lỗi giao dịch thất bại về hệ thống KTX.", "Giao dịch lỗi"),
                        ("EF-A-2", "Hệ thống", "Hiển thị thông báo chi tiết lỗi, giữ nguyên tình trạng đơn trong hạn 72h và hướng dẫn sinh viên thử lại.", "[End of Use Case: mục tiêu chưa đạt trong lượt này. Outcome: kind: failureEnd]")
                    ]
                },
                {
                    "name": "EF-B – Đơn thanh toán đã quá hạn 72 giờ quy định",
                    "point": "BF-2",
                    "cond": "Thời gian thanh toán vượt quá 72 giờ kể từ lúc công bố kết quả",
                    "steps": [
                        ("EF-B-1", "Hệ thống", "Khóa tính năng thanh toán, hiển thị thông báo kết quả giữ chỗ đã bị hủy do quá hạn 72h theo quy định BR-04.", "Tự động thu hồi suất phòng"),
                        ("EF-B-2", "Hệ thống", "Chuyển sinh viên sang danh sách chờ và kết thúc phiên làm việc.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                    ]
                }
            ],
            "add_info": "Business Rules áp dụng: BR-04 (Hạn cọc 72h), BR-07 (Quy định bảo lưu cọc). Non-functional: NFR-04 (Bảo mật giao dịch, đối soát SHA-256), NFR-07 (Độ sẵn sàng 99.9%)."
        },
        {
            "id": "UC-08",
            "title": "Thủ tục Trả phòng & Quyết toán KTX (Dormitory Check-out & Settlement)",
            "desc": "Quy trình kết thúc thời hạn lưu trú của sinh viên: Kiểm kê cơ sở vật chất phòng, đối soát công nợ dịch vụ, tính toán khoản khấu trừ bồi thường (nếu có), hoàn trả tiền cọc cho sinh viên và giải phóng giường trống về kho hệ thống.",
            "actors": "Sinh viên (Primary Actor), Cán bộ KTX (Staff Actor), Kế toán KTX (Finance Actor), Hệ thống KTX (Supporting).",
            "precond": "Sinh viên đang cư trú tại KTX và hợp đồng đến hạn kết thúc hoặc có đơn xin trả phòng được chấp thuận.",
            "postcond": "Phòng được bàn giao xong, giường chuyển về trạng thái Trống, tiền cọc thừa được chuyển khoản hoàn trả cho sinh viên.",
            "trigger": "Sinh viên chọn chức năng 'Làm thủ tục trả phòng' trên cổng dịch vụ hoặc đến ngày kết thúc học kỳ.",
            "bf": [
                ("BF-1", "Sinh viên", "Gửi yêu cầu làm thủ tục trả phòng và đăng ký lịch kiểm kê bàn giao với Ban quản lý KTX.", "Trigger: Đăng ký lịch trả phòng"),
                ("BF-2", "Cán bộ KTX", "Tiếp nhận lịch hẹn, trực tiếp đến phòng kiểm tra hiện trạng tài sản (giường, tủ, điều hòa, khóa cửa) và nhập chỉ số công tơ điện nước vào máy tính bảng công tác.", "Actor: Cán bộ KTX kiểm kê"),
                ("BF-3", "Hệ thống", "Tự động truy xuất số liệu sử dụng, tính toán công nợ dịch vụ kỳ cuối và ghi nhận chi phí bồi thường hư hại (nếu có biên bản đền bù).", "Tính toán nợ dịch vụ"),
                ("BF-4", "Hệ thống", "Áp dụng quy tắc tài chính BR-07 để tính toán quyết toán cọc: Số tiền hoàn lại = 2.000.000đ cọc − (Nợ điện nước + Phí hư hại).", "Quy tắc hoàn cọc BR-07. Rẽ EF-A: Tiền cọc không đủ bù đắp thiệt hại."),
                ("BF-5", "Hệ thống", "Xuất Biên bản nghiệm thu và thanh lý hợp đồng điện tử hiển thị bảng kê chi tiết số tiền hoàn trả cho sinh viên và Cán bộ duyệt xác nhận.", "Xác nhận thanh lý"),
                ("BF-6", "Sinh viên", "Kiểm tra bảng kê số liệu, bàn giao lại chìa khóa/thẻ từ phòng cho Cán bộ và ký xác nhận điện tử.", "Bàn giao vật lý"),
                ("BF-7", "Cán bộ KTX", "Nhấn nút 'Xác nhận hoàn tất bàn giao phòng' trên ứng dụng quản trị.", "Duyệt bàn giao"),
                ("BF-8", "Hệ thống", "Cập nhật trạng thái hợp đồng thành 'Closed', chuyển trạng thái giường phòng thành 'Vacant' (Phòng trống khả dụng) để nạp vào quỹ phòng cho đợt tiếp nhận mới.", "Giải phóng giường phòng"),
                ("BF-9", "Kế toán", "Phê duyệt lệnh hoàn tiền trên hệ thống tài chính; cổng thanh toán tự động chuyển số tiền cọc hoàn lại về tài khoản ngân hàng của sinh viên.", "Hoàn tiền cọc qua ngân hàng"),
                ("BF-10", "Hệ thống", "Gửi email thông báo thanh lý hợp đồng thành công kèm biên lai hoàn tiền cho sinh viên.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                {
                    "name": "AF-A – Sinh viên trả phòng đúng hạn, nguyên vẹn tài sản và không phát sinh nợ",
                    "point": "BF-4",
                    "cond": "Phòng bảo quản hoàn hảo, công tơ điện nước trong định mức tiêu chuẩn",
                    "steps": [
                        ("AF-A-1", "Hệ thống", "Xác định chi phí khấu trừ bằng 0, duyệt hoàn trả đủ 100% tiền cọc (2.000.000 VNĐ).", "Hoàn cọc 100%"),
                        ("AF-A-2", "Hệ thống", "Chuyển thẳng sang bước lập lệnh hoàn tiền nhanh cho Kế toán.", "[Outcome: kind: return, stepId: BF-5]")
                    ]
                }
            ],
            "ef": [
                {
                    "name": "EF-A – Chi phí hư hại tài sản và công nợ vượt quá số tiền cọc 2.000.000đ",
                    "point": "BF-4",
                    "cond": "Tài sản bị hư hại nặng hoặc vi phạm nội quy lớn khiến tổng phạt > 2.000.000đ",
                    "steps": [
                        ("EF-A-1", "Hệ thống", "Tính toán số tiền chênh lệch thiếu hụt (Phát sinh âm sau khi trừ hết tiền cọc).", "Ghi nhận công nợ phụ"),
                        ("EF-A-2", "Cán bộ KTX", "Lập biên bản vi phạm kỷ luật, yêu cầu sinh viên thanh toán bổ sung phần thiếu trước khi cấp giấy chứng nhận hoàn tất thủ tục KTX.", "Xử lý bồi thường bổ sung"),
                        ("EF-A-3", "Hệ thống", "Treo trạng thái thanh lý cho đến khi sinh viên nộp đủ khoản bồi thường phụ trội.", "[End of Use Case: mục tiêu chưa hoàn tất. Outcome: kind: failureEnd]")
                    ]
                }
            ],
            "add_info": "Business Rules áp dụng: BR-02 (Thời hạn hợp đồng), BR-07 (Quy tắc quyết toán và hoàn cọc). Non-functional: NFR-06 (Ghi nhật ký kiểm kê và bàn giao), NFR-08 (Thời gian xử lý quyết toán tức thì)."
        }
    ]

    for uc in detailed_ucs:
        add_h2(doc, f"{uc['id']}: {uc['title']}")
        
        # Summary Table
        add_h3(doc, "A. Bảng Tóm Tắt (Summary Table - Chuẩn Slide p110 & Nhóm 2)")
        tbl_s = doc.add_table(rows=5, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        s_data = [
            ("Description", uc["desc"]),
            ("Actors", uc["actors"]),
            ("Preconditions", uc["precond"]),
            ("Postconditions", uc["postcond"]),
            ("Trigger", uc["trigger"])
        ]
        for idx, (lbl, val) in enumerate(s_data):
            row = tbl_s.rows[idx]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width, c1.width = Inches(1.6), Inches(5.1)
            set_cell_background(c0, "F1F5F9")
            set_cell_background(c1, "FFFFFF")
            set_cell_margins(c0, 50, 50, 80, 80)
            set_cell_margins(c1, 50, 50, 80, 80)
            set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            
            p0 = c0.paragraphs[0]
            r0 = p0.add_run(lbl)
            r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9), True
            r0.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

            p1 = c1.paragraphs[0]
            r1 = p1.add_run(val)
            r1.font.name, r1.font.size = 'Times New Roman', Pt(9)
            r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=4)

        # Basic Flow
        add_h3(doc, f"B. Luồng Cơ Bản (Basic Flow – {uc['id']})")
        tbl_bf = doc.add_table(rows=len(uc["bf"])+1, cols=4)
        tbl_bf.alignment = WD_TABLE_ALIGNMENT.CENTER
        bf_w = [Inches(0.8), Inches(1.4), Inches(2.6), Inches(1.9)]
        for j, h in enumerate(["Step ID", "Actor", "Action", "Notes and References"]):
            c = tbl_bf.rows[0].cells[j]
            c.width = bf_w[j]
            set_cell_background(c, "0F172A")
            set_cell_margins(c, 50, 50, 60, 60)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(h)
            r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(8.5), True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for i, (sid, sact, saction, sref) in enumerate(uc["bf"]):
            row = tbl_bf.rows[i+1]
            bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
            for j, val in enumerate([sid, sact, saction, sref]):
                c = row.cells[j]
                c.width = bf_w[j]
                set_cell_background(c, bg)
                set_cell_margins(c, 40, 40, 60, 60)
                set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
                p = c.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
                r.font.name, r.font.size = 'Times New Roman', Pt(8.5)
                if j == 0:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x0F, 0x76, 0x6E) # Teal
                elif j == 1:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
                else:
                    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=4)

        # Alternate Flows
        if uc["af"]:
            add_h3(doc, "C. Các Luồng Thay Thế (Alternate Flows - AF)")
            for af_item in uc["af"]:
                add_body(doc, f"• {af_item['name']}", bold=True, color_rgb=(0x15, 0x80, 0x3D))
                add_body(doc, f"  Branch point: {af_item['point']} | Condition: {af_item['cond']}", italic=True, color_rgb=(0x47, 0x55, 0x69))
                
                tbl_af = doc.add_table(rows=len(af_item["steps"])+1, cols=4)
                tbl_af.alignment = WD_TABLE_ALIGNMENT.CENTER
                for j, h in enumerate(["Step ID", "Actor", "Action", "Notes and References"]):
                    c = tbl_af.rows[0].cells[j]
                    c.width = bf_w[j]
                    set_cell_background(c, "15803D")
                    set_cell_margins(c, 40, 40, 60, 60)
                    p = c.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    r = p.add_run(h)
                    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(8.5), True
                    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

                for i, (sid, sact, saction, sref) in enumerate(af_item["steps"]):
                    row = tbl_af.rows[i+1]
                    for j, val in enumerate([sid, sact, saction, sref]):
                        c = row.cells[j]
                        c.width = bf_w[j]
                        set_cell_background(c, "F0FDF4")
                        set_cell_margins(c, 30, 30, 60, 60)
                        set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'DCFCE7'}, bottom={'val': 'single', 'sz': 4, 'color': 'DCFCE7'})
                        p = c.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                        r = p.add_run(val)
                        r.font.name, r.font.size = 'Times New Roman', Pt(8.5)
                        if j == 0:
                            r.font.bold = True
                            r.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
                        else:
                            r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
                add_styled_p(doc, space_after=2)

        # Exception Flows
        if uc["ef"]:
            add_h3(doc, "D. Các Luồng Ngoại Lệ (Exception Flows - EF)")
            for ef_item in uc["ef"]:
                add_body(doc, f"• {ef_item['name']}", bold=True, color_rgb=(0xB9, 0x1C, 0x1C))
                add_body(doc, f"  Branch point: {ef_item['point']} | Condition: {ef_item['cond']}", italic=True, color_rgb=(0x47, 0x55, 0x69))
                
                tbl_ef = doc.add_table(rows=len(ef_item["steps"])+1, cols=4)
                tbl_ef.alignment = WD_TABLE_ALIGNMENT.CENTER
                for j, h in enumerate(["Step ID", "Actor", "Action", "Notes and References"]):
                    c = tbl_ef.rows[0].cells[j]
                    c.width = bf_w[j]
                    set_cell_background(c, "B91C1C")
                    set_cell_margins(c, 40, 40, 60, 60)
                    p = c.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    r = p.add_run(h)
                    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(8.5), True
                    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

                for i, (sid, sact, saction, sref) in enumerate(ef_item["steps"]):
                    row = tbl_ef.rows[i+1]
                    for j, val in enumerate([sid, sact, saction, sref]):
                        c = row.cells[j]
                        c.width = bf_w[j]
                        set_cell_background(c, "FEF2F2")
                        set_cell_margins(c, 30, 30, 60, 60)
                        set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'FEE2E2'}, bottom={'val': 'single', 'sz': 4, 'color': 'FEE2E2'})
                        p = c.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                        r = p.add_run(val)
                        r.font.name, r.font.size = 'Times New Roman', Pt(8.5)
                        if j == 0:
                            r.font.bold = True
                            r.font.color.rgb = RGBColor(0xB9, 0x1C, 0x1C)
                        else:
                            r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
                add_styled_p(doc, space_after=2)

        # Additional Information
        add_h3(doc, "E. Thông Tin Bổ Sung (Additional Information)")
        add_body(doc, uc["add_info"], italic=True, color_rgb=(0x1E, 0x3A, 0x8A))
        add_styled_p(doc, space_after=10)

    # ==================== PHẦN 5: MA TRẬN VÒNG ĐỜI & SEQUENCE DIAGRAM ====================
    add_h1(doc, "5. MA TRẬN VÒNG ĐỜI TƯƠNG TÁC & SEQUENCE DIAGRAM")
    add_body(doc, "Để khắc phục triệt để lỗi 'đặc tả sai dẫn đến vẽ diagram sai vòng đời', biểu đồ tuần tự bên dưới được thiết kế với sự phân định rõ ràng giữa hai tác nhân con người (Sinh viên A và Sinh viên B), kết hợp các thanh kích hoạt vòng đời (Activation Bars / Lifelines) phản ánh chính xác khoảng thời gian thực thi của từng thành phần:")

    seq_mermaid = """sequenceDiagram
    autonumber
    actor SVA as 🧑 Sinh viên A (Gửi Request)
    participant UI as 🖥️ Giao diện KTX Web
    participant MatchSvc as ⚙️ Matching Service
    participant DB as 🗄️ Database KTX
    actor SVB as 🧑 Sinh viên B (Nhận Request)

    Note over SVA, SVB: VÒNG ĐỜI 1: KHỞI TẠO & GỬI YÊU CẦU GHÉP PHÒNG (MATCHING REQUEST)
    SVA->>UI: 1. (BF-1) Chọn ứng viên B & Nhấn "Gửi yêu cầu ghép bạn"
    activate UI
    UI->>MatchSvc: 2. (BF-2) Kiểm tra điều kiện (cùng giới tính, loại phòng, BR-05)
    activate MatchSvc
    MatchSvc->>DB: 3. (BF-2) Truy vấn hồ sơ B & Kiểm tra cờ nhóm
    activate DB
    DB-->>MatchSvc: 4. (BF-2) Xác nhận B hợp lệ & chưa thuộc nhóm nào
    deactivate DB
    
    MatchSvc->>DB: 5. (BF-3) Lưu yêu cầu trạng thái "Pending" (Hạn 48h)
    activate DB
    DB-->>MatchSvc: 6. (BF-3) Xác nhận lưu bản ghi thành công
    deactivate DB

    MatchSvc->>SVB: 7. (BF-3) Đẩy thông báo Push / Email: "Bạn có lời mời ghép phòng từ SV A"
    MatchSvc-->>UI: 8. (BF-3) Phản hồi: Đã gửi lời mời thành công
    deactivate MatchSvc
    UI-->>SVA: 9. (BF-3) Thông báo gửi request thành công, chờ B phản hồi
    deactivate UI

    Note over SVA, SVB: VÒNG ĐỜI 2: SINH VIÊN B ĐỐI SOÁT & PHẢN HỒI (BẤT ĐỒNG BỘ)
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
        MatchSvc->>SVA: 18. (BF-6) Gửi thông báo chúc mừng tới A: "SV B đã đồng ý ghép phòng!"
        MatchSvc-->>UI: 19. (BF-6) Thông báo thành công tới B
        deactivate MatchSvc
        UI-->>SVB: 20. (BF-7) Hiển thị thông báo hoàn tất, kết thúc use case
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
        MatchSvc->>SVA: 25. (AF-A-3) Gửi thông báo tới A: "Lời mời ghép phòng không được chấp thuận"
        deactivate MatchSvc
        UI-->>SVB: 26. (AF-A-3) Xác nhận đóng yêu cầu thành công
        deactivate UI
    end"""

    add_body(doc, "Mã biểu đồ Sequence Diagram tương ứng chuẩn Mermaid (Khớp 1-1 với Step ID):", bold=True)
    p_code = add_styled_p(doc, space_before=2, space_after=8)
    r_code = p_code.add_run(seq_mermaid)
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(8)
    r_code.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    # Output file paths
    docx_docs = os.path.join(os.path.dirname(__file__), "docs", "Dac_Ta_Use_Case_Va_Business_Rules_KTX_Chuan_VNUK.docx")
    docx_dl = os.path.join(r"C:\Users\LENOVO\Downloads", "Dac_Ta_Use_Case_Va_Business_Rules_KTX_Chuan_VNUK.docx")
    
    os.makedirs(os.path.dirname(docx_docs), exist_ok=True)
    doc.save(docx_docs)
    shutil.copy2(docx_docs, docx_dl)
    print(f"[DOCX SUCCESS] Generated:\n  - {docx_docs}\n  - {docx_dl}")

if __name__ == "__main__":
    build_docx()
