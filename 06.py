#coding=utf-8
'''
输出9*9乘法口诀表。
'''

for x in range(1,10):
    for y in range(1,x + 1):
        print "%d * %d = %d\t"%(x,y,x*y),
    print '\n'