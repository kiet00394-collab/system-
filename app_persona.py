import os
import json
import base64
import urllib.parse
from typing import List, Dict, Set, Optional
from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="KTX Roommate Compatibility Ranking Dashboard")

# 8 Tiêu chí sinh hoạt và Trọng số
WEIGHTS = {
    "sleep": 0.25,
    "wake": 0.10,
    "tidy": 0.20,
    "study": 0.10,
    "noise": 0.15,
    "smoke": 0.10,
    "guests": 0.05,
    "hobbies": 0.05
}

CRITERIA_LABELS = {
    "sleep": "Giờ đi ngủ",
    "wake": "Giờ thức dậy",
    "tidy": "Độ gọn gàng",
    "study": "Thói quen học",
    "noise": "Chịu tiếng ồn",
    "smoke": "Hút thuốc",
    "guests": "Dắt bạn về phòng",
    "hobbies": "Sở thích chung"
}

# 3 Persona sinh viên chính thức
PERSONAS = {
    "thaibao": {
        "id": "thaibao",
        "student_id": "22VNUK0101",
        "name": "Nguyễn Duy Thái Bảo",
        "school": "Viện NC & ĐT Việt - Anh (VNUK) - ĐH Đà Nẵng",
        "major": "Khoa học Máy tính (CNTT Quốc tế)",
        "group": "A",
        "sleep": 22.0, "wake": 6.0, "tidy": 5, "study": "thuvien",
        "noise": 1, "smoke": 0, "guests": 1,
        "hobbies": ["doc sach", "the thao", "nhac"],
        "top": "sleep",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=ThaiBaoVNUK&backgroundColor=b6e3f4"
    },
    "vanviet": {
        "id": "vanviet",
        "student_id": "21SPKT0205",
        "name": "Lê Văn Việt",
        "school": "ĐH Sư phạm Kỹ thuật (SPKT) - ĐH Đà Nẵng",
        "major": "Kỹ thuật Cơ điện tử",
        "group": "B",
        "sleep": 26.0, "wake": 9.5, "tidy": 2, "study": "phong",
        "noise": 4, "smoke": 0, "guests": 4,
        "hobbies": ["game", "phim", "nhac"],
        "top": "noise",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=VanVietSPKT&backgroundColor=ffdfbf"
    },
    "minhquan": {
        "id": "minhquan",
        "student_id": "22DUE0342",
        "name": "Lê Minh Quân",
        "school": "Trường ĐH Kinh tế (DUE) - ĐH Đà Nẵng",
        "major": "Quản trị Kinh doanh",
        "group": "B",
        "sleep": 23.5, "wake": 6.5, "tidy": 4, "study": "it",
        "noise": 3, "smoke": 0, "guests": 2,
        "hobbies": ["the thao", "nau an", "nhac"],
        "top": "smoke",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=MinhQuanDUE&backgroundColor=c0aede"
    }
}

# Danh sách ứng viên trong hệ thống (gồm 3 persona và danh sách sinh viên KTX)
CANDIDATES = [
    {
        "id": 101,
        "name": "Nguyễn Duy Thái Bảo",
        "tagline": "Sinh viên VNUK - Học bá kỷ luật, thích yên tĩnh và ngủ trước 23h",
        "group": "A",
        "sleep": 22.0, "wake": 6.0, "tidy": 5, "study": "thuvien", "noise": 1, "smoke": 0, "guests": 1,
        "hobbies": ["doc sach", "the thao", "nhac"],
        "top": "sleep",
        "major": "CNTT Quốc tế (VNUK)",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=ThaiBaoVNUK&backgroundColor=b6e3f4"
    },
    {
        "id": 102,
        "name": "Lê Văn Việt",
        "tagline": "Sinh viên SPKT - Cú đêm làm đồ án cơ điện tử, chịu ồn tốt",
        "group": "B",
        "sleep": 26.0, "wake": 9.5, "tidy": 2, "study": "phong", "noise": 4, "smoke": 0, "guests": 4,
        "hobbies": ["game", "phim", "nhac"],
        "top": "noise",
        "major": "Cơ điện tử (SPKT)",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=VanVietSPKT&backgroundColor=ffdfbf"
    },
    {
        "id": 103,
        "name": "Lê Minh Quân",
        "tagline": "Sinh viên Kinh tế - Lối sống healthy, thể thao, thích nấu ăn & ghét thuốc lá",
        "group": "B",
        "sleep": 23.5, "wake": 6.5, "tidy": 4, "study": "it", "noise": 3, "smoke": 0, "guests": 2,
        "hobbies": ["the thao", "nau an", "nhac"],
        "top": "smoke",
        "major": "Kinh doanh (DUE)",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=MinhQuanDUE&backgroundColor=c0aede"
    },
    {
        "id": 104,
        "name": "Phạm Hoàng Đạt",
        "tagline": "Mọt sách thư viện, thích yên ắng và ngăn nắp",
        "group": "A",
        "sleep": 22.5, "wake": 6.5, "tidy": 5, "study": "thuvien", "noise": 1, "smoke": 0, "guests": 1,
        "hobbies": ["doc sach", "the thao"],
        "top": "tidy",
        "major": "Khoa học Máy tính",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=DatPham&backgroundColor=d1d4f9"
    },
    {
        "id": 105,
        "name": "Vũ Hải Nam",
        "tagline": "Cú đêm lập trình, hay thức cày hackathon",
        "group": "B",
        "sleep": 25.5, "wake": 9.0, "tidy": 3, "study": "phong", "noise": 4, "smoke": 0, "guests": 3,
        "hobbies": ["game", "nhac"],
        "top": "sleep",
        "major": "Hệ thống Thông tin",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=NamVu&backgroundColor=ffd5dc"
    },
    {
        "id": 106,
        "name": "Đặng Tuấn Kiệt",
        "tagline": "Người năng động, hay chơi thể thao và thích giao lưu",
        "group": "A",
        "sleep": 23.0, "wake": 7.0, "tidy": 4, "study": "it", "noise": 2, "smoke": 0, "guests": 2,
        "hobbies": ["the thao", "nau an", "phim"],
        "top": "tidy",
        "major": "Kỹ thuật Dữ liệu",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=KietDang&backgroundColor=b6e3f4"
    },
    {
        "id": 107,
        "name": "Hoàng Xuân Bách",
        "tagline": "Thích xem phim, nghe nhạc, lịch sinh hoạt tự do",
        "group": "B",
        "sleep": 25.0, "wake": 8.5, "tidy": 2, "study": "phong", "noise": 3, "smoke": 1, "guests": 4,
        "hobbies": ["phim", "game"],
        "top": "smoke",
        "major": "Marketing",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=BachHoang&backgroundColor=ffdfbf"
    },
    {
        "id": 108,
        "name": "Ngô Gia Huy",
        "tagline": "Điềm đạm, thích đọc sách và nấu ăn tại phòng",
        "group": "A",
        "sleep": 22.5, "wake": 6.5, "tidy": 4, "study": "thuvien", "noise": 2, "smoke": 0, "guests": 2,
        "hobbies": ["doc sach", "nau an", "nhac"],
        "top": "sleep",
        "major": "Thương mại Điện tử",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=HuyNgo&backgroundColor=c0aede"
    },
    {
        "id": 109,
        "name": "Đỗ Quang Minh",
        "tagline": "Thích giao lưu, hay mời bạn bè về cùng học",
        "group": "B",
        "sleep": 24.5, "wake": 8.0, "tidy": 3, "study": "phong", "noise": 4, "smoke": 0, "guests": 5,
        "hobbies": ["game", "the thao"],
        "top": "noise",
        "major": "Quản trị Khách sạn",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=MinhDo&backgroundColor=d1d4f9"
    },
    {
        "id": 110,
        "name": "Bùi Đức Thịnh",
        "tagline": "Ngủ sớm dậy sớm, rèn luyện thể lực mỗi sáng",
        "group": "A",
        "sleep": 21.5, "wake": 5.5, "tidy": 5, "study": "thuvien", "noise": 1, "smoke": 0, "guests": 1,
        "hobbies": ["the thao", "doc sach"],
        "top": "sleep",
        "major": "Logistics",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=ThinhBui&backgroundColor=b6e3f4"
    },
    {
        "id": 111,
        "name": "Trần Đình Trọng",
        "tagline": "Thích bóng đá, nếp sống quy củ và chan hòa",
        "group": "A",
        "sleep": 23.0, "wake": 7.0, "tidy": 4, "study": "thuvien", "noise": 2, "smoke": 0, "guests": 2,
        "hobbies": ["the thao", "nhac"],
        "top": "tidy",
        "major": "Khoa học Máy tính",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=TrongTran&backgroundColor=c0aede"
    },
    {
        "id": 112,
        "name": "Lê Thanh Tùng",
        "tagline": "Học bá thư viện, không gian sống luôn tinh tươm",
        "group": "A",
        "sleep": 22.0, "wake": 6.0, "tidy": 5, "study": "thuvien", "noise": 1, "smoke": 0, "guests": 1,
        "hobbies": ["doc sach", "the thao"],
        "top": "sleep",
        "major": "Toán Tin Ứng dụng",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=TungLe&backgroundColor=ffd5dc"
    },
    {
        "id": 113,
        "name": "Nguyễn Hoàng Long",
        "tagline": "Dậy trễ, thích thức khuya xem đá bóng",
        "group": "B",
        "sleep": 26.0, "wake": 10.0, "tidy": 2, "study": "phong", "noise": 4, "smoke": 0, "guests": 3,
        "hobbies": ["the thao", "game", "phim"],
        "top": "sleep",
        "major": "Cơ khí Động lực",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=LongNguyen&backgroundColor=d1d4f9"
    },
    {
        "id": 114,
        "name": "Phan Hữu Nghĩa",
        "tagline": "Thích yên tĩnh, chăm chỉ học hành và nấu nướng",
        "group": "A",
        "sleep": 22.5, "wake": 6.5, "tidy": 4, "study": "thuvien", "noise": 2, "smoke": 0, "guests": 1,
        "hobbies": ["nau an", "doc sach", "nhac"],
        "top": "tidy",
        "major": "Kế toán Doanh nghiệp",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=NghiaPhan&backgroundColor=b6e3f4"
    },
    {
        "id": 115,
        "name": "Nguyễn Trọng Khang",
        "tagline": "Đam mê eSports, năng nổ tham gia hoạt động câu lạc bộ",
        "group": "B",
        "sleep": 25.5, "wake": 9.0, "tidy": 2, "study": "phong", "noise": 4, "smoke": 0, "guests": 4,
        "hobbies": ["game", "the thao"],
        "top": "noise",
        "major": "Truyền thông Đa phương tiện",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=KhangNguyen&backgroundColor=ffdfbf"
    },
    {
        "id": 116,
        "name": "Đinh Hữu Phúc",
        "tagline": "Tân sinh viên chăm chỉ, hay lên thư viện học bài",
        "group": "B",
        "sleep": 23.0, "wake": 7.0, "tidy": 4, "study": "thuvien", "noise": 2, "smoke": 0, "guests": 2,
        "hobbies": ["doc sach", "nhac"],
        "top": "tidy",
        "major": "Kinh tế Đối ngoại",
        "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=PhucDinh&backgroundColor=b6e3f4"
    }
]

