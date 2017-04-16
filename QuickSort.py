def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]

def partition(lst, p, r):
    if p > r:
        return

    if r - p == 1:
        if lst[p] > lst[r]:
            lst[p], lst[r] = lst[r], lst[p]
        return

    oldP = p
    oldR = r

    # tmpLst = lst
    tmpLst = lst[:]
    prior = r
    lstLeft = p
    lstRight = r
    r -= 1

    while p <= r:
        if tmpLst[p] < tmpLst[prior]:
            lst[lstLeft] = tmpLst[p]
            lstLeft += 1
        elif tmpLst[p] > tmpLst[prior]:
            lst[lstRight] = tmpLst[p]
            lstRight -= 1
        p += 1

    lst[lstLeft] = tmpLst[prior]
    print(lst)

    posMid = lstLeft
    print('posmid',posMid)
    print('part1', oldP, posMid-1)
    print('part2', posMid+1, oldR)
    # do left
    partition(lst, oldP, posMid-1)
    # do right
    partition(lst, posMid+1, oldR)



def quickSort(lst):
    arrLen = len(lst)
    p = 0
    r = arrLen - 1





if __name__ == '__main__':
    # a = [3,1,2]
    # partition(a, 0, 2)
    # print(a)


    a = [9,2,4,1,3,7,9,8,6]
    partition(a, 0, len(a)-1)
    print('end',a)