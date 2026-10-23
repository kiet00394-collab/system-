# -*- coding: utf-8 -*-
"""
make_spec_sequence_doc.py
Generates the official Word document (.docx) strictly adhering to:
1. Google Slide Use Case Specification template
2. KTX_Smart_Match_UseCase.drawio (26 Use Cases, 8 Actors)
3. Whiteboard teacher rules
Outputs to Downloads and docs/
"""

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

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
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
            tag = f'w:{edge}'
            element = OxmlElement(tag)
            element.set(qn('w:val'), edge_data.get('val', 'single'))
            element.set(qn('w:sz'), str(edge_data.get('sz', 4)))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), edge_data.get('color', 'D1D5DB'))
            tcBorders.append(element)
    tcPr.append(tcBorders)

def add_styled_paragraph(doc, text="", style='Normal', space_before=0, space_after=4, line_spacing=1.15, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = doc.add_paragraph(text, style=style)
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    return p

def add_heading_1(doc, text):
    p = add_styled_paragraph(doc, space_before=14, space_after=4)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    return p

def add_heading_2(doc, text):
    p = add_styled_paragraph(doc, space_before=9, space_after=3)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x2C, 0x52, 0x82)
    return p

def add_body(doc, text, bold=False, italic=False):
    p = add_styled_paragraph(doc, space_before=0, space_after=4, line_spacing=1.15)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10.5)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)
    return p