# Hàm tính toán tương đồng và chấm điểm
def calculate_criterion_sims(x: dict, y: dict) -> dict:
    clip = lambda v: max(0.0, min(1.0, float(v)))
    x_hobbies = set(x.get("hobbies", []))
    y_hobbies = set(y.get("hobbies", []))
    union = x_hobbies | y_hobbies
    
    return {
        "sleep": clip(1.0 - abs(x["sleep"] - y["sleep"]) / 5.0),
        "wake": clip(1.0 - abs(x["wake"] - y["wake"]) / 5.0),
        "tidy": clip(1.0 - abs(x["tidy"] - y["tidy"]) / 4.0),
        "study": 1.0 if x["study"] == y["study"] else 0.0,
        "noise": clip(1.0 - abs(x["noise"] - y["noise"]) / 4.0),
        "smoke": 1.0 if x["smoke"] == y["smoke"] else 0.0,
        "guests": clip(1.0 - abs(x["guests"] - y["guests"]) / 4.0),
        "hobbies": float(len(x_hobbies & y_hobbies) / len(union)) if union else 0.0,
    }

def calculate_pair_score(x: dict, y: dict) -> float:
    w = dict(WEIGHTS)
    top_key = x.get("top", "sleep")
    if top_key in w:
        w[top_key] *= 1.5
    total = sum(w.values())
    sims = calculate_criterion_sims(x, y)
    score = 100.0 * sum(w[k] * sims[k] for k in w) / total
    return round(score, 1)

def explain_pair(x: dict, y: dict) -> dict:
    sims = calculate_criterion_sims(x, y)
    good = [CRITERIA_LABELS[k] for k, v in sims.items() if v >= 0.75]
    bad = [CRITERIA_LABELS[k] for k, v in sims.items() if v <= 0.40]
    return {
        "sims": sims,
        "good": good,
        "bad": bad
    }

# Helper session authentication
def get_current_user_from_request(request: Request) -> Optional[dict]:
    raw_cookie = request.cookies.get("ktx_auth_session")
    if not raw_cookie:
        return None
    try:
        decoded = base64.b64decode(raw_cookie.encode('ascii')).decode('utf-8')
        user_data = json.loads(decoded)
        if isinstance(user_data, dict) and "name" in user_data:
            return user_data
    except Exception:
        return None
    return None

class LoginRequest(BaseModel):
    student_id: str
    password: str
    school: str = "VNUK"
    persona_key: str = "custom"
    full_name: str = ""

class UserProfileInput(BaseModel):
    name: str = "Bạn (Sinh viên tìm phòng)"
    group: str = "A"
    sleep: float = 22.5
    wake: float = 6.5
    tidy: int = 4
    study: str = "thuvien"
    noise: int = 2
    smoke: int = 0
    guests: int = 1
    hobbies: List[str] = ["doc sach", "the thao"]
    top: str = "sleep"

# ==================== ROUTE ĐĂNG NHẬP / ĐĂNG XUẤT ====================

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    user = get_current_user_from_request(request)
    if user:
        return RedirectResponse(url="/", status_code=303)
    return HTMLResponse(content=get_login_html())

