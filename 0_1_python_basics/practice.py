"""Bài 0.1: Python cho dev C# — tự điền vào các chỗ TODO rồi chạy: python3 check.py"""

candidates = [
    {"name": "An", "role": "BE", "score": 8.5},
    {"name": "Bình", "role": "FE", "score": 6.0},
    {"name": "Chi", "role": "BE", "score": 7.0},
    {"name": "Dũng", "role": "BA", "score": 9.0},
    {"name": "Em", "role": "BE", "score": 5.5},
]


# ---- Bài 0.1.1 (a): tên ứng viên BE có điểm >= 7, sắp xếp điểm giảm dần ----
def top_be_names(cands: list[dict]) -> list[str]:
    # Gợi ý: sorted(..., key=..., reverse=True) + comprehension
    return [d["name"] for d in sorted([c for c in cands if c["score"]>=7 and c["role"]=="BE"], key= lambda c: c["score"], reverse=True)]


# ---- Bài 0.1.1 (b): điểm trung bình theo từng role -> dict ----
def avg_by_role(cands: list[dict]) -> dict[str, float]:
    # Gợi ý: gom điểm theo role vào dict rồi tính trung bình
    groups = {}
    for c in cands:
        role = c["role"]
        if role not in groups:
            groups[role] = []
        groups[role].append(c["score"])
    result =  {}
    for role, scores in groups.items():
        result[role] = sum(scores)/len(scores)
    return result


# ---- Bài 0.1.1 (c): có ứng viên nào dưới 6 điểm không? ----
def has_below_6(cands: list[dict]) -> bool:
    # Gợi ý: any(... for ...)
    return any(x["score"]<6 for x in cands)


# ---- Bài 0.1.2 (a): đếm từ, không phân biệt hoa thường ----
def count_words(text: str) -> dict[str, int]:
    # Gợi ý: text.lower().split(), dict.get(w, 0) + 1
    count = {}
    for w in text.lower().split():
        count[w]= count.get(w, 0) + 1
    return count


def top_2_words(text: str) -> list[tuple[str, int]]:
    # Gợi ý: sorted(counts.items(), key=..., reverse=True)[:2]
    return sorted(count_words(text).items(), key= lambda c:c[1], reverse=True)[:2]


# ---- Bài 0.1.2 (b): sửa bẫy tham số mặc định ----
def add_item_bad(item, bucket=[]):
    bucket.append(item)
    return bucket


def add_item_good(item, bucket=None):
    # Gợi ý: dùng None làm mặc định, tạo list mới bên trong hàm
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
