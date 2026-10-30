# -*- coding: utf-8 -*-
"""
generate_three_separate_deliverables.py
Tạo 3 bộ tài liệu RIÊNG BIỆT hoàn toàn theo yêu cầu của user:
1. Business Rules riêng: BR_KTX_Smart_Match_VNUK.docx & .pdf (Format 3 cột chuẩn Slide p125: Rule ID | Name | Description)
2. Đặc tả Use Case riêng: Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.docx & .pdf (Đặc tả chi tiết chuẩn Slide p110, sửa thẳng feedback của thầy)
3. Diagram riêng: Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.docx & .pdf (Sơ đồ Use Case vẽ lại + Sequence Diagrams chuẩn thanh vòng đời activation bars)

Không gộp chung, sửa thẳng feedback không ghi bảng feedback vào docs.
Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều (Nhóm 3)
Trường: Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
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
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    return p

def add_h2(doc, text):
    p = add_styled_p(doc, space_before=12, space_after=4)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    return p

def add_h3(doc, text):
    p = add_styled_p(doc, space_before=8, space_after=3)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
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

# ==============================================================================
# 1. BUILD BUSINESS RULES DOCUMENT (RIÊNG BIỆT)
# ==============================================================================
def build_br_doc():
    doc = docx.Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.27), Inches(11.69)
        s.top_margin, s.bottom_margin = Inches(0.8), Inches(0.8)
        s.left_margin, s.right_margin = Inches(0.85), Inches(0.85)

    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=4)
    r = p_title.add_run("HỆ THỐNG QUY TẮC NGHIỆP VỤ\n(BUSINESS RULES BASELINE)")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(16), True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    r = p_sub.add_run("Dự án: Hệ thống Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nĐịnh dạng chuẩn: Slide System Engineering p125 (Rule ID | Name | Description)")
    r.font.name, r.font.size, r.font.italic = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Info table
    tbl_info = doc.add_table(rows=3, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info = [
        ("Nhóm thực hiện:", "Nhóm 3: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều"),
        ("Đơn vị đào tạo:", "Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng"),
        ("Bản chất tài liệu:", "Tập trung 100% các Ràng buộc nghiệp vụ (Business Rules), tách biệt hoàn toàn với Đặc tả")
    ]
    for i, (k, v) in enumerate(info):
        row = tbl_info.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.0), Inches(4.5)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 50, 50, 80, 80)
        set_cell_margins(c1, 50, 50, 80, 80)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(k)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(9.5), True
        p0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        p1 = c1.paragraphs[0].add_run(v)
        p1.font.name, p1.font.size = 'Times New Roman', Pt(9.5)
        p1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=10)

    add_h2(doc, "1. Nguyên tắc Định nghĩa Business Rules (Theo chuẩn Slide bài giảng p125)")
    add_body(doc, "Quy tắc nghiệp vụ (Business Rule) là các tuyên bố định nghĩa hoặc hạn chế một số khía cạnh của việc vận hành kinh doanh / quản trị Ký túc xá. Nó khẳng định cấu trúc nghiệp vụ hoặc kiểm soát/ảnh hưởng đến hành vi của hệ thống.")
    add_body(doc, "Lưu ý quan trọng: Business Rules KHÔNG PHẢI là yêu cầu chức năng (Functional Requirements) hay các bước thao tác bấm nút của người dùng, mà là LUẬT LỆ, RÀNG BUỘC VÀ CÔNG THỨC bắt buộc hệ thống phải tuân thủ.")

    add_h2(doc, "2. Bảng Danh mục Quy tắc Nghiệp vụ KTX Smart Match (Chuẩn 3 cột)")
    
    br_data = [
        ("BR-01", "Mã số sinh viên duy nhất & Đối tượng tiếp nhận",
         "Mỗi sinh viên có duy nhất một Mã số sinh viên (MSSV) không trùng lặp trong toàn bộ hệ thống, đóng vai trò khóa chính định danh tài khoản. KTX chỉ tiếp nhận sinh viên chính quy thuộc khối liên kết VNUK có trạng thái đào tạo hợp lệ và sử dụng email trường cấp (@vnuk.edu.vn). Tài khoản ngoài hệ thống hoặc MSSV không hợp lệ bị từ chối đăng ký."),
        ("BR-02", "Cam kết thời hạn lưu trú tối thiểu 01 học kỳ",
         "Mỗi hồ sơ đăng ký KTX bắt buộc phải có cam kết thời hạn cư trú tối thiểu 01 học kỳ (05 tháng) hoặc trọn năm học (10 tháng). Hệ thống kiên quyết không thụ lý hợp đồng ngắn hạn theo ngày/tuần nhằm bảo toàn nếp sống văn hóa ổn định và kế hoạch vận hành tài chính của KTX."),
        ("BR-03", "Phê duyệt nghiệp vụ bắt buộc (Business Approve)",
         "Mọi hồ sơ đăng ký phòng của sinh viên sau khi nộp trực tuyến bắt buộc phải trải qua bước thẩm định và phê duyệt nghiệp vụ của Cán bộ KTX (rà soát lịch sử kỷ luật, đối soát diện ưu tiên chính sách, kiểm tra nợ cũ) trước khi được đưa vào hàng đợi chạy thuật toán phân bổ phòng."),
        ("BR-04", "Đặt cọc giữ chỗ và thời hạn thanh toán 72 giờ",
         "Trong vòng chính xác 72 giờ kể từ thời điểm công bố kết quả phân phòng, sinh viên phải hoàn tất thanh toán tiền phòng kỳ 1 kèm tiền đặt cọc tài sản (2.000.000 VNĐ) qua cổng VNPay. Quá thời hạn 72 giờ không thanh toán, hệ thống tự động hủy kết quả giữ chỗ và chuyển suất cho sinh viên trong danh sách chờ (Waitlist)."),
        ("BR-05", "Ghép bạn cùng phòng theo cơ chế Request hai chiều",
         "Việc ghép bạn cùng phòng giữa hai cá nhân bắt buộc phải dựa trên sự đồng thuận tự nguyện của cả hai bên: Một bên gửi yêu cầu (Matching Request), bên còn lại phải nhận thông tin, xem xét hồ sơ nếp sống và chủ động bấm 'Đồng ý' thì quan hệ ghép cặp mới được xác lập hợp lệ. Thời hạn phản hồi tối đa là 48 giờ."),
        ("BR-06", "Tối ưu hóa tỷ lệ lấp đầy phòng (Occupancy Rate)",
         "Thuật toán phân bổ phòng ưu tiên lấp đầy 100% số giường của từng phòng (2, 4, 6 người) trước khi mở phòng mới nhằm tối ưu hóa chi phí điện nước chung, khấu hao điều hòa và bảo toàn biên lợi nhuận vận hành cho KTX."),
        ("BR-07", "Quy tắc quyết toán và hoàn cọc khi trả phòng (Check-out)",
         "Khi làm thủ tục trả phòng, tiền đặt cọc chỉ được hoàn trả sau khi Cán bộ KTX nghiệm thu hiện trạng cơ sở vật chất. Số tiền cọc hoàn lại = 2.000.000đ − (Công nợ dịch vụ phát sinh + Chi phí bồi thường hư hỏng tài sản nếu có). Nếu sinh viên đơn phương phá vỡ hợp đồng trước 1 học kỳ, toàn bộ tiền cọc không được hoàn lại."),
        ("BR-08", "Ràng buộc yêu cầu đổi phòng / đổi bạn",
         "Mỗi sinh viên chỉ được phép có tối đa 01 yêu cầu đổi phòng đang trong trạng thái xử lý; yêu cầu bắt buộc phải có lý do cụ thể và chỉ được Cán bộ KTX phê duyệt khi phòng đích còn chỗ trống khả dụng và phù hợp về giới tính, loại phòng."),
        ("BR-09", "Tính điểm tương thích hai chiều và trọng số ưu tiên 1.5x",
         "Điểm hòa hợp nếp sống giữa hai sinh viên được tính toán trên vector 8 tiêu chí thói quen; tiêu chí mà mỗi sinh viên đánh dấu là quan trọng nhất (Top Criterion) sẽ được nhân hệ số trọng số 1.5x khi tính toán ma trận tương thích hai chiều bất đối xứng.")
    ]

    tbl_br = doc.add_table(rows=len(br_data)+1, cols=3)
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

    for i, (rid, rname, rdesc) in enumerate(br_data):
        row = tbl_br.rows[i+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = br_w[0], br_w[1], br_w[2]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, 50, 50, 80, 80)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(rid)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(9), True
        p0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        p1 = c1.paragraphs[0].add_run(rname)
        p1.font.name, p1.font.size, p1.font.bold = 'Times New Roman', Pt(9), True
        p1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p2 = c2.paragraphs[0].add_run(rdesc)
        p2.font.name, p2.font.size = 'Times New Roman', Pt(9)
        p2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    docx_path = os.path.join(os.path.dirname(__file__), "docs", "BR_KTX_Smart_Match_VNUK.docx")
    dl_path = os.path.join(r"C:\Users\LENOVO\Downloads", "BR_KTX_Smart_Match_VNUK.docx")
    doc.save(docx_path)
    shutil.copy2(docx_path, dl_path)
    print(f"[SUCCESS] Saved BR DOCX to {dl_path}")

# ==============================================================================
# 2. BUILD USE CASE SPECIFICATION DOCUMENT (RIÊNG BIỆT)
# ==============================================================================
def build_spec_doc():
    doc = docx.Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.27), Inches(11.69)
        s.top_margin, s.bottom_margin = Inches(0.8), Inches(0.8)
        s.left_margin, s.right_margin = Inches(0.85), Inches(0.85)

    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=4)
    r = p_title.add_run("TÀI LIỆU ĐẶC TẢ USE CASE HỆ THỐNG KTX\n(USE CASE SPECIFICATION)")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(16), True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    r = p_sub.add_run("Hệ thống: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nCăn cứ: Khung bài giảng Use Case Specification (Slide p110) • Sửa thẳng chuẩn hóa toàn bộ luồng")
    r.font.name, r.font.size, r.font.italic = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Info table
    tbl_info = doc.add_table(rows=3, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info = [
        ("Nhóm thực hiện:", "Nhóm 3: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều"),
        ("Đơn vị đào tạo:", "Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng"),
        ("Quy ước luồng:", "Mỗi use case gồm: Summary Table, Basic Flow (BF), Alternate Flows (AF), Exception Flows (EF)")
    ]
    for i, (k, v) in enumerate(info):
        row = tbl_info.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.0), Inches(4.5)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 50, 50, 80, 80)
        set_cell_margins(c1, 50, 50, 80, 80)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(k)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(9.5), True
        p0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        p1 = c1.paragraphs[0].add_run(v)
        p1.font.name, p1.font.size = 'Times New Roman', Pt(9.5)
        p1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=10)

    # Bảng Use case catalog vẽ lại tinh gọn
    add_h2(doc, "1. Bảng Danh mục Use Case Hệ Thống (Vẽ lại Tinh gọn & Chuẩn hóa)")
    add_body(doc, "Danh mục Use Case được tinh gọn từ cấu trúc cồng kềnh ban đầu xuống các Use Case nghiệp vụ cốt lõi, phản ánh đúng vai trò thực tế của người dùng và hệ thống:")

    uc_catalog = [
        ("UC-01", "Đăng nhập & Xác thực hệ thống", "Sinh viên, Cán bộ KTX", "Lựa chọn đăng nhập bằng Tên/Email (@vnuk.edu.vn) hoặc MSSV + Mật khẩu là 1 chức năng duy nhất."),
        ("UC-02", "Đăng ký tài khoản & Khai báo thông tin/thói quen", "Sinh viên", "Đăng ký tài khoản bằng MSSV duy nhất và khai báo hồ sơ nếp sống sinh hoạt 8 tiêu chí."),
        ("UC-03", "Cập nhật hồ sơ & nếp sống sinh hoạt", "Sinh viên", "Chỉnh sửa thông tin cá nhân và 8 thói quen sinh hoạt; hỗ trợ nạp Persona mẫu."),
        ("UC-04", "Chọn loại phòng & Nộp đơn đăng ký KTX", "Sinh viên", "Chọn loại phòng (2/4/6), tiện ích, ký cam kết ở tối thiểu 1 kỳ và nộp hồ sơ chờ duyệt."),
        ("UC-05", "Ghép bạn cùng phòng theo yêu cầu (Matching by Request)", "Sinh viên gửi (SV A), Sinh viên nhận (SV B)", "SV A gửi Matching Request -> SV B nhận thông báo, xem profile và chọn Đồng ý/Từ chối."),
        ("UC-06", "Xem kết quả phân phòng & thông tin phòng ở", "Sinh viên", "Tra cứu phòng được phân, danh sách bạn cùng phòng, viện phí và hạn chót thanh toán 72h."),
        ("UC-07", "Thanh toán tiền phòng & Đặt cọc giữ chỗ 72h", "Sinh viên, Cổng VNPay", "Thanh toán tiền phòng kỳ 1 và cọc 2tr; hệ thống tự động tạo và in/tải biên lai trong luồng chính."),
        ("UC-08", "Thủ tục Trả phòng & Quyết toán KTX (Check-out)", "Sinh viên, Cán bộ KTX, Kế toán", "Quy trình trả phòng: Kiểm kê tài sản -> Khấu trừ hư hại -> Hoàn trả cọc -> Giải phóng chỗ."),
        ("UC-09", "Yêu cầu chuyển phòng / chuyển bạn cùng phòng", "Sinh viên, Cán bộ KTX", "Gửi yêu cầu đổi phòng kèm lý do/minh chứng khi có xung đột nếp sống phát sinh."),
        ("UC-10", "Gửi phản ánh dịch vụ & Báo hỏng cơ sở vật chất", "Sinh viên, Kỹ thuật", "Khai báo sự cố điện nước, thiết bị hư hỏng trong phòng và theo dõi tiến độ sửa chữa."),
        ("UC-11", "Quản lý danh mục tòa, phòng & bảng giá", "Quản trị viên (Admin)", "Thêm, cập nhật, cấu hình danh mục tòa nhà, phòng ở, định mức giá và chỉ tiêu tiếp nhận."),
        ("UC-12", "Thẩm định & Phê duyệt đơn KTX (Business Approve)", "Cán bộ quản lý KTX", "Kiểm tra điều kiện lưu trú, xét duyệt hồ sơ hợp lệ để đưa vào thuật toán phân phòng."),
        ("UC-13", "Khởi chạy Phân bổ phòng tự động & Tối ưu lấp đầy", "Hệ thống (Scheduler), Admin", "Chạy thuật toán Gale-Shapley kết hợp lấp đầy 100% giường, triệt tiêu cặp chặn BP=0."),
        ("UC-14", "Theo dõi, đối soát thanh toán & Hoàn cọc", "Kế toán, Cổng VNPay", "Quản lý dòng tiền thu cọc/viện phí, đối soát tự động với VNPay và thực thi lệnh hoàn cọc."),
        ("UC-15", "Tự động hủy đơn quá 72h & Xếp phòng danh sách chờ", "Hệ thống (Scheduler)", "Quét định kỳ các đơn quá hạn thanh toán 72h, tự động thu hồi phòng và phân bổ cho Waitlist."),
        ("UC-16", "Báo cáo doanh thu, chi phí & Công suất phòng KTX", "Kế toán, Admin", "Xuất báo cáo thống kê tỷ lệ lấp đầy, doanh thu viện phí, công nợ và hiệu quả vận hành.")
    ]

    tbl_cat = doc.add_table(rows=len(uc_catalog)+1, cols=4)
    tbl_cat.alignment = WD_TABLE_ALIGNMENT.CENTER
    cat_w = [Inches(0.9), Inches(2.2), Inches(1.6), Inches(2.0)]
    for j, h in enumerate(["Mã UC", "Tên Use Case", "Tác nhân chính", "Phạm vi chức năng"]):
        c = tbl_cat.rows[0].cells[j]
        c.width = cat_w[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 50, 50, 60, 60)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (ucid, ucname, ucact, ucdesc) in enumerate(uc_catalog):
        row = tbl_cat.rows[i+1]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for j, val in enumerate([ucid, ucname, ucact, ucdesc]):
            c = row.cells[j]
            c.width = cat_w[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 40, 40, 60, 60)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
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

    add_styled_p(doc, space_after=10)

    # 2. Đặc tả chi tiết từng Use Case
    add_h2(doc, "2. Đặc Tả Chi Tiết Các Use Case Cốt Lõi (Đặc tả hết bước, sửa thẳng quy trình)")

    # Data for 5 Core UCs
    detailed_data = [
        {
            "id": "UC-01",
            "title": "Đăng nhập & Xác thực hệ thống (Sign in and Authenticate)",
            "desc": "Cho phép người dùng lựa chọn đăng nhập linh hoạt giữa Tên đăng nhập / Email trường cấp (@vnuk.edu.vn) hoặc MSSV kết hợp với Mật khẩu cá nhân, hệ thống kiểm tra và cấp phiên làm việc bảo mật (JWT Token).",
            "actors": "Sinh viên, Cán bộ KTX (Primary Actors); Dịch vụ xác thực trung tâm Trường A (Secondary Actor).",
            "precond": "Người dùng đã có tài khoản hợp lệ trên hệ thống KTX.",
            "postcond": "Phiên làm việc bảo mật được thiết lập, người dùng được chuyển hướng vào Dashboard theo đúng phân quyền.",
            "trigger": "Người dùng mở trang đăng nhập KTX và chọn 'Đăng nhập'.",
            "bf": [
                ("BF-1", "Người dùng", "Truy cập cổng đăng nhập của hệ thống KTX.", "Trigger: Mở màn hình Login"),
                ("BF-2", "Hệ thống", "Hiển thị biểu mẫu đăng nhập với ô nhập danh tính (cho phép nhập MSSV hoặc Email @vnuk.edu.vn) và Mật khẩu.", "Lựa chọn Tên/MSSV là 1 chức năng"),
                ("BF-3", "Người dùng", "Nhập thông tin định danh (MSSV hoặc Email) và mật khẩu, nhấn nút 'Đăng nhập'.", "Kiểm tra cú pháp đầu vào"),
                ("BF-4", "Hệ thống", "Kiểm tra tính hợp lệ của tài khoản, đối soát dữ liệu với cơ sở dữ liệu trường và băm mật khẩu để so khớp.", "Rẽ AF-A: Đăng nhập bằng Google SSO. Rẽ EF-A: Sai mật khẩu quá 5 lần. Rẽ EF-B: Tài khoản không hợp lệ."),
                ("BF-5", "Hệ thống", "Khởi tạo phiên làm việc bảo mật (JWT Token), ghi nhật ký đăng nhập và chuyển hướng người dùng vào Dashboard.", "[End of Use Case: mục tiêu đã đạt thành công].")
            ],
            "af": [
                ("AF-A – Đăng nhập nhanh qua Google SSO trường cấp", "BF-2", "Người dùng chọn đăng nhập bằng Google Workspace VNUK", [
                    ("AF-A-1", "Người dùng", "Nhấn nút 'Đăng nhập với Google (@vnuk.edu.vn)'.", "Chuyển hướng OAuth 2.0"),
                    ("AF-A-2", "Hệ thống", "Chuyển hướng sang trang xác thực Google và nhận mã ủy quyền hợp lệ.", "Kiểm tra tên miền @vnuk.edu.vn"),
                    ("AF-A-3", "Hệ thống", "Đối khớp email trường với hồ sơ sinh viên, cấp token và đưa vào Dashboard.", "Quay lại BF-5; [Outcome: kind: return, stepId: BF-5]")
                ]),
                ("AF-B – Quên mật khẩu và khôi phục trực tuyến", "BF-2", "Người dùng không nhớ mật khẩu đăng nhập", [
                    ("AF-B-1", "Người dùng", "Chọn 'Quên mật khẩu' và nhập email trường cấp.", "Yêu cầu khôi phục"),
                    ("AF-B-2", "Hệ thống", "Kiểm tra email, sinh mã OTP xác thực có hạn 15 phút và gửi về hộp thư.", "Bảo mật NFR-01"),
                    ("AF-B-3", "Người dùng", "Nhập mã OTP và đặt mật khẩu mới đạt độ phức tạp (BR-01).", "Cập nhật mật khẩu"),
                    ("AF-B-4", "Hệ thống", "Cập nhật mật khẩu đã băm, thông báo thành công và chuyển về trang đăng nhập.", "[Outcome: kind: return, stepId: BF-2]")
                ])
            ],
            "ef": [
                ("EF-A – Nhập sai mật khẩu quá 5 lần liên tiếp", "BF-4", "Người dùng nhập sai thông tin xác thực quá số lần quy định", [
                    ("EF-A-1", "Hệ thống", "Phát hiện sai mật khẩu 5 lần, kích hoạt cơ chế khóa tạm thời tài khoản trong 15 phút.", "Chống Brute-force NFR-01"),
                    ("EF-A-2", "Hệ thống", "Hiển thị thông báo tài khoản bị tạm khóa kèm thời gian mở lại và ghi nhật ký cảnh báo an ninh.", "[End of Use Case: chưa đạt mục tiêu trong lần thực hiện này. Outcome: kind: failureEnd]")
                ]),
                ("EF-B – Tài khoản không thuộc đối tượng tiếp nhận", "BF-4", "MSSV không tồn tại trong danh sách sinh viên hợp lệ của trường", [
                    ("EF-B-1", "Hệ thống", "Hiển thị cảnh báo: 'Tài khoản không thuộc diện được tiếp nhận tại KTX theo quy định BR-01'.", "Từ chối truy cập"),
                    ("EF-B-2", "Hệ thống", "Chặn phiên làm việc và hướng dẫn sinh viên liên hệ Phòng Đào tạo.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                ])
            ],
            "ref": "Áp dụng BR-01 (MSSV duy nhất & đối tượng hợp lệ). NFR-01 (Bảo mật mật khẩu, JWT)."
        },
        {
            "id": "UC-02",
            "title": "Đăng ký tài khoản & Khai báo thông tin/thói quen (Register Account & Lifestyle Survey)",
            "desc": "Sinh viên tạo tài khoản mới bằng Mã số sinh viên duy nhất trường cấp và thực hiện khai báo toàn bộ thông tin cá nhân kèm bộ 8 tiêu chí thói quen sinh hoạt phục vụ thuật toán phân phòng.",
            "actors": "Sinh viên (Primary Actor), Hệ thống KTX (Supporting).",
            "precond": "Sinh viên chưa có tài khoản trên hệ thống KTX và sở hữu MSSV trường cấp hợp lệ.",
            "postcond": "Tài khoản được tạo thành công, hồ sơ nếp sống 8 tiêu chí được lưu trữ sẵn sàng để đăng ký phòng.",
            "trigger": "Sinh viên chọn chức năng 'Đăng ký tài khoản mới' trên cổng dịch vụ KTX.",
            "bf": [
                ("BF-1", "Sinh viên", "Mở biểu mẫu đăng ký tài khoản từ trang chủ KTX.", "Trigger: Bắt đầu đăng ký"),
                ("BF-2", "Hệ thống", "Hiển thị form đăng ký gồm các trường định danh: MSSV, Họ tên, Email trường, SĐT và Mật khẩu khởi tạo.", "Kiểm tra MSSV duy nhất"),
                ("BF-3", "Sinh viên", "Nhập thông tin cá nhân và nhấn nút 'Tiếp tục khai báo nếp sống'.", "Gửi dữ liệu định danh. Rẽ EF-A: MSSV đã tồn tại."),
                ("BF-4", "Hệ thống", "Kiểm tra tính hợp lệ của MSSV theo quy định BR-01 và chuyển sang giao diện khảo sát nếp sống.", "Đối soát BR-01"),
                ("BF-5", "Sinh viên", "Điều chỉnh 8 thanh trượt thói quen (Giờ ngủ, Giờ dậy, Ngăn nắp, Độ ồn, Hút thuốc, Học tập, Tiếp bạn, Sở thích) và chọn 01 tiêu chí ưu tiên nhất (1.5x).", "Vector 8 chiều thói quen"),
                ("BF-6", "Sinh viên", "Nhấn nút 'Hoàn tất đăng ký & Lưu hồ sơ'.", "Xác nhận gửi toàn bộ hồ sơ"),
                ("BF-7", "Hệ thống", "Tạo tài khoản người dùng, băm mật khẩu, lưu vector thói quen và gửi email xác nhận kích hoạt.", "Hoàn tất lưu cơ sở dữ liệu"),
                ("BF-8", "Hệ thống", "Thông báo đăng ký thành công và tự động chuyển hướng sinh viên vào trang chủ cá nhân.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                ("AF-A – Nạp nhanh hồ sơ mẫu Persona có sẵn", "BF-5", "Sinh viên muốn điền nhanh các tiêu chí theo phong cách sống mẫu", [
                    ("AF-A-1", "Sinh viên", "Bấm nút 'Nạp hồ sơ Persona mẫu' (Thái Bảo - Chăm học / Văn Việt - Thể thao).", "Tính năng tiện ích UI"),
                    ("AF-A-2", "Hệ thống", "Tự động điền giá trị 8 thanh trượt theo mẫu đã chọn để sinh viên tinh chỉnh lại.", "Quay lại BF-6; [Outcome: kind: return, stepId: BF-6]")
                ])
            ],
            "ef": [
                ("EF-A – Mã sinh viên (MSSV) đã được đăng ký trước đó", "BF-3", "MSSV nhập vào đã có tài khoản trên hệ thống", [
                    ("EF-A-1", "Hệ thống", "Hiển thị thông báo: 'Mã sinh viên này đã được đăng ký tài khoản. Vui lòng sử dụng tính năng Đăng nhập hoặc Quên mật khẩu'.", "Ràng buộc BR-01 duy nhất"),
                    ("EF-A-2", "Hệ thống", "Dừng tiến trình và chuyển hướng sang màn hình Đăng nhập.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                ])
            ],
            "ref": "Áp dụng BR-01 (MSSV duy nhất), BR-09 (Trọng số 1.5x cho tiêu chí ưu tiên). NFR-05 (Giao diện trực quan)."
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
                ("BF-3", "Hệ thống", "Tạo bản ghi yêu cầu ghép phòng ở trạng thái 'Pending', thiết lập thời hạn phản hồi 48 giờ và gửi thông báo tức thì đến Sinh viên B.", "Tạo thông báo thời gian thực. Rẽ AF-B: A chủ động thu hồi."),
                ("BF-4", "Sinh viên B", "Đăng nhập hệ thống, mở thông báo nhận được và xem chi tiết hồ sơ đối chiếu 8 thói quen của Sinh viên A.", "Actor: Sinh viên B phản hồi. Rẽ AF-A: SV B từ chối yêu cầu."),
                ("BF-5", "Sinh viên B", "Nhấn nút 'Đồng ý kết bạn cùng phòng'.", "Xác nhận đồng thuận hai chiều"),
                ("BF-6", "Hệ thống", "Xác lập liên kết nhóm giữa SV A và SV B, cập nhật trạng thái 'Matched' ưu tiên xếp chung phòng và gửi thông báo chúc mừng tới cả hai sinh viên.", "BR-05: Hoàn tất ghép cặp"),
                ("BF-7", "Hệ thống", "Đóng yêu cầu thành công và cập nhật bảng danh sách bạn cùng phòng của cả hai bên.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                ("AF-A – Sinh viên B từ chối lời mời ghép phòng", "BF-4", "Sinh viên B sau khi xem xét thấy không phù hợp về thói quen sinh hoạt", [
                    ("AF-A-1", "Sinh viên B", "Nhấn nút 'Từ chối' kèm lời nhắn lịch sự (tùy chọn).", "B từ chối lời mời"),
                    ("AF-A-2", "Hệ thống", "Cập nhật trạng thái yêu cầu thành 'Declined', giải phóng cờ chờ cho cả hai bên.", "Hủy trạng thái Pending"),
                    ("AF-A-3", "Hệ thống", "Gửi thông báo nhẹ nhàng đến Sinh viên A để A tiếp tục tìm kiếm ứng viên khác trên hệ thống.", "[End of Use Case: kết thúc với trạng thái không ghép. Outcome: kind: successEnd]")
                ]),
                ("AF-B – Sinh viên A chủ động thu hồi lời mời trước khi B phản hồi", "BF-3", "Sinh viên A đổi ý muốn kết nối với bạn khác khi B chưa bấm duyệt", [
                    ("AF-B-1", "Sinh viên A", "Mở danh sách lời mời đã gửi và nhấn 'Thu hồi yêu cầu'.", "A chủ động hủy"),
                    ("AF-B-2", "Hệ thống", "Hủy bản ghi yêu cầu Pending, thu hồi thông báo hiển thị phía B và cập nhật lại trạng thái khả dụng cho A.", "[Outcome: kind: successEnd]")
                ])
            ],
            "ef": [
                ("EF-A – Không đủ điều kiện ràng buộc ghép đôi", "BF-2", "Hai sinh viên khác giới tính, khác loại phòng đăng ký hoặc đối phương đã chốt nhóm", [
                    ("EF-A-1", "Hệ thống", "Chặn gửi yêu cầu và thông báo lý do cụ thể (Ví dụ: 'Bạn và ứng viên không đăng ký cùng loại phòng' hoặc 'Ứng viên đã có phòng chính thức').", "Kiểm soát an toàn"),
                    ("EF-A-2", "Hệ thống", "Giữ nguyên trạng thái và hướng dẫn SV A chọn bạn khác phù hợp với tiêu chí.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                ]),
                ("EF-B – Yêu cầu hết hạn 48 giờ không phản hồi", "BF-3", "Quá 48 giờ kể từ khi gửi nhưng Sinh viên B không thực hiện chấp nhận hay từ chối", [
                    ("EF-B-1", "Hệ thống", "Bộ lập lịch quét quá hạn, tự động chuyển trạng thái yêu cầu sang 'Expired' (Hết hạn).", "Tự động dọn dẹp"),
                    ("EF-B-2", "Hệ thống", "Gửi thông báo cho SV A về việc yêu cầu đã hết hạn để SV A chủ động gửi lời mời tới người khác.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                ])
            ],
            "ref": "Áp dụng BR-05 (Cơ chế Request hai chiều), BR-06 (Quy tắc lấp đầy phòng), BR-09 (Điểm hòa hợp 1.5x)."
        },
        {
            "id": "UC-07",
            "title": "Thanh toán tiền phòng & Đặt cọc giữ chỗ 72h (Dormitory Payment & Deposit)",
            "desc": "Sinh viên thực hiện thanh toán trực tuyến tiền phòng kỳ 1 kèm tiền đặt cọc giữ chỗ 2.000.000đ qua cổng VNPay trong hạn chót 72 giờ; hệ thống tự động xác thực, chốt phòng và tạo/in biên lai thu tiền điện tử trực tiếp trong luồng chính.",
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
                ("BF-7", "Hệ thống", "Tự động tạo Biên lai thu tiền điện tử có mã tra cứu và hiển thị nút 'In biên lai' / 'Tải file PDF biên lai' trực tiếp trên màn hình kết quả.", "TẠO VÀ IN BIÊN LAI TRỰC TIẾP TRONG BF"),
                ("BF-8", "Sinh viên", "Xem biên lai, bấm in hoặc tải file biên lai về máy và nhận phòng thành công.", "[End of Use Case: mục tiêu đã đạt thành công. Outcome: kind: successEnd].")
            ],
            "af": [
                ("AF-A – Thanh toán qua Chuyển khoản ngân hàng có mã định danh (Virtual Account)", "BF-3", "Sinh viên không sử dụng ví quét QR mà muốn chuyển khoản qua tài khoản ngân hàng", [
                    ("AF-A-1", "Sinh viên", "Chọn 'Chuyển khoản theo số tài khoản định danh KTX'.", "Phương thức thanh toán thay thế"),
                    ("AF-A-2", "Hệ thống", "Cung cấp số tài khoản ảo duy nhất kèm cú pháp nội dung chuyển khoản tự động khớp lệnh.", "Tích hợp Open Banking"),
                    ("AF-A-3", "Hệ thống", "Nhận tín hiệu báo có từ ngân hàng, tự động gạch nợ và chuyển sang bước BF-6 để tạo biên lai.", "[Outcome: kind: return, stepId: BF-6]")
                ])
            ],
            "ef": [
                ("EF-A – Giao dịch ngân hàng bị từ chối hoặc tài khoản không đủ số dư", "BF-5", "Số dư thẻ không đủ, thẻ hết hạn hoặc sinh viên hủy thao tác trên App ngân hàng", [
                    ("EF-A-1", "Cổng VNPay", "Gửi thông báo mã lỗi giao dịch thất bại về hệ thống KTX.", "Giao dịch lỗi"),
                    ("EF-A-2", "Hệ thống", "Hiển thị thông báo chi tiết lỗi, giữ nguyên tình trạng đơn trong hạn 72h và hướng dẫn sinh viên thử lại.", "[End of Use Case: mục tiêu chưa đạt trong lượt này. Outcome: kind: failureEnd]")
                ]),
                ("EF-B – Đơn thanh toán đã quá hạn 72 giờ quy định", "BF-2", "Thời gian thanh toán vượt quá 72 giờ kể từ lúc công bố kết quả", [
                    ("EF-B-1", "Hệ thống", "Khóa tính năng thanh toán, hiển thị thông báo kết quả giữ chỗ đã bị hủy do quá hạn 72h theo quy định BR-04.", "Tự động thu hồi suất phòng"),
                    ("EF-B-2", "Hệ thống", "Chuyển sinh viên sang danh sách chờ và kết thúc phiên làm việc.", "[End of Use Case: mục tiêu không đạt. Outcome: kind: failureEnd]")
                ])
            ],
            "ref": "Áp dụng BR-04 (Hạn cọc 72h), BR-07 (Quy định bảo lưu cọc). NFR-04 (Bảo mật giao dịch, đối soát SHA-256)."
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
                ("AF-A – Sinh viên trả phòng đúng hạn, nguyên vẹn tài sản và không phát sinh nợ", "BF-4", "Phòng bảo quản hoàn hảo, công tơ điện nước trong định mức tiêu chuẩn", [
                    ("AF-A-1", "Hệ thống", "Xác định chi phí khấu trừ bằng 0, duyệt hoàn trả đủ 100% tiền cọc (2.000.000 VNĐ).", "Hoàn cọc 100%"),
                    ("AF-A-2", "Hệ thống", "Chuyển thẳng sang bước lập lệnh hoàn tiền nhanh cho Kế toán.", "[Outcome: kind: return, stepId: BF-5]")
                ])
            ],
            "ef": [
                ("EF-A – Chi phí hư hại tài sản và công nợ vượt quá số tiền cọc 2.000.000đ", "BF-4", "Tài sản bị hư hại nặng hoặc vi phạm nội quy lớn khiến tổng phạt > 2.000.000đ", [
                    ("EF-A-1", "Hệ thống", "Tính toán số tiền chênh lệch thiếu hụt (Phát sinh âm sau khi trừ hết tiền cọc).", "Ghi nhận công nợ phụ"),
                    ("EF-A-2", "Cán bộ KTX", "Lập biên bản vi phạm kỷ luật, yêu cầu sinh viên thanh toán bổ sung phần thiếu trước khi cấp giấy chứng nhận hoàn tất thủ tục KTX.", "Xử lý bồi thường bổ sung"),
                    ("EF-A-3", "Hệ thống", "Treo trạng thái thanh lý cho đến khi sinh viên nộp đủ khoản bồi thường phụ trội.", "[End of Use Case: mục tiêu chưa hoàn tất. Outcome: kind: failureEnd]")
                ])
            ],
            "ref": "Áp dụng BR-02 (Thời hạn hợp đồng), BR-07 (Quy tắc quyết toán và hoàn cọc). NFR-06 (Ghi nhật ký kiểm kê và bàn giao)."
        }
    ]

    for uc in detailed_data:
        add_h3(doc, f"{uc['id']}: {uc['title']}")
        
        # Summary
        tbl_s = doc.add_table(rows=5, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        s_rows = [
            ("Description", uc["desc"]),
            ("Actors", uc["actors"]),
            ("Preconditions", uc["precond"]),
            ("Postconditions", uc["postcond"]),
            ("Trigger", uc["trigger"])
        ]
        for idx, (k, v) in enumerate(s_rows):
            row = tbl_s.rows[idx]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width, c1.width = Inches(1.5), Inches(5.2)
            set_cell_background(c0, "F1F5F9")
            set_cell_background(c1, "FFFFFF")
            set_cell_margins(c0, 40, 40, 60, 60)
            set_cell_margins(c1, 40, 40, 60, 60)
            set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            p0 = c0.paragraphs[0].add_run(k)
            p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(8.5), True
            p0.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
            p1 = c1.paragraphs[0].add_run(v)
            p1.font.name, p1.font.size = 'Times New Roman', Pt(8.5)
            p1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=3)

        # BF
        tbl_bf = doc.add_table(rows=len(uc["bf"])+1, cols=4)
        tbl_bf.alignment = WD_TABLE_ALIGNMENT.CENTER
        bf_w = [Inches(0.8), Inches(1.3), Inches(2.7), Inches(1.9)]
        for j, h in enumerate(["Step ID", "Actor", "Action", "Notes and References"]):
            c = tbl_bf.rows[0].cells[j]
            c.width = bf_w[j]
            set_cell_background(c, "0F172A")
            set_cell_margins(c, 40, 40, 60, 60)
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
                set_cell_margins(c, 30, 30, 60, 60)
                set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
                p = c.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                r = p.add_run(val)
                r.font.name, r.font.size = 'Times New Roman', Pt(8)
                if j == 0:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x0F, 0x76, 0x6E)
                elif j == 1:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
                else:
                    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=3)

        # AF
        for af_name, af_pt, af_cond, af_steps in uc["af"]:
            add_body(doc, f"• {af_name} (Branch point: {af_pt} | Condition: {af_cond})", bold=True, color_rgb=(0x15, 0x80, 0x3D))
            tbl_af = doc.add_table(rows=len(af_steps), cols=4)
            tbl_af.alignment = WD_TABLE_ALIGNMENT.CENTER
            for i, (sid, sact, saction, sref) in enumerate(af_steps):
                row = tbl_af.rows[i]
                for j, val in enumerate([sid, sact, saction, sref]):
                    c = row.cells[j]
                    c.width = bf_w[j]
                    set_cell_background(c, "F0FDF4")
                    set_cell_margins(c, 25, 25, 50, 50)
                    set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'DCFCE7'}, bottom={'val': 'single', 'sz': 4, 'color': 'DCFCE7'})
                    p = c.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    r = p.add_run(val)
                    r.font.name, r.font.size = 'Times New Roman', Pt(8)
                    if j == 0:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
                    else:
                        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
            add_styled_p(doc, space_after=2)

        # EF
        for ef_name, ef_pt, ef_cond, ef_steps in uc["ef"]:
            add_body(doc, f"• {ef_name} (Branch point: {ef_pt} | Condition: {ef_cond})", bold=True, color_rgb=(0xB9, 0x1C, 0x1C))
            tbl_ef = doc.add_table(rows=len(ef_steps), cols=4)
            tbl_ef.alignment = WD_TABLE_ALIGNMENT.CENTER
            for i, (sid, sact, saction, sref) in enumerate(ef_steps):
                row = tbl_ef.rows[i]
                for j, val in enumerate([sid, sact, saction, sref]):
                    c = row.cells[j]
                    c.width = bf_w[j]
                    set_cell_background(c, "FEF2F2")
                    set_cell_margins(c, 25, 25, 50, 50)
                    set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'FEE2E2'}, bottom={'val': 'single', 'sz': 4, 'color': 'FEE2E2'})
                    p = c.paragraphs[0]
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    r = p.add_run(val)
                    r.font.name, r.font.size = 'Times New Roman', Pt(8)
                    if j == 0:
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0xB9, 0x1C, 0x1C)
                    else:
                        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
            add_styled_p(doc, space_after=2)

        add_body(doc, f"Thông tin bổ sung: {uc['ref']}", italic=True, color_rgb=(0x1E, 0x3A, 0x8A))
        add_styled_p(doc, space_after=6)

    docx_path = os.path.join(os.path.dirname(__file__), "docs", "Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.docx")
    dl_path = os.path.join(r"C:\Users\LENOVO\Downloads", "Dac_Ta_Use_Case_KTX_Smart_Match_VNUK.docx")
    doc.save(docx_path)
    shutil.copy2(docx_path, dl_path)
    print(f"[SUCCESS] Saved Spec DOCX to {dl_path}")

# ==============================================================================
# 3. BUILD DIAGRAMS & SEQUENCE DOCUMENT (RIÊNG BIỆT)
# ==============================================================================
def build_diagram_doc():
    doc = docx.Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.27), Inches(11.69)
        s.top_margin, s.bottom_margin = Inches(0.8), Inches(0.8)
        s.left_margin, s.right_margin = Inches(0.85), Inches(0.85)

    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=4)
    r = p_title.add_run("BỘ SƠ ĐỒ USE CASE & SEQUENCE DIAGRAM CHUẨN VÒNG ĐỜI\n(SYSTEM DIAGRAMS & SEQUENCE SPECIFICATION)")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(16), True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    r = p_sub.add_run("Hệ thống: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nChuẩn hóa thanh kích hoạt vòng đời (Activation Bars) & Khớp 1-1 với Bảng đặc tả")
    r.font.name, r.font.size, r.font.italic = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    add_h2(doc, "1. Sơ đồ Use Case Tổng Thể Hệ Thống (Vẽ lại Tinh gọn)")
    add_body(doc, "Hệ thống KTX Smart Match được phân chia thành 2 phân hệ rõ ràng: Phân hệ Sinh viên (Cổng dịch vụ trực tuyến) và Phân hệ Quản trị / Vận hành KTX (Dành cho Admin, Cán bộ KTX, Kế toán và Kỹ thuật).")
    
    uc_ascii = """+----------------------------------------------------------------------------------------------------+
