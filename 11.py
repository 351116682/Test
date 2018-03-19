#coding=utf-8
'''
 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
 '''

def fenjie(number):
    ls = []
    i = 2
    while True:
        if number % i == 0:
            ls.append(i)
            number = number/i
            if number / i == 1:
                ls.append(number)
                break
        else:
            i += 1
        if number / i == 1:
            ls.append(number)
            break

    return ls

if __name__ == "__main__":
    num = int(raw_input('请输入一个数字：\n'))
    print "%d的所有质因数是：%d" % (num,num),
    for item in fenjie(num):
        print item,'*',