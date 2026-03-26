from collections import deque
import time


def custom_remove(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            del lst[i]
            return
    raise ValueError(f"list.remove(x): x not in list")


def custom_items(d):
    result = []
    for key in d:
        result.append((key, d[key]))
    return result


def custom_intersection(s, *others):
    result = set()
    for item in s:
        in_all = True
        for other in others:
            if item not in other:
                in_all = False
                break
        if in_all:
            result.add(item)
    return result


def custom_index(s, sub, start=0, end=None):
    if end is None:
        end = len(s)
    sub_len = len(sub)
    for i in range(start, end - sub_len + 1):
        if s[i:i + sub_len] == sub:
            return i
    raise ValueError("substring not found")


def custom_copy(dq):
    new_dq = deque()
    for item in dq:
        new_dq.append(item)
    return new_dq


def run_examples():
    print("--- ПРИКЛАДИ ВИКОНАННЯ ---")

    print("\n1. custom_remove:")
    l1 = [1, 2, 3, 4, 5];
    custom_remove(l1, 3);
    print("Приклад 1:", l1)
    l2 = ['a', 'b', 'c', 'b'];
    custom_remove(l2, 'b');
    print("Приклад 2:", l2)
    l3 = [10.5, 20.1, 30.0];
    custom_remove(l3, 10.5);
    print("Приклад 3:", l3)
    l4 = [[1], [2], [3]];
    custom_remove(l4, [2]);
    print("Приклад 4:", l4)
    l5 = [True, False, True];
    custom_remove(l5, False);
    print("Приклад 5:", l5)
    try:
        custom_remove([1, 2], 3)
    except ValueError as e:
        print("Приклад 6 (Помилка):", e)

    print("\n2. custom_items:")
    print("Приклад 1:", custom_items({'a': 1, 'b': 2}))
    print("Приклад 2:", custom_items({1: 'one', 2: 'two'}))
    print("Приклад 3:", custom_items({}))
    print("Приклад 4:", custom_items({'x': [1, 2], 'y': [3, 4]}))
    print("Приклад 5:", custom_items({True: 100, False: 0}))

    print("\n3. custom_intersection:")
    print("Приклад 1:", custom_intersection({1, 2, 3}, {2, 3, 4}))
    print("Приклад 2:", custom_intersection({'a', 'b'}, {'b', 'c'}, {'b', 'd'}))
    print("Приклад 3:", custom_intersection({1, 2}, {3, 4}))
    print("Приклад 4:", custom_intersection(set(), {1, 2}))
    print("Приклад 5:", custom_intersection({1, 2, 3}, {1, 2, 3}))

    print("\n4. custom_index:")
    print("Приклад 1:", custom_index("hello world", "world"))
    print("Приклад 2:", custom_index("banana", "na"))
    print("Приклад 3:", custom_index("banana", "na", 3))
    print("Приклад 4:", custom_index("abracadabra", "cad"))
    print("Приклад 5:", custom_index("test", "t", 1))
    try:
        custom_index("python", "java")
    except ValueError as e:
        print("Приклад 6 (Помилка):", e)

    print("\n5. custom_copy:")
    d1 = deque([1, 2, 3]);
    c1 = custom_copy(d1);
    print("Приклад 1:", c1, "| ID різні:", id(d1) != id(c1))
    d2 = deque(['a', 'b']);
    c2 = custom_copy(d2);
    print("Приклад 2:", c2)
    d3 = deque();
    c3 = custom_copy(d3);
    print("Приклад 3:", c3)
    d4 = deque([True, False]);
    c4 = custom_copy(d4);
    print("Приклад 4:", c4)
    d5 = deque([10.5, 20.5]);
    c5 = custom_copy(d5);
    print("Приклад 5:", c5)


def run_benchmarks():
    print("\n--- БЕНЧМАРКИ (Очікуємо виконання стандартного методу ~0.1с) ---")

    N_list = 30_000_000
    print(f"\nГенеруємо список з {N_list} елементів...")
    test_list1 = list(range(N_list)) + [-1]
    test_list2 = list(range(N_list)) + [-1]

    start = time.perf_counter()
    test_list1.remove(-1)
    t_std = time.perf_counter() - start
    print(f"Стандартний list.remove: {t_std:.4f} сек")

    start = time.perf_counter()
    custom_remove(test_list2, -1)
    t_cust = time.perf_counter() - start
    print(f"Аматорський custom_remove: {t_cust:.4f} сек")

    N_str = 50_000_000
    print(f"\nГенеруємо рядок з {N_str} символів...")
    test_str = "a" * N_str + "b"

    start = time.perf_counter()
    test_str.index("b")
    t_std = time.perf_counter() - start
    print(f"Стандартний str.index: {t_std:.4f} сек")

    start = time.perf_counter()
    custom_index(test_str, "b")
    t_cust = time.perf_counter() - start
    print(f"Аматорський custom_index: {t_cust:.4f} сек")


    N_dict = 3_000_000
    print(f"\nГенеруємо словник з {N_dict} елементів...")
    test_dict = {i: i for i in range(N_dict)}

    start = time.perf_counter()
    _ = list(test_dict.items())
    t_std = time.perf_counter() - start
    print(f"Стандартний dict.items: {t_std:.4f} сек")

    start = time.perf_counter()
    _ = custom_items(test_dict)
    t_cust = time.perf_counter() - start
    print(f"Аматорський custom_items: {t_cust:.4f} сек")


if __name__ == "__main__":
    run_examples()
    run_benchmarks()