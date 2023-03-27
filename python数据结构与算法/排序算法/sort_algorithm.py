def bubble_sort(li):
    """
    冒泡排序
    """
    n = len(li)
    for i in range(n):
        exchange = False
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j+1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li
    return li


def select_sort(li):
    """
    选择排序
    """
    pass

if __name__ == "__main__":
    a = [90, 19, 29, 100, 40]
    print(bubble_sort(a))
            