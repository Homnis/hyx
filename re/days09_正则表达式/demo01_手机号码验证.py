'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 9:45
desc: 需求：验证用户输入的手机号码是否合法
'''
def validate_phone(phone):
    '''
    验证手机号码是否合法的函数
        长度->开头->数字
    :param phone: 要验证的手机号码
    :return: True 合法  False 非法
    '''
    if len(phone) == 11:
        #if phone.startswith("156") or phone.startswith("158") or phone.startswith("188"):
        if phone[0:3] in ["156", "158", "188"]:
            ###########
            # for i in phone:
            #     if not i.isdigit():
            #         print("手机号码包含非数字")
            #         return False
            # else:
            #     print("手机号码合法")
            #     return True
            ###########
            # if phone.isdigit():
            #     print("手机号码合法")
            #     return True
            # else:
            #     print("手机号码包含非数字字符")
            #     return False
            ###########
            try:
                int(phone)
                print("手机号码合法")
                return True
            except:
                print("手机号码包含非数字")
                return False

        else:
            print("手机号码开头不合法")
    else:
        print("长度不合法")
        return False

if __name__ == "__main__":
    # 提示用户输入手机号
    p = input("请输入您的手机号码：")
    res = validate_phone(p)
    print(res)
