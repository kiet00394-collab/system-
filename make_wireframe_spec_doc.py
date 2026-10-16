import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
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
            element.set(qn('w:color'), edge_data.get('color', 'CCCCCC'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def add_styled_paragraph(doc, text="", style='Normal', space_before=0, space_after=5, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph(text, style=style)
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    return p

def add_heading_1(doc, text):
    p = add_styled_paragraph(doc, space_before=14, space_after=6)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    return p

def add_heading_2(doc, text):
    p = add_styled_paragraph(doc, space_before=10, space_after=4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x2C, 0x52, 0x82)
    return p

def add_heading_3(doc, text):
    p = add_styled_paragraph(doc, space_before=6, space_after=2)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    return p

def add_body(doc, text, bold=False, italic=False):
    p = add_styled_paragraph(doc, space_before=0, space_after=5, line_spacing=1.2)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    return p

def add_bullet(doc, text, bold_prefix="", level=0):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.2
    p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Times New Roman'
        r_pre.font.size = Pt(12)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
        
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x37, 0x41, 0x51)
    return p

def render_uc_summary_table(doc, summary_data):
    tbl = doc.add_table(rows=len(summary_data), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    col_widths = [Inches(1.8), Inches(4.8)]
    for i, (k, v) in enumerate(summary_data):
        r = tbl.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width, c1.width = col_widths[0], col_widths[1]
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'}, bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'}, bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(10.5), True
        r0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(10.5)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    add_styled_paragraph(doc, space_after=8)

def render_flow_table(doc, flow_data, title="Basic Flow (Happy Path)"):
    add_heading_3(doc, title)
    tbl = doc.add_table(rows=len(flow_data) + 1, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Inches(0.9), Inches(1.2), Inches(3.0), Inches(1.5)]
    headers = ["Step ID", "Tác nhân (Actor)", "Hành động thực hiện (Action)", "Ghi chú / Tham chiếu"]
    
    # Header
    for j, h in enumerate(headers):
        c = tbl.rows[0].cells[j]
        c.width = widths[j]
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    for i, row_data in enumerate(flow_data):
        row = tbl.rows[i + 1]
        bg = "F8FAFC" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 or j == 1 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name, r.font.size = 'Times New Roman', Pt(9.5)
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            else:
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    add_styled_paragraph(doc, space_after=8)

def build_document():
    doc = docx.Document()

    # Lề chuẩn A4
    for s in doc.sections:
        s.top_margin = Inches(0.9)
        s.bottom_margin = Inches(0.9)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(0.9)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)

    # ==================== TRANG BÌA ====================
    p_inst = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r_inst = p_inst.add_run("ĐẠI HỌC ĐÀ NẴNG\nVIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK)")
    r_inst.font.name, r_inst.font.size, r_inst.font.bold = 'Times New Roman', Pt(11), True
    r_inst.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_sub = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    r_sub = p_sub.add_run("BỘ MÔN CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r_sub.font.name, r_sub.font.size = 'Times New Roman', Pt(10.5)
    r_sub.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    p_title = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=14, space_after=6)
    r_title = p_title.add_run("HỒ SƠ ĐẶC TẢ USE CASE VÀ BẢN VẼ WIREFRAME\n(USE CASE SPECIFICATION & UI WIREFRAMES)")
    r_title.font.name, r_title.font.size, r_title.font.bold = 'Times New Roman', Pt(16), True
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_desc = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    r_desc = p_desc.add_run("Đề tài: Hệ thống ghép bạn cùng phòng Ký túc xá thông minh theo độ tương thích (KTX Smart Roommate Matching)\nSoạn thảo chuẩn xác theo cấu trúc tài liệu giảng dạy: Summary, Three Types of Flows, Business Rules, NFRs và Wireframe UI")
    r_desc.font.name, r_desc.font.size, r_desc.font.italic = 'Times New Roman', Pt(11), True
    r_desc.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Bảng Metadata
    tbl_meta = doc.add_table(rows=4, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_info = [
        ("Môn học / Đồ án:", "Nhập môn Kỹ thuật Phần mềm & Trí tuệ Nhân tạo (CKI 2026)"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 3 (Đại diện VNUK - SPKT - DUE)"),
        ("Tài liệu tham chiếu chuẩn:", "Use Case Specification Slides (Giảng viên hướng dẫn)"),
        ("Phạm vi chuyển giao:", "Đặc tả chi tiết các Use Case cốt lõi & Thiết kế bản vẽ Wireframe tương ứng")
    ]
    for i, (k, v) in enumerate(meta_info):
        r = tbl_meta.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.4)
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'}, bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'CBD5E1'}, bottom={'val': 'single', 'sz': 4, 'color': 'CBD5E1'})
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(10.5), True
        r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(10.5)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_paragraph(doc, space_after=14)

    # ==================== PHẦN 1 ====================
    add_heading_1(doc, "1. CẤU TRÚC CHUẨN CỦA HỒ SƠ ĐẶC TẢ USE CASE VÀ WIREFRAME")
    add_body(doc, "Căn cứ theo bài giảng hướng dẫn 'Use Case Specification' của Giảng viên, một tài liệu đặc tả ca sử dụng hoàn chỉnh không chỉ dừng lại ở biểu đồ UML tổng quan, mà bắt buộc phải mô tả chi tiết bằng văn bản và minh họa bằng bản vẽ giao diện (Wireframe).")
    add_body(doc, "Tài liệu này được biên soạn đầy đủ theo cấu trúc chuẩn bao gồm:")
    add_bullet(doc, "Gồm mã số định danh (ID), Tên Use Case (Title theo cấu trúc Verb + Noun Phrase), Mô tả mục đích (Description), Tác nhân (Actors), Điều kiện tiên quyết (Preconditions), Điều kiện kết thúc (Post conditions), và Sự kiện kích hoạt (Trigger).", "Phần 1 - Tóm tắt (Summary): ")
    add_bullet(doc, "Gồm Luồng cơ sở thành công (Basic Flow - Happy Path), Các luồng rẽ nhánh mở rộng (Alternate Flows - AF) và Các luồng ngoại lệ xử lý sự cố (Exception Flows - EF) với bảng đánh số bước rõ ràng (Step ID, Actor, Action, Notes).", "Phần 2 - Ba loại luồng sự kiện (Three Types of Flows): ")
    add_bullet(doc, "Gồm Quy tắc nghiệp vụ (Business Rules) và Yêu cầu phi chức năng (Non-functional Requirements).", "Phần 3 - Thông tin bổ trợ (Additional Information): ")
    add_bullet(doc, "Bản vẽ minh họa trực quan giao diện người dùng tương ứng cho từng màn hình của Use Case, đánh số callout chú thích rõ ràng các vùng nhập liệu và nút bấm.", "Phần 4 - Bản vẽ Wireframe (Wireframes): ")

    # ==================== ĐẶC TẢ USE CASE 1 ====================
    add_heading_1(doc, "2. ĐẶC TẢ CHI TIẾT USE CASE UC-01: ĐĂNG NHẬP VÀ XÁC THỰC KÝ TÚC XÁ")
    add_heading_2(doc, "2.1 Bảng tóm tắt Use Case (Summary)")
    render_uc_summary_table(doc, [
        ("ID:", "UC-01"),
        ("Title:", "Đăng nhập hệ thống Ký túc xá (Log in to Dormitory Portal)"),
        ("Description:", "Use Case này mô tả cách thức sinh viên nội trú hoặc ban quản lý xác thực danh tính vào hệ thống ghép phòng KTX."),
        ("Actors:", "Sinh viên (Primary Actor), Ban quản lý KTX, Hệ thống (System Engine)."),
        ("Preconditions:", "Người dùng đã được cấp tài khoản hoặc có Mã sinh viên hợp lệ tại các trường thành viên Đại học Đà Nẵng (VNUK, SPKT, DUE...)."),
        ("Post conditions:", "Người dùng được xác thực thành công, hệ thống cấp phiên làm việc (Session) và điều hướng về màn hình Dashboard."),
        ("Trigger:", "Sinh viên truy cập vào cổng dịch vụ KTX và bấm chọn đăng nhập.")
    ])

    add_heading_2(doc, "2.2 Ba loại luồng sự kiện (Three Types of Flows)")
    # Basic Flow
    render_flow_table(doc, [
        ("BF-1", "Sinh viên", "Truy cập đường dẫn cổng KTX và chuyển đến màn hình Đăng nhập (Wireframe WF-01).", "Giao diện hiển thị form nhập liệu và 3 thẻ Persona mẫu."),
        ("BF-2", "Sinh viên", "Nhập Mã sinh viên, Mật khẩu và chọn Trường đại học trực thuộc.", "Tham chiếu trường dữ liệu bắt buộc."),
        ("BF-3", "Hệ thống", "Gọi Use Case được include 'Xác thực thông tin sinh viên' để kiểm tra tính hợp lệ.", "Include UC-03."),
        ("BF-4", "Hệ thống", "Cấp phiên làm việc an toàn và điều hướng người dùng vào Dashboard xếp phòng.", "Hoàn tất mục tiêu Use Case (Goal met).")
    ], title="Luồng cơ bản (Basic Flow - Happy Path)")

    # Alternate Flow
    render_flow_table(doc, [
        ("AF-A1", "Sinh viên", "Tại bước BF-1, sinh viên nhấp chọn một trong 3 thẻ Persona mẫu (Thái Bảo - VNUK, Văn Việt - SPKT, Minh Quân - DUE).", "Hành vi tùy chọn nhanh."),
        ("AF-A2", "Hệ thống", "Tự động điền thông tin định danh tương ứng và đăng nhập tức thì vào Dashboard mà không cần gõ phím.", "Hoàn tất mục tiêu Use Case.")
    ], title="Luồng rẽ nhánh (Alternate Flow AF-A: Đăng nhập nhanh bằng Persona mẫu)")

    # Exception Flows
    render_flow_table(doc, [
        ("EF-A1", "Hệ thống", "Tại bước BF-3, nếu Mã sinh viên hoặc Mật khẩu không chính xác, hệ thống từ chối đăng nhập.", "Mục tiêu không đạt (Goal not met)."),
        ("EF-A2", "Hệ thống", "Hiển thị hộp cảnh báo màu đỏ 'Thông tin đăng nhập không chính xác' và giữ nguyên giao diện để người dùng nhập lại.", "Quay về BF-2.")
    ], title="Luồng ngoại lệ (Exception Flow EF-A: Sai thông tin xác thực)")

    add_heading_2(doc, "2.3 Quy tắc nghiệp vụ và Yêu cầu phi chức năng")
    add_bullet(doc, "Mã sinh viên phải tuân thủ định dạng của Đại học Đà Nẵng (ví dụ: 22VNUK..., 21SPKT..., 22DUE...).", "BR-01 (Định dạng tài khoản): ")
    add_bullet(doc, "Tài khoản sinh viên thuộc nhóm A (sinh viên cũ) và nhóm B (tân sinh viên) được phân quyền bình đẳng trong việc khai báo và tìm bạn cùng phòng.", "BR-02 (Quyền hạn sinh viên): ")
    add_bullet(doc, "Thời gian xác thực và điều hướng vào trang Dashboard phải nhỏ hơn 1.0 giây.", "NFR-01 (Thời gian đáp ứng): ")
    add_bullet(doc, "Giao diện đăng nhập tương thích tốt trên cả máy tính để bàn, máy tính bảng và điện thoại thông minh.", "NFR-02 (Tính khả dụng Usability): ")

    add_heading_2(doc, "2.4 Đặc tả bản vẽ Wireframe WF-01 (Màn hình Đăng nhập)")
    add_body(doc, "Bản vẽ Wireframe WF-01 được thiết kế theo bố cục 2 cột cân xứng (truy cập trực tiếp tại http://localhost:8000/wireframe tab WF-01):")
    add_bullet(doc, "Cụm 3 thẻ Persona đại diện cho 3 trường (VNUK, SPKT, DUE) có ảnh đại diện, tóm tắt phong cách sống và nút 'Vào ngay' phục vụ đăng nhập nhanh 1 chạm.", "[Khu vực bên trái - Callout 1]: ")
    add_bullet(doc, "Biểu mẫu nhập liệu chuẩn gồm: Dropdown chọn trường, ô nhập Mã sinh viên, ô nhập Mật khẩu và nút hành động chính 'ĐĂNG NHẬP HỆ THỐNG'.", "[Khu vực bên phải - Callout 2]: ")
    add_bullet(doc, "Khối thông báo đỏ nổi bật xuất hiện ngay khi kích hoạt ngoại lệ EF-A.", "[Vùng hiển thị lỗi - Callout 3]: ")

    # ==================== ĐẶC TẢ USE CASE 2 ====================
    add_heading_1(doc, "3. ĐẶC TẢ CHI TIẾT USE CASE UC-04: KHAI BÁO THÓI QUEN SINH HOẠT VÀ NẠP MẪU")
    add_heading_2(doc, "3.1 Bảng tóm tắt Use Case (Summary)")
    render_uc_summary_table(doc, [
        ("ID:", "UC-04"),
        ("Title:", "Khai báo thói quen sinh hoạt (Declare Living Habits)"),
        ("Description:", "Use Case này cho phép sinh viên khai báo 8 tiêu chí nếp sống thực tế và chỉ định tiêu chí ưu tiên số một của bản thân."),
        ("Actors:", "Sinh viên (Primary Actor)."),
        ("Preconditions:", "Sinh viên đã đăng nhập thành công vào hệ thống (hoàn tất UC-01)."),
        ("Post conditions:", "Hồ sơ thói quen được lưu trữ tạm thời và truyền sang thuật toán chấm điểm tương thích hai chiều."),
        ("Trigger:", "Sinh viên truy cập vào Dashboard và điều chỉnh các trường dữ liệu trên form.")
    ])

    add_heading_2(doc, "3.2 Ba loại luồng sự kiện (Three Types of Flows)")
    render_flow_table(doc, [
        ("BF-1", "Sinh viên", "Mở biểu mẫu khảo sát tại cột bên trái của Dashboard (Wireframe WF-02).", "Hiển thị 8 tiêu chí chuẩn hóa."),
        ("BF-2", "Sinh viên", "Chọn phân nhóm KTX (Nhóm A: sinh viên cũ, Nhóm B: tân sinh viên).", "Phân nhóm hai phía của Gale-Shapley."),
        ("BF-3", "Sinh viên", "Kéo thanh trượt Giờ đi ngủ (sleep: 20h - 04h sáng) và Giờ thức dậy (wake: 05h - 11h).", "Hiển thị nhãn thời gian thực trực quan."),
        ("BF-4", "Sinh viên", "Chọn mức độ Ngăn nắp (tidy: 1-5) và Khả năng chịu tiếng ồn (noise: 1-5).", "Thang đo 5 mức."),
        ("BF-5", "Sinh viên", "Chọn Thói quen học tập (study), Tình trạng hút thuốc (smoke: 0/1) và Tần suất dắt bạn về phòng (guests).", "Bộ lọc tiêu chí sinh hoạt."),
        ("BF-6", "Sinh viên", "Tích chọn các sở thích chung (Đọc sách, Thể thao, Game, Nhạc, Nấu ăn, Xem phim).", "Tính độ tương đồng Jaccard."),
        ("BF-7", "Sinh viên", "Chọn tiêu chí ưu tiên số 1 (top priority) tại dropdown nổi bật màu vàng.", "Hệ số nhân 1.5x."),
        ("BF-8", "Sinh viên", "Nhấn nút 'TÍNH TOÁN & CẬP NHẬT XẾP HẠNG'.", "Kích hoạt chuyển sang UC-06.")
    ], title="Luồng cơ bản (Basic Flow - Happy Path)")

    render_flow_table(doc, [
        ("AF-A1", "Sinh viên", "Tại bước BF-1, sinh viên nhấp chọn 1 trong 3 nút Persona mẫu (Thái Bảo, Văn Việt, Minh Quân).", "Extend UC-05."),
        ("AF-A2", "Hệ thống", "Tự động điền trước toàn bộ 8 thông số tương ứng và tự động kích hoạt tính toán xếp hạng.", "Hoàn tất mục tiêu Use Case.")
    ], title="Luồng rẽ nhánh (Alternate Flow AF-A: Nạp nhanh hồ sơ Persona)")

    render_flow_table(doc, [
        ("EF-A1", "Hệ thống", "Nếu sinh viên chọn giờ đi ngủ và giờ thức dậy trùng nhau hoặc không hợp lý (ví dụ: ngủ 6h dậy 6h), hệ thống cảnh báo.", "Cảnh báo logic."),
        ("EF-A2", "Sinh viên", "Điều chỉnh lại thanh trượt thời gian về khoảng hợp lệ và tiếp tục.", "Quay về BF-3.")
    ], title="Luồng ngoại lệ (Exception Flow EF-A: Dữ liệu thời gian không hợp lệ)")

    add_heading_2(doc, "3.3 Quy tắc nghiệp vụ và Yêu cầu phi chức năng")
    add_bullet(doc, "Tiêu chí ưu tiên số 1 được nhân trọng số 1.5x trong công thức tính điểm tương thích tổng thể.", "BR-03 (Trọng số ưu tiên cá nhân): ")
    add_bullet(doc, "Tiêu chí hút thuốc (smoke = 0) có tính chất là ràng buộc khử (Hard Constraint), nếu người dùng dị ứng thuốc lá thì các ứng viên hút thuốc sẽ bị giảm mạnh điểm hòa hợp.", "BR-04 (Ràng buộc không khói thuốc): ")
    add_bullet(doc, "Các thanh trượt phải phản hồi mượt mà và cập nhật nhãn số giờ tức thì (dưới 50ms).", "NFR-03 (Độ nhạy giao diện): ")

    add_heading_2(doc, "3.4 Đặc tả bản vẽ Wireframe WF-02 (Màn hình Khảo sát Thói quen)")
    add_body(doc, "Bản vẽ Wireframe WF-02 mô tả chi tiết biểu mẫu khảo sát (xem tại http://localhost:8000/wireframe tab WF-02):")
    add_bullet(doc, "Hai thanh trượt kép với dải hiển thị giờ trực quan từ 20:00 tối đến 04:00 sáng hôm sau và 05:00 sáng đến 11:00 trưa.", "[Khu vực nhịp sinh học]: ")
    add_bullet(doc, "Bộ chọn 4 ô gọn gàng, độ ồn, học tập và hút thuốc được bố trí dạng lưới 2 cột gọn gàng.", "[Khu vực tiêu chuẩn phòng]: ")
    add_bullet(doc, "Khối chọn sở thích 6 ô checkbox kèm biểu tượng minh họa.", "[Khu vực sở thích]: ")

    # ==================== ĐẶC TẢ USE CASE 3 ====================
    add_heading_1(doc, "4. ĐẶC TẢ CHI TIẾT USE CASE UC-06: XEM BẢNG XẾP HẠNG BẠN CÙNG PHÒNG VÀ GIẢI THÍCH")
    add_heading_2(doc, "4.1 Bảng tóm tắt Use Case (Summary)")
    render_uc_summary_table(doc, [
        ("ID:", "UC-06"),
        ("Title:", "Xem Bảng xếp hạng bạn cùng phòng (View Roommate Compatibility Ranking)"),
        ("Description:", "Use Case này hiển thị danh sách các ứng viên tương thích nhất được sắp xếp từ Hạng 1 đến Hạng 8 kèm phân tích tiêu chí chi tiết."),
        ("Actors:", "Sinh viên (Primary Actor), Hệ thống (System Engine)."),
        ("Preconditions:", "Sinh viên đã hoàn tất việc khai báo thói quen tại UC-04."),
        ("Post conditions:", "Danh sách Top 8 ứng viên được hiển thị trực quan cùng điểm số hòa hợp hai chiều."),
        ("Trigger:", "Hệ thống nhận được dữ liệu thói quen hoặc người dùng bấm nút Tính toán xếp hạng.")
    ])

    add_heading_2(doc, "4.2 Ba loại luồng sự kiện (Three Types of Flows)")
    render_flow_table(doc, [
        ("BF-1", "Hệ thống", "Lọc danh sách các ứng viên thuộc nhóm đối diện (sinh viên Nhóm A đối chiếu với Nhóm B, và ngược lại).", "Mô hình hai phía."),
        ("BF-2", "Hệ thống", "Gọi Use Case được include 'Tính điểm tương thích 2 chiều' (UC-07) để tính M[User, Cand] và M[Cand, User].", "Include UC-07."),
        ("BF-3", "Hệ thống", "Tính điểm trung bình cộng hai chiều AvgScore và sắp xếp danh sách theo thứ tự giảm dần.", "Thuật toán xếp hạng."),
        ("BF-4", "Hệ thống", "Gán nhãn thứ hạng từ Hạng 1 đến Hạng 8 và gắn nhãn đánh giá (Siêu hòa hợp, Hòa hợp tốt, Cần thỏa hiệp, Dễ xung đột).", "Phân loại mức độ."),
        ("BF-5", "Hệ thống", "Hiển thị các thẻ kết quả trên giao diện (Wireframe WF-03) với thẻ Hạng 1 viền vàng nổi bật.", "Trực quan hóa kết quả."),
        ("BF-6", "Sinh viên", "Quan sát danh sách và lựa chọn ứng viên ưng ý nhất.", "Hoàn tất mục tiêu Use Case.")
    ], title="Luồng cơ bản (Basic Flow - Happy Path)")

    render_flow_table(doc, [
        ("AF-A1", "Sinh viên", "Tại bước BF-5, sinh viên nhấp vào nút 'Chi tiết tiêu chí ▼' trên thẻ ứng viên bất kỳ.", "Extend UC-08."),
        ("AF-A2", "Hệ thống", "Mở rộng khối thông tin chi tiết hiển thị danh sách 'Điểm cộng tương thích' (>=0.75) và 'Điểm cần lưu ý' (<=0.40).", "Minh bạch hóa thuật toán.")
    ], title="Luồng rẽ nhánh (Alternate Flow AF-A: Xem chi tiết giải thích tiêu chí)")

    render_flow_table(doc, [
        ("EF-A1", "Hệ thống", "Nếu cơ sở dữ liệu nhóm đối diện rỗng, hệ thống hiển thị thông báo 'Chưa có ứng viên phù hợp trong nhóm đối diện'.", "Mục tiêu không đạt."),
        ("EF-A2", "Sinh viên", "Đổi lựa chọn nhóm hoặc chờ ban quản lý nạp thêm dữ liệu sinh viên mới.", "Kết thúc luồng.")
    ], title="Luồng ngoại lệ (Exception Flow EF-A: Không có ứng viên đối diện)")

    add_heading_2(doc, "4.3 Quy tắc nghiệp vụ và Yêu cầu phi chức năng")
    add_bullet(doc, "Điểm tương thích không tính một chiều mà bắt buộc tính trung bình đối xứng: AvgScore = (Score_User_to_Cand + Score_Cand_to_User) / 2.", "BR-05 (Tính điểm hai chiều đối xứng): ")
    add_bullet(doc, "Chỉ hiển thị tối đa Top 8 ứng viên có điểm cao nhất để tránh làm người dùng bị quá tải thông tin (Cognitive Overload).", "BR-06 (Giới hạn hiển thị Top 8): ")
    add_bullet(doc, "Thời gian tính toán và kết xuất bảng xếp hạng phải nhỏ hơn 300 mili-giây.", "NFR-04 (Tốc độ tính toán ma trận): ")

    add_heading_2(doc, "4.4 Đặc tả bản vẽ Wireframe WF-03 (Bảng xếp hạng Top 1 đến Top 8)")
    add_body(doc, "Bản vẽ Wireframe WF-03 thể hiện danh sách xếp hạng trực quan (xem tại http://localhost:8000/wireframe tab WF-03):")
    add_bullet(doc, "Thẻ Hạng 1 có viền vàng ánh kim, huy hiệu '🥇 HẠNG 1', hiển thị % điểm lớn màu xanh lá (88.5%) và nhãn 'Siêu hòa hợp'.", "[Thẻ Top 1 Vàng nổi bật]: ")
    add_bullet(doc, "Các thẻ tiếp theo mang huy hiệu Bạc (🥈 Hạng 2), Đồng (🥉 Hạng 3) và các thứ hạng #4 đến #8.", "[Các thứ hạng tiếp theo]: ")
    add_bullet(doc, "Accordion mở rộng phân tách 2 cột màu: Cột xanh lục (Điểm cộng tương thích) và Cột đỏ gạch (Điểm cần lưu ý/xung đột).", "[Khối mở rộng chi tiết UC-08]: ")

    # ==================== ĐẶC TẢ USE CASE 4 ====================
    add_heading_1(doc, "5. ĐẶC TẢ CHI TIẾT USE CASE UC-12: GHÉP PHÒNG TỰ ĐỘNG GALE-SHAPLEY VÀ BÁO CÁO")
    add_heading_2(doc, "5.1 Bảng tóm tắt Use Case (Summary)")
    render_uc_summary_table(doc, [
        ("ID:", "UC-12"),
        ("Title:", "Thực hiện ghép phòng tự động (Perform Automated Roommate Matching)"),
        ("Description:", "Use Case này cho phép Ban quản lý KTX kích hoạt giải thuật Gale-Shapley để xếp phòng hàng loạt cho toàn bộ sinh viên."),
        ("Actors:", "Ban quản lý KTX (Primary Actor), Hệ thống (System Engine)."),
        ("Preconditions:", "Ban quản lý đã nạp dữ liệu sinh viên nhóm A và B (qua file CSV hoặc sinh giả lập Seed)."),
        ("Post conditions:", "Hệ thống hoàn tất danh sách phân phòng chính thức với chỉ số Cặp chặn bằng 0 (Blocking Pairs = 0)."),
        ("Trigger:", "Ban quản lý nhấn nút 'Khởi chạy ghép phòng tự động' trên bảng điều khiển Admin.")
    ])

    add_heading_2(doc, "5.2 Ba loại luồng sự kiện (Three Types of Flows)")
    render_flow_table(doc, [
        ("BF-1", "Ban quản lý", "Truy cập bảng điều khiển Admin (Wireframe WF-04) và kiểm tra danh sách sinh viên hiện có.", "Giao diện quản trị."),
        ("BF-2", "Ban quản lý", "Bấm nút 'KHỞI CHẠY GHÉP PHÒNG'.", "Kích hoạt xử lý."),
        ("BF-3", "Hệ thống", "Gọi Use Case được include 'Chạy thuật toán Gale-Shapley' (UC-13) để thực thi cơ chế đề xuất và chấp nhận hoãn lại.", "Include UC-13."),
        ("BF-4", "Hệ thống", "Gọi Use Case được include 'Đếm cặp chặn' (UC-14) để quét toàn bộ các cặp chéo nhằm xác thực tính ổn định.", "Include UC-14."),
        ("BF-5", "Hệ thống", "Kết xuất kết quả phân phòng lên giao diện và hiển thị huy hiệu '0 CẶP CHẶN' màu xanh lục.", "Xác nhận thành công."),
        ("BF-6", "Hệ thống", "Vẽ biểu đồ cột đối sánh điểm hài lòng trung bình giữa Gale-Shapley và Phân phòng ngẫu nhiên.", "Trực quan hóa hiệu quả."),
        ("BF-7", "Ban quản lý", "Xem báo cáo đối chứng và đánh giá chất lượng phân bổ phòng.", "Hoàn tất mục tiêu Use Case.")
    ], title="Luồng cơ bản (Basic Flow - Happy Path)")

    render_flow_table(doc, [
        ("AF-A1", "Ban quản lý", "Tại bước BF-7, Ban quản lý bấm nút 'Xuất file CSV' để tải về danh sách phân phòng hoàn chỉnh.", "Extend UC-16."),
        ("AF-A2", "Hệ thống", "Tạo file bảng tính CSV chứa mã sinh viên, tên, phòng được xếp và điểm tương thích hai chiều để in ấn niêm yết.", "Hoàn tất mở rộng.")
    ], title="Luồng rẽ nhánh (Alternate Flow AF-A: Xuất file danh sách phân phòng)")

    render_flow_table(doc, [
        ("EF-A1", "Hệ thống", "Nếu số lượng sinh viên nhóm A và nhóm B bị lệch nhau, hệ thống cảnh báo số lượng sinh viên dư chưa được xếp.", "Cảnh báo chênh lệch."),
        ("EF-A2", "Ban quản lý", "Chọn phương án điều phối sinh viên dư vào danh sách phòng dự phòng.", "Xử lý ngoại lệ.")
    ], title="Luồng ngoại lệ (Exception Flow EF-A: Chênh lệch số lượng hai phía)")

    add_heading_2(doc, "5.3 Quy tắc nghiệp vụ và Yêu cầu phi chức năng")
    add_bullet(doc, "Bắt buộc thuật toán phải đạt trạng thái ổn định hoàn hảo: Số cặp chặn Blocking Pairs = 0 (không có cặp sinh viên nào muốn bỏ phòng hiện tại để ghép với nhau).", "BR-07 (Độ ổn định tuyệt đối): ")
    add_bullet(doc, "Điểm hài lòng trung bình của phương pháp Gale-Shapley phải cao hơn phương pháp ghép ngẫu nhiên tối thiểu 20%.", "BR-08 (Mục tiêu tối ưu hóa): ")
    add_bullet(doc, "Thời gian thực thi thuật toán phân phòng cho 200 sinh viên phải hoàn thành trong vòng dưới 5.0 giây.", "NFR-05 (Hiệu năng thuật toán): ")

    add_heading_2(doc, "5.4 Đặc tả bản vẽ Wireframe WF-04 (Bảng điều khiển Quản trị KTX)")
    add_body(doc, "Bản vẽ Wireframe WF-04 mô tả trung tâm điều phối của Ban quản lý (xem tại http://localhost:8000/wireframe tab WF-04):")
    add_bullet(doc, "Thanh tác vụ gồm nút nạp CSV, nút sinh dữ liệu Seed (N=20, 50, 100, 200) và nút khởi chạy động cơ Gale-Shapley.", "[Thanh công cụ nạp và chạy]: ")
    add_bullet(doc, "Hộp chỉ số lớn '0 CẶP CHẶN' (Blocking Pairs = 0) khẳng định độ ổn định của hệ thống.", "[Hộp đo lường độ ổn định]: ")
    add_bullet(doc, "Biểu đồ cột so sánh điểm hài lòng trung bình giữa Gale-Shapley (cột tím ~85%) và Ghép ngẫu nhiên (cột xám ~55%) qua 4 quy mô khảo nghiệm.", "[Biểu đồ đối chứng hiệu năng]: ")

    # ==================== KẾT LUẬN ====================
    add_heading_1(doc, "6. KẾT LUẬN VÀ LIÊN KẾT BẢO VỆ ĐỒ ÁN")
    add_body(doc, "Hồ sơ đặc tả Use Case Specification kèm bản vẽ Wireframe này đã chuẩn hóa toàn bộ các yêu cầu chức năng của hệ thống Ghép bạn cùng phòng KTX theo đúng mẫu chuẩn của Giảng viên hướng dẫn. Việc kết hợp chặt chẽ giữa bảng tóm tắt (Summary), phân tích 3 loại luồng (Basic, Alternate, Exception Flows), quy tắc nghiệp vụ (Business Rules), phi chức năng (NFRs) và bản vẽ Wireframe UI trực quan đã tạo nên một sản phẩm cuối kỳ (CKI) hoàn chỉnh, chuyên nghiệp và có tính thuyết phục học thuật rất cao.")

    # Lưu tài liệu
    out_dl = r"C:\Users\LENOVO\Downloads\Use_Case_Specification_Va_Wireframe_KTX.docx"
    out_docs = r"C:\Users\LENOVO\.gemini\antigravity\scratch\system-\docs\Use_Case_Specification_Va_Wireframe_KTX.docx"

    doc.save(out_dl)
    doc.save(out_docs)
    print(f"Successfully generated docx at:\n1. {out_dl}\n2. {out_docs}")

if __name__ == "__main__":
    build_document()
