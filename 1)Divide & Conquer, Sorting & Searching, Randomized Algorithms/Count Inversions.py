#Uses IntegerArray.txt

def merge_and_count_split(arrB, arrC):
    i=0
    j=0
    count =0
    arrD = []
    for k in range(len(arrB)+len(arrC)):
        if arrB[i] < arrC[j]:
            arrD.append(arrB[i])
            i += 1
        else:
            arrD.append(arrC[j])
            j += 1
            count += len(arrB)-i
        if i == len(arrB):
            arrD += arrC[j:]
            break
        elif j == len(arrC):
            arrD += arrB[i:]
            break

    return (arrD, count)


def sort_and_count(arr):
    if len(arr) == 1:
        return (arr,0)

    (arrB, countL) = sort_and_count(arr[ : len(arr)//2])
    (arrC, countR) = sort_and_count(arr[len(arr)//2 : ])
    (arrD, countS) = merge_and_count_split(arrB, arrC)

    return (arrD, countL+countR+countS)



if __name__ == '__main__':
    f = open("IntegerArray.txt", "r")
    arr = [int(x) for x in f]

    #arr = [1,3,5,2,4,6]

    (newArr, count) = sort_and_count(arr)
    print(count)