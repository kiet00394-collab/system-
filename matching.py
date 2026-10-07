import random

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