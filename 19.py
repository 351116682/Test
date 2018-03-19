#coding=utf-8
'''
将一个数组逆序输出。
'''

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr

if __name__ == "__main__":
    arr = ['1',2,3,'Hello']
    arr = reverse_array(arr)
    print arr