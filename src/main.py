def search(number: int, sorted_list: list) -> bool:
    left, right = 0, len(sorted_list) - 1
    # можно было сделать намного проще, но попросили сложность алгоритма O(log n)
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == number:
            return True
        elif sorted_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return False


list_numbers = [1, 2, 3, 45, 356, 569, 600, 705, 923]

print(search(3, list_numbers))
