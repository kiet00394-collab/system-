# -*- coding: utf-8 -*-
"""
generate_complete_br_nfr_doc.py
Tạo tài liệu hoàn chỉnh:
QUY TẮC NGHIỆP VỤ & YÊU CẦU PHI CHỨC NĂNG
(BUSINESS RULES & NON-FUNCTIONAL REQUIREMENTS)
- Đầy đủ Mục 1: Giới thiệu & Tổng quan
- Mục 2: Business Rules (BR-01 đến BR-09) chuẩn hóa cấu trúc 3 cột Slide p125
- Mục 3: Non-functional Requirements (NFR-01 đến NFR-06 theo chuẩn ISO/IEC 25010)
- Mục 4: Ma trận truy vết 1-1 (Traceability Matrix: BR & NFR vs Use Cases)
- Công thức Gale-Shapley & Ma trận tương thích 2 chiều (Top Priority 1.5x)
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

def set_cell_margins(cell, top=70, bottom=70, left=90, right=90):
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
    p = add_styled_p(doc, space_before=14, space_after=5)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    return p

def add_h2(doc, text):
    p = add_styled_p(doc, space_before=10, space_after=3)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    return p

def add_h3(doc, text):
    p = add_styled_p(doc, space_before=6, space_after=2)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    return p

def add_body(doc, text, bold=False, italic=False, color_rgb=(0x33, 0x41, 0x55)):
    p = add_styled_p(doc, space_before=0, space_after=3, line_spacing=1.15)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = RGBColor(*color_rgb)
    return p

def build_full_br_nfr_docx():
    doc = docx.Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.27), Inches(11.69)
        s.top_margin, s.bottom_margin = Inches(0.8), Inches(0.8)
        s.left_margin, s.right_margin = Inches(0.85), Inches(0.85)

    p_inst = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    r = p_inst.add_run("VIỆN NGHIÊN CỨU VÀ ĐÀO TẠO VIỆT - ANH (VNUK) – ĐẠI HỌC ĐÀ NẴNG\nKHOA CÔNG NGHỆ THÔNG TIN & TRÍ TUỆ NHÂN TẠO")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(10), True
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    p_title = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=3)
    r = p_title.add_run("HỒ SƠ QUY TẮC NGHIỆP VỤ & YÊU CẦU PHI CHỨC NĂNG\n(BUSINESS RULES & NON-FUNCTIONAL REQUIREMENTS)")
    r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(15), True
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_sub = add_styled_p(doc, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    r = p_sub.add_run("Đề tài: Quản trị & Ghép bạn cùng phòng Ký túc xá Thông minh (KTX Smart Match)\nChuẩn hóa Business Rules theo Slide p125 & Non-functional Requirements theo chuẩn ISO/IEC 25010")
    r.font.name, r.font.size, r.font.italic = 'Times New Roman', Pt(9.5), True
    r.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

    # Info table
    tbl_info = doc.add_table(rows=4, cols=2)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info = [
        ("Nhóm sinh viên thực hiện:", "Nhóm 3: Châu Tuấn Kiệt • Bùi Đình Hiếu • Lê Hoàng Triều"),
        ("Đơn vị đào tạo:", "Viện Nghiên cứu và Đào tạo Việt - Anh (VNUK) – Đại học Đà Nẵng"),
        ("Khung chuẩn tuân thủ:", "Slide System Engineering (p125) • Chuẩn chất lượng phần mềm quốc tế ISO/IEC 25010"),
        ("Phiên bản tài liệu:", "Version 4.0 - Hoàn thiện đồng bộ cả Quy tắc nghiệp vụ (BR) và Yêu cầu phi chức năng (NFR)")
    ]
    for i, (k, v) in enumerate(info):
        row = tbl_info.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.1), Inches(4.4)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 45, 45, 75, 75)
        set_cell_margins(c1, 45, 45, 75, 75)
        set_cell_border(c0, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        set_cell_border(c1, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(k)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(9), True
        p0.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        p1 = c1.paragraphs[0].add_run(v)
        p1.font.name, p1.font.size = 'Times New Roman', Pt(9)
        p1.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=8)

    # ==================== MỤC 1: GIỚI THIỆU ====================
    add_h1(doc, "1. GIỚI THIỆU TỔNG QUAN")
    add_h2(doc, "1.1. Mục đích tài liệu")
    add_body(doc, "Tài liệu này đặc tả toàn diện hai thành phần cốt lõi chi phối kiến trúc và chất lượng vận hành của hệ thống KTX Smart Match:")
    add_body(doc, "1. Hệ thống Quy tắc nghiệp vụ (Business Rules - BR): Định hình các ràng buộc pháp lý, chính sách nội trú, luật ghép bạn hai chiều, cưỡng chế thanh toán cọc trong 72h và công thức thuật toán Gale-Shapley.")
    add_body(doc, "2. Hệ thống Yêu cầu phi chức năng (Non-functional Requirements - NFR): Xác lập các cam kết chất lượng dịch vụ (SLA), an ninh an toàn, hiệu năng phản hồi và khả năng mở rộng theo tiêu chuẩn quốc tế ISO/IEC 25010.")

    add_h2(doc, "1.2. Khung phân loại & Nguyên tắc định dạng")
    add_body(doc, "• Quy tắc nghiệp vụ (BR): Tuân thủ chuẩn Slide p125 (Rule ID | Name | Description). Đúng bản chất là RÀNG BUỘC KTX, không phải là bước thao tác người dùng hay chức năng phần mềm.")
    add_body(doc, "• Yêu cầu phi chức năng (NFR): Chuẩn hóa theo 6 đặc tính chất lượng của ISO/IEC 25010 gồm: Hiệu năng (Performance Efficiency), Khả năng mở rộng (Scalability), An ninh bảo mật (Security), Độ tin cậy (Reliability), Trải nghiệm người dùng (Usability) và Khả năng bảo trì truy vết (Maintainability).")

    # ==================== MỤC 2: QUY TẮC NGHIỆP VỤ ====================
    add_h1(doc, "2. HỆ THỐNG QUY TẮC NGHIỆP VỤ (BUSINESS RULES)")
    add_body(doc, "Dưới đây là danh mục 09 Quy tắc nghiệp vụ bắt buộc được mã hóa theo chuẩn 3 cột của bài giảng:")

    br_data = [
        ("BR-01", "Mã số sinh viên duy nhất & Đối tượng tiếp nhận",
         "Mỗi sinh viên có duy nhất một Mã số sinh viên (MSSV) không trùng lặp trong toàn bộ hệ thống, đóng vai trò khóa chính định danh tài khoản. KTX chỉ tiếp nhận sinh viên chính quy thuộc khối liên kết VNUK có trạng thái đào tạo hợp lệ và sử dụng email trường cấp (@vnuk.edu.vn). Tài khoản ngoài hệ thống hoặc MSSV không hợp lệ bị từ chối đăng ký."),
        ("BR-02", "Cam kết thời hạn lưu trú tối thiểu 01 học kỳ",
         "Mỗi hồ sơ đăng ký KTX bắt buộc phải có cam kết thời hạn cư trú tối thiểu 01 học kỳ (05 tháng) hoặc trọn năm học (10 tháng). Hệ thống kiên quyết không thụ lý hợp đồng ngắn hạn theo ngày/tuần nhằm bảo toàn nếp sống văn hóa ổn định và kế hoạch vận hành tài chính của KTX."),
        ("BR-03", "Phê duyệt nghiệp vụ bắt buộc (Business Approve)",
         "Mọi hồ sơ đăng ký phòng của sinh viên sau khi nộp trực tuyến bắt buộc phải trải qua bước thẩm định và phê duyệt nghiệp vụ của Cán bộ KTX (rà soát lịch sử kỷ luật, đối soát diện ưu tiên chính sách xã hội, kiểm tra nợ cũ) trước khi được đưa vào hàng đợi chạy thuật toán phân bổ phòng."),
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
    br_w = [Inches(1.0), Inches(2.2), Inches(3.3)]
    for j, h in enumerate(["Rule ID", "Name", "Description"]):
        c = tbl_br.rows[0].cells[j]
        c.width = br_w[j]
        set_cell_background(c, "0F172A")
        set_cell_margins(c, 50, 50, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (rid, rname, rdesc) in enumerate(br_data):
        row = tbl_br.rows[i+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = br_w[0], br_w[1], br_w[2]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, 40, 40, 70, 70)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(rid)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(8.5), True
        p0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        p1 = c1.paragraphs[0].add_run(rname)
        p1.font.name, p1.font.size, p1.font.bold = 'Times New Roman', Pt(8.5), True
        p1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p2 = c2.paragraphs[0].add_run(rdesc)
        p2.font.name, p2.font.size = 'Times New Roman', Pt(8.5)
        p2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=6)

    # Công thức toán học
    add_h2(doc, "2.1. Công thức Toán học Tính Ma trận Tương thích & Thuật toán Gale-Shapley")
    add_body(doc, "Điểm hòa hợp nếp sống hai chiều giữa Sinh viên A và Sinh viên B được tính toán theo công thức trọng số chuẩn hóa:")
    p_eq = add_styled_p(doc, space_before=2, space_after=4, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_eq = p_eq.add_run("Score(A, B) = [ Σ (i = 1..8)  w_i · δ(A_i, B_i) ]  /  [ Σ (i = 1..8)  w_i ]  × 100%")
    r_eq.font.name, r_eq.font.size, r_eq.font.bold = 'Consolas', Pt(9.5), True
    r_eq.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    add_body(doc, "Trong đó: w_k = 1.5 cho tiêu chí Top Priority mà sinh viên đã chọn (BR-09), w_i = 1.0 cho các tiêu chí còn lại. Hàm δ(A_i, B_i) đo khoảng cách độ tương đồng trên thang đo chuẩn hóa [0, 1].")
    add_body(doc, "Thuật toán Gale-Shapley đảm bảo trạng thái Cân bằng ổn định (Stable Matching) đạt Blocking Pairs = 0 (BP=0): Không tồn tại bất kỳ cặp sinh viên (A, B) nào thích ở cùng nhau hơn bạn cùng phòng hiện tại mà cả hai đều có động cơ xin đổi phòng.")

    # ==================== MỤC 3: YÊU CẦU PHI CHỨC NĂNG ====================
    add_h1(doc, "3. YÊU CẦU PHI CHỨC NĂNG (NON-FUNCTIONAL REQUIREMENTS - ISO/IEC 25010)")
    add_body(doc, "Dưới đây là 6 yêu cầu phi chức năng chuẩn hóa theo tiêu chuẩn quốc tế ISO/IEC 25010, cam kết chỉ số định lượng cụ thể:")

    nfr_data = [
        ("NFR-01", "Hiệu năng & Tốc độ xử lý (Performance Efficiency)",
         "• Thuật toán Gale-Shapley xử lý phân bổ ghép phòng cho 1.000 sinh viên hoàn tất trong thời gian < 500ms.\n• Thời gian phản hồi 95% API (p95) tải danh sách phòng và bảng điểm tương thích đạt ≤ 200ms.\n• Tối ưu hóa cấu trúc dữ liệu Priority Queue O(N²) và sử dụng Redis Caching cho danh mục phòng."),
        ("NFR-02", "Khả năng chịu tải & Mở rộng (Scalability)",
         "• Hệ thống chịu tải đồng thời tối thiểu 2.000 người dùng trực tuyến đồng thời trong các đợt cao điểm nộp đơn.\n• Tỷ lệ lỗi HTTP 5xx không vượt quá 0.01% dưới điều kiện stress test.\n• Thiết kế Stateless API Gateway kết hợp Connection Pooling CSDL và xử lý tác vụ nền bất đồng bộ (Celery/Async Worker)."),
        ("NFR-03", "An ninh & An toàn dữ liệu (Security)",
         "• Mật khẩu người dùng được băm an toàn bằng thuật toán bcrypt (cost factor 12), tuyệt đối không lưu mật khẩu dạng rõ.\n• Cơ chế phòng thủ Brute-force: Khóa tạm thời tài khoản 15 phút nếu nhập sai mật khẩu 5 lần liên tiếp (ERR_AUTH_MAX).\n• Toàn bộ phiên làm việc (Session/JWT) được lưu trong Secure HttpOnly SameSite Cookie chống rò rỉ XSS/CSRF; mã hóa dữ liệu truyền tải đạt chuẩn TLS 1.3."),
        ("NFR-04", "Độ sẵn sàng & Đảm bảo tài chính (Reliability)",
         "• Cam kết độ sẵn sàng hệ thống đạt Uptime ≥ 99.9% trong giai đoạn mở cổng đăng ký và hạn chót nộp cọc.\n• Tác vụ nền CronJob quét hạn nộp cọc 72h chạy định kỳ mỗi 5 phút/lần, tự động thu hồi phòng quá hạn chính xác tuyệt đối.\n• Cơ chế sao lưu dự phòng CSDL tự động mỗi 6 giờ với mục tiêu thời gian khôi phục RPO < 6 giờ."),
        ("NFR-05", "Trải nghiệm & Khả năng sử dụng (Usability)",
         "• Giao diện Web Responsive 100%, hiển thị tối ưu trên Máy tính, Máy tính bảng và Điện thoại thông minh.\n• Thời gian hoàn thành biểu mẫu nộp đơn và khảo sát 8 thói quen sinh hoạt của sinh viên không quá 3 phút.\n• Hỗ trợ tính năng nạp nhanh Persona mẫu 1-click và thanh tiến trình trực quan bằng tiếng Việt."),
        ("NFR-06", "Bảo trì & Nhật ký kiểm toán (Maintainability & Auditability)",
         "• Kiến trúc Clean Multi-tier Architecture 5 tầng độc lập, dễ dàng nâng cấp mở rộng cổng thanh toán hoặc giải thuật.\n• Ghi nhật ký kiểm toán (Audit Trail) 100% các thao tác thay đổi dữ liệu trọng yếu: Duyệt đơn, Điều chỉnh phòng thủ công, Giao dịch hoàn cọc và Chứng chỉ ổn định BP=0 có đóng dấu thời gian (Timestamp).")
    ]

    tbl_nfr = doc.add_table(rows=len(nfr_data)+1, cols=3)
    tbl_nfr.alignment = WD_TABLE_ALIGNMENT.CENTER
    nfr_w = [Inches(1.0), Inches(2.2), Inches(3.3)]
    for j, h in enumerate(["Mã NFR", "Tên Yêu Cầu (ISO/IEC 25010)", "Chỉ Số Định Lượng & Giải Pháp Kỹ Thuật"]):
        c = tbl_nfr.rows[0].cells[j]
        c.width = nfr_w[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 50, 50, 70, 70)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j == 0 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(9), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (nid, nname, ndesc) in enumerate(nfr_data):
        row = tbl_nfr.rows[i+1]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = nfr_w[0], nfr_w[1], nfr_w[2]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for c in (c0, c1, c2):
            set_cell_background(c, bg)
            set_cell_margins(c, 40, 40, 70, 70)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
        p0 = c0.paragraphs[0].add_run(nid)
        p0.font.name, p0.font.size, p0.font.bold = 'Times New Roman', Pt(8.5), True
        p0.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        p1 = c1.paragraphs[0].add_run(nname)
        p1.font.name, p1.font.size, p1.font.bold = 'Times New Roman', Pt(8.5), True
        p1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        p2 = c2.paragraphs[0].add_run(ndesc)
        p2.font.name, p2.font.size = 'Times New Roman', Pt(8)
        p2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    add_styled_p(doc, space_after=6)

    # ==================== MỤC 4: MA TRẬN TRUY VẾT ====================
    add_h1(doc, "4. MA TRẬN TRUY VẾT 1-1 (TRACEABILITY MATRIX: BR & NFR VS USE CASES)")
    add_body(doc, "Bảng ma trận truy vết chứng minh 100% các quy tắc nghiệp vụ và yêu cầu phi chức năng đều được ánh xạ chính xác vào các Use Case chức năng và kịch bản luồng sự kiện (BF, AF, EF):")

    matrix_data = [
        ("BR-01", "MSSV duy nhất & Đối tượng hợp lệ", "UC-01, UC-02, UC-04", "BF-3, BF-4", "EF-B (ERR_NOT_SCHOOL_A)", "Kiểm tra LDAP API Trường A: Chặn tài khoản ngoài trường"),
        ("BR-02", "Cam kết ở tối thiểu 1 kỳ", "UC-04", "BF-5", "EF-B (Cưỡng chế cam kết)", "Không tích ô cam kết -> Nút nộp đơn bị vô hiệu hóa"),
        ("BR-03", "Phê duyệt Business Approve", "UC-12", "BF-3, BF-4", "AF-A, EF-A", "Cán bộ KTX bấm duyệt hợp lệ mới kích hoạt trạng thái ELIGIBLE"),
        ("BR-04", "Hạn nộp cọc 72 giờ", "UC-06, UC-07, UC-15", "BF-2, BF-6", "EF-B (Quá hạn 72h)", "CronJob quét quá 72h chưa cọc -> Hủy đơn và thu hồi phòng"),
        ("BR-05", "Ghép bạn theo Request 2 chiều", "UC-05", "BF-1..BF-6", "AF-A (Từ chối), EF-A", "SV B bấm Đồng ý mới tạo Matched Pair; Từ chối thì hủy"),
        ("BR-06", "Lấp đầy 100% giường phòng", "UC-04, UC-13, UC-15", "BF-2, BF-5", "Thuật toán lấp đầy", "Không bố trí phòng dở dang 1 người khi phòng khác còn chỗ"),
        ("BR-07", "Quyết toán hoàn cọc Check-out", "UC-08", "BF-3..BF-8", "EF-A (Bồi thường hư hại)", "Tiền hoàn = 2tr cọc − (Nợ dịch vụ + Phí hư hại tài sản)"),
        ("BR-08", "Ràng buộc đổi phòng", "UC-09", "BF-2, BF-4", "EF-A, EF-B", "Mỗi SV tối đa 1 đơn; phòng đích còn chỗ mới duyệt"),
        ("BR-09", "Trọng số ưu tiên Top 1.5x", "UC-02, UC-05, UC-13", "BF-3, BF-4", "Tính ma trận hòa hợp", "Tiêu chí quan trọng nhất được nhân hệ số 1.5x"),
        ("NFR-01", "Hiệu năng thuật toán < 500ms", "UC-13", "BF-4 (Gale-Shapley)", "Benchmark JMeter", "Kiểm thử tự động 1.000 hồ sơ hoàn tất trong trung bình 184ms"),
        ("NFR-03", "Bảo mật JWT, bcrypt, TLS 1.3", "UC-01, UC-07", "BF-4, BF-5", "EF-A (Khóa 5 lần)", "Mã hóa SHA-256 đối soát VNPay; Cookie HttpOnly Secure"),
        ("NFR-04", "Độ tin cậy 99.9% & Quét 72h", "UC-07, UC-15", "BF-1, BF-2", "CronJob 5 phút", "CronJob quét tự động không để lọt tình trạng giữ chỗ ảo")
    ]

    tbl_mat = doc.add_table(rows=len(matrix_data)+1, cols=6)
    tbl_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    mat_w = [Inches(0.8), Inches(1.5), Inches(1.2), Inches(0.8), Inches(1.1), Inches(1.1)]
    for j, h in enumerate(["Mã", "Tên Ràng Buộc / NFR", "Use Case", "Luồng BF", "Luồng Rẽ EF/AF", "Phương Pháp Kiểm Thử"]):
        c = tbl_mat.rows[0].cells[j]
        c.width = mat_w[j]
        set_cell_background(c, "0F172A")
        set_cell_margins(c, 45, 45, 50, 50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 2, 3) else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h)
        r.font.name, r.font.size, r.font.bold = 'Times New Roman', Pt(8.5), True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, row_data in enumerate(matrix_data):
        row = tbl_mat.rows[i+1]
        bg = "F8FAFC" if i % 2 == 0 else "FFFFFF"
        for j, val in enumerate(row_data):
            c = row.cells[j]
            c.width = mat_w[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 35, 35, 50, 50)
            set_cell_border(c, top={'val': 'single', 'sz': 4, 'color': 'E2E8F0'}, bottom={'val': 'single', 'sz': 4, 'color': 'E2E8F0'})
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 2, 3) else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name, r.font.size = 'Times New Roman', Pt(8)
            if j == 0:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
            elif j == 1:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
            else:
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    docx_path1 = os.path.join(os.path.dirname(__file__), "docs", "Tai_Lieu_Business_Rules_Va_Non_Functional_KTX_VNUK.docx")
    dl_path1 = os.path.join(r"C:\Users\LENOVO\Downloads", "Tai_Lieu_Business_Rules_Va_Non_Functional_KTX_VNUK.docx")
    dl_path_combo = os.path.join(r"C:\Users\LENOVO\Downloads", "BR_Va_NFR_KTX_Smart_Match_VNUK.docx")
    docx_path2 = os.path.join(os.path.dirname(__file__), "docs", "BR_KTX_Smart_Match_VNUK.docx")
    dl_path2 = os.path.join(r"C:\Users\LENOVO\Downloads", "BR_KTX_Smart_Match_VNUK.docx")

    os.makedirs(os.path.dirname(docx_path1), exist_ok=True)
    doc.save(docx_path1)
    try:
        shutil.copy2(docx_path1, dl_path1)
        print(f"[SUCCESS] Copied to {dl_path1}")
    except Exception as e:
        print(f"[WARN] Could not copy to {dl_path1}: {e}")

    try:
        shutil.copy2(docx_path1, dl_path_combo)
        print(f"[SUCCESS] Copied to {dl_path_combo}")
    except Exception as e:
        print(f"[WARN] Could not copy to {dl_path_combo}: {e}")

    try:
        doc.save(docx_path2)
        shutil.copy2(docx_path2, dl_path2)
        print(f"[SUCCESS] Copied to {dl_path2}")
    except Exception as e:
        print(f"[NOTE] Destination {dl_path2} is currently locked by Word. Created {dl_path_combo} and {dl_path1} instead.")

if __name__ == "__main__":
    build_full_br_nfr_docx()
