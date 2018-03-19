#coding=utf-8
'''
取一个整数a从右端开始的4〜7位。
'''


# 将所给的数字分解，取后四位
def split1(number):
    number = str(number)
    result = []
    length = len(number) - 1
    index = length - 3
    while index <= length:
        result.append(number[index])
        index += 1
    return ''.join(char for char in result)


def split2(number):
        return int(number) % (10000)


if __name__ == "__main__":
    number = 1234567890
    print split1(number)
    print split2(number)
    str_num = str(1234567)
    print split2(str_num)