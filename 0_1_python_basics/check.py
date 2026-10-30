from practice import *


def run(label, fn):
    try:
        fn()
        print(f"PASS  {label}")
    except NotImplementedError:
        print(f"TODO  {label}")
    except AssertionError as e:
        print(f"FAIL  {label}: {e}")
    except Exception as e:
        print(f"ERROR {label}: {type(e).__name__}: {e}")


def t_a():
    assert top_be_names(candidates) == ["An", "Chi"], top_be_names(candidates)


def t_b():
    r = avg_by_role(candidates)
    assert set(r) == {"BE", "FE", "BA"}, r
    assert abs(r["BE"] - 7.0) < 1e-9 and r["FE"] == 6.0 and r["BA"] == 9.0, r


def t_c():
    assert has_below_6(candidates) is True
    assert has_below_6([{"name": "X", "role": "BE", "score": 6.0}]) is False


def t_count():
    r = count_words("The cat and the Hat and THE bat")
    assert r == {"the": 3, "cat": 1, "and": 2, "hat": 1, "bat": 1}, r


def t_top2():
    r = top_2_words("The cat and the Hat and THE bat")
    assert r == [("the", 3), ("and", 2)], r


def t_good():
    assert add_item_good(1) == [1]
    assert add_item_good(2) == [2], "list bị dùng chung giữa các lần gọi!"
    mine = [9]
    assert add_item_good(3, mine) == [9, 3]


run("0.1.1a top_be_names", t_a)
run("0.1.1b avg_by_role", t_b)
run("0.1.1c has_below_6", t_c)
run("0.1.2a count_words", t_count)
run("0.1.2a top_2_words", t_top2)
run("0.1.2b add_item_good", t_good)

print("\nBẫy mặc định (đọc kết quả rồi giải thích vì sao):")
print(add_item_bad("a"), add_item_bad("b"))
