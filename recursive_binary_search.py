def binary_search(array, num):
    return search(array, num, 0, len(array) - 1)


def search(array, num, min, max):
    if min > max:
        return -1
    else:
        mid = (min + max) // 2
    if array[mid] == num:
      if mid != (len(array)-1):
        if array[mid+1] == array[mid]:
          return int(mid - 1)
        else:
          return mid
      else:
        return mid
    elif array[mid] > num:
        return search(array, num, min, mid - 1)
    else:
        return search(array, num, mid + 1, max)


def main():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    print(a)
    for n in [2]:
        print("%5d index? %d" % (n, binary_search(a, n)))


def test_last():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
    assert binary_search(a, 3) == 9


def test_first():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert binary_search(a, 2) == 3

def test_first1():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    assert binary_search(a, 1) == 0


main()
