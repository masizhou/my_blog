"""
二分查找：递归实现
"""
def binarySearch(alist, item):
    if len(alist) == 0:  # 边界条件
        return False
    else:

        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            return binarySearch(alist[midpoint+1:], item) # 一定要记得减小规模
        else:
            return binarySearch(alist[:midpoint], item)  # 减小规模

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))  # False
print(binarySearch(testlist, 13))  # True