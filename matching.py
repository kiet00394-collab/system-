import random

def gale_shapley(pref_a: dict[int, list[int]], pref_b: dict[int, list[int]]) -> dict[int, int]:
    """Ghép ổn định Gale-Shapley. Trả về {id_A: id_B}. A là bên đề nghị."""
    rank_b = {b: {a: r for r, a in enumerate(lst)} for b, lst in pref_b.items()}
    free = list(pref_a.keys())              
    nxt = {a: 0 for a in pref_a}            
    engaged = {}                           

    while free:
        a = free.pop(0)
        if nxt[a] >= len(pref_a[a]):       
            continue
        b = pref_a[a][nxt[a]]
        nxt[a] += 1

        if b not in engaged:
            engaged[b] = a
        elif rank_b[b][a] < rank_b[b][engaged[b]]:  
            free.append(engaged[b])
            engaged[b] = a
        else:
            free.append(a)                  
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