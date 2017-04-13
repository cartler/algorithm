
def mergeSort():
    pass

def mergeSortRecursive(arr, start, end):
    arrLen = (end - start) + 1

    print('enter func ', start, end, arrLen)

    if arrLen <= 1:
        print('arrlen = 1')
    elif arrLen == 2:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
        print('arrlen = 2')
    else:
        posMid = int((start + end + 1)/2)
        print('mid ', posMid)
        print('part1 ', start, posMid-1)
        print('part2 ', posMid, end)
        # do left
        mergeSortRecursive(arr, start, posMid-1)
        mergeSortRecursive(arr, posMid, end)

        print('------------------')
        print('return func ', start, end, arrLen)
        merge(arr, start, end, posMid)


    print(arr)

def merge(arr, start, end, mid):
    start1 = start
    end1 = mid-1
    start2 = mid
    end2 = end

    tmpArr = arr[:]

    iterRange = list(range(start, end+1))
    print('iterRange:', iterRange)
    for iter in iterRange:
        if start1 > end1:
            arr[iter] = tmpArr[start2]
            start2 += 1
            continue

        if start2 > end2:
            arr[iter] = tmpArr[start1]
            start1 += 1
            continue

        if tmpArr[start1] < tmpArr[start2]:
            arr[iter] = tmpArr[start1]
            start1 += 1
        else:
            arr[iter] = tmpArr[start2]
            start2 += 1


if __name__ == '__main__':
    # arr = [2,3,1,4,5,7]
    # merge(arr, 0 , 3, 2)
    # print(arr)

    # arr = [3,2,4,1,5,9,6,8,7]
    arr = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
    print('origin:', arr)
    mergeSortRecursive(arr, 0, len(arr)-1)
    print('end sort:', arr)


# def mergesort(seq):
#     if len(seq) <= 1:
#         return seq
#     mid = int(len(seq) / 2)
#     left = mergesort(seq[:mid])
#     right = mergesort(seq[mid:])
#     return merge(left, right)
#
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result += left[i:]
#     result += right[j:]
#     return result
#
#
# if __name__ == '__main__':
#     seq = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
#     print(mergesort(seq))