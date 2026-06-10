"""Problem Set 5 — Recursion & HTTP / APIs"""


# ── Problem 1 ─────────────────────────────────────────────────────────────────
def recursive_squares(num: int) -> list[int]:
    # base cases
    if num == 0:
        return []
    if num == 1:
        return [1]

    # recursive step
    childs_list = recursive_squares(num - 1)
    
    # add our number to child's
    square = num ** 2
    childs_list.append(square)

    return childs_list