@app.post("/api/login")
def api_login(req: LoginRequest):
    p_key = req.persona_key
    if p_key in PERSONAS:
        user_data = dict(PERSONAS[p_key])
    else:
        s_id = req.student_id.strip()
        pwd = req.password.strip()
        if not s_id or not pwd:
            raise HTTPException(status_code=400, detail="Vui lòng nhập đầy đủ Mã sinh viên và Mật khẩu.")
        
        name = req.full_name.strip() if req.full_name.strip() else f"Sinh viên {s_id.upper()}"
        user_data = {
            "id": s_id.lower(),
            "student_id": s_id.upper(),
            "name": name,
            "school": req.school.strip() if req.school.strip() else "ĐH Đà Nẵng",
            "major": "Sinh viên Ký túc xá",
            "group": "A",
            "sleep": 22.5,
            "wake": 6.5,
            "tidy": 4,
            "study": "thuvien",
            "noise": 2,
            "smoke": 0,
            "guests": 2,
            "hobbies": ["doc sach", "the thao"],
            "top": "sleep",
            "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={urllib.parse.quote(name)}&backgroundColor=b6e3f4"
        }

    cookie_val = base64.b64encode(json.dumps(user_data, ensure_ascii=False).encode('utf-8')).decode('ascii')
    response = JSONResponse(content={"success": True, "redirect": "/", "user": user_data})
    response.set_cookie(key="ktx_auth_session", value=cookie_val, max_age=86400, path="/")
    return response

@app.get("/logout")
def logout():
    res = RedirectResponse(url="/login", status_code=303)
    res.delete_cookie(key="ktx_auth_session", path="/")
    return res

@app.post("/api/logout")
def api_logout():
    res = JSONResponse(content={"success": True, "redirect": "/login"})
    res.delete_cookie(key="ktx_auth_session", path="/")
    return res

# ==================== ROUTE DASHBOARD CHÍNH ====================

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    user = get_current_user_from_request(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    return HTMLResponse(content=get_dashboard_html(user))

@app.get("/usecase", response_class=HTMLResponse)
def usecase_diagram():
    html_path = os.path.join(os.path.dirname(__file__), "ui", "usecase_view.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/wireframe", response_class=HTMLResponse)
@app.get("/wireframes", response_class=HTMLResponse)
def wireframe_page():
    html_path = os.path.join(os.path.dirname(__file__), "ui", "wireframe_view.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/download-spec-docx")
def download_spec_docx():
    docx_path = os.path.join(os.path.dirname(__file__), "docs", "Tai_Lieu_Dac_Ta_UseCase_Va_Sequence_Diagram_KTX.docx")
    if os.path.exists(docx_path):
        return FileResponse(
            docx_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename="Tai_Lieu_Dac_Ta_UseCase_Va_Sequence_Diagram_KTX.docx"
        )
    raise HTTPException(status_code=404, detail="File tài liệu Word chưa được tạo.")

@app.get("/download-wireframe-pdf")
def download_wireframe_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), "docs", "Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf")
    if os.path.exists(pdf_path):
        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename="Tai_Lieu_Wireframe_Chi_Tiet_He_Thong_KTX.pdf"
        )
    raise HTTPException(status_code=404, detail="File tài liệu PDF chưa được tạo.")

@app.get("/download-usecase-drawio")
def download_usecase_drawio():
    drawio_path = os.path.join(os.path.dirname(__file__), "docs", "KTX_Smart_Match_UseCase.drawio")
    if os.path.exists(drawio_path):
        return FileResponse(
            drawio_path,
            media_type="application/xml",
            filename="KTX_Smart_Match_UseCase.drawio"
        )
    raise HTTPException(status_code=404, detail="File drawio chưa được tạo.")

@app.get("/wireframe-detail", response_class=HTMLResponse)
def wireframe_detail_page():
    html_path = os.path.join(os.path.dirname(__file__), "ui", "wireframe_detail_export.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/api/rank")
def rank_roommates(user: UserProfileInput, request: Request):
    auth_user = get_current_user_from_request(request)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Vui lòng đăng nhập trước khi sử dụng tính năng này.")

    user_dict = user.model_dump()
    target_group = "B" if user_dict["group"] == "A" else "A"
    
    # Lọc danh sách ứng viên (trừ người dùng hiện tại nếu trùng tên)
    pool = [c for c in CANDIDATES if c["group"] == target_group and c["name"].lower() != user_dict["name"].lower()]
    if not pool:
        pool = [c for c in CANDIDATES if c["name"].lower() != user_dict["name"].lower()]

    ranked = []
    for cand in pool:
        score_user_to_cand = calculate_pair_score(user_dict, cand)
        score_cand_to_user = calculate_pair_score(cand, user_dict)
        avg_score = round((score_user_to_cand + score_cand_to_user) / 2.0, 1)
        explanation = explain_pair(user_dict, cand)
        
        tag = "Siêu hòa hợp" if avg_score >= 75 else (
            "Hòa hợp tốt" if avg_score >= 60 else (
                "Cần thỏa hiệp" if avg_score >= 45 else "Dễ xung đột"
            )
        )
        badge_color = "emerald" if avg_score >= 75 else (
            "sky" if avg_score >= 60 else (
                "amber" if avg_score >= 45 else "rose"
            )
        )
        
        ranked.append({
            "id": cand["id"],
            "name": cand["name"],
            "tagline": cand["tagline"],
            "major": cand["major"],
            "group": cand["group"],
            "avatar": cand["avatar"],
            "sleep": cand["sleep"],
            "wake": cand["wake"],
            "tidy": cand["tidy"],
            "study": cand["study"],
            "noise": cand["noise"],
            "smoke": cand["smoke"],
            "guests": cand["guests"],
            "hobbies": cand["hobbies"],
            "top": cand["top"],
            "score_user_to_cand": score_user_to_cand,
            "score_cand_to_user": score_cand_to_user,
            "avg_score": avg_score,
            "tag": tag,
            "badge_color": badge_color,
            "explanation": explanation
        })
        
    ranked.sort(key=lambda x: x["avg_score"], reverse=True)
    for i, item in enumerate(ranked):
        item["rank"] = i + 1
        
    return {
        "user": user_dict,
        "target_group": target_group,
        "rankings": ranked
    }

# ==================== HTML TEMPLATES ====================

