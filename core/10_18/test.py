# phone=input("请输入手机号码：")
# if len(phone)==11:
#     if phone[0:3] == "156" or phone[0:3]=="158" or phone[0:3]=="188":
#         for i in phone:
#             if i.isdigit() is False:
#                 print("你输入了非数字的手机号码")
#                 break
#     else:
#         print("不合法的手机号码")
# else:
#     print("手机号码长度有误")

import re


s="hello world 15101012345"
r=r'[0-125]'
print(re.findall(r, s))