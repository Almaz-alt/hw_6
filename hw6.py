def bubble_sort(arr):
    """
    Функция сортировки списка методом пузырьковой сортировки.
    :param arr: несортированный список
    :return: отсортированный список
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Обмен элементов
    return arr


def binary_search(target, arr):
    """
    Функция для поиска элемента в отсортированном списке методом двоичного поиска.
    :param target: элемент для поиска
    :param arr: отсортированный список
    :return: None
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Элемент {target} не найден в списке.")


# Пример использования функций
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

# Поиск элемента в отсортированном списке
binary_search(23, sorted_list)
binary_search(99, sorted_list)
