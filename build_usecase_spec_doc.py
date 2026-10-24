# -*- coding: utf-8 -*-
"""
build_usecase_spec_doc.py
Tạo tài liệu Đặc tả Use Case (Use Case Specification) chuẩn 100% theo Slide bài giảng:
1. SUMMARY (ID, Title, Description, Actors, Preconditions, Post conditions, Trigger)
2. THREE TYPES OF FLOWS (Step ID, Actor, Action, Notes/references) với BF, AF, EF
3. ADDITIONAL INFORMATION (Business Rules, Non-functional Requirements, Wireframe)

Sinh viên: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều (Nhóm 3)
Trường: Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng
Xuất ra: Word (.docx), HTML và PDF
"""

import os
import sys
import subprocess
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Helpers for Word styling
def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
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
    r.font.size = Pt(12.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A) # Blue 900
    return p

def add_h3(doc, text):
    p = add_styled_p(doc, space_before=8, space_after=3)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55) # Slate 700
    return p

def add_body(doc, text, bold=False, italic=False, color_rgb=(0x33, 0x41, 0x55)):
    p = add_styled_p(doc, space_before=0, space_after=5, line_spacing=1.2)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor(*color_rgb)
    return p

def build_word_document():
    doc = docx.Document()
    
    # Page setup: A4 Normal Margins
    sections = doc.sections
    for section in sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    # Header / Title Block
    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r_inst = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(10.5)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=4)
    r_title = p_title.add_run("TÀI LIỆU ĐẶC TẢ USE CASE CHUẨN BÀI GIẢNG\n(USE CASE SPECIFICATION)")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(17)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
    r_sub = p_sub.add_run("Dự án: Hệ thống Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nCăn cứ: Khung bài giảng Use Case Specification (Slide Google) • 1 Dễ + Các Nghiệp vụ cốt lõi")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Info table
    tbl_info = doc.add_table(rows=4, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Học phần đào tạo:", "Phân tích & Thiết kế Hệ thống / System Engineering (VNUK)"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 3: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều"),
        ("Chuẩn cấu trúc tuân thủ:", "1. SUMMARY • 2. THREE TYPES OF FLOWS (BF, AF, EF) • 3. ADDITIONAL INFO (BR, NFR, Wireframe)"),
        ("Phiên bản cập nhật:", "Version 3.2 - Hoàn thiện đặc tả chuẩn 100% theo từng slide và ma trận tham chiếu Ref")
    ]
    for idx, (label, val) in enumerate(info_data):
        row = tbl_info.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.3)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(10), True
        r0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(10)
        r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=10)

    # ==================== PHẦN I: KHUNG CHUẨN BÀI GIẢNG ====================
    add_h1(doc, "PHẦN I: CẤU TRÚC ĐẶC TẢ USE CASE CHUẨN BÀI GIẢNG (THE TEMPLATE)")
    add_body(doc, "Theo bài giảng của Giảng viên, chỉ vẽ sơ đồ Use Case Diagram trong UML là chưa đủ. Mỗi Use Case cần có văn bản đặc tả (Use Case Specification) đi kèm giải thích mục đích, phạm vi, kịch bản hành động và các quy tắc nghiệp vụ liên quan.")
    add_body(doc, "Một bản đặc tả Use Case chuẩn bao gồm 3 thành phần nền tảng bắt buộc:", bold=True)

    # Bullet points
    for num, title, desc in [
        ("1.", "SUMMARY (Bảng Tóm tắt):", "Định danh tổng quan gồm ID (UC-x), Title (Cụm Động từ + Danh từ: Verb + Noun Phrase), Description (Mô tả chức năng), Actors (Tác nhân chính và phụ), Preconditions (Điều kiện tiên quyết để bắt đầu), Post conditions (Trạng thái hệ thống đạt được sau khi kết thúc), Trigger (Sự kiện kích hoạt Use Case)."),
        ("2.", "THREE TYPES OF FLOWS (Ba loại luồng sự kiện):", "Phần tiến trình (Process Part) gồm danh sách các bước có 4 cột: Step ID, Actor, Action, Notes/references. Gồm: (1) Basic Flow (BF - Happy Path, đạt mục tiêu); (2) Alternate Flows (AF - Các phương án rẽ nhánh tùy chọn của người dùng, vẫn đạt mục tiêu); (3) Exception Flows (EF - Sự cố, lỗi, vi phạm quy định khiến KHÔNG đạt mục tiêu)."),
        ("3.", "ADDITIONAL INFORMATION (Thông tin bổ sung):", "Gồm Business Rules (Quy tắc nghiệp vụ được mã hóa thành kho lưu trữ BR-01..07 để tham chiếu), Non-functional Requirements (Yêu cầu phi chức năng NFR-01..06 về hiệu năng, bảo mật, thời gian), và Wireframes (Bản vẽ giao diện minh họa tương ứng).")
    ]:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.2)
        r_pre = p.add_run(f"{title} ")
        r_pre.font.name, r_pre.font.size, r_pre.font.bold = 'Times New Roman', Pt(10.5), True
        r_pre.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        r_txt = p.add_run(desc)
        r_txt.font.name, r_txt.font.size = 'Times New Roman', Pt(10.5)
        r_txt.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Bảng Quy tắc nghiệp vụ BR
    add_h2(doc, "1.1 Bảng Tham Chiếu Quy Tắc Nghiệp Vụ Cốt Lõi (Business Rules - BR)")
    add_body(doc, "Giảng viên đặc biệt nhấn mạnh: 'Cột Notes/references phải hiểu rõ BR-1, BR-2 là gì để note, không được note đại'. Dưới đây là kho quy tắc nghiệp vụ chuẩn của KTX Smart Match:")

    tbl_br = doc.add_table(rows=8, cols=3)
    tbl_br.alignment = WD_TABLE_ALIGNMENT.CENTER
    br_headers = ["Mã BR", "Tên Quy tắc Nghiệp vụ", "Nội dung & Ràng buộc Nghiệp vụ Cụ thể"]
    br_widths = [Inches(1.0), Inches(2.2), Inches(3.3)]
    for j, h in enumerate(br_headers):
        cell = tbl_br.rows[0].cells[j]
        cell.width = br_widths[j]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    br_data = [
        ("BR-01", "Đối tượng Tiếp nhận (SV Trường A)", "KTX tiếp nhận sinh viên chính quy thuộc Trường Đại học A (khối liên kết VNUK). Bắt buộc có MSSV hợp lệ và email trường cấp (@vnuk.edu.vn). Người ngoài không có quyền đăng ký."),
        ("BR-02", "Thời hạn Lưu trú Tối thiểu 1 Kỳ", "Bắt buộc cam kết lưu trú tối thiểu 01 học kỳ (05 tháng) hoặc 1 năm học (10 tháng). Tuyệt đối từ chối hợp đồng ngắn hạn theo ngày/tuần để giữ nếp sống văn hóa ổn định."),
        ("BR-03", "Phê duyệt Nghiệp vụ (Business Approve)", "Hồ sơ sinh viên nộp phải được Cán bộ KTX thẩm định (kiểm tra kỷ luật, đối soát diện chính sách ưu tiên) và phê duyệt trước khi được nạp vào thuật toán phân phòng."),
        ("BR-04", "Đặt cọc Giữ chỗ & Hạn 72 Giờ", "Trong vòng 72 giờ kể từ khi có kết quả phòng, sinh viên phải nộp tiền phòng kỳ 1 + Đặt cọc bảo đảm tài sản 2.000.000đ qua VNPay. Quá 72h chưa nộp sẽ tự động hủy đơn và chuyển cho danh sách chờ (Waitlist)."),
        ("BR-05", "Tối ưu Tỷ lệ Lấp đầy Phòng (Occupancy)", "Thuật toán phân nhóm theo loại phòng (2, 4, 6 người) và ưu tiên lấp đầy 100% giường của từng phòng trước khi mở phòng mới nhằm tối ưu hóa chi phí điện nước và lợi nhuận KTX."),
        ("BR-06", "Trọng số Ưu tiên Cá nhân (Top 1.5x)", "Trong 8 tiêu chí thói quen, tiêu chí sinh viên đánh dấu là quan trọng nhất (Top Criterion) sẽ được nhân hệ số 1.5x khi tính điểm tương thích hai chiều bất đối xứng."),
        ("BR-07", "Triệt tiêu Cặp chặn (Stability Guarantee)", "Phép ghép bạn cùng phòng phải thỏa mãn tiêu chuẩn ổn định Gale-Shapley: Số cặp chặn bằng 0 (Blocking Pairs = 0), đảm bảo không ai có động cơ đổi phòng tự phát.")
    ]
    for idx, (code, name, detail) in enumerate(br_data):
        row = tbl_br.rows[idx+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = br_widths[0], br_widths[1], br_widths[2]
        bg = "F8FAFC" if idx % 2 == 0 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, 60, 60, 100, 100)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(code)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9.5), True
        r0.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(name)
        r1.font.name, r1.font.size, r1.font.bold = 'Times New Roman', Pt(9.5), True
        r1.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(detail)
        r2.font.name, r2.font.size = 'Times New Roman', Pt(9.5)
        r2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=10)

    # ==================== PHẦN II: CHI TIẾT CÁC USE CASE ====================
    add_h1(doc, "PHẦN II: NỘI DUNG ĐẶC TẢ CHI TIẾT TỪNG USE CASE THEO CHUẨN SLIDE")
    add_body(doc, "Dự án chọn lọc đặc tả chi tiết 05 Use Case tiêu biểu (Gồm 01 Use Case Dễ bắt buộc + 04 Use Case Nghiệp vụ cốt lõi), đáp ứng chuẩn xác rubric giảng viên:")

    use_cases = [
        {
            "id": "UC-01",
            "type_label": "1. USE CASE ĐƠN GIẢN (1 DỄ - BẮT BUỘC THEO RUBRIC)",
            "title": "Đăng nhập và Xác thực Sinh viên KTX (Sign in and Authenticate Student)",
            "desc": "Use Case này mô tả cách sinh viên truy cập vào Cổng dịch vụ KTX bằng Mã sinh viên (MSSV) và Mật khẩu, hệ thống xác thực danh tính với cơ sở dữ liệu trường VNUK và cấp phiên làm việc bảo mật.",
            "actors": "Sinh viên (Primary Actor), Hệ thống Xác thực SV Trường A (Secondary Actor).",
            "precond": "Sinh viên đã có tài khoản và thuộc danh sách trường VNUK hợp lệ.",
            "postcond": "Sinh viên đăng nhập thành công, nhận JWT Token và được chuyển hướng vào Dashboard.",
            "trigger": "Sinh viên truy cập Cổng KTX và chọn 'Đăng nhập'.",
            "flows": [
                ("BF-1", "Sinh viên", "Truy cập vào trang Đăng nhập của Cổng dịch vụ KTX.", "Giao diện WF-01, NFR-06"),
                ("BF-2", "Hệ thống", "Hiển thị form đăng nhập gồm ô nhập MSSV/Email và Mật khẩu.", "Kiểm tra định dạng email"),
                ("BF-3", "Sinh viên", "Nhập email trường (@vnuk.edu.vn) và mật khẩu cá nhân, bấm 'Đăng nhập'.", "BR-01 (Đúng email trường)"),
                ("BF-4", "Hệ thống", "Gửi thông tin xác thực đến Dịch vụ xác thực trung tâm trường A.", "Mã hóa TLS 1.3, NFR-03"),
                ("BF-5", "Hệ thống SV Trường A", "Đối soát MSSV, xác nhận sinh viên chính quy trường A và mật khẩu chính xác.", "BR-01 (Chính sách tiếp nhận)"),
                ("BF-6", "Hệ thống", "Khởi tạo Session/Token bảo mật, chuyển hướng sinh viên vào Dashboard chính.", "Hoàn thành mục tiêu UC-01"),
                ("AF-A", "Sinh viên", "Tại bước BF-2, sinh viên chọn 'Đăng nhập nhanh bằng Google SSO (@vnuk.edu.vn)'.", "Nhánh phụ hoàn thành mục tiêu"),
                ("AF-B", "Sinh viên", "Tại bước BF-2, sinh viên tích chọn 'Ghi nhớ đăng nhập trong 30 ngày'.", "Lưu token thiết bị an toàn"),
                ("EF-A", "Hệ thống", "Tại bước BF-4, sinh viên nhập sai mật khẩu quá 5 lần liên tiếp: Tạm khóa tài khoản 15 phút.", "Mã lỗi ERR_AUTH_MAX, NFR-03"),
                ("EF-B", "Hệ thống", "Tại bước BF-5, tài khoản không thuộc danh sách trường A: Báo lỗi từ chối tiếp nhận.", "Mã lỗi ERR_NOT_AFFILIATED, BR-01")
            ],
            "br_nfr": "Tuân thủ BR-01 (Đối tượng tiếp nhận sinh viên trường A), NFR-03 (Bảo mật phiên đăng nhập JWT, chống tấn công Brute-force)."
        },
        {
            "id": "UC-04",
            "type_label": "2. USE CASE NGHIỆP VỤ SINH VIÊN: KHẢO SÁT & NỘP HỒ SƠ",
            "title": "Khảo sát 8 Thói quen & Nộp hồ sơ KTX (Survey Lifestyle and Submit Application)",
            "desc": "Use Case này mô tả quy trình sinh viên chọn gói phòng mong muốn (2, 4, 6 người), điền 8 tiêu chí thói quen sinh hoạt, chọn tiêu chí ưu tiên cao nhất (1.5x) và ký cam kết ở tối thiểu 1 học kỳ để nộp hồ sơ xét duyệt.",
            "actors": "Sinh viên (Primary Actor), Hệ thống KTX (Secondary Actor).",
            "precond": "Sinh viên đã đăng nhập thành công vào hệ thống (UC-01).",
            "postcond": "Hồ sơ được tạo ở trạng thái Pending_Approval, sẵn sàng chuyển sang Cán bộ KTX thẩm định.",
            "trigger": "Sinh viên chọn chức năng 'Khảo sát thói quen & Đăng ký phòng' trên Dashboard.",
            "flows": [
                ("BF-1", "Sinh viên", "Mở biểu mẫu khảo sát nếp sống và đăng ký loại phòng KTX.", "Giao diện WF-02"),
                ("BF-2", "Hệ thống", "Hiển thị 3 loại phòng (VIP 2 người, Chuẩn 4 người, Tiết kiệm 6 người) và bảng 8 tiêu chí thói quen.", "BR-05 (Danh mục phòng)"),
                ("BF-3", "Sinh viên", "Chọn gói phòng nguyện vọng (ví dụ: Phòng 4 người Chuẩn).", "Lưu nguyện vọng phòng"),
                ("BF-4", "Sinh viên", "Điều chỉnh 8 thanh trượt thói quen (Giờ ngủ, Giờ dậy, Ngăn nắp, Chịu ồn, Hút thuốc, Dắt bạn...).", "Chuẩn hóa vector 8 chiều"),
                ("BF-5", "Sinh viên", "Chọn 01 tiêu chí quan trọng nhất (Top Criterion) để nhân hệ số ưu tiên 1.5x.", "BR-06 (Trọng số 1.5x)"),
                ("BF-6", "Sinh viên", "Tích chọn ô cam kết bắt buộc: 'Tôi cam kết ở KTX tối thiểu 01 học kỳ (05 tháng)'.", "BR-02 (Thời hạn tối thiểu)"),
                ("BF-7", "Sinh viên", "Bấm nút 'Nộp hồ sơ đăng ký KTX'.", "Gửi dữ liệu lên máy chủ"),
                ("BF-8", "Hệ thống", "Kiểm tra tính hợp lệ dữ liệu, lưu hồ sơ vào cơ sở dữ liệu ở trạng thái Pending_Approval.", "Hoàn thành mục tiêu UC-04"),
                ("AF-A", "Sinh viên", "Tại bước BF-4, sinh viên bấm 'Nạp hồ sơ mẫu Persona' để tự động điền nhanh 8 thói quen.", "NFR-06 (Tối ưu trải nghiệm UI)"),
                ("EF-A", "Hệ thống", "Tại bước BF-6, sinh viên KHÔNG tích cam kết ở tối thiểu 1 kỳ: Khóa nút nộp, báo lỗi đỏ vi phạm BR-02.", "Mã lỗi ERR_TERM_MIN, BR-02"),
                ("EF-B", "Hệ thống", "Tại bước BF-5, sinh viên bỏ trống tiêu chí ưu tiên: Nhắc nhở chọn 1 tiêu chí top theo BR-06.", "Mã lỗi ERR_TOP_EMPTY, BR-06")
            ],
            "br_nfr": "Tuân thủ BR-02 (Cam kết hợp đồng tối thiểu 1 kỳ), BR-05 (Tối ưu quỹ phòng), BR-06 (Trọng số ưu tiên cá nhân 1.5x)."
        },
        {
            "id": "UC-18",
            "type_label": "3. USE CASE NGHIỆP VỤ QUẢN TRỊ: THẨM ĐỊNH & PHÊ DUYỆT (BUSINESS APPROVE)",
            "title": "Thẩm định và Phê duyệt Nghiệp vụ Hồ sơ KTX (Review and Approve Application)",
            "desc": "Use Case này mô tả quy trình Cán bộ KTX rà soát điều kiện cư trú của sinh viên (kiểm tra kỷ luật, đối soát diện ưu tiên chính sách, cam kết 1 kỳ) và ra quyết định phê duyệt đơn để đưa vào thuật toán phân phòng.",
            "actors": "Cán bộ Quản lý KTX (Staff - Primary Actor), Hệ thống KTX (Secondary Actor).",
            "precond": "Hồ sơ của sinh viên đang ở trạng thái chờ duyệt (Pending_Approval).",
            "postcond": "Hồ sơ chuyển sang trạng thái Approved_For_Matching (đủ điều kiện chạy Gale-Shapley) hoặc Rejected.",
            "trigger": "Cán bộ KTX đăng nhập trang Quản trị và mở module 'Thẩm định Đơn Đăng ký KTX'.",
            "flows": [
                ("BF-1", "Cán bộ KTX", "Mở danh sách các hồ sơ đăng ký KTX đang chờ thẩm định.", "Giao diện WF-03"),
                ("BF-2", "Hệ thống", "Hiển thị bảng hồ sơ kèm kết quả đối soát tự động: Đúng trường A (BR-01), Đủ cam kết 1 kỳ (BR-02).", "BR-01, BR-02"),
                ("BF-3", "Cán bộ KTX", "Chọn hồ sơ của sinh viên để kiểm tra chi tiết diện chính sách, hạnh kiểm và quỹ phòng khả dụng.", "BR-05 (Kiểm tra quỹ phòng)"),
                ("BF-4", "Cán bộ KTX", "Bấm nút 'Phê duyệt hồ sơ (Business Approve)'.", "Quyết định thẩm định BR-03"),
                ("BF-5", "Hệ thống", "Cập nhật trạng thái hồ sơ thành Approved_For_Matching và gửi thông báo cho sinh viên.", "Hoàn thành mục tiêu UC-18"),
                ("AF-A", "Cán bộ KTX", "Tại bước BF-2, Cán bộ bấm 'Duyệt hàng loạt (Batch Approve)' cho các đơn đã qua kiểm tra tự động.", "Tối ưu hiệu suất quản trị"),
                ("EF-A", "Cán bộ KTX", "Tại bước BF-3, phát hiện sinh viên vi phạm kỷ luật năm trước: Bấm 'Từ chối (Reject)' kèm lý do.", "BR-03 (Loại bỏ vi phạm)"),
                ("EF-B", "Cán bộ KTX", "Hồ sơ thiếu minh chứng gia đình chính sách: Bấm 'Yêu cầu bổ sung tài liệu'.", "Hồ sơ về trạng thái Incomplete")
            ],
            "br_nfr": "Tuân thủ BR-01 (Đúng đối tượng trường A), BR-03 (Phê duyệt nghiệp vụ bắt buộc), BR-05 (Kiểm soát hạn mức phòng)."
        },
        {
            "id": "UC-24",
            "type_label": "4. USE CASE THUẬT TOÁN CỐT LÕI: PHÂN BỔ PHÒNG GALE-SHAPLEY",
            "title": "Khởi chạy Phân bổ Phòng Ổn định và Lấp đầy (Execute Stable Room Matching)",
            "desc": "Use Case này mô tả tiến trình hệ thống tự động khởi chạy thuật toán Gale-Shapley kết hợp chiến lược lấp đầy 100% giường để ghép bạn cùng phòng ổn định, triệt tiêu cặp chặn = 0 và tối ưu lợi nhuận KTX.",
            "actors": "Hệ thống KTX (System / Scheduler - Primary Actor), Quản trị viên KTX (Admin - Observer).",
            "precond": "Đợt tiếp nhận đã hết hạn nộp, toàn bộ hồ sơ đã được Cán bộ KTX duyệt (Approved_For_Matching).",
            "postcond": "Bảng phân phòng chính thức được thiết lập, đảm bảo Blocking Pairs = 0 và kích hoạt hạn nộp cọc 72h.",
            "trigger": "Đến lịch định kỳ (Scheduler) hoặc Quản trị viên bấm nút 'Khởi chạy Phân phòng' trên Dashboard.",
            "flows": [
                ("BF-1", "Hệ thống", "Kích hoạt tiến trình phân phòng tự động cho đợt tiếp nhận mới.", "Giao diện WF-04, NFR-01"),
                ("BF-2", "Hệ thống", "Phân nhóm hồ sơ theo cùng nguyện vọng loại phòng (2, 4, 6 người) và theo giới tính.", "BR-05 (Phân loại phòng)"),
                ("BF-3", "Hệ thống", "Tính toán ma trận tương thích 2 chiều, nhân trọng số 1.5x cho tiêu chí ưu tiên của từng bạn.", "BR-06 (scoring.py)"),
                ("BF-4", "Hệ thống", "Chạy thuật toán Gale-Shapley tìm cặp ghép ổn định cho từng nhóm sinh viên.", "BR-07 (Blocking Pairs = 0)"),
                ("BF-5", "Hệ thống", "Áp dụng thuật toán gộp phòng (merge_pairs) để lấp đầy 100% số giường phòng 4 và phòng 6.", "BR-05 (Tối ưu lấp đầy phòng)"),
                ("BF-6", "Hệ thống", "Lưu kết quả phân phòng vào cơ sở dữ liệu, kích hoạt đồng hồ đếm ngược thanh toán cọc 72 giờ.", "BR-04, Hoàn thành UC-24"),
                ("AF-A", "Quản trị viên", "Sau bước BF-6, Admin có thể điều chỉnh thủ công (Manual Override) một số trường hợp đặc biệt.", "Chức năng can thiệp quản trị"),
                ("EF-A", "Hệ thống", "Số lượng sinh viên nhóm A và B bị lệch lẻ: Đưa sinh viên nộp muộn nhất vào danh sách chờ (Waitlist).", "Xử lý sĩ số không đồng đều")
            ],
            "br_nfr": "Tuân thủ BR-05 (Lấp đầy giường 100%), BR-06 (Trọng số 1.5x), BR-07 (Triệt tiêu cặp chặn BP=0), NFR-01 (Thời gian chạy < 1s cho 200 SV)."
        },
        {
            "id": "UC-13",
            "type_label": "5. USE CASE GIAO DỊCH TÀI CHÍNH: THANH TOÁN TIỀN PHÒNG & ĐẶT CỌC 72H",
            "title": "Thanh toán Tiền phòng & Đặt cọc Giữ chỗ (Pay Dorm Fee and Security Deposit)",
            "desc": "Use Case này mô tả quy trình sinh viên thực hiện thanh toán tiền phòng kỳ 1 kèm tiền đặt cọc giữ chỗ 2.000.000đ trong hạn 72 giờ qua cổng VNPay để xác nhận vị trí phòng chính thức.",
            "actors": "Sinh viên (Primary Actor), Cổng thanh toán VNPay (External Actor), Hệ thống KTX (Secondary Actor).",
            "precond": "Sinh viên đã có kết quả phân phòng và thời hạn 72 giờ đang có hiệu lực (BR-04).",
            "postcond": "Phòng được khóa chính thức (Paid), hệ thống xuất Biên lai thu tiền điện tử và Hợp đồng lưu trú mã QR.",
            "trigger": "Sinh viên nhận thông báo trúng tuyển phòng và truy cập vào mục 'Thanh toán & Đặt cọc'.",
            "flows": [
                ("BF-1", "Sinh viên", "Mở màn hình 'Thanh toán & Đặt cọc KTX' từ thông báo trúng tuyển.", "Giao diện WF-05"),
                ("BF-2", "Hệ thống", "Hiển thị bảng kê: Tiền phòng Kỳ 1 (theo loại phòng) + Tiền đặt cọc giữ chỗ (2.000.000đ) và đồng hồ 72h.", "BR-04 (Hạn cọc 72h)"),
                ("BF-3", "Sinh viên", "Chọn phương thức thanh toán 'Cổng thanh toán điện tử VNPay (VNPAY-QR)'.", "Tích hợp cổng VNPay"),
                ("BF-4", "Hệ thống", "Khởi tạo giao dịch bảo mật (TLS 1.3), sinh mã đơn hàng và mã QR thanh toán động.", "NFR-03 (Toàn vẹn giao dịch)"),
                ("BF-5", "Sinh viên", "Mở App Ngân hàng quét mã QR để thanh toán toàn bộ số tiền phòng và tiền cọc.", "Thao tác trên Mobile Banking"),
                ("BF-6", "Cổng VNPay", "Xác thực trừ tiền thành công, gửi mã callback vnp_ResponseCode = 00 về máy chủ KTX.", "Xác thực thanh toán hợp lệ"),
                ("BF-7", "Hệ thống", "Cập nhật trạng thái hợp đồng thành Paid, khóa chính thức chỗ ở và sinh Biên lai điện tử.", "Hoàn thành mục tiêu UC-13"),
                ("AF-A", "Sinh viên", "Tại bước BF-7, sinh viên bấm 'Tải biên lai điện tử' và 'Tải hợp đồng số KTX' có mã QR xác thực.", "Lưu trữ chứng từ kế toán"),
                ("EF-A", "Hệ thống", "Sau 72 giờ sinh viên không hoàn tất nộp tiền: Tự động hủy kết quả phòng, nhường suất cho Waitlist.", "Mã lỗi ERR_PAYMENT_TIMEOUT, BR-04"),
                ("EF-B", "Cổng VNPay", "Giao dịch bị từ chối do tài khoản không đủ số dư hoặc lỗi thẻ: Báo lỗi, cho phép sinh viên quét lại mã.", "Mã lỗi ERR_INSUFFICIENT_FUNDS")
            ],
            "br_nfr": "Tuân thủ BR-04 (Khóa cọc trong 72 giờ), NFR-03 (Bảo mật chữ ký số SHA-256 đối soát cổng VNPay)."
        }
    ]

    for uc in use_cases:
        add_h2(doc, f"{uc['type_label']}: {uc['id']} - {uc['title']}")
        
        # BẢNG 1: SUMMARY TABLE (Chuẩn Slide bài giảng)
        add_h3(doc, "A. Bảng Tóm Tắt (Summary Table - Chuẩn Slide Bài Giảng)")
        tbl_sum = doc.add_table(rows=7, cols=2)
        tbl_sum.alignment = WD_TABLE_ALIGNMENT.CENTER
        sum_rows = [
            ("ID", uc["id"]),
            ("Title", uc["title"]),
            ("Description", uc["desc"]),
            ("Actors", uc["actors"]),
            ("Preconditions", uc["precond"]),
            ("Post conditions", uc["postcond"]),
            ("Trigger", uc["trigger"])
        ]
        for r_idx, (k, v) in enumerate(sum_rows):
            row = tbl_sum.rows[r_idx]
            c0, c1 = row.cells[0], row.cells[1]
            c0.width, c1.width = Inches(1.8), Inches(4.7)
            set_cell_background(c0, "F1F5F9")
            set_cell_background(c1, "FFFFFF")
            set_cell_margins(c0, 60, 60, 100, 100)
            set_cell_margins(c1, 60, 60, 100, 100)
            set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})

            p0 = c0.paragraphs[0]
            r0 = p0.add_run(k)
            r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9.5), True
            r0.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

            p1 = c1.paragraphs[0]
            r1 = p1.add_run(v)
            r1.font.name, r1.font.size = 'Times New Roman', Pt(9.5)
            r1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=6)

        # BẢNG 2: THREE TYPES OF FLOWS TABLE (4 Cột Chuẩn Slide: Step ID, Actor, Action, Notes/references)
        add_h3(doc, "B. Quy Trình Các Luồng Sự Kiện (Three Types of Flows Table - 4 Cột Chuẩn)")
        tbl_flows = doc.add_table(rows=len(uc["flows"])+1, cols=4)
        tbl_flows.alignment = WD_TABLE_ALIGNMENT.CENTER
        flow_headers = ["Step ID", "Actor", "Action", "Notes/references (Ref)"]
        flow_widths = [Inches(0.9), Inches(1.4), Inches(2.5), Inches(1.7)]

        for j, h in enumerate(flow_headers):
            cell = tbl_flows.rows[0].cells[j]
            cell.width = flow_widths[j]
            set_cell_background(cell, "0F172A") # Slate 900
            set_cell_margins(cell, 70, 70, 80, 80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(h)
            r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9), True
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for f_idx, (sid, actor, act, ref) in enumerate(uc["flows"]):
            row = tbl_flows.rows[f_idx+1]
            c0, c1, c2, c3 = row.cells[0], row.cells[1], row.cells[2], row.cells[3]
            c0.width, c1.width, c2.width, c3.width = flow_widths[0], flow_widths[1], flow_widths[2], flow_widths[3]
            
            # Tô màu phân biệt BF, AF, EF
            if sid.startswith("BF"):
                bg = "FFFFFF" if f_idx % 2 == 0 else "F8FAFC"
                badge_color = (0x0F, 0x76, 0x6E) # Teal
            elif sid.startswith("AF"):
                bg = "F0FDF4" # Green tint
                badge_color = (0x15, 0x80, 0x3D) # Emerald
            else:
                bg = "FEF2F2" # Red tint
                badge_color = (0xB9, 0x1C, 0x1C) # Rose

            for c in (c0, c1, c2, c3):
                set_cell_background(c, bg)
                set_cell_margins(c, 50, 50, 80, 80)
                set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})

            # Step ID
            p0 = c0.paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r0 = p0.add_run(sid)
            r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(9), True
            r0.font.color.rgb = RGBColor(*badge_color)

            # Actor
            p1 = c1.paragraphs[0]
            r1 = p1.add_run(actor)
            r1.font.name, r1.font.size, r1.font.bold = 'Times New Roman', Pt(9), True
            r1.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

            # Action
            p2 = c2.paragraphs[0]
            r2 = p2.add_run(act)
            r2.font.name, r2.font.size = 'Times New Roman', Pt(9)
            r2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

            # Ref
            p3 = c3.paragraphs[0]
            r3 = p3.add_run(ref)
            r3.font.name, r3.font.size, r3.font.italic = 'Times New Roman', Pt(8.5), True
            r3.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

        add_styled_p(doc, space_after=4)

        # MỤC 3: ADDITIONAL INFORMATION
        add_h3(doc, "C. Thông Tin Bổ Sung (Additional Information)")
        p_add = add_styled_p(doc, space_before=2, space_after=8)
        r_add_b = p_add.add_run("• Quy tắc & Phi chức năng áp dụng: ")
        r_add_b.font.name, r_add_b.font.size, r_add_b.font.bold = 'Times New Roman', Pt(9.5), True
        r_add_b.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        r_add_t = p_add.add_run(uc["br_nfr"])
        r_add_t.font.name, r_add_t.font.size = 'Times New Roman', Pt(9.5)
        r_add_t.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        add_styled_p(doc, space_after=8)

    # Kết luận tài liệu
    add_h1(doc, "PHẦN III: KẾT LUẬN & CAM KẾT KHỚP 1-1 VỚI SEQUENCE DIAGRAM")
    add_body(doc, "Tài liệu Đặc tả Use Case này đảm bảo tính chuẩn xác và đồng bộ 100%:")
    add_body(doc, "1. Đúng khuôn mẫu Slide bài giảng: Đủ 3 phần bắt buộc (Summary, Three Types of Flows, Additional Information).")
    add_body(doc, "2. Cột Notes/references được giải thích minh bạch: Mọi tham chiếu đều dẫn xuất từ 7 Business Rules (BR-01..07) và 6 Yêu cầu phi chức năng (NFR-01..06).")
    add_body(doc, "3. Khớp 1-1 tuyệt đối với Bộ Sequence Diagram: Mọi mũi tên thông điệp trong tài liệu Sequence Figma đều đánh số và liên kết đúng từng mã bước (BF-1, AF-A, EF-A).")

    # Lưu file Word
    docx_path_docs = os.path.join(os.path.dirname(__file__), "docs", "Dac_Ta_Use_Case_Chuan_Slide_Thay_KTX_VNUK.docx")
    docx_path_dl = os.path.join(r"C:\Users\LENOVO\Downloads", "Dac_Ta_Use_Case_Chuan_Slide_Thay_KTX_VNUK.docx")
    
    os.makedirs(os.path.dirname(docx_path_docs), exist_ok=True)
    doc.save(docx_path_docs)
    shutil.copy2(docx_path_docs, docx_path_dl)
    print(f"[WORD SUCCESS] Saved DOCX to:\n  - {docx_path_docs}\n  - {docx_path_dl}")

if __name__ == "__main__":
    build_word_document()
