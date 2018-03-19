#coding=utf-8
'''
输入三个整数x,y,z，请把这三个数由小到大输出。

'''

ls = [1,3,6,2,4,8,7,9,0]

target = []

for item in ls:
    target.append(item)
    target.sort()
    print target

print '输入的数据由大到小的顺序为：\n',target