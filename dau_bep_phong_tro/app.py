import random
import uuid
from collections import Counter
from flask import Flask, jsonify, request, render_template, session
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.secret_key = "doi-chuoi-nay-thanh-mot-chuoi-bi-mat-bat-ky"

NGAY_THANG = 15          # sống sót đủ 15 ngày là thắng
MAU_MAX = 100
TIEN_MOI_NGAY = 25       # tiền gia đình gửi / làm thêm mỗi ngày (nghìn đồng)

# ---------- Cấu trúc dữ liệu ----------
GIA_GOC = {"gao": 10, "trung": 5, "ca_rot": 4, "mi_goi": 3, "thit": 20, "rau": 4}
TEN = {"gao": "Gạo", "trung": "Trứng", "ca_rot": "Cà rốt",
       "mi_goi": "Mì gói", "thit": "Thịt", "rau": "Rau"}
ICON = {"gao": "🍚", "trung": "🥚", "ca_rot": "🥕",
        "mi_goi": "🍜", "thit": "🍖", "rau": "🥬"}

# Công thức: tuple nguyên liệu đã sắp xếp -> (tên món, máu hồi)
CONG_THUC = {
    tuple(sorted(["mi_goi", "trung"])): ("Mì trứng", 25),
    tuple(sorted(["gao", "trung"])): ("Cơm trứng", 30),
    tuple(sorted(["trung", "rau"])): ("Trứng xào rau", 20),
    tuple(sorted(["mi_goi", "rau"])): ("Mì xào rau", 20),
    tuple(sorted(["gao", "ca_rot", "thit"])): ("Cơm thịt xào cà rốt", 40),
    tuple(sorted(["gao", "thit", "rau"])): ("Cơm thịt rau", 45),
}

GAMES = {}   # mỗi người chơi (session) có một ván riêng


def moi_game():
    return {
        "tien": 60, "mau": MAU_MAX, "ngay": 1,
        "tu_lanh": {"gao": 1, "trung": 2, "ca_rot": 0, "mi_goi": 2, "thit": 0, "rau": 0},
        "gia": dict(GIA_GOC),
        "over": False, "thang": False,
        "log": "Chào mừng đến phòng trọ! Sống sót 15 ngày nhé.",
        "su_kien": None,
    }


def get_game():
    sid = session.get("sid")
    if sid not in GAMES:
        sid = uuid.uuid4().hex
        session["sid"] = sid
        GAMES[sid] = moi_game()
    return GAMES[sid]


state = LocalProxy(get_game)   # các hàm bên dưới vẫn dùng state như cũ


def kiem_tra_game_over():
    if state["mau"] <= 0:
        state["mau"] = 0
        state["over"], state["thang"] = True, False
        state["log"] = "Bạn kiệt sức vì đói. Game over!"
    elif state["ngay"] > NGAY_THANG:
        state["over"], state["thang"] = True, True
        state["log"] = f"Bạn đã sống sót qua {NGAY_THANG} ngày. Đầu bếp phòng trọ thực thụ!"


def su_kien_moi_ngay():
    ev = random.choice(["gia_gao", "hong_tu_lanh", "roi_vi", "nhat_tien", "me_gui", None, None])
    if ev == "gia_gao":
        state["gia"]["gao"] = min(state["gia"]["gao"] + 5, 30)
        return "📈 Giá gạo tăng thêm 5k/kg!"
    if ev == "hong_tu_lanh":
        mat = min(2, state["tu_lanh"]["trung"])
        state["tu_lanh"]["trung"] -= mat
        return f"🧊 Tủ lạnh hỏng, bạn mất {mat} quả trứng."
    if ev == "roi_vi":
        mat = min(20, state["tien"])
        state["tien"] -= mat
        return f"👛 Rơi ví! Mất {mat}k."
    if ev == "nhat_tien":
        state["tien"] += 15
        return "🍀 Nhặt được 15k dưới gầm giường."
    if ev == "me_gui":
        state["tu_lanh"]["mi_goi"] += 2
        return "📦 Mẹ gửi lên 2 gói mì."
    return None


def di_ngu():
    state["ngay"] += 1
    state["mau"] -= 15
    state["tien"] += TIEN_MOI_NGAY
    state["su_kien"] = None
    kiem_tra_game_over()
    if not state["over"]:
        state["su_kien"] = su_kien_moi_ngay()
        state["log"] = f"Sang ngày {state['ngay']}. Đói thêm rồi, -15 máu, +{TIEN_MOI_NGAY}k."


def di_cho(nl, sl):
    if nl not in state["gia"] or sl < 1:
        return "Hàng không hợp lệ."
    tong = state["gia"][nl] * sl
    if tong > state["tien"]:
        return f"Không đủ tiền! Cần {tong}k, bạn chỉ có {state['tien']}k."
    state["tien"] -= tong
    state["tu_lanh"][nl] += sl
    return f"Đã mua {sl} {TEN[nl]} hết {tong}k."


def nau_an(ds):
    dem = Counter(ds)
    if not ds:
        return "Chảo còn trống!"
    for nl, c in dem.items():
        if state["tu_lanh"].get(nl, 0) < c:
            return f"Tủ lạnh không đủ {TEN.get(nl, nl)}!"
    for nl, c in dem.items():
        state["tu_lanh"][nl] -= c
    mon = CONG_THUC.get(tuple(sorted(ds)))
    if mon:
        state["mau"] = min(MAU_MAX, state["mau"] + mon[1])
        return f"Ngon! {mon[0]} giúp bạn hồi {mon[1]} máu."
    state["mau"] -= 10
    kiem_tra_game_over()
    return "Món hỏng! Ăn xong đau bụng, -10 máu."


# ---------- API ----------
def phan_hoi(thong_bao=None):
    if thong_bao:
        state["log"] = thong_bao
    return jsonify({**state, "ten": TEN, "icon": ICON})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def api_state():
    return phan_hoi()


@app.route("/api/mua", methods=["POST"])
def api_mua():
    if state["over"]:
        return phan_hoi()
    d = request.get_json()
    return phan_hoi(di_cho(d.get("nl"), int(d.get("sl", 1))))


@app.route("/api/nau", methods=["POST"])
def api_nau():
    if state["over"]:
        return phan_hoi()
    return phan_hoi(nau_an(request.get_json().get("ds", [])))


@app.route("/api/ngu", methods=["POST"])
def api_ngu():
    if not state["over"]:
        di_ngu()
    return phan_hoi()


@app.route("/api/reset", methods=["POST"])
def api_reset():
    get_game()
    GAMES[session["sid"]] = moi_game()
    return phan_hoi()


if __name__ == "__main__":
    app.run(debug=True)
