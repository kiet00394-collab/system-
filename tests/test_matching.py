import random
from matching import gale_shapley, random_matching, count_blocking_pairs

def make_random_prefs(n, seed):
    rng = random.Random(seed)
    ids_a, ids_b = list(range(n)), list(range(n, 2 * n))
    pa = {a: rng.sample(ids_b, n) for a in ids_a}
    pb = {b: rng.sample(ids_a, n) for b in ids_b}
    return pa, pb

def test_gale_shapley_is_stable():
    for seed in range(50):
        pa, pb = make_random_prefs(20, seed)
        m = gale_shapley(pa, pb)
        assert len(m) == 20
        assert count_blocking_pairs(m, pa, pb) == 0

def test_random_usually_unstable():
    pa, pb = make_random_prefs(20, 1)
    assert count_blocking_pairs(random_matching(pa, pb, seed=1), pa, pb) > 0
    from matching import analyze_matching_quality, merge_pairs_into_rooms
import numpy as np

def test_analyze_matching_quality_perfect():
    """Kiểm tra thống kê chất lượng khi mọi sinh viên đều đạt nguyện vọng 1."""
    pa = {0: [2, 3], 1: [3, 2]}
    pb = {2: [0, 1], 3: [1, 0]}
    match = gale_shapley(pa, pb)
    stats = analyze_matching_quality(match, pa, pb)
    assert stats["avg_rank_a"] == 1.0
    assert stats["avg_rank_b"] == 1.0
    assert stats["top3_rate_a"] == 100.0

def test_merge_pairs_into_rooms_4():
    """Kiểm tra gộp các cặp 2 người thành phòng 4 người."""
    match = {0: 4, 1: 5, 2: 6, 3: 7}
    M = np.ones((8, 8)) * 75.0
    rooms = merge_pairs_into_rooms(match, M, room_size=4)
    assert len(rooms) == 2
    assert all(len(r) == 4 for r in rooms)