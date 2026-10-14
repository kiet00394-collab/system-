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