|                                    HỆ THỐNG KTX SMART MATCH                                        |
+----------------------------------------------------------------------------------------------------+
| [PHÂN HỆ SINH VIÊN]                                                                                |
|   (UC-01: Đăng nhập & Xác thực) <---- Sinh viên / Cán bộ KTX                                       |
|   (UC-02: Đăng ký & Khai báo nếp sống) <---- Sinh viên                                             |
|   (UC-03: Cập nhật hồ sơ & thói quen) <---- Sinh viên (<<extend>> Nạp Persona)                    |
|   (UC-04: Chọn loại phòng & Nộp đơn KTX) <---- Sinh viên                                           |
|   (UC-05: Ghép bạn theo yêu cầu Matching Request) <---- Sinh viên A (Gửi) & Sinh viên B (Nhận)      |
|   (UC-06: Xem kết quả phân phòng & giá) <---- Sinh viên                                            |
|   (UC-07: Thanh toán viện phí & Đặt cọc 72h) <---- Sinh viên & Cổng VNPay (Tạo/In biên lai trong BF)|
|   (UC-08: Thủ tục Trả phòng & Quyết toán Check-out) <---- Sinh viên, Cán bộ KTX, Kế toán           |
|   (UC-09: Yêu cầu chuyển phòng / chuyển bạn) <---- Sinh viên                                       |
|   (UC-10: Gửi phản ánh & Báo hỏng cơ sở vật chất) <---- Sinh viên                                  |
+----------------------------------------------------------------------------------------------------+
| [PHÂN HỆ QUẢN TRỊ & VẬN HÀNH]                                                                      |
|   (UC-11: Quản lý danh mục tòa, phòng, giá) <---- Quản trị viên (Admin)                            |
|   (UC-12: Thẩm định & Phê duyệt đơn Business Approve) <---- Cán bộ KTX (Staff)                     |
|   (UC-13: Khởi chạy Phân bổ phòng tự động Gale-Shapley & Lấp đầy 100%) <---- Hệ thống (Scheduler) |
|   (UC-14: Theo dõi, đối soát thanh toán & Hoàn cọc) <---- Kế toán KTX & VNPay                      |
|   (UC-15: Tự động hủy đơn quá 72h & Xếp phòng Waitlist) <---- Hệ thống (Scheduler)                 |
|   (UC-16: Báo cáo doanh thu & Công suất lấp đầy) <---- Kế toán & Quản trị viên                     |
+----------------------------------------------------------------------------------------------------+"""

    p_box = add_styled_p(doc, space_before=4, space_after=8)
    r_b = p_box.add_run(uc_ascii)
    r_b.font.name, r_b.font.size = 'Consolas', Pt(7.5)
    r_b.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    add_h2(doc, "2. Sequence Diagram 1: Ghép bạn cùng phòng theo yêu cầu (Matching by Request - UC-05)")
    add_body(doc, "Khắc phục triệt để lỗi vẽ sai vòng đời: Phân định rõ 2 tác nhân con người (SV A và SV B); thanh kích hoạt (Activation Bars) mở ra khi nhận thông điệp và đóng lại khi hoàn tất (deactivate), thể hiện đúng 2 giai đoạn tương tác bất đồng bộ:")

    seq_1 = """sequenceDiagram
    autonumber
    actor SVA as 🧑 Sinh viên A (Gửi Request)
    participant UI as 🖥️ Giao diện KTX Web
    participant MatchSvc as ⚙️ Matching Service
    participant DB as 🗄️ Database KTX
    actor SVB as 🧑 Sinh viên B (Nhận Request)

    Note over SVA, SVB: GIAI ĐOẠN 1: SINH VIÊN A GỬI YÊU CẦU GHÉP PHÒNG
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
        MatchSvc->>SVA: 25. (AF-A-3) Gửi thông báo tới A: "Lời mời chưa được chấp thuận"
        deactivate MatchSvc
        UI-->>SVB: 26. (AF-A-3) Xác nhận đóng yêu cầu thành công
        deactivate UI
    end"""

    p_s1 = add_styled_p(doc, space_before=2, space_after=8)
    r1 = p_s1.add_run(seq_1)
    r1.font.name, r1.font.size = 'Consolas', Pt(7.5)
    r1.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    add_h2(doc, "3. Sequence Diagram 2: Thanh toán tiền phòng & Tạo/In biên lai trực tiếp (UC-07)")
    add_body(doc, "Bước tạo và in biên lai điện tử nằm trực tiếp trong luồng chính Basic Flow sau khi cổng VNPay trả về kết quả thành công:")

    seq_2 = """sequenceDiagram
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
    deactivate UI"""

    p_s2 = add_styled_p(doc, space_before=2, space_after=8)
    r2 = p_s2.add_run(seq_2)
    r2.font.name, r2.font.size = 'Consolas', Pt(7.5)
    r2.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    add_h2(doc, "4. Sequence Diagram 3: Thủ tục Trả phòng & Quyết toán cọc Check-out (UC-08)")
    add_body(doc, "Quy trình kết thúc thời hạn lưu trú phản ánh đúng vòng đời: Kiểm kê tài sản -> Khấu trừ nợ -> Hoàn cọc theo BR-07 -> Bàn giao & Giải phóng giường trống:")

    seq_3 = """sequenceDiagram
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
    deactivate UI"""

    p_s3 = add_styled_p(doc, space_before=2, space_after=8)
    r3 = p_s3.add_run(seq_3)
    r3.font.name, r3.font.size = 'Consolas', Pt(7.5)
    r3.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    docx_path = os.path.join(os.path.dirname(__file__), "docs", "Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.docx")
    dl_path = os.path.join(r"C:\Users\LENOVO\Downloads", "Bo_Diagram_Va_Sequence_KTX_Smart_Match_VNUK.docx")
    doc.save(docx_path)
    shutil.copy2(docx_path, dl_path)
    print(f"[SUCCESS] Saved Diagram DOCX to {dl_path}")

if __name__ == "__main__":
    build_br_doc()
    build_spec_doc()
    build_diagram_doc()
    print("All 3 separate Word documents generated successfully.")
