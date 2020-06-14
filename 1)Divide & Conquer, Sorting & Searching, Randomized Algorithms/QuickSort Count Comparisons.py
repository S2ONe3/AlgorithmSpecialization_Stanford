from random import sample

def swap(arr, index1, index2):
    if index1 == index2:
        return

    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return

def MO3(arr, start, end):
    first = arr[start]
    mid = arr[(start + end - 1) // 2]
    last = arr[end - 1]

    if (first > mid):
        if (first > last):
            if (mid > last):
                return (start + end - 1) // 2
            else:
                return end - 1
        else:
            return start
    else:
        if (last > first):
            if (last > mid):
                return (start + end - 1) // 2
            else:
                return end - 1
        else:
            return start


def ChoosePivot(arr, start, end, method = ''):
    if method == 'first':
        return
    if method == 'last':
        swap(arr,start, end-1)
        return
    if method == 'mo3':
        pivotIdx = MO3(arr, start, end)
        swap(arr, start, pivotIdx)
        return
    else:
        pass



#assumes that the pivot is in the 1st position
def Partition(arr, start, end):
    pivot = arr[start]
    i = start+1

    for j in range(start+1, end):
        if arr[j] < pivot:
            swap(arr, j, i)
            i += 1

    swap(arr, start, i-1)
    return i-1



def QuickSort(arr, start, end):
    if len(arr[start:end]) <= 1:
        return

    global count
    count += len(arr[start:end])-1

    ChoosePivot(arr, start, end, 'mo3')
    pivotIdx = Partition(arr, start, end)
    QuickSort(arr, start, pivotIdx)
    QuickSort(arr, pivotIdx+1, end)

if __name__ == '__main__':
    f = open('QuickSort.txt', 'r')
    arr = [int(x) for x in f]

    count =0
    QuickSort(arr, 0, len(arr))

    print(count)