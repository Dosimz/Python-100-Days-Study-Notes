def select_sort(origin_items, comp=lambda x, y: x < y):
    """
    简单选择排序(从小到大排列)
    依次选出每个位置的最小数
    """
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

print(select_sort([4,1,7,2,9,3,5,4]))