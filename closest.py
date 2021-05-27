#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    tups = zip(x, y)
    sorted_tups = sorted(tups)
    x, y = zip(*sorted_tups)
    x, y = list(x), list(y)
    return divide_conquer(x, y, 0, len(x))

def divide_conquer(x, y, left, right):
    if right - left <= 3:
        tups = zip(x[left:right], y[left:right])
        sorted_tups = sorted(tups, key=lambda s: s[1])
        l, m = zip(*sorted_tups)
        x[left:right], y[left:right] = list(l), list(m)
        return closest(x, y, left, right)
    mid = (left + right)//2
    dl = divide_conquer(x, y, left, mid)
    dr = divide_conquer(x, y, mid, right)
    d = min(dl, dr)
    x, y = merge(x, y, left, right)
    stripx = []
    stripy = []
    for i in range(left, right):
        if abs(x[i] - x[mid] < d):
            stripx.append(x[i])
            stripy.append(y[i])
    d_strip = closest(stripx, stripy, 0, len(stripx))
    if d_strip == None:
        return d
    else:
        return min(d, d_strip)

def closest(x, y, left, right):
    d = None
    for i in range(left, right):
        j = i + 1
        while j < min(i + 8, right):
            if d == None:
                d = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            else:
                d = min(d, math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2))
            j += 1
    return d

def merge(x, y, left, right):
    a = (right-left)*[0]
    b = (right-left)*[0]
    mid = (left + right)//2
    i, j = left, mid
    while i < mid and j < right:
        if y[i] <= y[j]:
            b[i + j - mid - left] = y[i]
            a[i + j - mid - left] = x[i]
            i += 1
        else:
            b[i + j - mid - left] = y[j]
            a[i + j - mid - left] = x[j]
            j += 1
        if i == mid:
            b[i + j - mid - left:right - left] = y[j:right]
            a[i + j - mid - left:right - left] = x[j:right]
        elif j == right:
            b[i + j - mid - left:right - left] = y[i:mid]
            a[i + j - mid - left:right - left] = x[i:mid]
    y[left:right] = b[:]
    x[left:right] = a[:]
    return x, y

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
