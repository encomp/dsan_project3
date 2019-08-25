class HeapSort:

    @staticmethod
    def heap_sort(array):
        for i in range(len(array)):
            HeapSort.__heapify_up(array, i)
        for i in range(len(array) - 1, 0, -1):
            tmp = array[0]
            array[0] = array[i]
            array[i] = tmp
            HeapSort.__heapify_down(array, i - 1)
        if array[0] > array[1]:
            tmp = array[0]
            array[0] = array[1]
            array[1] = tmp

    @staticmethod
    def __heapify_up(arr, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        while parent >= 0 and arr[parent] < arr[index]:
            tmp = arr[index]
            arr[index] = arr[parent]
            arr[parent] = tmp
            index = parent
            parent = (index - 1) // 2
        return

    @staticmethod
    def __heapify_down(arr, limit):
        if limit == 0:
            return
        index = 0
        left = 1
        right = 2
        while left <= limit and right <= limit and (arr[index] < arr[left] or arr[index] < arr[right]):
            tmp = arr[index]
            if arr[left] > arr[right]:
                arr[index] = arr[left]
                index = left
            else:
                arr[index] = arr[right]
                index = right
            arr[index] = tmp
            left = 2 * index + 1
            right = 2 * index + 2
