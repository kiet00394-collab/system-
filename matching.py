import random
import time

def gale_shapley(pref_a: dict[int, list[int]], pref_b: dict[int, list[int]]) -> dict[int, int]:
    """Ghép ổn định Gale-Shapley. Trả về {id_A: id_B}. A là bên đề nghị."""
    rank_b = {b: {a: r for r, a in enumerate(lst)} for b, lst in pref_b.items()}
    free = list(pref_a.keys())              # những A chưa có cặp
    nxt = {a: 0 for a in pref_a}            # A đang định đề nghị người thứ mấy
    engaged = {}                            # {b: a}

    while free:
        a = free.pop(0)
        if nxt[a] >= len(pref_a[a]):        # A hết người để thử -> không có cặp
            continue
        b = pref_a[a][nxt[a]]
        nxt[a] += 1

        if b not in engaged:
            engaged[b] = a
        elif rank_b[b][a] < rank_b[b][engaged[b]]:   # b thích a hơn người hiện tại
            free.append(engaged[b])
            engaged[b] = a
        else:
            free.append(a)                  # bị từ chối, thử người kế tiếp sau

    return {a: b for b, a in engaged.items()}

def random_matching(pref_a: dict[int, list[int]], pref_b: dict[int, list[int]], seed=None) -> dict[int, int]:
    """Ghép ngẫu nhiên để đối chứng."""
    rng = random.Random(seed)
    a_ids = list(pref_a.keys())
    b_ids = list(pref_b.keys())
    rng.shuffle(b_ids)
    return dict(zip(a_ids, b_ids))

def count_blocking_pairs(match: dict[int, int], pref_a: dict[int, list[int]], pref_b: dict[int, list[int]]) -> int:
    """Đếm số cặp chặn. Trả về 0 nghĩa là ổn định tuyệt đối."""
    rank_a = {a: {b: r for r, b in enumerate(l)} for a, l in pref_a.items()}
    rank_b = {b: {a: r for r, a in enumerate(l)} for b, l in pref_b.items()}
    partner_of_b = {b: a for a, b in match.items()}
    
    count = 0
    for a in pref_a:
        for b in pref_b:
            if match.get(a) == b:
                continue
            a_prefers = a not in match or rank_a[a][b] < rank_a[a][match[a]]
            b_prefers = b not in partner_of_b or rank_b[b][a] < rank_b[b][partner_of_b[b]]
            if a_prefers and b_prefers:
                count += 1
    return count

def merge_pairs_into_rooms(match: dict[int, int], M, room_size=4) -> list[list[int]]:
    """Gộp 2 cặp thành phòng 4. Điểm giữa 2 cặp = trung bình 4 điểm chéo."""
    pairs = list(match.items())
    def pair_sim(p, q):
        return sum(M[x][y] for x in p for y in q) / 4
    rooms, used = [], set()
    cand = sorted(((pair_sim(p, q), i, j)
                   for i, p in enumerate(pairs) for j, q in enumerate(pairs) if i < j),
                  reverse=True)
    for _, i, j in cand:
        if i not in used and j not in used:
            rooms.append(list(pairs[i]) + list(pairs[j]))
            used.update((i, j))
    rooms += [list(pairs[i]) for i in range(len(pairs)) if i not in used]
    return rooms

def make_random_prefs(n_per_group: int, seed: int = 0) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """Tạo danh sách ưu tiên ngẫu nhiên cho n_per_group sinh viên nhóm A và n_per_group nhóm B."""
    rng = random.Random(seed)
    ids_a = list(range(n_per_group))
    ids_b = list(range(n_per_group, 2 * n_per_group))
    pa = {a: rng.sample(ids_b, n_per_group) for a in ids_a}
    pb = {b: rng.sample(ids_a, n_per_group) for b in ids_b}
    return pa, pb

def run_benchmark(student_totals: list[int] = [100, 200, 400, 1000], seeds: int = 5) -> dict[int, float]:
    """
    Đo thời gian thực thi thuật toán Gale-Shapley (Bước A6 - NFR-01).
    student_totals: Tổng số sinh viên (chia đều cho 2 nhóm A và B).
    """
    results = {}
    for total in student_totals:
        n_group = total // 2
        total_time = 0.0
        for s in range(seeds):
            pa, pb = make_random_prefs(n_group, seed=s)
            t0 = time.perf_counter()
            gale_shapley(pa, pb)
            total_time += (time.perf_counter() - t0)
        results[total] = round(total_time / seeds, 5)
    return results
    def analyze_matching_quality(match: dict[int, int], pref_a: dict[int, list[int]], pref_b: dict[int, list[int]]) -> dict[str, float]:
    """
    Thống kê chất lượng phép ghép (Bước A7 - Báo cáo phân tích):
    - Thứ hạng ưu tiên trung bình của nhóm A và nhóm B (1 là nguyện vọng 1).
    - Tỷ lệ % sinh viên đạt được Top 3 nguyện vọng đầu tiên.
    """
    if not match:
        return {"avg_rank_a": 0.0, "avg_rank_b": 0.0, "top3_rate_a": 0.0, "top3_rate_b": 0.0}

    ranks_a = []
    ranks_b = []
    for a, b in match.items():
        r_a = pref_a[a].index(b) + 1 if b in pref_a[a] else len(pref_a[a])
        r_b = pref_b[b].index(a) + 1 if a in pref_b[b] else len(pref_b[b])
        ranks_a.append(r_a)
        ranks_b.append(r_b)

    n = len(match)
    return {
        "avg_rank_a": round(sum(ranks_a) / n, 2),
        "avg_rank_b": round(sum(ranks_b) / n, 2),
        "top3_rate_a": round(sum(1 for r in ranks_a if r <= 3) * 100.0 / n, 1),
        "top3_rate_b": round(sum(1 for r in ranks_b if r <= 3) * 100.0 / n, 1),
    }