def get_login_html() -> str:
    return """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng Nhập - Hệ Thống Ghép Bạn Cùng Phòng Ký Túc Xá</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-indigo-500 selection:text-white">
    <!-- Background glow decor -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none -z-10">
        <div class="absolute -top-40 left-1/2 -translate-x-1/2 w-[700px] h-[500px] bg-gradient-to-b from-indigo-600/25 via-indigo-900/10 to-transparent blur-3xl rounded-full"></div>
        <div class="absolute bottom-0 right-10 w-96 h-96 bg-amber-500/10 blur-3xl rounded-full"></div>
        <div class="absolute top-1/3 left-10 w-80 h-80 bg-sky-500/10 blur-3xl rounded-full"></div>
    </div>

    <!-- Header -->
    <header class="border-b border-slate-800/80 bg-slate-900/60 backdrop-blur-md px-6 py-4">
        <div class="max-w-6xl mx-auto flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 to-indigo-600 flex items-center justify-center text-white font-extrabold text-xl shadow-lg shadow-indigo-500/20">
                    🏢
                </div>
                <div>
                    <h1 class="text-sm font-extrabold tracking-wide text-slate-200 uppercase">Ký Túc Xá Đại Học Đà Nẵng</h1>
                    <p class="text-[11px] text-slate-400">Cổng xác thực sinh viên nội trú & Ghép phòng thông minh</p>
                </div>
            </div>
            <span class="text-xs bg-slate-800/80 border border-slate-700/60 px-3 py-1.5 rounded-full text-slate-300">
                🔒 Kết nối bảo mật KTX
            </span>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-5xl mx-auto px-4 py-8 md:py-12 flex-1 w-full flex flex-col items-center justify-center">
        <div class="w-full max-w-4xl space-y-8">
            
            <!-- Hero Title -->
            <div class="text-center space-y-2.5">
                <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-semibold">
                    <span>✨</span> Hệ thống phân tích xếp hạng tương thích Gale-Shapley
                </div>
                <h2 class="text-2xl md:text-3xl font-extrabold text-white tracking-tight">
                    Đăng Nhập Trước Khi Sử Dụng
                </h2>
                <p class="text-xs md:text-sm text-slate-400 max-w-lg mx-auto">
                    Chọn nhanh tài khoản Persona sinh viên mẫu hoặc nhập mã sinh viên của bạn để vào Bảng xếp hạng Bạn cùng phòng KTX.
                </p>
            </div>

            <!-- Two-Column Layout -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                
                <!-- Left: 1-Click Persona Login (7 cols) -->
                <div class="lg:col-span-7 bg-slate-900/80 border border-slate-800 rounded-3xl p-6 shadow-2xl backdrop-blur-xl space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                        <div class="flex items-center gap-2">
                            <span class="text-lg">⚡</span>
                            <h3 class="text-sm font-bold text-slate-200 uppercase tracking-wider">Đăng nhập nhanh 1 chạm (3 Persona mẫu)</h3>
                        </div>
                        <span class="text-[11px] text-emerald-400 font-semibold bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/20">Khuyên dùng</span>
                    </div>
                    <p class="text-xs text-slate-400">Nhấp chọn 1 trong 3 sinh viên để hệ thống tự động đăng nhập và nạp sẵn thói quen sinh hoạt:</p>

                    <!-- Persona 1: Nguyễn Duy Thái Bảo -->
                    <div onclick="quickLogin('thaibao')" class="group p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-indigo-500/60 hover:bg-slate-900/90 transition-all duration-200 cursor-pointer shadow-lg hover:shadow-indigo-500/10 flex items-center justify-between gap-4">
                        <div class="flex items-center gap-3.5">
                            <img src="https://api.dicebear.com/7.x/bottts/svg?seed=ThaiBaoVNUK&backgroundColor=b6e3f4" class="w-12 h-12 rounded-xl border border-slate-700 bg-slate-900 p-0.5">
                            <div>
                                <div class="flex items-center gap-2">
                                    <h4 class="text-sm font-bold text-white group-hover:text-indigo-300 transition">Nguyễn Duy Thái Bảo</h4>
                                    <span class="text-[10px] bg-sky-500/20 text-sky-300 border border-sky-500/30 font-bold px-2 py-0.5 rounded-md">VNUK</span>
                                </div>
                                <p class="text-[11px] text-slate-400 mt-0.5">CNTT Quốc tế • Ngủ 22:00 • Học thư viện • Rất ngăn nắp</p>
                                <span class="text-[10px] text-amber-400 font-medium">🎯 Ưu tiên số 1: Giờ đi ngủ (cần phòng yên tĩnh)</span>
                            </div>
                        </div>
                        <span class="shrink-0 text-xs font-semibold px-3 py-1.5 rounded-xl bg-indigo-600 group-hover:bg-indigo-500 text-white transition shadow">
                            Vào ngay →
                        </span>
                    </div>

                    <!-- Persona 2: Lê Văn Việt -->
                    <div onclick="quickLogin('vanviet')" class="group p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-amber-500/60 hover:bg-slate-900/90 transition-all duration-200 cursor-pointer shadow-lg hover:shadow-amber-500/10 flex items-center justify-between gap-4">
                        <div class="flex items-center gap-3.5">
                            <img src="https://api.dicebear.com/7.x/bottts/svg?seed=VanVietSPKT&backgroundColor=ffdfbf" class="w-12 h-12 rounded-xl border border-slate-700 bg-slate-900 p-0.5">
                            <div>
                                <div class="flex items-center gap-2">
                                    <h4 class="text-sm font-bold text-white group-hover:text-amber-300 transition">Lê Văn Việt</h4>
                                    <span class="text-[10px] bg-amber-500/20 text-amber-300 border border-amber-500/30 font-bold px-2 py-0.5 rounded-md">SPKT</span>
                                </div>
                                <p class="text-[11px] text-slate-400 mt-0.5">Cơ điện tử • Cú đêm 02:00 AM • Làm mạch & code khuya</p>
                                <span class="text-[10px] text-amber-400 font-medium">🎯 Ưu tiên số 1: Tìm bạn cùng phòng chịu ồn tốt</span>
                            </div>
                        </div>
                        <span class="shrink-0 text-xs font-semibold px-3 py-1.5 rounded-xl bg-amber-600 group-hover:bg-amber-500 text-white transition shadow">
                            Vào ngay →
                        </span>
                    </div>

                    <!-- Persona 3: Lê Minh Quân -->
                    <div onclick="quickLogin('minhquan')" class="group p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-emerald-500/60 hover:bg-slate-900/90 transition-all duration-200 cursor-pointer shadow-lg hover:shadow-emerald-500/10 flex items-center justify-between gap-4">
                        <div class="flex items-center gap-3.5">
                            <img src="https://api.dicebear.com/7.x/bottts/svg?seed=MinhQuanDUE&backgroundColor=c0aede" class="w-12 h-12 rounded-xl border border-slate-700 bg-slate-900 p-0.5">
                            <div>
                                <div class="flex items-center gap-2">
                                    <h4 class="text-sm font-bold text-white group-hover:text-emerald-300 transition">Lê Minh Quân</h4>
                                    <span class="text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-bold px-2 py-0.5 rounded-md">DUE</span>
                                </div>
                                <p class="text-[11px] text-slate-400 mt-0.5">Quản trị KD • Healthy • Thể thao • Tự nấu ăn ở KTX</p>
                                <span class="text-[10px] text-rose-400 font-medium">🚫 Ưu tiên số 1: Dị ứng khói thuốc (smoke = 0)</span>
                            </div>
                        </div>
                        <span class="shrink-0 text-xs font-semibold px-3 py-1.5 rounded-xl bg-emerald-600 group-hover:bg-emerald-500 text-white transition shadow">
                            Vào ngay →
                        </span>
                    </div>
                </div>

                <!-- Right: Manual Login Form (5 cols) -->
                <div class="lg:col-span-5 bg-slate-900/80 border border-slate-800 rounded-3xl p-6 shadow-2xl backdrop-blur-xl space-y-4">
                    <div class="border-b border-slate-800 pb-3">
                        <h3 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                            <span>🔑</span> Nhập Tài Khoản Tùy Chọn
                        </h3>
                        <p class="text-xs text-slate-400 mt-0.5">Dành cho sinh viên đăng ký mới</p>
                    </div>

                    <form id="custom-login-form" onsubmit="handleCustomLogin(event)" class="space-y-3.5 text-xs">
                        <div id="login-error" class="hidden p-3 rounded-xl bg-rose-950/40 border border-rose-800/60 text-rose-300 text-xs"></div>

                        <div>
                            <label class="block font-semibold text-slate-300 mb-1">Trường trực thuộc ĐHĐN:</label>
                            <select id="login-school" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                                <option value="Viện NC & ĐT Việt - Anh (VNUK)">Viện NC & ĐT Việt - Anh (VNUK)</option>
                                <option value="ĐH Sư phạm Kỹ thuật (SPKT)">ĐH Sư phạm Kỹ thuật (SPKT)</option>
                                <option value="Trường ĐH Kinh tế (DUE)">Trường ĐH Kinh tế (DUE)</option>
                                <option value="Trường ĐH Bách khoa (DUT)">Trường ĐH Bách khoa (DUT)</option>
                                <option value="Khác (Tân sinh viên KTX)">Khác (Tân sinh viên KTX)</option>
                            </select>
                        </div>

                        <div>
                            <label class="block font-semibold text-slate-300 mb-1">Họ và tên của bạn:</label>
                            <input type="text" id="login-fullname" placeholder="VD: Nguyễn Văn An" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 placeholder-slate-600">
                        </div>

                        <div>
                            <label class="block font-semibold text-slate-300 mb-1">Mã sinh viên / Tên đăng nhập: <span class="text-rose-400">*</span></label>
                            <input type="text" id="login-studentid" required placeholder="VD: 22VNUK099, 21SPKT120..." class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 placeholder-slate-600">
                        </div>

                        <div>
                            <label class="block font-semibold text-slate-300 mb-1">Mật khẩu: <span class="text-rose-400">*</span></label>
                            <input type="password" id="login-password" required value="123456" placeholder="Nhập mật khẩu" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500 placeholder-slate-600">
                        </div>

                        <button type="submit" id="btn-submit" class="w-full py-3 mt-2 rounded-xl bg-gradient-to-r from-indigo-600 via-indigo-500 to-sky-600 hover:opacity-95 text-white font-bold text-xs shadow-lg shadow-indigo-500/25 transition flex items-center justify-center gap-2">
                            <span>ĐĂNG NHẬP KÝ TÚC XÁ</span>
                            <span>➔</span>
                        </button>
                    </form>
                </div>

            </div>

        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800/80 bg-slate-900/40 text-center py-4 text-xs text-slate-500">
        Phần mềm hỗ trợ sinh viên KTX ghép phòng theo thuật toán Asymmetric Gale-Shapley © 2026
    </footer>

    <script>
        async function quickLogin(personaKey) {
            try {
                const res = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        student_id: personaKey,
                        password: 'demo',
                        persona_key: personaKey
                    })
                });
                const data = await res.json();
                if (data.success) {
                    window.location.href = data.redirect;
                }
            } catch (err) {
                alert('Lỗi đăng nhập: ' + err.message);
            }
        }

        async function handleCustomLogin(e) {
            e.preventDefault();
            const studentId = document.getElementById('login-studentid').value.trim();
            const password = document.getElementById('login-password').value.trim();
            const fullName = document.getElementById('login-fullname').value.trim();
            const school = document.getElementById('login-school').value;
            const errDiv = document.getElementById('login-error');

            if (!studentId || !password) {
                errDiv.innerText = 'Vui lòng nhập đầy đủ Mã sinh viên và Mật khẩu.';
                errDiv.classList.remove('hidden');
                return;
            }

            try {
                const res = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        student_id: studentId,
                        password: password,
                        full_name: fullName,
                        school: school,
                        persona_key: 'custom'
                    })
                });
                const data = await res.json();
                if (res.ok && data.success) {
                    window.location.href = data.redirect;
                } else {
                    errDiv.innerText = data.detail || 'Đăng nhập không thành công.';
                    errDiv.classList.remove('hidden');
                }
            } catch (err) {
                errDiv.innerText = 'Lỗi mạng: ' + err.message;
                errDiv.classList.remove('hidden');
            }
        }
    </script>
</body>
</html>
    """

