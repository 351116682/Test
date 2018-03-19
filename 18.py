#coding=utf-8
'''
按逗号分隔列表。
'''

def devide_list(list):
    return ','.join(str(item) for item in list)

if __name__ == "__main__":
    list = [1,2,3,4,5,6,7]
    print devide_list(list)