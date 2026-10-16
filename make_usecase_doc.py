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

def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
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

def add_styled_paragraph(doc, text="", style='Normal', space_before=0, space_after=6, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.LEFT):
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

def build_document():
    doc = docx.Document()

    # Thiết lập lề A4 chuẩn học thuật
    for s in doc.sections:
        s.top_margin = Inches(0.9)
        s.bottom_margin = Inches(0.9)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(0.9)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)

    # ==================== TRANG BÌA TIÊU ĐỀ ====================
    p_inst = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r_inst = p_inst.add_run("ĐẠI HỌC ĐÀ NẴNG\nVIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK)")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_sub = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    r_sub = p_sub.add_run("BỘ MÔN KHOA HỌC MÁY TÍNH & TRÍ TUỆ NHÂN TẠO")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(10.5)
    r_sub.font.bold = False
    r_sub.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    p_title = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=16, space_after=8)
    r_title = p_title.add_run("TÀI LIỆU THUYẾT MINH VÀ BẢO VỆ BIỂU ĐỒ USE CASE\n(HỆ THỐNG GHÉP BẠN CÙNG PHÒNG KÝ TÚC XÁ THÔNG MINH)")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

    p_desc = add_styled_paragraph(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=20)
    r_desc = p_desc.add_run("Mô hình hóa yêu cầu chức năng, phân tích tương tác Actor - Use Case và luận giải chuẩn xác các quan hệ <<include>>, <<extend>> theo tiêu chuẩn UML")
    r_desc.font.name = 'Times New Roman'
    r_desc.font.size = Pt(11)
    r_desc.font.italic = True
    r_desc.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Hộp thông tin nhóm thực hiện
    tbl_meta = doc.add_table(rows=4, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_info = [
        ("Đề tài nghiên cứu:", "Hệ thống xếp phòng KTX theo độ tương thích thói quen (Gale-Shapley Matching)"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 3 (Đại diện các trường thành viên ĐH Đà Nẵng)"),
        ("Sinh viên bảo vệ:", "Nguyễn Duy Thái Bảo (VNUK), Lê Văn Việt (SPKT), Lê Minh Quân (DUE)"),
        ("Thời gian báo cáo:", "Học kỳ 1 – Năm học 2026")
    ]
    for i, (k, v) in enumerate(meta_info):
        r = tbl_meta.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.2)
        set_cell_background(c0, "F3F4F6")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, top=80, bottom=80, left=120, right=120)
        set_cell_margins(c1, top=80, bottom=80, left=120, right=120)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
        
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r0 = p0.add_run(k)
        r0.font.name, r0.font.size, r0.font.bold = 'Times New Roman', Pt(10.5), True
        r0.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r1 = p1.add_run(v)
        r1.font.name, r1.font.size = 'Times New Roman', Pt(10.5)
        r1.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    add_styled_paragraph(doc, space_after=14)

    # ==================== MỤC 1: TỔNG QUAN HỆ THỐNG VÀ BỐI CẢNH ====================
    add_heading_1(doc, "1. BỐI CẢNH DỰ ÁN VÀ TRIẾT LÝ THIẾT KẾ USE CASE")
    add_body(doc, "Trong công tác quản lý nội trú tại các ký túc xá đại học hiện nay, phương thức phân bổ phòng phổ biến là xếp ngẫu nhiên hoặc xếp theo thứ tự nộp hồ sơ. Cách làm truyền thống này bộc lộ nhược điểm nghiêm trọng khi đưa những sinh viên có nhịp sinh học và lối sống đối nghịch vào chung một không gian khép kín (điển hình như trường hợp sinh viên học sáng ngủ sớm bị xếp chung phòng với sinh viên chơi game đêm gõ phím cơ, hoặc người dị ứng khói thuốc bị xếp chung với người hút thuốc). Những xung đột kéo dài dẫn đến mất đoàn kết, sa sút kết quả học tập và tạo gánh nặng giải quyết đơn xin đổi phòng cho Ban quản lý.")
    add_body(doc, "Đề tài 'Hệ thống ghép bạn cùng phòng KTX thông minh' được xây dựng nhằm giải quyết triệt để bài toán này. Hệ thống số hóa quy trình khảo sát 8 tiêu chí kỹ thuật (giờ ngủ, giờ dậy, độ gọn gàng, không gian học tập, khả năng chịu tiếng ồn, tình trạng hút thuốc, tần suất dắt bạn về phòng, sở thích chung) kết hợp cùng trọng số ưu tiên cá nhân. Dựa trên ma trận điểm tương thích hai chiều, hệ thống áp dụng thuật toán Gale-Shapley (Deferred Acceptance) để xác lập các cặp ghép phòng đạt trạng thái cân bằng ổn định cao nhất, đảm bảo chỉ số cặp chặn bằng 0 (Blocking Pairs = 0).")
    add_body(doc, "Biểu đồ Use Case đóng vai trò là xương sống kiến trúc phần mềm, xác lập ranh giới rõ ràng giữa tác vụ người dùng sinh viên và quyền hạn điều hành của Ban quản lý ký túc xá, đồng thời phân định mạch lạc giữa các hành vi cốt lõi bắt buộc (<<include>>) và các hành vi mở rộng tùy chọn theo ngữ cảnh (<<extend>>).")

    # ==================== MỤC 2: PHÂN TÍCH TÁC NHÂN (ACTORS) ====================
    add_heading_1(doc, "2. PHÂN TÍCH VAI TRÒ CỦA CÁC TÁC NHÂN (ACTORS)")
    add_body(doc, "Hệ thống phân định 02 tác nhân chính (Primary Actors) tương tác trực tiếp với giao diện và 01 tác nhân phụ trợ (Secondary Actor / Engine) thực thi ngầm:")

    add_heading_2(doc, "2.1 Tác nhân Sinh viên (Student / Resident)")
    add_bullet(doc, "Là đối tượng hưởng thụ trực tiếp dịch vụ nội trú của ký túc xá.", "Đặc điểm vai trò: ")
    add_bullet(doc, "Được cấp tài khoản cá nhân gắn liền với mã số sinh viên và trường thành viên Đại học Đà Nẵng (VNUK, SPKT, DUE, DUT...).", "Phạm vi định danh: ")
    add_bullet(doc, "Thực hiện đăng ký, đăng nhập cổng dịch vụ, khai báo hồ sơ thói quen cá nhân (8 tiêu chí), chỉ định tiêu chí quan trọng nhất, xem bảng xếp hạng những người bạn cùng phòng tiềm năng (Top 1 đến Top 8) và tra cứu phân tích lý do tương thích.", "Các hành vi nghiệp vụ: ")

    add_heading_2(doc, "2.2 Tác nhân Ban quản lý KTX (Dormitory Management / Admin)")
    add_bullet(doc, "Là cán bộ phụ trách công tác quản lý phòng ốc, sinh viên nội trú và đảm bảo trật tự ký túc xá.", "Đặc điểm vai trò: ")
    add_bullet(doc, "Nắm giữ quyền quản trị cao nhất trên cơ sở dữ liệu phân bổ.", "Phạm vi thẩm quyền: ")
    add_bullet(doc, "Nạp dữ liệu khảo sát tập trung từ file CSV của toàn trường; thiết lập dữ liệu giả lập (Seed) để kiểm thử tải thuật toán ở các quy mô 20, 50, 100, 200 sinh viên; kích hoạt tiến trình ghép phòng tự động toàn diện; theo dõi báo cáo phân tích đối chứng giữa Gale-Shapley và ghép ngẫu nhiên; trích xuất file kết quả phân phòng chính thức.", "Các hành vi nghiệp vụ: ")

    add_heading_2(doc, "2.3 Tác nhân Hệ thống xử lý nền (System Engine)")
    add_bullet(doc, "Đóng vai trò là thành phần tự động hóa, thực thi các tính toán logic phức tạp mà người dùng không thể can thiệp thủ công (chạy ngầm).", "Bản chất kỹ thuật: ")
    add_bullet(doc, "Chịu trách nhiệm thực hiện thuật toán chấm điểm ma trận hai chiều, điều phối vòng lặp đề xuất - từ chối hoãn lại của Gale-Shapley, và duyệt ma trận để kiểm chứng tính ổn định (đếm cặp chặn).", "Chức năng cốt lõi: ")

    # ==================== MỤC 3: BẢNG DANH MỤC 16 USE CASE ====================
    add_heading_1(doc, "3. DANH MỤC CHI TIẾT 16 USE CASE VÀ ÁNH XẠ CHỨC NĂNG")
    add_body(doc, "Toàn bộ hệ thống được phân rã thành 16 Use Case chuẩn hóa, tương ứng trực tiếp với các Yêu cầu Chức năng (FR) và Yêu cầu Bên liên quan (SR) trong hồ sơ đặc tả phần mềm:")

    tbl_uc = doc.add_table(rows=17, cols=5)
    tbl_uc.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Mã UC", "Tên Use Case", "Tác nhân chính", "Phân loại UML", "Mục tiêu và Hành vi nghiệp vụ"]
    col_widths = [Inches(0.8), Inches(1.8), Inches(1.2), Inches(1.1), Inches(2.2)]

    # Header Row
    hdr_row = tbl_uc.rows[0]
    for j, h in enumerate(headers):
        cell = hdr_row.cells[j]
        cell.width = col_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(10), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    uc_data = [
        ("UC-01", "Đăng ký tài khoản", "Sinh viên", "Chính", "Sinh viên thiết lập tài khoản mới gắn với Mã sinh viên và mật khẩu."),
        ("UC-02", "Đăng nhập", "Sinh viên", "Chính", "Xác thực danh tính sinh viên trước khi cho phép vào Dashboard xếp phòng."),
        ("UC-03", "Xác thực thông tin sinh viên", "Hệ thống", "<<include>>", "Kiểm tra tính hợp lệ của tài khoản, trường đào tạo (VNUK, SPKT, DUE...)."),
        ("UC-04", "Khai báo thói quen sinh hoạt", "Sinh viên", "Chính", "Nhập 8 tiêu chí nếp sống (ngủ, dậy, gọn, ồn, thuốc...) và 1 tiêu chí ưu tiên 1.5x."),
        ("UC-05", "Nạp hồ sơ mẫu Persona", "Sinh viên", "<<extend>>", "Tùy chọn tải nhanh thói quen của Thái Bảo (VNUK), Văn Việt (SPKT), Minh Quân (DUE)."),
        ("UC-06", "Xem Bảng xếp hạng bạn cùng phòng", "Sinh viên", "Chính", "Hiển thị danh sách các ứng viên hòa hợp nhất được xếp thứ tự từ Hạng 1 đến Hạng 8."),
        ("UC-07", "Tính điểm tương thích 2 chiều", "Hệ thống", "<<include>>", "Tính toán đồng thời M[a][b] và M[b][a] theo trọng số 8 tiêu chí chuẩn hóa."),
        ("UC-08", "Xem chi tiết giải thích tiêu chí", "Sinh viên", "<<extend>>", "Hiển thị chi tiết các điểm cộng tương thích (>=0.75) và các cảnh báo nguy cơ (<=0.40)."),
        ("UC-09", "Quản lý dữ liệu sinh viên KTX", "Ban quản lý KTX", "Chính", "Quản trị danh sách tổng thể sinh viên nội trú Nhóm A (cũ) và Nhóm B (mới)."),
        ("UC-10", "Nạp dữ liệu từ file CSV", "Ban quản lý KTX", "<<extend>>", "Tùy chọn nạp dữ liệu hàng loạt từ file bảng tính khảo sát toàn trường."),
        ("UC-11", "Sinh dữ liệu giả lập (Seed)", "Ban quản lý KTX", "<<extend>>", "Tự động sinh N sinh viên giả lập có seed để thử nghiệm quy mô 20, 50, 100, 200."),
        ("UC-12", "Thực hiện ghép phòng tự động", "Ban quản lý KTX", "Chính", "Kích hoạt tiến trình xếp phòng tổng thể toàn ký túc xá."),
        ("UC-13", "Chạy thuật toán Gale-Shapley", "Hệ thống", "<<include>>", "Thực thi thuật toán đề xuất và chấp nhận hoãn lại đảm bảo ghép cặp ổn định."),
        ("UC-14", "Đếm cặp chặn (Blocking Pairs)", "Hệ thống", "<<include>>", "Quét kiểm tra toàn bộ các cặp chéo để chứng minh số cặp chặn bằng 0."),
        ("UC-15", "Xem báo cáo & so sánh đối chứng", "Ban quản lý KTX", "Chính", "Theo dõi biểu đồ cột đối sánh điểm hài lòng trung bình giữa Gale-Shapley và Ngẫu nhiên."),
        ("UC-16", "Xuất kết quả phân phòng (CSV)", "Ban quản lý KTX", "<<extend>>", "Tùy chọn tải về file bảng tính danh sách phòng chính thức để niêm yết.")
    ]

    for i, row_data in enumerate(uc_data):
        row = tbl_uc.rows[i + 1]
        bg_col = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        if "<<include>>" in row_data[3]:
            bg_col = "F0FDF4"
        elif "<<extend>>" in row_data[3]:
            bg_col = "FAF5FF"

        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = col_widths[j]
            set_cell_background(cell, bg_col)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j != 0 and j != 3 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(val)
            run.font.name, run.font.size = 'Times New Roman', Pt(9.5)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            elif j == 3:
                run.font.bold = True
                if "<<include>>" in val:
                    run.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
                elif "<<extend>>" in val:
                    run.font.color.rgb = RGBColor(0x7E, 0x22, 0xCE)
                else:
                    run.font.color.rgb = RGBColor(0x03, 0x69, 0xA1)
            else:
                run.font.color.rgb = RGBColor(0x37, 0x41, 0x51)

    add_styled_paragraph(doc, space_after=14)

    # ==================== MỤC 4: BẢN CHẤT LÝ THUYẾT INCLUDE VÀ EXTEND ====================
    add_heading_1(doc, "4. BẢN CHẤT LÝ THUYẾT VÀ LUẬN GIẢI QUAN HỆ <<INCLUDE>> VÀ <<EXTEND>>")
    add_body(doc, "Một trong những nội dung trọng tâm mà Giảng viên thường xuyên đặt câu hỏi kiểm tra tính vững vàng về mặt kỹ thuật phần mềm là: 'Tại sao lại dùng include ở đây mà không phải extend?' hoặc 'Mũi tên chỉ theo hướng nào và tại sao?'. Nhóm nghiên cứu làm rõ các nguyên lý cốt lõi như sau:")

    add_heading_2(doc, "4.1 Bản chất quan hệ <<include>> (Bắt buộc dùng chung)")
    add_body(doc, "Theo chuẩn OMG UML, quan hệ <<include>> thể hiện sự phụ thuộc bắt buộc. Khi Use case A thực hiện, hành vi của Use case B bắt buộc phải được kích hoạt như một mắt xích không thể tách rời trong luồng sự kiện chính. Use case A không thể hoàn tất nếu không gọi Use case B.")
    add_bullet(doc, "Mũi tên nét đứt có chữ <<include>> luôn hướng TỪ Use case chính SANG Use case được include (A ..> B).", "Quy tắc biểu diễn: ")
    add_bullet(doc, "Đăng ký (UC-01) và Đăng nhập (UC-02) bắt buộc phải qua Xác thực thông tin (UC-03). Không thể cho phép một sinh viên chưa được xác thực danh tính vào can thiệp dữ liệu phòng.", "Minh chứng 1 trong KTX: ")
    add_bullet(doc, "Xem Bảng xếp hạng (UC-06) bắt buộc phải qua Tính điểm tương thích 2 chiều (UC-07). Nếu không có thuật toán tính toán ma trận điểm, hệ thống hoàn toàn không có dữ liệu để kết xuất bảng xếp hạng Hạng 1 đến Hạng 8.", "Minh chứng 2 trong KTX: ")
    add_bullet(doc, "Thực hiện ghép phòng tự động (UC-12) bắt buộc phải qua Chạy thuật toán Gale-Shapley (UC-13) và Đếm cặp chặn (UC-14). Quy trình xếp phòng không thể xem là hoàn tất nếu chưa chạy giải thuật tối ưu và chưa kiểm tra chứng minh chỉ số Blocking Pairs = 0.", "Minh chứng 3 trong KTX: ")

    add_heading_2(doc, "4.2 Bản chất quan hệ <<extend>> (Mở rộng tùy điều kiện)")
    add_body(doc, "Quan hệ <<extend>> mô tả một hành vi tùy chọn (optional behavior) chỉ được kích hoạt khi thỏa mãn một điều kiện kích hoạt cụ thể (Extension Point). Điểm mấu chốt là Use case gốc (Base Use Case) vẫn hoàn toàn độc lập, đầy đủ ngữ nghĩa và có thể hoạt động trọn vẹn mà không cần đến Use case mở rộng.")
    add_bullet(doc, "Mũi tên nét đứt có chữ <<extend>> luôn hướng NGƯỢC TỪ Use case mở rộng VỀ Use case gốc (B ..> A). Đây là quy tắc rất dễ nhầm lẫn trong UML.", "Quy tắc biểu diễn: ")
    add_bullet(doc, "Nạp hồ sơ mẫu Persona (UC-05) extend Khai báo thói quen (UC-04). Sinh viên hoàn toàn có thể tự tay kéo thả các thanh trượt và tích chọn sở thích (luồng chính hoạt động độc lập). Hành vi nạp mẫu chỉ diễn ra khi sinh viên chủ động bấm vào các nút thử nhanh như Thái Bảo (VNUK), Văn Việt (SPKT) hay Minh Quân (DUE).", "Minh chứng 1 trong KTX: ")
    add_bullet(doc, "Xem chi tiết giải thích tiêu chí (UC-08) extend Xem Bảng xếp hạng (UC-06). Màn hình bảng xếp hạng mặc định chỉ hiển thị thẻ thông tin tóm tắt và % điểm. Chỉ khi người dùng tò mò muốn biết sâu và bấm 'Chi tiết tiêu chí ▼', khối giải thích tiêu chí cộng/trừ mới được mở ra.", "Minh chứng 2 trong KTX: ")
    add_bullet(doc, "Nạp CSV (UC-10) và Sinh dữ liệu Seed (UC-11) extend Quản lý dữ liệu sinh viên (UC-09). Quản lý sinh viên có thể thông qua nhập liệu giao diện từng người; việc tải file hay sinh giả lập chỉ là phương thức hỗ trợ mở rộng khi cần xử lý dữ liệu lớn.", "Minh chứng 3 trong KTX: ")
    add_bullet(doc, "Xuất kết quả CSV (UC-16) extend Xem báo cáo (UC-15). Ban quản lý có thể chỉ xem biểu đồ so sánh trên màn hình mà không bắt buộc phải tải file CSV về máy.", "Minh chứng 4 trong KTX: ")

    add_heading_2(doc, "4.3 Bảng so sánh đối chiếu toàn diện giữa <<include>> và <<extend>>")
    
    tbl_cmp = doc.add_table(rows=6, cols=3)
    tbl_cmp.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_heads = ["Tiêu chí phân biệt", "Quan hệ <<include>>", "Quan hệ <<extend>>"]
    c_widths = [Inches(1.8), Inches(2.6), Inches(2.6)]

    for j, h in enumerate(c_heads):
        cell = tbl_cmp.rows[0].cells[j]
        cell.width = c_widths[j]
        set_cell_background(cell, "1B365D")
        set_cell_margins(cell, top=90, bottom=90, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name, run.font.size, run.font.bold = 'Times New Roman', Pt(10), True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    cmp_data = [
        ("Tính chất thực thi", "Bắt buộc 100% (Phải chạy qua thì Use case chính mới hoàn tất).", "Tùy chọn (Chỉ kích hoạt khi người dùng hoặc hệ thống kích hoạt điều kiện mở rộng)."),
        ("Tính trọn vẹn của Use case gốc", "Use case gốc không hoàn chỉnh nếu thiếu phần logic của Use case được include.", "Use case gốc vẫn hoàn toàn trọn vẹn và hoạt động bình thường nếu không có mở rộng."),
        ("Hướng của mũi tên UML", "Hướng TỪ Use case chính ĐẾN Use case phụ thuộc (Chính --> Phụ).", "Hướng TỪ Use case mở rộng VỀ Use case chính ban đầu (Mở rộng --> Chính)."),
        ("Điểm mở rộng (Extension Point)", "Không cần định nghĩa Extension Point.", "Bắt buộc phải gắn với một điều kiện hoặc sự kiện kích hoạt xác định."),
        ("Ví dụ tiêu biểu trong dự án", "Xem Bảng xếp hạng buộc phải Tính điểm tương thích hai chiều (UC-06 -> UC-07).", "Xem Bảng xếp hạng được mở rộng bởi Xem chi tiết tiêu chí (UC-08 -> UC-06).")
    ]

    for i, (crit, inc_val, ext_val) in enumerate(cmp_data):
        row = tbl_cmp.rows[i + 1]
        bg = "F9FAFB" if i % 2 == 1 else "FFFFFF"
        for j, text_val in enumerate([crit, inc_val, ext_val]):
            cell = row.cells[j]
            cell.width = c_widths[j]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_border(cell, top={'val': 'single', 'sz': 4, 'color': 'E5E7EB'}, bottom={'val': 'single', 'sz': 4, 'color': 'E5E7EB'})
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(text_val)
            run.font.name, run.font.size = 'Times New Roman', Pt(9.5)
            if j == 0:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
            elif j == 1:
                run.font.color.rgb = RGBColor(0x15, 0x80, 0x3D)
            else:
                run.font.color.rgb = RGBColor(0x7E, 0x22, 0xCE)

    add_styled_paragraph(doc, space_after=14)

    # ==================== MỤC 5: GIẢI THÍCH VÌ SAO KHÔNG CÓ EXCLUDE ====================
    add_heading_1(doc, "5. LUẬN GIẢI CHUYÊN SÂU: VÌ SAO HOÀN TOÀN KHÔNG CÓ <<EXCLUDE>> TRONG UML")
    add_body(doc, "Đây là câu hỏi 'bẫy' kinh điển của các Giảng viên hội đồng bảo vệ phần mềm khi chất vấn sinh viên: 'Nếu hệ thống có tính năng loại trừ người hút thuốc hoặc cấm ghép hai người mâu thuẫn, tại sao trên sơ đồ không vẽ quan hệ <<exclude>>?'.")
    add_body(doc, "Câu trả lời khẳng định vững chắc về mặt học thuật:")
    add_bullet(doc, "Theo tiêu chuẩn đặc tả UML quốc tế do Tổ chức Quản lý Đối tượng (OMG - Object Management Group) ban hành, mô hình Use Case Diagram CHỈ CÔNG NHẬN 02 quan hệ phụ thuộc tiêu chuẩn giữa các Use Case là <<include>> và <<extend>>. Quan hệ có tên '<<exclude>>' HOÀN TOÀN KHÔNG TỒN TẠI trong cú pháp và ngữ nghĩa của UML.", "1. Chuẩn hóa quốc tế OMG: ")
    add_bullet(doc, "Biểu đồ Use Case được thiết kế để mô tả chức năng người dùng có thể THỰC HIỆN ĐƯỢC (What the system does), chứ không phải để mô hình hóa những gì hệ thống TỪ CHỐI hoặc NGĂN CẢM. Một hành động 'bị loại trừ' bản chất không phải là một ca sử dụng độc lập.", "2. Triết lý thiết kế hướng đối tượng: ")
    add_body(doc, "Để thể hiện các nghiệp vụ loại trừ trong đề tài Ký túc xá, nhóm sinh viên áp dụng các giải pháp kỹ thuật chuẩn mực của Công nghệ phần mềm thay vì tự ý bịa đặt quan hệ sai chuẩn:")
    add_bullet(doc, "Được thiết lập thông qua toán tử điều kiện trong giải thuật. Ví dụ: Sinh viên Lê Minh Quân (DUE) có thuộc tính smoke = 0 và chọn tiêu chí top = smoke. Khi giải thuật tính toán ma trận độ tương thích, bất kỳ ứng viên nào có smoke = 1 sẽ bị phạt điểm tương đương giá trị 0% hoặc bị bộ lọc tiền xử lý loại bỏ khỏi danh sách ghép cặp khả dĩ. Đây là ràng buộc logic (Constraint), không phải một Use Case.", "Giải pháp 1 - Áp dụng Constraint (Ràng buộc nghiệp vụ): ")
    add_bullet(doc, "Được mô tả rõ trong hồ sơ đặc tả Use Case. Ví dụ: Để thực hiện 'Xem bảng xếp hạng', tiền điều kiện bắt buộc là sinh viên phải đã đăng nhập thành công. Người dùng chưa đăng nhập sẽ bị ngăn chặn truy cập.", "Giải pháp 2 - Áp dụng Precondition (Tiền điều kiện): ")
    add_bullet(doc, "Quy định bài trừ hai sinh viên cùng thuộc nhóm A hoặc cùng thuộc nhóm B không được phép ghép cặp với nhau trong mô hình hôn nhân bền vững hai phía. Quy tắc này được gắn vào ghi chú kiến trúc (Architecture Note) đính kèm biểu đồ.", "Giải pháp 3 - Áp dụng Business Rule (Quy tắc nghiệp vụ): ")

    # ==================== MỤC 6: BỘ CÂU HỎI VẤN ĐÁP VÀ KỊCH BẢN BẢO VỆ ====================
    add_heading_1(doc, "6. BỘ CÂU HỎI VẤN ĐÁP (Q&A) VÀ KỊCH BẢN BẢO VỆ TRƯỚC HỘI ĐỒNG")
    add_body(doc, "Dưới đây là 8 câu hỏi phản biện thực tế mà Giảng viên thường đặt ra cho đồ án, kèm theo câu trả lời mẫu ngắn gọn, tự tin và chuẩn xác về mặt chuyên môn:")

    qa_list = [
        ("Câu 1: Tại sao nhóm em lại phân tách thành 02 tác nhân Sinh viên và Ban quản lý KTX?",
         "Dạ thưa Thầy/Cô, việc phân tách 2 tác nhân xuất phát từ sự phân quyền nghiệp vụ và mục tiêu sử dụng hoàn toàn khác nhau: Sinh viên là người dùng cuối, chỉ có quyền thao tác trên dữ liệu cá nhân của mình, khai báo thói quen và xem kết quả bạn cùng phòng phù hợp. Trong khi đó, Ban quản lý KTX là quản trị viên hệ thống, có thẩm quyền can thiệp vào cơ sở dữ liệu lớn của toàn trường, nạp file CSV, khởi chạy thuật toán tối ưu tổng thể và xem báo cáo đối sánh thực nghiệm. Việc phân định rõ giúp đảm bảo tính an toàn thông tin và kiến trúc phân quyền chuẩn MVC."),

        ("Câu 2: Tại sao Đăng ký (UC-01) và Đăng nhập (UC-02) lại cùng <<include>> Xác thực thông tin (UC-03)?",
         "Dạ thưa Thầy/Cô, cả hai quy trình này đều chia sẻ chung một bước logic bắt buộc là kiểm tra tính hợp lệ của thông tin sinh viên (kiểm tra định dạng Mã SV, kiểm tra mật khẩu, xác minh xem sinh viên có thuộc các trường thành viên như VNUK, SPKT, DUE hay không). Theo nguyên lý tái sử dụng (Reuse) trong UML, việc tách bước này thành Use Case được include (UC-03) giúp tránh trùng lặp mã nguồn và chuẩn hóa cơ chế kiểm tra bảo mật tại một điểm duy nhất."),

        ("Câu 3: Tại sao Nạp hồ sơ mẫu Persona (UC-05) lại là <<extend>> của Khai báo thói quen (UC-04) mà không phải <<include>>?",
         "Dạ thưa Thầy/Cô, vì bản chất hành vi này là không bắt buộc. Trong thực tế, một sinh viên khi vào KTX hoàn toàn có thể tự tay nhập giờ ngủ, giờ thức dậy và các sở thích riêng của họ mà không cần dùng đến mẫu có sẵn. Use Case 'Khai báo thói quen' vẫn chạy bình thường độc lập. Tính năng nạp nhanh Persona mẫu (Thái Bảo, Văn Việt, Minh Quân) chỉ là một tiện ích mở rộng bổ trợ để sinh viên thử nghiệm nhanh giao diện khi thỏa mãn điều kiện họ bấm vào nút Persona."),

        ("Câu 4: Mũi tên của quan hệ <<extend>> giữa UC-05 và UC-04 chỉ theo hướng nào và tại sao?",
         "Dạ thưa Thầy/Cô, theo đúng chuẩn UML của OMG, mũi tên <<extend>> bắt buộc phải chỉ từ Use Case mở rộng (UC-05) ngược về Use case gốc (UC-04). Lý do là vì Use case gốc hoàn toàn không cần biết về sự tồn tại của Use case mở rộng (đảm bảo tính đóng gói và độc lập). Ngược lại, Use case mở rộng phải tham chiếu và chèn hành vi của mình vào điểm mở rộng (extension point) của Use case gốc, do đó mũi tên phụ thuộc chỉ về Use case gốc."),

        ("Câu 5: Tính năng Xem chi tiết giải thích tiêu chí (UC-08) có vai trò gì và vì sao là <<extend>>?",
         "Dạ thưa Thầy/Cô, Use Case này giải quyết Yêu cầu Nghiệp vụ BR-04 về tính minh bạch thuật toán. Sinh viên sau khi xem bảng xếp hạng Top 1 đến Top 8 có thể muốn biết tại sao mình lại hợp hoặc chưa hợp bạn đó. Tuy nhiên, hành động xem giải thích chi tiết này không bắt buộc cho quy trình xem danh sách tổng quan. Chỉ khi sinh viên nhấp vào 'Chi tiết tiêu chí ▼', khối phân tích điểm cộng (>=0.75) và điểm lưu ý (<=0.40) mới được hiển thị. Do đó, đây là quan hệ <<extend>> chuẩn mực."),

        ("Câu 6: Tại sao Thuật toán Gale-Shapley (UC-13) và Đếm cặp chặn (UC-14) lại là <<include>> của Ghép phòng tự động (UC-12)?",
         "Dạ thưa Thầy/Cô, để hoàn tất quy trình phân phòng cho KTX, Ban quản lý không thể ghép thủ công mà bắt buộc hệ thống phải thực thi giải thuật Gale-Shapley hai chiều. Hơn thế nữa, mục tiêu cốt lõi của đề tài là đảm bảo không sinh viên nào muốn tự ý bỏ phòng để sang phòng khác (tính ổn định cao). Do đó, bước quét ma trận kiểm tra số cặp chặn (Blocking Pairs) là bắt buộc thực hiện kèm theo ngay sau khi ghép để chứng minh tính đúng đắn của giải thuật trước khi công bố kết quả."),

        ("Câu 7: Nếu có trường hợp sinh viên ghét nhau hoặc sinh viên hút thuốc không được ở chung người dị ứng, sao nhóm không vẽ quan hệ <<exclude>>?",
         "Dạ thưa Thầy/Cô, chuẩn UML quốc tế không hề có quan hệ nào tên là <<exclude>>. Biểu đồ Use Case chỉ mô hình hóa chức năng người dùng có thể thực hiện. Các điều kiện cấm đoán hoặc loại trừ lẫn nhau được nhóm em mô hình hóa dưới dạng Ràng buộc nghiệp vụ (Constraint) và cài đặt thông qua trọng số trong ma trận điểm và bộ lọc logic của giải thuật, hoàn toàn tuân thủ chặt chẽ chuẩn mực kỹ thuật phần mềm."),

        ("Câu 8: Nhóm em đã kiểm chứng biểu đồ này trên phần mềm chạy thực tế chưa?",
         "Dạ thưa Thầy/Cô, toàn bộ 16 Use Case trên biểu đồ đã được nhóm em hiện thực hóa hoàn chỉnh bằng ứng dụng Web chạy trên nền FastAPI và HTML5/Tailwind CSS. Hệ thống đã có trang đăng nhập xác thực tài khoản sinh viên, form nhập 8 tiêu chí có nạp nhanh 3 Persona mẫu, bảng hiển thị Top 8 bạn cùng phòng tương thích và chức năng xem chi tiết tiêu chí hai chiều. Thầy/Cô có thể trực tiếp trải nghiệm và kiểm chứng toàn bộ luồng hoạt động trên hệ thống cục bộ của nhóm.")
    ]

    for q_title, q_ans in qa_list:
        p_q = add_styled_paragraph(doc, space_before=8, space_after=2)
        r_q = p_q.add_run(q_title)
        r_q.font.name, r_q.font.size, r_q.font.bold = 'Times New Roman', Pt(12), True
        r_q.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

        p_a = add_styled_paragraph(doc, space_before=0, space_after=6, line_spacing=1.2)
        r_a = p_a.add_run(q_ans)
        r_a.font.name, r_a.font.size = 'Times New Roman', Pt(11.5)
        r_a.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # ==================== MỤC 7: KẾT LUẬN ====================
    add_heading_1(doc, "7. KẾT LUẬN VÀ KIẾN NGHỊ")
    add_body(doc, "Biểu đồ Use Case được xây dựng cho hệ thống Ghép bạn cùng phòng KTX không chỉ đáp ứng nghiêm ngặt các quy chuẩn kỹ thuật của ngôn ngữ mô hình hóa UML, mà còn phản ánh chân thực các đòi hỏi nghiệp vụ đời thường trong môi trường nội trú đại học. Việc phân định chính xác giữa quan hệ <<include>> (tính bắt buộc, tái sử dụng) và <<extend>> (tính tùy chọn có điều kiện), đồng thời loại bỏ quan niệm sai lầm về <<exclude>>, là minh chứng cho sự chuẩn bị nghiêm túc, sâu sắc về mặt học thuật của nhóm sinh viên.")
    add_body(doc, "Tài liệu này là căn cứ vững chắc để nhóm tự tin bảo vệ đề tài trước Giảng viên và Hội đồng đánh giá, đồng thời làm kim chỉ nam để tiếp tục hoàn thiện các pha triển khai mã nguồn và kiểm thử hệ thống trong các giai đoạn tiếp theo.")

    # Lưu tài liệu vào Downloads và Backup vào scratch docs
    out_dl = r"C:\Users\LENOVO\Downloads\Tai_Lieu_Giai_Thich_So_Do_Use_Case_KTX.docx"
    out_docs = r"C:\Users\LENOVO\.gemini\antigravity\scratch\system-\docs\Tai_Lieu_Giai_Thich_So_Do_Use_Case_KTX.docx"

    doc.save(out_dl)
    doc.save(out_docs)
    print(f"Successfully generated docx at:\n1. {out_dl}\n2. {out_docs}")

if __name__ == "__main__":
    build_document()