def build_document():
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)

    # ==================== TRANG BÌA ====================
    p_inst = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r_inst = p_inst.add_run("ĐẠI HỌC ĐÀ NẴNG\nVIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK)")
    r_inst.font.name, r_inst.font.size, r_inst.font.bold = 'Times New Roman', Pt(11), True
    r_inst.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_title = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=6)
    r_title = p_title.add_run("HỒ SƠ ĐẶC TẢ USE CASE VÀ BỘ SEQUENCE DIAGRAM ĐỒNG BỘ\n(HỆ THỐNG QUẢN TRỊ & GHÉP BẠN CÙNG PHÒNG KTX THÔNG MINH)")
    r_title.font.name, r_title.font.size, r_title.font.bold = 'Times New Roman', Pt(15), True
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_desc = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=16)
    r_desc = p_desc.add_run("Chuẩn hóa cấu trúc theo Slide bài giảng (Summary + Three Types of Flows) và Sơ đồ Use Case mới nhất (KTX_Smart_Match_UseCase.drawio)")
    r_desc.font.name, r_desc.font.size, r_desc.font.italic = 'Times New Roman', Pt(10), True
    r_desc.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    tbl_meta = doc.add_table(rows=4, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_info = [
        ("Đề tài dự án:", "Hệ thống Quản trị & Ghép Bạn Cùng Phòng KTX (KTX Smart Match)"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 3 (Châu Tuấn Kiệt, Bùi Đình Hiếu, Lê Hoàng Triều)"),
        ("Căn cứ thiết kế:", "Slide Use Case Specification + File KTX_Smart_Match_UseCase.drawio"),
        ("Nội dung báo cáo:", "Business Rules, NFRs, Bảng 26 Use Cases, Đặc tả chi tiết, Sequence Diagram, Wireframe")
    ]
    for i, (k, v) in enumerate(meta_info):
        r = tbl_meta.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.3)
        set_cell_background(c0, "F3F4F6")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=50, bottom=50, left=80, right=80)
        set_cell_margins(c1, top=50, bottom=50, left=80, right=80)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9.5), True
        r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(9.5)
        r1.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    add_styled_paragraph(doc, space_after=10)

    # ==================== MỤC 1: BUSINESS RULES ====================
    add_heading_1(doc, "1. HỆ THỐNG 7 QUY TẮC NGHIỆP VỤ (BUSINESS RULES - BR)")
    add_body(doc, "Theo đúng yêu cầu của Giảng viên: 'Sai cơ bản là điền references, làm mà không hiểu BR1 là gì, BR-2 là gì, AF là gì phải hiểu để note, không được note đại'. Dưới đây là bảng định nghĩa tường minh 7 Quy tắc nghiệp vụ được tham chiếu trong toàn bộ use case:")

    br_table = doc.add_table(rows=8, cols=4)
    br_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    br_heads = ["Mã BR", "Tên Quy tắc Nghiệp vụ", "Nội dung Chi tiết & Điều kiện Áp dụng", "Ý nghĩa Vận hành & Module"]
    br_widths = [Inches(0.8), Inches(1.8), Inches(2.7), Inches(1.7)]

    for j, h in enumerate(br_heads):
        cell = br_table.rows[0].cells[j]
        cell.width = br_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=70, bottom=70, left=50, right=50)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(9), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    br_data = [
        ("BR-01", "Đối tượng Tiếp nhận (SV Trường A)", "KTX A phục vụ riêng cho sinh viên trường Đại học A (hoặc khối thành viên). Phải có MSSV và email trường cấp (@edu.vn). Đúng đối tượng mới được kích hoạt ghép tự động.", "Bảo đảm an ninh, phục vụ đúng đối tượng (Cổng đăng nhập, Xác thực SV Trường A)."),
        ("BR-02", "Thời hạn Lưu trú Tối thiểu 1 Kỳ", "Bắt buộc cam kết lưu trú tối thiểu 01 học kỳ (5 tháng) hoặc trọn năm học. Hệ thống kiên quyết từ chối hợp đồng ngắn hạn theo ngày/tuần.", "Ổn định nề nếp văn hóa phòng, bảo toàn kế hoạch dòng tiền KTX (Form Đăng ký, Hợp đồng)."),
        ("BR-03", "Phê duyệt Nghiệp vụ (Business Approve)", "Hồ sơ đăng ký KTX phải qua bước BQL thẩm định tư cách, kiểm tra lịch sử kỷ luật và diện ưu tiên. Chỉ hồ sơ 'Approved' mới được phân phòng.", "Kiểm soát an ninh cửa ngõ, không cho đối tượng vi phạm vào ở (Dashboard Quản trị Thẩm định Đơn)."),
        ("BR-04", "Đặt cọc & Hạn Thanh toán 72h", "Trong vòng 72 giờ từ khi có kết quả, sinh viên phải nộp tiền phòng kỳ 1 + Tiền cọc tài sản (1.000.000 VNĐ) qua VNPay. Quá hạn tự động hủy giữ chỗ, chuyển cho Waitlist.", "Tránh giữ chỗ ảo, bảo đảm thu hồi vốn KTX (Màn hình Thanh toán, Cổng VNPay)."),
        ("BR-05", "Tối ưu Lợi nhuận & Lấp đầy Phòng", "Phân nhóm theo loại phòng (2, 4, 6 người) trước, sau đó ghép Gale-Shapley. Ưu tiên lấp đầy 100% số giường từng phòng trước khi mở phòng mới để tiết kiệm chi phí.", "Tối đa hóa biên lợi nhuận ròng KTX (Thuật toán matching, Báo cáo Doanh thu)."),
        ("BR-06", "Trọng số Ưu tiên Cá nhân (Top 1.5x)", "Tiêu chí sinh viên coi trọng nhất (top) được nhân trọng số 1.5x, tạo ma trận điểm bất đối xứng M[a][b] khác M[b][a].", "Mô phỏng tâm lý con người trong thực tế (Module scoring.py)."),
        ("BR-07", "Triệt tiêu Cặp chặn (Stability)", "Kết quả phân phòng bắt buộc phải đạt độ ổn định tuyệt đối (Blocking Pairs = 0).", "Không sinh viên nào có động cơ tự ý đổi phòng (Thuật toán Gale-Shapley).")
    ]

    for i, row_data in enumerate(br_data):
        row = br_table.rows[i + 1]
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = br_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=45, bottom=45, left=50, right=50)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j != 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(val)
            run.font.name, run.font.size = 'Times New Roman', Pt(8.5)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            elif j == 1:
                run.font.bold = True

    add_styled_paragraph(doc, space_after=8)

    # ==================== MỤC 2: NON-FUNCTIONAL REQUIREMENTS ====================
    add_heading_1(doc, "2. HỆ THỐNG YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - NFR)")
    
    nfr_table = doc.add_table(rows=7, cols=4)
    nfr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    nfr_heads = ["Mã NFR", "Tên Yêu cầu Phi chức năng", "Tiêu chuẩn Định lượng Đo lường", "Phương pháp Kiểm chứng"]
    nfr_widths = [Inches(0.9), Inches(1.8), Inches(2.5), Inches(1.8)]

    for j, h in enumerate(nfr_heads):
        cell = nfr_table.rows[0].cells[j]
        cell.width = nfr_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=70, bottom=70, left=50, right=50)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(9), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    nfr_data = [
        ("NFR-01", "Hiệu năng Xử lý Thuật toán", "Xử lý quy mô 200 SV trong < 1.0 giây; quy mô 1.000 SV trong < 5.0 giây.", "Benchmark tự động bằng time.perf_counter() trong test_benchmark.py."),
        ("NFR-02", "Độ Ổn định Toán học Tuyệt đối", "Triệt tiêu 100% cặp chặn (Blocking Pairs = 0) qua 50 seed kiểm thử ngẫu nhiên.", "Bộ test tự động test_matching.py với 50 hạt giống ngẫu nhiên."),
        ("NFR-03", "Bảo mật & Toàn vẹn Giao dịch", "Mã hóa TLS 1.3, đối soát chữ ký số SHA-256 phản hồi từ cổng VNPay.", "Tích hợp cổng VNPay Sandbox, xác thực mã vnp_ResponseCode == 00."),
        ("NFR-04", "Khả năng Chịu lỗi Dữ liệu", "Nạp CSV lỗi (thiếu cột, sai kiểu số, rỗng) chỉ báo lỗi thân thiện, không sập app.", "Bộ test test_error_handling.py xử lý 3 kịch bản file CSV lỗi."),
        ("NFR-05", "Khả năng Mở rộng Loại phòng", "Mở rộng linh hoạt từ phòng 2 người sang phòng 4 và 6 người qua hàm merge.", "Hàm merge_pairs_into_rooms trong matching.py và unit test phòng 4."),
        ("NFR-06", "Trải nghiệm & Phản hồi UI", "Thời gian phản hồi UI < 2.0s; hỗ trợ nạp nhanh 3 Persona chỉ với 1 cú click.", "Thử nghiệm trên Dashboard giao diện web FastAPI/Streamlit.")
    ]

    for i, row_data in enumerate(nfr_data):
        row = nfr_table.rows[i + 1]
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = nfr_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=45, bottom=45, left=50, right=50)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j != 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(val)
            run.font.name, run.font.size = 'Times New Roman', Pt(8.5)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x16, 0x65, 0x34)
            elif j == 1:
                run.font.bold = True

    add_styled_paragraph(doc, space_after=8)

    # ==================== MỤC 3: BẢNG DANH MỤC 26 USE CASE ====================
    add_heading_1(doc, "3. DANH MỤC TOÀN BỘ 26 USE CASE (CHUẨN HÓA THEO KTX_SMART_MATCH_USECASE.DRAWIO)")
    add_body(doc, "Sơ đồ Use Case hoàn thiện bao gồm 8 Tác nhân (Sinh viên, Quản trị viên, Cán bộ KTX, Hệ thống SV Trường A, Cổng VNPay, Kế toán, Kỹ thuật, Scheduler) và 26 Use Case phân bổ đồng đều:")

    tbl_catalog = doc.add_table(rows=27, cols=5)
    tbl_catalog.alignment = WD_TABLE_ALIGNMENT.CENTER
    cat_heads = ["Mã UC", "Tên Use Case", "Tác nhân (Actor)", "Phân hệ", "Mối quan hệ UML / Ghi chú"]
    cat_widths = [Inches(0.7), Inches(2.3), Inches(1.4), Inches(1.3), Inches(1.3)]

    for j, h in enumerate(cat_heads):
        cell = tbl_catalog.rows[0].cells[j]
        cell.width = cat_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=60, bottom=60, left=40, right=40)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(8.5), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    usecases_list = [
        ("UC-01", "Đăng nhập / Quên mật khẩu", "Sinh viên", "Sinh viên", "include: Xác thực SV (BR-01)"),
        ("UC-02", "Đăng ký tài khoản & khai báo thói quen", "Sinh viên", "Sinh viên", "include: Xác thực SV (BR-01)"),
        ("UC-03", "Cập nhật hồ sơ & thói quen", "Sinh viên", "Sinh viên", "extend: Nạp mẫu Persona"),
        ("UC-04", "Chọn loại phòng, tiện ích & nộp đơn KTX", "Sinh viên", "Sinh viên", "Cam kết >= 1 kỳ (BR-02, BR-05)"),
        ("UC-05", "Xem bảng xếp hạng bạn cùng phòng", "Sinh viên", "Sinh viên", "include: Tính điểm tương thích"),
        ("UC-06", "Gửi / phản hồi lời mời ghép nhóm bạn", "Sinh viên", "Sinh viên", "Kết nối sinh viên quen"),
        ("UC-07", "Xem kết quả phân phòng & thông tin", "Sinh viên", "Sinh viên", "Tra cứu kết quả phân phòng"),
        ("UC-08", "Yêu cầu đổi phòng / đổi bạn cùng phòng", "Sinh viên", "Sinh viên", "extend: Đính kèm lý do & minh chứng"),
        ("UC-09", "Gửi phản ánh & báo sự cố", "Sinh viên", "Sinh viên", "Hỗ trợ nội trú"),
        ("UC-10", "Xem thông báo", "Sinh viên", "Sinh viên", "Nhận tin tức KTX"),
        ("UC-11", "Đánh giá bạn cùng phòng cuối kỳ", "Sinh viên", "Sinh viên", "extend: Báo cáo vi phạm"),
        ("UC-12", "Gia hạn / Trả phòng", "Sinh viên", "Sinh viên", "include: Tính phí & hoàn cọc"),
        ("UC-13", "Thanh toán tiền phòng & cọc (72h)", "Sinh viên", "Sinh viên", "include: Cổng VNPay (BR-04)"),
        ("UC-14", "Quản lý danh mục tòa, phòng & giá", "Quản trị viên", "Quản trị", "Cấu hình cơ sở vật chất"),
        ("UC-15", "Quản lý tài khoản & phân quyền", "Quản trị viên", "Quản trị", "Phân quyền cán bộ"),
        ("UC-16", "Quản lý dữ liệu sinh viên KTX", "Quản trị viên", "Quản trị", "extend: Nạp CSV, Sinh Seed"),
        ("UC-17", "Cấu hình trọng số tiêu chí & luật ghép", "Quản trị viên", "Quản trị", "Thiết lập trọng số BR-06"),
        ("UC-18", "Phê duyệt đơn KTX (Business Approve)", "Cán bộ KTX", "Quản trị", "Thẩm định điều kiện BR-03"),
        ("UC-19", "Điều chỉnh phân phòng thủ công", "Cán bộ KTX", "Quản trị", "Override thủ công"),
        ("UC-20", "Xử lý yêu cầu đổi phòng / đổi bạn", "Cán bộ KTX", "Quản trị", "Giải quyết khiếu nại"),
        ("UC-21", "Quản lý phản ánh & sự cố", "Cán bộ, Kỹ thuật", "Quản trị", "Tiếp nhận sửa chữa"),
        ("UC-22", "Theo dõi & đối soát thanh toán", "Kế toán", "Quản trị", "extend: Hoàn tiền / cọc"),
        ("UC-23", "Báo cáo doanh thu & lợi nhuận", "Kế toán, Admin", "Quản trị", "extend: Xuất báo cáo CSV"),
        ("UC-24", "Thực hiện ghép phòng tự động", "Hệ thống (Scheduler)", "Quản trị", "include: Gale-Shapley, BP=0"),
        ("UC-25", "Gửi thông báo & nhắc hạn thanh toán", "Hệ thống (Scheduler)", "Quản trị", "Tự động gửi email/app"),
        ("UC-26", "Tự động hủy đơn quá 72h & xếp hàng chờ", "Hệ thống (Scheduler)", "Quản trị", "Quét hạn chót BR-04")
    ]

    for i, udata in enumerate(usecases_list):
        row = tbl_catalog.rows[i + 1]
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(udata):
            cell = row.cells[j]
            cell.width = cat_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=35, bottom=35, left=40, right=40)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j != 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(val)
            run.font.name, run.font.size = 'Times New Roman', Pt(8)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            elif j == 1:
                run.font.bold = True

    add_styled_paragraph(doc, space_after=10)

    # ==================== HÀM RENDER ĐẶC TẢ CHI TIẾT THEO SLIDE ====================
    def render_detailed_usecase(sec_num, uc_id, uc_title, uc_desc, actors, precond, postcond, trigger, flow_rows, seq_messages, wf_id, wf_name, wf_elements):
        add_heading_1(doc, f"{sec_num}. ĐẶC TẢ CHI TIẾT USE CASE {uc_id}: {uc_title.upper()}")
        
        # 1. SUMMARY TABLE (Theo Slide)
        add_heading_2(doc, f"{sec_num}.1 Summary Table (Tóm tắt thông tin Use Case theo Slide)")
        
        t_sum = doc.add_table(rows=7, cols=2)
        t_sum.alignment = WD_TABLE_ALIGNMENT.CENTER
        sum_rows = [
            ("ID", uc_id),
            ("Title", uc_title),
            ("Description", uc_desc),
            ("Actors", actors),
            ("Preconditions", precond),
            ("Post conditions", postcond),
            ("Trigger", trigger)
        ]
        for i, (k, v) in enumerate(sum_rows):
            row = t_sum.rows[i]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width, c1.width = Inches(1.8), Inches(5.2)
            set_cell_background(c0, "F3F4F6")
            set_cell_background(c1, "FFFFFF")
            set_cell_margins(c0, top=45, bottom=45, left=60, right=60)
            set_cell_margins(c1, top=45, bottom=45, left=60, right=60)
            set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            
            p0 = c0.paragraphs[0]
            r0 = p0.add_run(k)
            r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9), True
            r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            
            p1 = c1.paragraphs[0]
            r1 = p1.add_run(v)
            r1.font.name, r1.font.size = 'Times New Roman', Pt(9)
            r1.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

        add_styled_paragraph(doc, space_after=6)

        # 2. THREE TYPES OF FLOWS TABLE (Theo Slide: Step ID, Actor, Action, Notes/references)
        add_heading_2(doc, f"{sec_num}.2 Three Types of Flows Table (Luồng sự kiện BF, AF, EF)")
        
        t_flow = doc.add_table(rows=len(flow_rows) + 1, cols=4)
        t_flow.alignment = WD_TABLE_ALIGNMENT.CENTER
        flow_heads = ["Step ID", "Actor", "Action", "Notes/references"]
        flow_widths = [Inches(1.0), Inches(1.5), Inches(3.2), Inches(1.3)]

        for j, h in enumerate(flow_heads):
            cell = t_flow.rows[0].cells[j]
            cell.width = flow_widths[j]
            set_cell_background(cell, "1B365D")
            set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(h)
            run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(9), True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for i, (sid, sact, saction, snotes) in enumerate(flow_rows):
            row = t_flow.rows[i + 1]
            bg = "FFFFFF"
            if sid.startswith("BF"):
                bg = "F0FDF4" if i % 2 == 1 else "FFFFFF"
            elif sid.startswith("AF"):
                bg = "FAF5FF"
            elif sid.startswith("EF"):
                bg = "FEF2F2"

            for j, val in enumerate([sid, sact, saction, snotes]):
                cell = row.cells[j]
                cell.width = flow_widths[j]
                set_cell_background(cell, bg)
                set_cell_margins(cell, top=45, bottom=45, left=50, right=50)
                set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j >= 2 else WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(val)
                run.font.name, run.font.size = 'Times New Roman', Pt(8.5)
                if j == 0:
                    run.font.bold = True
                    if sid.startswith("BF"): run.font.color.rgb = RGBColor(0x16, 0x65, 0x34)
                    elif sid.startswith("AF"): run.font.color.rgb = RGBColor(0x7E, 0x22, 0xCE)
                    else: run.font.color.rgb = RGBColor(0x99, 0x1B, 0x1B)
                elif j == 3:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)

        add_styled_paragraph(doc, space_after=6)

        # 3. SEQUENCE DIAGRAM MESSAGES
        add_heading_2(doc, f"{sec_num}.3 Biểu đồ Tuần tự (Sequence Diagram) - Khớp 1-1 từng bước")
        for smsg in seq_messages:
            add_body(doc, smsg)

        # 4. WIREFRAME MAPPING
        add_heading_2(doc, f"{sec_num}.4 Thiết kế Wireframe UI ({wf_id}: {wf_name})")
        twf = doc.add_table(rows=len(wf_elements) + 1, cols=3)
        twf.alignment = WD_TABLE_ALIGNMENT.CENTER
        twf_heads = ["Mã Callout", "Thành phần Giao diện Wireframe", "Ánh xạ Bước Đặc tả (Khớp 1-1)"]
        twf_widths = [Inches(1.2), Inches(3.2), Inches(2.6)]

        for j, h in enumerate(twf_heads):
            cell = twf.rows[0].cells[j]
            cell.width = twf_widths[j]
            set_cell_background(cell, "2C5282")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(h)
            run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(8.5), True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for i, (wfid, wfname, wfmap) in enumerate(wf_elements):
            row = twf.rows[i + 1]
            bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
            for j, val in enumerate([wfid, wfname, wfmap]):
                cell = row.cells[j]
                cell.width = twf_widths[j]
                set_cell_background(cell, bg)
                set_cell_margins(cell, top=40, bottom=40, left=50, right=50)
                set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j != 0 else WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(val)
                run.font.name, run.font.size = 'Times New Roman', Pt(8)
                if j == 0:
                    run.font.bold = True
                    run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

        add_styled_paragraph(doc, space_after=10)

    # ==================== ĐẶC TẢ 6 USE CASES ĐẠI DIỆN ====================
    # UC-01
    render_detailed_usecase(
        sec_num="4",
        uc_id="UC-01",
        uc_title="Đăng nhập và Quên mật khẩu (Sign in and Reset Password)",
        uc_desc="Mô tả cách sinh viên đăng nhập vào Cổng thông tin KTX bằng MSSV trường A và mật khẩu, xác thực với hệ thống trường liên kết theo BR-01 hoặc khôi phục mật khẩu.",
        actors="Sinh viên (Primary Actor), Hệ thống SV Trường A (Secondary Actor)",
        precond="Sinh viên thuộc danh sách tiếp nhận của Trường Đại học A (hoặc khối thành viên liên kết).",
        postcond="Hệ thống cấp token phiên làm việc bảo mật (Session HttpOnly), chuyển hướng vào Dashboard Sinh viên.",
        trigger="Sinh viên truy cập Cổng KTX và chọn chức năng 'Đăng nhập'.",
        flow_rows=[
            ("BF-1", "Sinh viên", "Truy cập Cổng thông tin KTX và chọn chức năng Đăng nhập.", "WF-01, NFR-06"),
            ("BF-2", "Hệ thống", "Hiển thị biểu mẫu đăng nhập gồm ô nhập MSSV và Mật khẩu.", "WF-01 Form"),
            ("BF-3", "Sinh viên", "Nhập MSSV trường A (VD: 22VNUK0101) và mật khẩu, nhấn Đăng nhập.", "Kiểm tra cú pháp"),
            ("BF-4", "Hệ thống", "Gửi credentials sang Dịch vụ xác thực sinh viên Trường A.", "Include: Xác thực SV, BR-01"),
            ("BF-5", "Hệ thống SV Trường A", "Xác nhận đúng sinh viên trường A, mật khẩu hợp lệ và gửi tín hiệu chấp thuận.", "BR-01 (Đúng trường A)"),
            ("BF-6", "Hệ thống", "Khởi tạo phiên bảo mật (Session HttpOnly), chuyển hướng vào Dashboard.", "Hoàn tất UC-01, NFR-03"),
            ("AF-A", "Sinh viên", "Tại bước BF-3, tích chọn 'Ghi nhớ đăng nhập 30 ngày'.", "Lưu Cookie an toàn"),
            ("AF-B", "Sinh viên", "Tại bước BF-2, nhấn 'Quên mật khẩu', nhập email trường cấp để nhận mã OTP.", "Khôi phục mật khẩu"),
            ("EF-A", "Hệ thống", "Tại bước BF-4, nếu nhập sai mật khẩu quá 5 lần: Khóa tạm tài khoản 15 phút.", "ERR_AUTH_MAX, NFR-03"),
            ("EF-B", "Hệ thống", "Tại bước BF-5, nếu MSSV không thuộc trường A: Từ chối đăng nhập và báo lỗi BR-01.", "ERR_NOT_AFFILIATED, BR-01")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Sinh viên -> UI: Truy cập trang đăng nhập KTX",
            "• Message 2 (BF-2): UI -> Sinh viên: Hiển thị form đăng nhập (MSSV, Mật khẩu)",
            "• Message 3 (BF-3): Sinh viên -> UI: Nhập MSSV và Mật khẩu, nhấn Đăng nhập",
            "• Message 4 (BF-4): UI -> Auth Service: Gửi yêu cầu xác thực credentials",
            "• Message 5 (BF-4, BF-5): Auth Service -> Hệ thống Trường A: Đối soát MSSV (Ref: BR-01)",
            "• Message 6 (BF-5): Hệ thống Trường A -> Auth Service: Xác nhận hợp lệ",
            "• Message 7 (BF-6): Auth Service -> UI -> Sinh viên: Cấp Session Token, vào Dashboard",
            "• Khối opt (AF-A): Sinh viên tích chọn ghi nhớ đăng nhập 30 ngày",
            "• Khối alt 1 (EF-A): Sai mật khẩu quá 5 lần -> Khóa tạm tài khoản 15 phút",
            "• Khối alt 2 (EF-B): MSSV không thuộc trường A -> Báo lỗi từ chối theo BR-01"
        ],
        wf_id="WF-01",
        wf_name="Cổng Đăng Nhập & Xác Thực",
        wf_elements=[
            ("WF-01-C01", "3 Card Persona mẫu 1-click (Thái Bảo, Văn Việt, Minh Quân)", "Ánh xạ AF-A, NFR-06"),
            ("WF-01-C02", "Form đăng nhập (Ô nhập MSSV trường A và Mật khẩu)", "Ánh xạ BF-2, BF-3"),
            ("WF-01-C03", "Hộp kiểm 'Ghi nhớ đăng nhập 30 ngày'", "Ánh xạ AF-A"),
            ("WF-01-C04", "Nút bấm 'ĐĂNG NHẬP VÀO HỆ THỐNG'", "Ánh xạ BF-3, BF-4"),
            ("WF-01-C05", "Khung Alert đỏ cảnh báo lỗi vi phạm BR-01", "Ánh xạ EF-B (BR-01)")
        ]
    )

    # UC-04
    render_detailed_usecase(
        sec_num="5",
        uc_id="UC-04",
        uc_title="Chọn Loại phòng, Tiện ích & Nộp đơn KTX (Select Room and Submit Application)",
        uc_desc="Mô tả quy trình sinh viên chọn gói phòng nguyện vọng, khai báo 8 tiêu chí thói quen, chọn tiêu chí ưu tiên 1.5x và cam kết ở tối thiểu 1 kỳ theo BR-02 để nộp đơn xét duyệt.",
        actors="Sinh viên (Primary Actor), Hệ thống KTX (Secondary Actor)",
        precond="Sinh viên đã đăng nhập thành công vào hệ thống (UC-01).",
        postcond="Hồ sơ được lưu ở trạng thái Pending_Approval, sẵn sàng chuyển cho cán bộ KTX thẩm định (UC-18).",
        trigger="Sinh viên chọn 'Đăng ký Phòng & Khảo sát Thói quen' trên Dashboard.",
        flow_rows=[
            ("BF-1", "Sinh viên", "Mở biểu mẫu đăng ký phòng và khảo sát nếp sống KTX.", "WF-02"),
            ("BF-2", "Hệ thống", "Hiển thị 3 gói phòng: VIP 2 người (1.4tr), Chuẩn 4 người (850k), Tiết kiệm 6 người (550k).", "BR-02, BR-05"),
            ("BF-3", "Sinh viên", "Chọn loại phòng mong muốn (ví dụ: Phòng 2 người VIP).", "Thu thập nguyện vọng"),
            ("BF-4", "Sinh viên", "Khai báo 8 thanh trượt thói quen sinh hoạt (ngủ, dậy, gọn gàng, học, tiếng ồn...).", "Vector 8 tiêu chí"),
            ("BF-5", "Sinh viên", "Chọn 01 tiêu chí quan trọng nhất (nhân trọng số 1.5x).", "BR-06 (Top 1.5x)"),
            ("BF-6", "Sinh viên", "Tích chọn cam kết bắt buộc: 'Tôi cam kết ở KTX tối thiểu 1 kỳ (5 tháng) theo BR-02'.", "BR-02 (Tối thiểu 1 kỳ)"),
            ("BF-7", "Sinh viên", "Nhấn nút 'Nộp Hồ Sơ Đăng Ký Phòng'.", "Gửi dữ liệu lên máy chủ"),
            ("BF-8", "Hệ thống", "Kiểm tra dữ liệu, lưu Database trạng thái Pending_Approval và cấp Mã hồ sơ.", "Hoàn tất UC-04"),
            ("AF-A", "Sinh viên", "Tại bước BF-4, bấm 'Nạp hồ sơ mẫu Persona' để tự động điền 8 tiêu chí tức thì.", "Extend: Nạp mẫu Persona, NFR-06"),
            ("EF-A", "Hệ thống", "Tại bước BF-7, nếu chưa tích cam kết ở tối thiểu 1 kỳ: Khóa nút nộp, báo vi phạm BR-02.", "ERR_TERM_MIN, BR-02"),
            ("EF-B", "Hệ thống", "Tại bước BF-7, nếu chưa chọn tiêu chí ưu tiên top: Nhắc nhở chọn theo BR-06.", "ERR_TOP_EMPTY, BR-06")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Sinh viên -> UI: Mở biểu mẫu Đăng ký phòng & Thói quen",
            "• Message 2 (BF-2): UI -> Sinh viên: Hiển thị 3 gói phòng và điều khoản cam kết (Ref: BR-02, BR-05)",
            "• Message 3 (BF-3): Sinh viên -> UI: Chọn loại phòng 2 người / 4 người",
            "• Message 4 (BF-4): Sinh viên -> UI: Điều chỉnh 8 thanh trượt thói quen sinh hoạt",
            "• Message 5 (BF-5): Sinh viên -> UI: Chọn tiêu chí số 1 (nhân trọng số 1.5x) (Ref: BR-06)",
            "• Message 6 (BF-6): Sinh viên -> UI: Tích chọn hộp kiểm cam kết tối thiểu 1 kỳ (Ref: BR-02)",
            "• Message 7 (BF-7): Sinh viên -> UI: Nhấn nút Nộp Hồ Sơ",
            "• Message 8 (BF-8): UI -> Survey Service -> DB: Lưu hồ sơ trạng thái Pending_Approval",
            "• Khối opt (AF-A): Nạp nhanh Persona mẫu (Thái Bảo, Văn Việt, Minh Quân)",
            "• Khối alt 1 (EF-A): Chưa tích cam kết 1 kỳ -> Khóa nút nộp và báo lỗi theo BR-02",
            "• Khối alt 2 (EF-B): Bỏ trống tiêu chí ưu tiên -> Báo lỗi chọn tiêu chí top theo BR-06"
        ],
        wf_id="WF-02",
        wf_name="Đăng Ký Loại Phòng & Khảo Sát Thói Quen",
        wf_elements=[
            ("WF-02-C01", "3 Card chọn loại phòng kèm đơn giá (VIP 2, Chuẩn 4, Tiết kiệm 6)", "Ánh xạ BF-2, BF-3, BR-05"),
            ("WF-02-C02", "Dropdown chọn tiêu chí ưu tiên số 1 (nhân trọng số 1.5x)", "Ánh xạ BF-5, BR-06"),
            ("WF-02-C03", "8 Thanh trượt thói quen sinh hoạt chuẩn hóa", "Ánh xạ BF-4"),
            ("WF-02-C04", "Hộp kiểm cam kết bắt buộc lưu trú tối thiểu 1 kỳ (5 tháng)", "Ánh xạ BF-6, BR-02"),
            ("WF-02-C05", "Nút bấm 'NỘP HỒ SƠ ĐĂNG KÝ PHÒNG'", "Ánh xạ BF-7, BF-8")
        ]
    )

    # UC-05
    render_detailed_usecase(
        sec_num="6",
        uc_id="UC-05",
        uc_title="Xem Bảng Xếp hạng Bạn cùng phòng (View Roommate Ranking)",
        uc_desc="Mô tả cách sinh viên tra cứu danh sách bạn cùng phòng tương thích, sắp xếp giảm dần theo điểm hòa hợp 2 chiều và đối sánh chi tiết 8 tiêu chí.",
        actors="Sinh viên (Primary Actor), Động cơ Chấm điểm KTX (Secondary Service)",
        precond="Sinh viên đã hoàn thành khai báo thói quen sinh hoạt (UC-04).",
        postcond="Sinh viên nắm rõ danh sách ứng viên hòa hợp nhất và có thể gửi lời mời ghép nhóm quen (UC-06).",
        trigger="Sinh viên chọn tab 'Bảng Xếp Hạng Bạn Cùng Phòng'.",
        flow_rows=[
            ("BF-1", "Sinh viên", "Chọn tab 'Bảng Xếp Hạng Bạn Cùng Phòng' trên thanh menu.", "WF-03-Rank"),
            ("BF-2", "Hệ thống", "Gửi vector thói quen của sinh viên đến Dịch vụ Chấm điểm tương thích.", "Include: Tính điểm 2 chiều"),
            ("BF-3", "Động cơ Chấm điểm", "Tính điểm tương thích 2 chiều có nhân hệ số 1.5x cho tiêu chí top.", "BR-06, scoring.py"),
            ("BF-4", "Hệ thống", "Sắp xếp danh sách ứng viên giảm dần theo điểm trung bình (Top 1 đến Top N).", "Xếp hạng tương thích"),
            ("BF-5", "Hệ thống", "Hiển thị danh sách card ứng viên kèm điểm % và huy hiệu mức độ hòa hợp.", "Hoàn tất UC-05"),
            ("AF-A", "Sinh viên", "Bấm 'Xem chi tiết tiêu chí' trên card ứng viên để đối sánh trực quan 8 thói quen.", "Extend: Xem chi tiết tiêu chí"),
            ("EF-A", "Hệ thống", "Nếu chưa hoàn thành khảo sát: Hiển thị thông báo yêu cầu làm khảo sát trước.", "Bắt buộc dữ liệu đầu vào")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Sinh viên -> UI: Chọn chức năng Bảng xếp hạng bạn cùng phòng",
            "• Message 2 (BF-2): UI -> Scoring Service: Yêu cầu tính điểm tương thích với pool ứng viên",
            "• Message 3 (BF-2): Scoring Service -> DB: Truy vấn vector thói quen của các ứng viên",
            "• Message 4 (BF-3): Scoring Service: Tính ma trận điểm 2 chiều & nhân trọng số 1.5x (Ref: BR-06)",
            "• Message 5 (BF-4, BF-5): Scoring Service -> UI -> Sinh viên: Trả về danh sách Top ứng viên",
            "• Khối opt (AF-A): Xem phân tích so sánh song song 8 tiêu chí thói quen",
            "• Khối alt 1 (EF-A): Chưa làm khảo sát thói quen -> Báo lỗi yêu cầu hoàn thành khảo sát"
        ],
        wf_id="WF-03-Rank",
        wf_name="Bảng Xếp Hạng Bạn Cùng Phòng",
        wf_elements=[
            ("WF-Rank-C01", "Thanh bộ lọc ứng viên theo khoa và trường thành viên", "Ánh xạ BF-1"),
            ("WF-Rank-C02", "Card ứng viên Top 1 (Avatar, Tên, Trường, Điểm % hòa hợp, Huy hiệu)", "Ánh xạ BF-5"),
            ("WF-Rank-C03", "Nút 'Xem chi tiết tiêu chí' mở modal đối sánh 8 thanh trượt", "Ánh xạ AF-A"),
            ("WF-Rank-C04", "Nút 'Gửi lời mời ghép nhóm' kết nối bạn quen", "Ánh xạ liên kết UC-06")
        ]
    )

    # UC-13
    render_detailed_usecase(
        sec_num="7",
        uc_id="UC-13",
        uc_title="Thanh toán Tiền phòng & Đặt cọc 72h (Pay Dorm Fee and Deposit)",
        uc_desc="Mô tả quy trình sinh viên thanh toán tiền phòng kỳ 1 kèm tiền đặt cọc tài sản trong hạn 72 giờ qua Cổng thanh toán VNPay để chốt giữ chỗ chính thức.",
        actors="Sinh viên (Primary Actor), Cổng thanh toán VNPay (External Actor), Hệ thống KTX (Secondary Actor)",
        precond="Sinh viên đã có kết quả phân phòng chính thức và thời hạn 72h đang hiệu lực (BR-04).",
        postcond="Hợp đồng được chốt chính thức (Paid), sinh viên nhận Biên lai điện tử và Hợp đồng lưu trú có mã QR.",
        trigger="Sinh viên nhận thông báo trúng tuyển và mở màn hình 'Thanh toán & Đặt cọc'.",
        flow_rows=[
            ("BF-1", "Sinh viên", "Mở màn hình Thanh toán Tiền phòng & Đặt cọc từ thông báo trúng tuyển.", "WF-05, BR-04"),
            ("BF-2", "Hệ thống", "Hiển thị bảng kê: Tiền phòng Kỳ 1 (7tr) + Tiền cọc tài sản (1tr) = Tổng 8.000.000 VNĐ.", "BR-04 (Cọc 1tr, hạn 72h)"),
            ("BF-3", "Hệ thống", "Kích hoạt và hiển thị đồng hồ đếm ngược thời hạn thanh toán chính xác 72 giờ.", "BR-04 (Ràng buộc 72h)"),
            ("BF-4", "Sinh viên", "Chọn phương thức thanh toán: Cổng thanh toán VNPay (Quét mã VNPAY-QR).", "Include: Cổng VNPay"),
            ("BF-5", "Hệ thống", "Tạo đơn hàng bảo mật (TLS 1.3), sinh mã giao dịch và hiển thị mã VNPAY-QR.", "NFR-03 (Bảo mật giao dịch)"),
            ("BF-6", "Sinh viên", "Dùng Mobile Banking quét mã QR để xác nhận thanh toán số tiền 8.000.000 VNĐ.", "Thao tác thanh toán"),
            ("BF-7", "Cổng VNPay", "Xử lý trừ tiền an toàn, gửi callback vnp_ResponseCode == '00' về máy chủ KTX.", "Xác thực thành công"),
            ("BF-8", "Hệ thống", "Cập nhật trạng thái hợp đồng thành Paid, khóa vị trí giường chính thức.", "Chốt giữ chỗ 100%"),
            ("BF-9", "Hệ thống", "Tự động phát hành Biên lai điện tử và Hợp đồng lưu trú KTX có mã QR.", "Extend: Tải biên lai điện tử"),
            ("AF-A", "Sinh viên", "Tại bước BF-9, nhấn nút Tải biên lai điện tử và Tải hợp đồng số về thiết bị.", "Extend: Tải biên lai"),
            ("EF-A", "Hệ thống", "Tại bước BF-3, nếu quá 72h chưa nộp: Tự động hủy kết quả, chuyển phòng cho Waitlist.", "ERR_PAYMENT_TIMEOUT, BR-04"),
            ("EF-B", "Cổng VNPay", "Tại bước BF-7, nếu tài khoản không đủ số dư: Cổng báo FAILED, cho phép thử lại.", "ERR_INSUFFICIENT_FUNDS")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Sinh viên -> UI: Mở màn hình Thanh toán & Đặt cọc KTX",
            "• Message 2 (BF-2, BF-3): UI <-> Pay Service: Hiển thị bảng kê 8tr & Đồng hồ 72h (Ref: BR-04)",
            "• Message 3 (BF-4, BF-5): Sinh viên chọn VNPAY-QR -> UI gọi Payment Service tạo mã QR",
            "• Message 4 (BF-5): Payment Service -> Cổng VNPay: Tạo phiên thanh toán bảo mật (Ref: NFR-03)",
            "• Message 5 (BF-6): Sinh viên quét mã QR trên Mobile Banking",
            "• Message 6 (BF-7): Cổng VNPay gửi callback SUCCESS (vnp_ResponseCode = 00)",
            "• Message 7 (BF-8, BF-9): Cập nhật trạng thái Paid, khóa giường, phát hành Hợp đồng số",
            "• Khối alt 1 (EF-A): Quá 72h không thanh toán -> Hủy kết quả, thu hồi phòng cho Waitlist (Ref: BR-04)",
            "• Khối alt 2 (EF-B): Lỗi trừ tiền / Không đủ số dư -> Cổng báo FAILED, cho phép thử lại"
        ],
        wf_id="WF-05",
        wf_name="Thanh Toán Tiền Phòng & Cọc 72h",
        wf_elements=[
            ("WF-05-C01", "Đồng hồ đếm ngược 72 giờ thời gian thực", "Ánh xạ BF-3, BR-04"),
            ("WF-05-C02", "Bảng kê viện phí nội trú (7tr tiền phòng kỳ 1 + 1tr cọc cơ sở vật chất)", "Ánh xạ BF-2, BR-04"),
            ("WF-05-C03", "Khung hiển thị mã VNPAY-QR động thanh toán bảo mật TLS 1.3", "Ánh xạ BF-4, BF-5, NFR-03"),
            ("WF-05-C04", "Nút giả lập thanh toán thành công và nút Tải Hợp đồng KTX có mã QR", "Ánh xạ BF-7, BF-8, BF-9")
        ]
    )

    # UC-18
    render_detailed_usecase(
        sec_num="8",
        uc_id="UC-18",
        uc_title="Phê duyệt đơn KTX - Business Approve (Approve Application)",
        uc_desc="Mô tả quy trình Cán bộ KTX thẩm định tư cách lưu trú (MSSV trường A, kỷ luật, cam kết 1 kỳ) và phê duyệt đơn vào thuật toán phân phòng.",
        actors="Cán bộ quản lý KTX (Primary Actor), Hệ thống KTX (Secondary Actor)",
        precond="Hồ sơ đăng ký của sinh viên ở trạng thái Pending_Approval (UC-04).",
        postcond="Hồ sơ chuyển sang Approved_For_Matching (đủ điều kiện chạy Gale-Shapley) hoặc Rejected.",
        trigger="Cán bộ KTX đăng nhập Cổng Quản trị và mở module 'Thẩm định Đơn'.",
        flow_rows=[
            ("BF-1", "Cán bộ KTX", "Mở danh sách hồ sơ đăng ký KTX đang chờ thẩm định.", "WF-03"),
            ("BF-2", "Hệ thống", "Hiển thị danh sách hồ sơ Pending kèm tích xanh đối soát tự động BR-01 & BR-02.", "BR-01, BR-02"),
            ("BF-3", "Cán bộ KTX", "Chọn hồ sơ kiểm tra chi tiết nhân thân, điểm rèn luyện, lịch sử nội quy.", "Thẩm định nghiệp vụ"),
            ("BF-4", "Hệ thống", "Kiểm tra quỹ giường trống khả dụng đối với loại phòng sinh viên đăng ký.", "BR-05 (Quỹ phòng)"),
            ("BF-5", "Cán bộ KTX", "Nhấn nút 'Phê duyệt (Business Approve)'.", "BR-03 (Quyết định duyệt)"),
            ("BF-6", "Hệ thống", "Cập nhật trạng thái Approved_For_Matching, nạp vào hàng đợi phân phòng.", "Hoàn tất UC-18"),
            ("AF-A", "Cán bộ KTX", "Nhấn nút 'Duyệt hàng loạt (Batch Approve)' cho các hồ sơ đã có đủ tích xanh tự động.", "NFR-06 (Tối ưu vận hành)"),
            ("EF-A", "Cán bộ KTX", "Nếu phát hiện sinh viên vi phạm kỷ luật hoặc nợ phí: Nhấn 'Từ chối đơn' kèm lý do.", "Extend: Từ chối đơn, BR-03"),
            ("EF-B", "Cán bộ KTX", "Nếu thiếu minh chứng chính sách: Nhấn 'Yêu cầu bổ sung hồ sơ' để sinh viên cập nhật.", "Extend: Yêu cầu bổ sung")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Cán bộ KTX -> UI: Mở màn hình Thẩm định Hồ sơ",
            "• Message 2 (BF-2): UI <-> Approval Service: Lấy danh sách đơn Pending & Đối soát tự động BR-01, BR-02",
            "• Message 3 (BF-3, BF-4): Kiểm tra chi tiết hồ sơ & Hạn ngạch quỹ giường trống",
            "• Message 4 (BF-5, BF-6): Cán bộ KTX bấm 'Phê duyệt' -> Cập nhật trạng thái Approved_For_Matching",
            "• Khối opt (AF-A): Duyệt hàng loạt hồ sơ hợp lệ bằng 1 click",
            "• Khối alt 1 (EF-A): Phát hiện vi phạm kỷ luật -> Bấm 'Từ chối đơn' kèm lý do gửi email sinh viên"
        ],
        wf_id="WF-03",
        wf_name="Dashboard Thẩm Định Hồ Sơ KTX",
        wf_elements=[
            ("WF-03-C01", "KPI Bar: Tổng đơn, Đơn chờ duyệt (24 đơn), Quỹ phòng trống (120 giường)", "Ánh xạ BF-2, BF-4"),
            ("WF-03-C02", "Bảng danh sách hồ sơ Pending có huy hiệu đối soát tự động BR-01 & BR-02", "Ánh xạ BF-2"),
            ("WF-03-C03", "Nút bấm xanh 'Phê duyệt (Business Approve)'", "Ánh xạ BF-5, BR-03"),
            ("WF-03-C04", "Nút bấm đỏ 'Từ chối đơn' kèm modal nhập lý do kỷ luật", "Ánh xạ EF-A, BR-03")
        ]
    )

    # UC-24
    render_detailed_usecase(
        sec_num="9",
        uc_id="UC-24",
        uc_title="Thực hiện Ghép phòng Tự động (Execute Automated Room Matching)",
        uc_desc="Mô tả tiến trình hệ thống tự động chạy thuật toán Gale-Shapley kết hợp tối ưu lấp đầy 100% giường để phân phòng ổn định, triệt tiêu cặp chặn = 0 và tối đa hóa lợi nhuận KTX.",
        actors="Hệ thống / Scheduler (Primary Actor), Quản trị viên KTX (Observer)",
        precond="Kỳ đăng ký đã đóng, các hồ sơ tham gia đã được duyệt Approved_For_Matching (UC-18).",
        postcond="Kết quả phân phòng chính thức được lưu, đảm bảo Blocking Pairs = 0 và kích hoạt đồng hồ 72h.",
        trigger="Đến lịch tự động (Cron job) hoặc Quản trị viên KTX nhấn 'Khởi chạy Ghép phòng'.",
        flow_rows=[
            ("BF-1", "Hệ thống", "Kích hoạt tiến trình phân phòng tự động cho đợt tiếp nhận mới.", "WF-04, Scheduler"),
            ("BF-2", "Hệ thống", "Phân nhóm hồ sơ theo cùng loại phòng (2, 4, 6 người).", "BR-05, NFR-05"),
            ("BF-3", "Hệ thống", "Tính ma trận điểm tương thích 2 chiều, nhân trọng số 1.5x cho tiêu chí top.", "BR-06, scoring.py"),
            ("BF-4", "Hệ thống", "Xây dựng bảng ưu tiên sở thích giảm dần cho từng ứng viên.", "Preference Lists"),
            ("BF-5", "Hệ thống", "Thực thi giải thuật Gale-Shapley tìm các cặp ghép ổn định.", "Include: Gale-Shapley, NFR-01"),
            ("BF-6", "Hệ thống", "Gộp các cặp ổn định vào từng phòng thực tế theo nguyên tắc lấp đầy 100% giường.", "Include: Lấp đầy phòng, BR-05"),
            ("BF-7", "Hệ thống", "Kiểm chứng độ ổn định toán học: Xác nhận số cặp chặn bằng 0 (Blocking Pairs = 0).", "Include: Đếm BP, BR-07, NFR-02"),
            ("BF-8", "Hệ thống", "Lưu kết quả phân phòng vào DB và hiển thị báo cáo lấp đầy, doanh thu dự kiến.", "Hoàn tất UC-24"),
            ("BF-9", "Hệ thống", "Gửi thông báo trúng tuyển đến sinh viên và khởi động đồng hồ đếm ngược 72 giờ.", "Chuyển tiếp UC-13, BR-04"),
            ("AF-A", "Cán bộ KTX", "Sau khi có kết quả, cán bộ KTX có thể điều chỉnh thủ công (override) trước khi công bố.", "Chức năng Override UC-19"),
            ("EF-A", "Hệ thống", "Nếu số lượng sinh viên lẻ trong nhóm phòng: Ghép vào phòng dự phòng hoặc Waitlist đợt 2.", "Xử lý biên thuật toán")
        ],
        seq_messages=[
            "• Message 1 (BF-1): Scheduler -> UI: Kích hoạt lệnh chạy ghép phòng tự động",
            "• Message 2 (BF-2, BF-3): UI -> Gale-Shapley Engine: Truyền hồ sơ & Tính ma trận 2 chiều (Ref: BR-06)",
            "• Message 3 (BF-4, BF-5): Thực thi giải thuật Gale-Shapley (Benchmark < 1.0s theo NFR-01)",
            "• Message 4 (BF-6): Gộp cặp ổn định vào phòng theo nguyên tắc lấp đầy 100% giường (Ref: BR-05)",
            "• Message 5 (BF-7): Kiểm chứng độ ổn định: Blocking Pairs = 0 (Ref: BR-07, NFR-02)",
            "• Message 6 (BF-8, BF-9): Lưu kết quả, kích hoạt đồng hồ 72h & phát thông báo trúng tuyển (Ref: BR-04)",
            "• Khối opt (AF-A): Cán bộ KTX điều chỉnh phân phòng thủ công (manual override) trước khi công bố"
        ],
        wf_id="WF-04",
        wf_name="Phân Phòng Gale-Shapley & Lấp Đầy",
        wf_elements=[
            ("WF-04-C01", "Nút bấm '▶ KHỞI CHẠY GALE-SHAPLEY' (thời gian chạy < 1s)", "Ánh xạ BF-1, NFR-01"),
            ("WF-04-C02", "Widget chứng chỉ ổn định toán học: 0 CẶP CHẶN (Blocking Pairs = 0)", "Ánh xạ BF-7, BR-07, NFR-02"),
            ("WF-04-C03", "Widget tối ưu lấp đầy phòng: 100% LẤP ĐẦY GIƯỜNG", "Ánh xạ BF-6, BF-8, BR-05"),
            ("WF-04-C04", "Sơ đồ mặt bằng phân phòng thực tế theo Tầng 2 & Tầng 3", "Ánh xạ BF-6, BF-8"),
            ("WF-04-C05", "Nút 'Xuất file CSV' và nút 'Công bố kết quả & Kích hoạt 72h'", "Ánh xạ BF-9, BR-04")
        ]
    )

    # ==================== MỤC 10: MA TRẬN TRUY VẾT 1-TO-1 ====================
    add_heading_1(doc, "10. BẢNG MA TRẬN TRUY VẾT 1-TO-1 (TRACEABILITY MATRIX)")
    add_body(doc, "Bảng ma trận truy vết chứng minh sự liên kết nhất quán 100% giữa Bước đặc tả, Message Sequence, Thành phần Wireframe và Quy tắc nghiệp vụ:")

    tbl_trace = doc.add_table(rows=17, cols=6)
    tbl_trace.alignment = WD_TABLE_ALIGNMENT.CENTER
    trace_heads = ["Mã UC", "Bước Đặc Tả (Step ID)", "Message Sequence", "Mã Thành Phần Wireframe", "Quy Tắc Nghiệp Vụ (BR)", "Khớp 1-1?"]
    trace_widths = [Inches(0.7), Inches(1.1), Inches(1.6), Inches(1.5), Inches(1.4), Inches(0.7)]

    for j, h in enumerate(trace_heads):
        cell = tbl_trace.rows[0].cells[j]
        cell.width = trace_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=50, bottom=50, left=40, right=40)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(8.5), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    trace_data = [
        ("UC-01", "BF-3", "Message 3 (SV -> UI)", "WF-01-C02 (Form MSSV/Pass)", "BR-01 (Đúng trường A)", "✅ 100%"),
        ("UC-01", "AF-A", "Message opt (AF-A)", "WF-01-C03 (Ghi nhớ 30 ngày)", "NFR-06 (Tiện ích)", "✅ 100%"),
        ("UC-01", "EF-B", "Message 16, 17 (EF-B)", "WF-01-C05 (Alert sai trường)", "BR-01 (Từ chối sai trường)", "✅ 100%"),
        ("UC-04", "BF-2, BF-3", "Message 2, 3 (UI -> SV)", "WF-02-C01 (3 Gói phòng)", "BR-05 (Loại phòng)", "✅ 100%"),
        ("UC-04", "BF-4", "Message 4 (SV -> UI)", "WF-02-C03 (8 Thanh trượt)", "8 Tiêu chí thói quen", "✅ 100%"),
        ("UC-04", "BF-5", "Message 5 (SV -> UI)", "WF-02-C02 (Dropdown top)", "BR-06 (Trọng số 1.5x)", "✅ 100%"),
        ("UC-04", "BF-6", "Message 6 (SV -> UI)", "WF-02-C04 (Hộp kiểm cam kết)", "BR-02 (Tối thiểu 1 kỳ)", "✅ 100%"),
        ("UC-05", "BF-3", "Message 4 (Scoring)", "WF-Rank-C02 (Card Top 1)", "BR-06 (Ma trận 2 chiều)", "✅ 100%"),
        ("UC-05", "AF-A", "Message opt (AF-A)", "WF-Rank-C03 (Xem chi tiết)", "NFR-06 (Minh bạch điểm)", "✅ 100%"),
        ("UC-13", "BF-2", "Message 2 (Bảng kê)", "WF-05-C02 (Bảng kê 8tr)", "BR-04 (7tr phòng + 1tr cọc)", "✅ 100%"),
        ("UC-13", "BF-3", "Message 2 (Đồng hồ 72h)", "WF-05-C01 (Đồng hồ đếm ngược)", "BR-04 (Hạn 72h)", "✅ 100%"),
        ("UC-13", "BF-5", "Message 4 (Tạo QR)", "WF-05-C03 (Mã VNPAY-QR)", "NFR-03 (Bảo mật TLS 1.3)", "✅ 100%"),
        ("UC-18", "BF-2", "Message 2 (Đối soát)", "WF-03-C02 (Tích xanh BR-01/02)", "BR-01, BR-02", "✅ 100%"),
        ("UC-18", "BF-5", "Message 4 (Approve)", "WF-03-C03 (Nút Approve xanh)", "BR-03 (Business Approve)", "✅ 100%"),
        ("UC-24", "BF-6", "Message 4 (Lấp đầy)", "WF-04-C03 (Widget 100% Lấp đầy)", "BR-05 (Occupancy 100%)", "✅ 100%"),
        ("UC-24", "BF-7", "Message 5 (Đếm BP)", "WF-04-C02 (Widget 0 Cặp chặn)", "BR-07, NFR-02 (BP = 0)", "✅ 100%")
    ]

    for i, rdata in enumerate(trace_data):
        row = tbl_trace.rows[i + 1]
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(rdata):
            cell = row.cells[j]
            cell.width = trace_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=35, bottom=35, left=40, right=40)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if (1 <= j <= 4) else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(val)
            run.font.name, run.font.size = 'Times New Roman', Pt(8)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            elif j == 5:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x16, 0x65, 0x34)

    # ==================== PHẦN V: BỘ DIAGRAM (SEQUENCE, ACTIVITY, COMPONENT) ====================
    doc.add_page_break()
    add_heading_1(doc, "PHẦN V: BỘ DIAGRAM THEO CHỈ ĐẠO CỦA GIẢNG VIÊN (SEQUENCE, ACTIVITY, COMPONENT)")
    add_body(doc, "Căn cứ theo ghi chú trên bảng lớp của Giảng viên: 'Bộ diagram -> Sequence (1), Activity (2), Component (3)', hệ thống KTX Smart Match được phân tích và thiết kế hoàn chỉnh qua ba tầng biểu đồ chuẩn mực:")

    add_heading_2(doc, "1. Biểu Đồ Tuần Tự (Sequence Diagram - 1)")
    add_body(doc, "Toàn bộ 6 Use Case (UC-01, UC-04, UC-05, UC-13, UC-18, UC-24) đã được mô hình hóa bằng Sequence Diagram chi tiết ở Phần III, đánh số thứ tự thông điệp khớp 1-to-1 với từng Step ID trong Bảng Three Types of Flows (BF-1..n, AF-A..n, EF-A..n), có đầy đủ khối điều kiện rẽ nhánh alt và tùy chọn opt.")

    add_heading_2(doc, "2. Biểu Đồ Hoạt Động Tổng Thể (Activity Diagram - 2)")
    add_body(doc, "Activity Diagram thể hiện luồng nghiệp vụ end-to-end xuyên suốt toàn bộ vòng đời đăng ký và phân phòng KTX:")
    add_body(doc, "• Bước 1 (Khởi tạo): Sinh viên đăng nhập qua cổng trường A (BR-01) -> Mở form chọn loại phòng 2/4/6 người (BR-05) -> Khai báo 8 chỉ số thói quen -> Chọn tiêu chí top x1.5 (BR-06) -> Tích cam kết tối thiểu 1 kỳ (BR-02) -> Nộp đơn (UC-04).")
    add_body(doc, "• Bước 2 (Thẩm định Nghiệp vụ): Hồ sơ ở trạng thái Pending_Approval -> Cán bộ KTX thẩm định kỷ luật & quỹ phòng (UC-18) -> Nếu không đạt: Từ chối đơn và gửi email lý do -> Nếu đạt chuẩn: Phê duyệt Business Approve (BR-03), chuyển sang trạng thái Approved_For_Matching.")
    add_body(doc, "• Bước 3 (Ghép phòng Tự động): Động cơ Gale-Shapley tính ma trận tương thích 2 chiều -> Chạy thuật toán Gale-Shapley (< 1.0s, NFR-01) -> Gộp cặp lấp đầy 100% giường (BR-05) -> Kiểm chứng triệt tiêu cặp chặn Blocking Pairs = 0 (BR-07, NFR-02) -> Lưu kết quả và công bố.")
    add_body(doc, "• Bước 4 (Thanh toán 72h): Hệ thống kích hoạt đồng hồ đếm ngược 72 giờ (BR-04) -> Sinh viên quét mã VNPay-QR nộp 8.000.000 VNĐ (7tr tiền phòng + 1tr cọc) (UC-13) -> Nếu thành công: Cấp hợp đồng số & mã thẻ phòng -> Nếu quá hạn 72h: Tự động hủy kết quả, chuyển sinh viên sang danh sách chờ Waitlist (UC-26).")

    add_heading_2(doc, "3. Biểu Đồ Thành Phần Hệ Thống (Component Diagram - 3)")
    add_body(doc, "Component Diagram mô tả kiến trúc phân rã 5 tầng module phần mềm và giao thức kết nối:")
    add_body(doc, "• Tầng 1 (Presentation Layer): Student Web Portal (giao diện sinh viên Next.js/Tailwind) & Admin Dashboard (giao diện cán bộ thẩm định, điều hành).")
    add_body(doc, "• Tầng 2 (Security & Gateway Component): API Gateway, Authentication Service (JWT / HttpOnly Cookie / RBAC), School A Connector (kết nối LDAP/REST đối soát MSSV theo BR-01).")
    add_body(doc, "• Tầng 3 (Core Business Services): Application & Approval Service (thẩm định đơn BR-02, BR-03), Scoring & Ranking Service (ma trận 2 chiều BR-06), Gale-Shapley Matching Engine (BP=0, BR-07, NFR-01), Room Occupancy Optimizer (lấp đầy 100% giường BR-05), Timer & Cleanup Scheduler (đếm ngược 72h BR-04, UC-26).")
    add_body(doc, "• Tầng 4 (External Integration Component): VNPay Payment Adapter (tạo QR động, xử lý Webhook IPN, đối soát chữ ký băm SHA-256 theo NFR-03), E-Contract & Receipt Generator (sinh hợp đồng điện tử & biên lai có mã QR).")
    add_body(doc, "• Tầng 5 (Persistence Layer): Relational Database KTX (PostgreSQL/SQLite lưu sinh viên, phòng, hồ sơ, giao dịch) & Audit Log (lưu vết bảo mật và chứng chỉ cặp chặn).")

    # Save to Downloads and docs/
    p_downloads = r"C:\Users\LENOVO\Downloads\Tai_Lieu_Dac_Ta_UseCase_Va_Sequence_Diagram_KTX.docx"
    p_docs = os.path.join(os.path.dirname(__file__), "docs", "Tai_Lieu_Dac_Ta_UseCase_Va_Sequence_Diagram_KTX.docx")

    doc.save(p_downloads)
    doc.save(p_docs)
    print("SUCCESS: Generated docx at:")
    print("1.", p_downloads)
    print("2.", p_docs)

if __name__ == "__main__":
    build_document()