def get_dashboard_html(user: dict) -> str:
    user_json = json.dumps(user, ensure_ascii=False)
    user_name = user.get("name", "Bạn")
    user_school = user.get("school", "Sinh viên KTX")
    user_avatar = user.get("avatar", "https://api.dicebear.com/7.x/bottts/svg?seed=User&backgroundColor=b6e3f4")
    user_student_id = user.get("student_id", "KTX")
    
    return f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bảng Xếp Hạng Bạn Cùng Phòng KTX Tương Thích Nhất</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
    <!-- Top Navbar -->
    <header class="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 to-indigo-600 flex items-center justify-center text-white font-bold text-xl shadow-lg shadow-indigo-500/20">
                    🏆
                </div>
                <div>
                    <h1 class="text-base sm:text-lg font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-amber-400 via-sky-300 to-indigo-400">
                        ROOMMATE RANKING DASHBOARD
                    </h1>
                    <p class="text-[11px] text-slate-400">Nhập thói quen & Nhận ngay Bảng xếp hạng Bạn cùng phòng từ Hạng 1 đến Hạng 8</p>
                </div>
            </div>

            <!-- User Auth Profile & Logout -->
            <div class="flex items-center gap-3">
                <div class="flex items-center gap-2.5 bg-slate-800/80 border border-slate-700/80 px-3 py-1.5 rounded-2xl">
                    <img src="{user_avatar}" class="w-8 h-8 rounded-xl border border-indigo-500/40 bg-slate-900">
                    <div class="text-left">
                        <div class="text-xs font-bold text-white flex items-center gap-1.5">
                            <span>{user_name}</span>
                            <span class="text-[10px] text-indigo-300 font-mono bg-indigo-950/60 px-1.5 py-0.2 rounded border border-indigo-800">{user_student_id}</span>
                        </div>
                        <p class="text-[10px] text-slate-400 truncate max-w-[170px]">{user_school}</p>
                    </div>
                </div>

                <a href="/wireframe" target="_blank" class="px-3 py-1.5 text-xs font-semibold rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center gap-1.5">
                    <span>📐</span>
                    <span class="hidden sm:inline">Wireframe UI</span>
                </a>

                <a href="/usecase" target="_blank" class="px-3 py-1.5 text-xs font-semibold rounded-xl bg-indigo-950/40 hover:bg-indigo-900/60 text-indigo-300 border border-indigo-800/60 transition flex items-center gap-1.5">
                    <span>📊</span>
                    <span class="hidden sm:inline">Sơ đồ Use Case</span>
                </a>

                <a href="/logout" class="px-3 py-1.5 text-xs font-semibold rounded-xl bg-rose-950/40 hover:bg-rose-900/60 text-rose-300 border border-rose-800/60 transition flex items-center gap-1.5">
                    <span>🚪</span>
                    <span class="hidden sm:inline">Đăng xuất</span>
                </a>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8">
        <!-- LEFT COLUMN: INPUT FORM (5 cols) -->
        <div class="lg:col-span-5 space-y-6">
            <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-5">
                <div class="flex items-center justify-between border-b border-slate-800 pb-4">
                    <div>
                        <h2 class="text-base font-bold text-slate-100 flex items-center gap-2">
                            📝 Nhập Thói Quen Sinh Hoạt
                        </h2>
                        <p class="text-xs text-slate-400">Điều chỉnh thông số để tìm ứng viên hòa hợp nhất với bạn</p>
                    </div>
                </div>

                <!-- Quick Load Persona Buttons -->
                <div class="space-y-1.5">
                    <span class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Thử nhanh thói quen theo Persona mẫu:</span>
                    <div class="grid grid-cols-3 gap-2">
                        <button onclick="loadPersonaPreset('thaibao')" class="px-2.5 py-2 text-xs font-semibold rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition text-center truncate">
                            Thái Bảo (VNUK)
                        </button>
                        <button onclick="loadPersonaPreset('vanviet')" class="px-2.5 py-2 text-xs font-semibold rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition text-center truncate">
                            Văn Việt (SPKT)
                        </button>
                        <button onclick="loadPersonaPreset('minhquan')" class="px-2.5 py-2 text-xs font-semibold rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition text-center truncate">
                            Minh Quân (DUE)
                        </button>
                    </div>
                </div>

                <form id="profile-form" onsubmit="event.preventDefault(); triggerRanking();" class="space-y-4 text-xs">
                    <div>
                        <label class="block font-semibold text-slate-300 mb-1">Tên hiển thị của bạn:</label>
                        <input type="text" id="inp-name" value="{user_name}" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-slate-200 focus:outline-none focus:border-indigo-500">
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block font-semibold text-slate-300 mb-1">Bạn thuộc nhóm KTX:</label>
                            <select id="inp-group" class="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-slate-200 focus:outline-none focus:border-indigo-500">
                                <option value="A">Nhóm A (Sinh viên cũ)</option>
                                <option value="B">Nhóm B (Tân sinh viên)</option>
                            </select>
                        </div>
                        <div>
                            <label class="block font-semibold text-amber-400 mb-1">Ưu tiên số 1 (Hệ số 1.5x):</label>
                            <select id="inp-top" class="w-full bg-slate-950 border border-amber-500/40 rounded-xl px-3 py-2 text-amber-300 focus:outline-none focus:border-amber-400 font-medium">
                                <option value="sleep">Giờ đi ngủ (sleep)</option>
                                <option value="tidy">Độ gọn gàng (tidy)</option>
                                <option value="smoke">Không hút thuốc (smoke)</option>
                                <option value="noise">Chịu tiếng ồn (noise)</option>
                                <option value="study">Thói quen học (study)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Sleep & Wake Slider -->
                    <div class="bg-slate-950 p-3.5 rounded-2xl border border-slate-800/80 space-y-3">
                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <span class="text-slate-300 font-medium">🌙 Giờ đi ngủ:</span>
                                <span id="val-sleep" class="text-indigo-400 font-bold">22:00</span>
                            </div>
                            <input type="range" id="inp-sleep" min="20" max="28" step="0.5" value="22" oninput="updateSliderLabels()" class="w-full accent-indigo-500 cursor-pointer">
                            <div class="flex justify-between text-[10px] text-slate-500">
                                <span>20h (Sớm)</span>
                                <span>24h (Nửa đêm)</span>
                                <span>04h sáng</span>
                            </div>
                        </div>

                        <div>
                            <div class="flex justify-between items-center mb-1">
                                <span class="text-slate-300 font-medium">⏰ Giờ thức dậy:</span>
                                <span id="val-wake" class="text-indigo-400 font-bold">06:00</span>
                            </div>
                            <input type="range" id="inp-wake" min="5" max="11" step="0.5" value="6" oninput="updateSliderLabels()" class="w-full accent-indigo-500 cursor-pointer">
                            <div class="flex justify-between text-[10px] text-slate-500">
                                <span>05:00 AM</span>
                                <span>08:00 AM</span>
                                <span>11:00 AM</span>
                            </div>
                        </div>
                    </div>

                    <!-- Cleanliness & Noise Tolerance -->
                    <div class="grid grid-cols-2 gap-3">
                        <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800/80">
                            <label class="block text-slate-300 font-medium mb-1">🧹 Độ gọn gàng:</label>
                            <select id="inp-tidy" class="w-full bg-slate-900 border border-slate-800 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none">
                                <option value="5">5/5 - Cực kỳ ngăn nắp</option>
                                <option value="4" selected>4/5 - Khá sạch sẽ</option>
                                <option value="3">3/5 - Trung bình</option>
                                <option value="2">2/5 - Hơi bừa bộn</option>
                                <option value="1">1/5 - Bừa bộn</option>
                            </select>
                        </div>
                        <div class="bg-slate-950 p-3 rounded-2xl border border-slate-800/80">
                            <label class="block text-slate-300 font-medium mb-1">🎧 Chịu tiếng ồn:</label>
                            <select id="inp-noise" class="w-full bg-slate-900 border border-slate-800 rounded-lg px-2.5 py-1.5 text-slate-200 focus:outline-none">
                                <option value="1">1/5 - Rất nhạy cảm</option>
                                <option value="2" selected>2/5 - Nhạy cảm vừa</option>
                                <option value="3">3/5 - Bình thường</option>
                                <option value="4">4/5 - Chịu ồn tốt</option>
                                <option value="5">5/5 - Thích sôi động</option>
                            </select>
                        </div>
                    </div>

                    <!-- Study, Smoke, Guests -->
                    <div class="grid grid-cols-3 gap-2">
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800/80">
                            <label class="block text-slate-400 text-[10px] mb-1 font-semibold">📖 Thói quen học:</label>
                            <select id="inp-study" class="w-full bg-slate-900 border border-slate-800 rounded px-1.5 py-1 text-slate-200 text-xs">
                                <option value="thuvien">Lên thư viện</option>
                                <option value="phong">Học tại phòng</option>
                                <option value="it">Ít học tại KTX</option>
                            </select>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800/80">
                            <label class="block text-slate-400 text-[10px] mb-1 font-semibold">🚭 Hút thuốc lá:</label>
                            <select id="inp-smoke" class="w-full bg-slate-900 border border-slate-800 rounded px-1.5 py-1 text-slate-200 text-xs">
                                <option value="0">0 - Không hút</option>
                                <option value="1">1 - Có hút</option>
                            </select>
                        </div>
                        <div class="bg-slate-950 p-2.5 rounded-xl border border-slate-800/80">
                            <label class="block text-slate-400 text-[10px] mb-1 font-semibold">👥 Dắt bạn về:</label>
                            <select id="inp-guests" class="w-full bg-slate-900 border border-slate-800 rounded px-1.5 py-1 text-slate-200 text-xs">
                                <option value="1">Hiếm khi (1)</option>
                                <option value="2" selected>Thỉnh thoảng (2)</option>
                                <option value="4">Thường xuyên (4)</option>
                            </select>
                        </div>
                    </div>

                    <!-- Hobbies -->
                    <div class="bg-slate-950 p-3.5 rounded-2xl border border-slate-800/80 space-y-2">
                        <label class="block text-slate-300 font-medium">🎨 Sở thích chung:</label>
                        <div class="grid grid-cols-2 gap-2 text-xs">
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="doc sach" checked class="accent-indigo-500 rounded">
                                <span>📚 Đọc sách</span>
                            </label>
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="the thao" checked class="accent-indigo-500 rounded">
                                <span>⚽ Thể thao</span>
                            </label>
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="game" class="accent-indigo-500 rounded">
                                <span>🎮 Chơi game</span>
                            </label>
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="nhac" checked class="accent-indigo-500 rounded">
                                <span>🎵 Nghe nhạc</span>
                            </label>
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="nau an" class="accent-indigo-500 rounded">
                                <span>🍳 Nấu ăn</span>
                            </label>
                            <label class="flex items-center gap-2 text-slate-300 cursor-pointer">
                                <input type="checkbox" name="hobby" value="phim" class="accent-indigo-500 rounded">
                                <span>🎬 Xem phim</span>
                            </label>
                        </div>
                    </div>

                    <button type="submit" class="w-full py-3 rounded-2xl bg-gradient-to-r from-amber-500 via-indigo-600 to-indigo-700 hover:opacity-95 text-white font-bold text-sm shadow-lg shadow-indigo-500/20 transition flex items-center justify-center gap-2">
                        <span>🔍 TÍNH TOÁN & CẬP NHẬT XẾP HẠNG</span>
                    </button>
                </form>
            </div>
        </div>

        <!-- RIGHT COLUMN: RANKING LIST (7 cols) -->
        <div class="lg:col-span-7 space-y-5">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-slate-900 border border-slate-800 p-4 rounded-2xl">
                <div>
                    <h2 class="text-base font-bold text-white flex items-center gap-2">
                        <span>🏆</span> BẢNG XẾP HẠNG BẠN CÙNG PHÒNG PHÙ HỢP NHẤT
                    </h2>
                    <p id="ranking-subtitle" class="text-xs text-slate-400">Đang khởi tạo danh sách tương thích...</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="text-[11px] bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 px-2.5 py-1 rounded-xl font-bold">
                        Hiển thị Top 8
                    </span>
                </div>
            </div>

            <!-- List Container -->
            <div id="ranking-container" class="space-y-4">
                <!-- Javascript will render ranking cards here -->
            </div>
        </div>
    </main>

    <footer class="border-t border-slate-800/80 bg-slate-900/60 py-6 text-center text-xs text-slate-500 mt-12">
        Hệ thống xếp hạng phòng KTX ĐH Đà Nẵng • Gale-Shapley Matching Algorithm • Phiên bản 2026
    </footer>

    <script>
        const CURRENT_USER = {user_json};

        function updateSliderLabels() {{
            const sleepVal = parseFloat(document.getElementById('inp-sleep').value);
            const wakeVal = parseFloat(document.getElementById('inp-wake').value);
            
            let sleepStr = '';
            if (sleepVal < 24) {{
                sleepStr = (sleepVal % 1 === 0 ? sleepVal : Math.floor(sleepVal) + ':30') + ':00';
            }} else {{
                const amHour = sleepVal - 24;
                sleepStr = (amHour % 1 === 0 ? '0' + amHour : '0' + Math.floor(amHour) + ':30') + ':00 AM (sáng hôm sau)';
            }}
            document.getElementById('val-sleep').innerText = sleepStr;

            let wakeStr = (wakeVal % 1 === 0 ? '0' + wakeVal : '0' + Math.floor(wakeVal) + ':30') + ':00 AM';
            document.getElementById('val-wake').innerText = wakeStr;
        }}

        function loadPersonaPreset(type) {{
            if (type === 'thaibao') {{
                document.getElementById('inp-name').value = 'Nguyễn Duy Thái Bảo';
                document.getElementById('inp-group').value = 'A';
                document.getElementById('inp-top').value = 'sleep';
                document.getElementById('inp-sleep').value = '22.0';
                document.getElementById('inp-wake').value = '6.0';
                document.getElementById('inp-tidy').value = '5';
                document.getElementById('inp-study').value = 'thuvien';
                document.getElementById('inp-noise').value = '1';
                document.getElementById('inp-smoke').value = '0';
                document.getElementById('inp-guests').value = '1';
                setHobbies(['doc sach', 'the thao', 'nhac']);
            }} else if (type === 'vanviet') {{
                document.getElementById('inp-name').value = 'Lê Văn Việt';
                document.getElementById('inp-group').value = 'B';
                document.getElementById('inp-top').value = 'noise';
                document.getElementById('inp-sleep').value = '26.0';
                document.getElementById('inp-wake').value = '9.5';
                document.getElementById('inp-tidy').value = '2';
                document.getElementById('inp-study').value = 'phong';
                document.getElementById('inp-noise').value = '4';
                document.getElementById('inp-smoke').value = '0';
                document.getElementById('inp-guests').value = '4';
                setHobbies(['game', 'phim', 'nhac']);
            }} else if (type === 'minhquan') {{
                document.getElementById('inp-name').value = 'Lê Minh Quân';
                document.getElementById('inp-group').value = 'B';
                document.getElementById('inp-top').value = 'smoke';
                document.getElementById('inp-sleep').value = '23.5';
                document.getElementById('inp-wake').value = '6.5';
                document.getElementById('inp-tidy').value = '4';
                document.getElementById('inp-study').value = 'it';
                document.getElementById('inp-noise').value = '3';
                document.getElementById('inp-smoke').value = '0';
                document.getElementById('inp-guests').value = '2';
                setHobbies(['the thao', 'nau an', 'nhac']);
            }}
            updateSliderLabels();
            triggerRanking();
        }}

        function initUserValues() {{
            if (CURRENT_USER) {{
                if (CURRENT_USER.id === 'thaibao') {{
                    loadPersonaPreset('thaibao');
                    return;
                }} else if (CURRENT_USER.id === 'vanviet') {{
                    loadPersonaPreset('vanviet');
                    return;
                }} else if (CURRENT_USER.id === 'minhquan') {{
                    loadPersonaPreset('minhquan');
                    return;
                }}
                
                if (CURRENT_USER.name) document.getElementById('inp-name').value = CURRENT_USER.name;
                if (CURRENT_USER.group) document.getElementById('inp-group').value = CURRENT_USER.group;
                if (CURRENT_USER.top) document.getElementById('inp-top').value = CURRENT_USER.top;
                if (CURRENT_USER.sleep) document.getElementById('inp-sleep').value = CURRENT_USER.sleep;
                if (CURRENT_USER.wake) document.getElementById('inp-wake').value = CURRENT_USER.wake;
                if (CURRENT_USER.tidy) document.getElementById('inp-tidy').value = CURRENT_USER.tidy;
                if (CURRENT_USER.study) document.getElementById('inp-study').value = CURRENT_USER.study;
                if (CURRENT_USER.noise) document.getElementById('inp-noise').value = CURRENT_USER.noise;
                if (CURRENT_USER.smoke !== undefined) document.getElementById('inp-smoke').value = CURRENT_USER.smoke;
                if (CURRENT_USER.guests) document.getElementById('inp-guests').value = CURRENT_USER.guests;
                if (CURRENT_USER.hobbies) setHobbies(CURRENT_USER.hobbies);
            }}
            updateSliderLabels();
            triggerRanking();
        }}

        function setHobbies(selected) {{
            document.querySelectorAll('input[name="hobby"]').forEach(cb => {{
                cb.checked = selected.includes(cb.value);
            }});
        }}

        function getSelectedHobbies() {{
            const list = [];
            document.querySelectorAll('input[name="hobby"]:checked').forEach(cb => {{
                list.push(cb.value);
            }});
            return list;
        }}

        async function triggerRanking() {{
            const payload = {{
                name: document.getElementById('inp-name').value,
                group: document.getElementById('inp-group').value,
                top: document.getElementById('inp-top').value,
                sleep: parseFloat(document.getElementById('inp-sleep').value),
                wake: parseFloat(document.getElementById('inp-wake').value),
                tidy: parseInt(document.getElementById('inp-tidy').value),
                study: document.getElementById('inp-study').value,
                noise: parseInt(document.getElementById('inp-noise').value),
                smoke: parseInt(document.getElementById('inp-smoke').value),
                guests: parseInt(document.getElementById('inp-guests').value),
                hobbies: getSelectedHobbies()
            }};

            const container = document.getElementById('ranking-container');
            container.innerHTML = '<div class="text-center py-10 text-slate-400 animate-pulse">Đang tính toán ma trận điểm và xếp hạng ứng viên...</div>';

            try {{
                const res = await fetch('/api/rank', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                if (res.status === 401) {{
                    window.location.href = '/login';
                    return;
                }}
                const data = await res.json();
                renderRankings(data);
            }} catch (err) {{
                container.innerHTML = `<div class="text-rose-400 p-4">Lỗi kết nối: ${{err.message}}</div>`;
            }}
        }}

        function renderRankings(data) {{
            const container = document.getElementById('ranking-container');
            const items = data.rankings.slice(0, 8); // Lấy Top 8

            document.getElementById('ranking-subtitle').innerText = 
                `Đã đối chiếu hồ sơ của "${{data.user.name}}" với các ứng viên KTX Nhóm ${{data.target_group}}`;

            if (items.length === 0) {{
                container.innerHTML = '<div class="text-center py-10 text-slate-400">Không tìm thấy ứng viên phù hợp trong nhóm đối diện.</div>';
                return;
            }}

            container.innerHTML = items.map((cand) => {{
                const rankNum = cand.rank;
                const isTop1 = rankNum === 1;
                const isTop2 = rankNum === 2;
                const isTop3 = rankNum === 3;

                let rankBadge = '';
                let cardBorder = 'border-slate-800 bg-slate-950/80';
                
                if (isTop1) {{
                    rankBadge = '<span class="px-3 py-1 bg-gradient-to-r from-amber-400 to-yellow-500 text-slate-950 font-black rounded-xl text-xs shadow-lg shadow-amber-500/20 flex items-center gap-1">🥇 HẠNG 1</span>';
                    cardBorder = 'border-amber-500/50 bg-gradient-to-b from-amber-950/20 to-slate-950 shadow-amber-500/10 shadow-2xl';
                }} else if (isTop2) {{
                    rankBadge = '<span class="px-3 py-1 bg-slate-300 text-slate-900 font-black rounded-xl text-xs flex items-center gap-1">🥈 HẠNG 2</span>';
                    cardBorder = 'border-slate-700 bg-slate-950';
                }} else if (isTop3) {{
                    rankBadge = '<span class="px-3 py-1 bg-amber-700/80 text-amber-200 font-black rounded-xl text-xs flex items-center gap-1">🥉 HẠNG 3</span>';
                    cardBorder = 'border-amber-800/40 bg-slate-950';
                }} else {{
                    rankBadge = `<span class="px-2.5 py-1 bg-slate-800 text-slate-400 font-extrabold rounded-xl text-xs">#${{rankNum}}</span>`;
                }}

                const scoreColor = cand.avg_score >= 75 ? 'text-emerald-400' : (cand.avg_score >= 60 ? 'text-sky-400' : (cand.avg_score >= 45 ? 'text-amber-400' : 'text-rose-400'));

                return `
                    <div class="border ${{cardBorder}} rounded-2xl p-5 transition hover:border-slate-700 space-y-3.5">
                        <div class="flex items-start justify-between gap-3">
                            <div class="flex items-center gap-3.5">
                                <div class="relative">
                                    <img src="${{cand.avatar}}" class="w-13 h-13 rounded-2xl bg-slate-900 border border-slate-800 p-0.5">
                                </div>
                                <div>
                                    <div class="flex items-center gap-2">
                                        ${{rankBadge}}
                                        <h3 class="text-base font-bold text-white">${{cand.name}}</h3>
                                    </div>
                                    <p class="text-xs text-slate-400 mt-0.5">${{cand.tagline}}</p>
                                    <div class="flex items-center gap-2 mt-1">
                                        <span class="text-[10px] bg-slate-800/80 px-2 py-0.5 rounded text-slate-300 font-medium">${{cand.major}}</span>
                                        <span class="text-[10px] bg-indigo-500/10 text-indigo-400 px-2 py-0.5 rounded font-medium">Nhóm ${{cand.group}}</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Score Badge -->
                            <div class="text-right shrink-0">
                                <div class="text-2xl font-black ${{scoreColor}}">${{cand.avg_score}}%</div>
                                <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-800/80 text-slate-300">
                                    ${{cand.tag}}
                                </span>
                            </div>
                        </div>

                        <!-- Mini metrics comparison -->
                        <div class="pt-2 border-t border-slate-800/60 flex flex-wrap items-center justify-between text-slate-300 text-[11px] gap-2">
                            <div class="flex flex-wrap gap-2">
                                <span class="bg-slate-800/80 px-2.5 py-1 rounded-lg">🌙 Ngủ: ${{cand.sleep >= 24 ? (cand.sleep - 24) + ':00 AM' : cand.sleep + ':00 PM'}}</span>
                                <span class="bg-slate-800/80 px-2.5 py-1 rounded-lg">⏰ Dậy: ${{cand.wake}}:00 AM</span>
                                <span class="bg-slate-800/80 px-2.5 py-1 rounded-lg">🧹 Gọn: ${{cand.tidy}}/5</span>
                                <span class="bg-slate-800/80 px-2.5 py-1 rounded-lg">🚭 Hút thuốc: ${{cand.smoke === 1 ? 'Có' : 'Không'}}</span>
                            </div>

                            <button onclick="toggleDetails(${{cand.id}})" class="text-indigo-400 hover:text-indigo-300 font-semibold underline text-xs">
                                Chi tiết tiêu chí ▼
                            </button>
                        </div>

                        <!-- Expandable Details -->
                        <div id="details-${{cand.id}}" class="hidden pt-3 border-t border-slate-800/80 space-y-2 text-xs">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                <div class="bg-emerald-950/20 border border-emerald-900/30 p-2.5 rounded-xl text-emerald-300 text-[11px]">
                                    <strong>✅ Điểm cộng tương thích:</strong><br>
                                    ${{cand.explanation.good.length > 0 ? cand.explanation.good.join(', ') : 'Không có tiêu chí nào nổi bật'}}
                                </div>
                                <div class="bg-rose-950/20 border border-rose-900/30 p-2.5 rounded-xl text-rose-300 text-[11px]">
                                    <strong>⚠️ Điểm cần lưu ý:</strong><br>
                                    ${{cand.explanation.bad.length > 0 ? cand.explanation.bad.join(', ') : 'Không có xung đột lớn'}}
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }}).join('');
        }}

        function toggleDetails(id) {{
            const el = document.getElementById('details-' + id);
            if (el) el.classList.toggle('hidden');
        }}

        window.onload = () => {{
            initUserValues();
        }};
    </script>
</body>
</html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
