'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 9:53
desc: 通过正则表达式验证手机号码是否合法
    长度：11
    开头：156|158|188
    必须全部是数字
'''
import re

def validate_phone(phone):
    '''
    验证手机号码是否合法
    :param phone: 待验证的手机号码
    :return: 返回结果 True 合法   False 非法
    '''
    # 定义手机号码的规则
    reg = r'^(156|158|188)[0-9]{8}$'
    try:
        re.search(reg, phone)
        return True
    except:
        print("手机号码非法")
        return False


if __name__ == "__main__":
    p = input("输入手机号码：")

    res = validate_phone(p)

    print(res)