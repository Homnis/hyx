import  random as r
#
# print(r.randint(1,4),r.randint(1,7))
##
# 查找  index  find

#统计  count

#分割  split   splitlines  partition

#判断  isalnum  isalpha isdigit  isupper islower

#对齐  ljust  rjust  center

#裁切  strip  rstrip  lstrip

#编码 解码  encode  decode

#替换   replace

#链接  join

#格式化字符串 format  %s  %f %d

# \n \t  \r  \\  \" \'  转义字符

#
# 1.去掉字符串中的所有空格
# strA="  a  b  ac  sde   "
# strA=strA.replace(" ","")
# print(strA,len(strA))

# strA="".join(strA.split(" "))
# print(strA,len(strA))

# 2.根据完整的路径从路径中分离文件路径、文件名及扩展名

# pathA=r"C:\Users\Administrator\Desktop\py第一天.xmind"

# x=pathA.rpartition(".")

# print(x)
# print("文件路径：",x[0][0:x[0].rfind("\\")])
# print("文件名：",x[0][x[0].rfind("\\")+1:len(x[0])])
# print("后缀名：",x[2])



# 3.获取字符串中汉字的个数

# strA=input("请输入文本？")

# utf-8  编码
# 英文一个字节  中文三个字节

# abc你好 》》 （9-5）/2

# x=strA.encode()
#
# nums=(len(x)-len(strA))/2
#
# print("%s的汉字个数为%d"%(strA,nums))






# 4.对字符串进行加密与解密




# 5.将字母全部转换为大写或小写
#
# strA="anBFCCabwe"
#
# print(strA.upper())
# print(strA.lower())




# x=x[1:len(x)-1].split(",")
# for i in x:
#     print(i)# 6.根据标点符号对字符串进行分行
# # strA="十八大以来，习近平对党的新闻舆论工" \
# #      "作所面临的新形势新任务作出了宏观思考" \
# #      "和战略布局，提出了许多新思想新观点。 " \
# #      "今天，小组对此进行梳理，供组员学习思考。"
# #
# # strA=strA.replace("，","\n").replace("。","\n")
# # print(strA)
#
#
# #x=str(strA.split("，")).split("。")
# #
# # x=list(x)
# #
# # x="".join(x)
# #


# 7.去掉字符串数组中每个字符串的空格





# 8.随意输入你心中想到的一个书名，
# 然后输出它的字符串长度。
# （len()属性:可以得字符串的长度）




# 9.两个学员输入各自最喜欢的游戏名称，
# 判断是否一致,如果相等,
# 则输出你们俩喜欢相同的游戏；
# 如果不相同,则输出你们俩喜欢不相同的游戏。

# 10.上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
# strA="lol"
# strB="LOL"
#
# if strA.upper()==strB.upper():
#     print("兴趣爱好一致")
# else:
#     print("不一致")


# 11.让用户输入一个日期格式如“2008/08/08”，
# 将 输入的日期格式转换为“2008年-8月-8日”。

# strA="2013/12/31"
#
# x=strA.replace("/","")
# print("%s年-%s月-%s日"%(int(x[0:4]),int(x[4:6]),int(x[6:8])))
#






# 12.接收用户输入的字符串，
# 将其中的字符进行排序（升序），
# 并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。
# x="abcdefghijklmnopqrstuvwxyz"
# strA="cabed"
#列表处理方法
# strA=list(strA)
# print(strA)
# strA.sort() #列表排序
# print(strA)
# strA="".join(strA)
#
# print(strA)
# print(strA[::-1])

#简单方法 好理解
# end=""
# for i in x:
#     for j in strA:
#         if i==j:
#             end+=i
#     if len(end)==len(strA):
#         break
# print(end)
# print(end[::-1])



# 13.接收用户输入的一句英文，
# 将其中的单词以反序输出，
# “hello c sharp”→“sharp c hello”。

# strA="hello c sharp"
# x=strA.split(" ")
# print(x[::-1])



# 14.从请求地址中提取出用户名和域名
# http://www.163.com?userName=admin&pwd=123456

# pathA=r"http://www.163.com?userName=admin&pwd=123456"
#
# x=pathA.split("?")
# print("域名：",x[0][x[0].find("w"):len(x[0])])
#
# print("用户名：",x[1].split("&")[0].split("=")[1])
#
# print("密码：",x[1].split("&")[1].split("=")[1])


# 15.有个字符串数组，存储了10个书名，
# 书名有长有短，现在将他们统一处理，
# 若书名长度大于10，
# 则截取长度8的子串并且最后添加“...”，
# 加一个竖线后输出作者的名字。

# bookNames="python从入门到精通|佚名,java从入门到放弃|佚名," \
#           "C++从入门到绝望|佚名,那年花开月正圆，hahahaha|未知,延禧攻略|鸟哥"
#
# books=bookNames.split(",")
# print(books)
#
# for i in books:
#     temp=i.split("|")
#     if len(temp[0])>10:
#         print(temp[0][0:8]+"...|"+temp[1])
#     else:
#         print(temp[0] + "|" + temp[1])
# 16.让用户输入一句话,找出所有"呵"的位置。

# strA="呵你呵 我呵呵呵  呵大家呵"
#
# index=0
# while True:
#     index=strA.find("呵",index)
#     print(index)
#     index+=1
#     if index==len(strA):
#         break

#
# print("*"*20)
# for i in range(len(strA)):
#     if strA[i]=="呵":
#         print(i)


# 17.让用户输入一句话,找出所有"呵呵"的位置。
#
# strA="你呵呵，我呵呵呵，呵呵大家"

# for i in range(len(strA)-1):
#     if strA[i]+strA[i+1]=="呵呵":
#         print(i)


# index=0
# while True:
#     index=strA.find("呵呵",index)
#     if index==-1:
#         break
#     print(index)
#     index+=2
#     if index==len(strA):
#         break


# 18.让用户输入一句话,判断这句话中有没有邪恶,
# 如果有邪恶就替换成这种形式然后输出,
# 如:“老牛很邪恶”,输出后变成”老牛很**”;

# strA="老牛很邪恶"
#
# strA=strA.replace("邪恶","**")
# print(strA)


# 19.如何判断一个字符串是否为另一个字符串的子串

# strA="abcfdhg"
#
# strB="acb"
#
# if strA.count(strB)>0:
#     print("是子串")
# else:
#     print("不是子串")






# 20.如何验证一个字符串中的每一个字符均在另一个字符串中出现过

# strA="abcfdhg"
#
# strB="xacb"
#
# #反向思维 ，假定一定全部出现，有一个不出现一定不是
#
# isFind=True
# for i in strB:
#     if strA.count(i)==0: #有一个没出现
#         isFind=False
#         break
# if isFind:
#     print("全出现")
# else:
#     print("不是全出现的")



# 21.如何随机生成无数字的全字母的字符串
##随机的四个字符不能重复
#方案一
# strA="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# x=""
# for i in range(4):
#     x += strA[r.randint(0, len(strA) - 1)]
# print(x)
#方案二
# x=""
# for i in range(4):
#     if r.randint(0, 1) == 0:
#         x += chr(r.randint(65, 90))
#     else:
#         x += chr(r.randint(97, 122))
# print(x)
# 22.如何随机生成带数字和字母的字符串,必须有数字和字母
# x=""
# for i in range(4):
#     randNum=r.randint(0, 2)
#     if randNum == 0:
#         x += chr(r.randint(65, 90))
#     elif randNum==1 :
#         x += chr(r.randint(97, 122))
#     else:
#         x += chr(r.randint(48, 57))
# print(x)


# 23.如何判定一个字符串中既有数字又有字母

# strA="a14"
# #假定既包含 不 数字 也 不包含 字母
# isNum=False
# isAlpha=False
#
# for i in strA:
#     if 48<=ord(i)<=57:
#         isNum=True
#         break
# for i in strA:
#     if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
#         isAlpha = True
#         break
#
# if isNum and isAlpha:
#     print("铁定包含数字和字母")
# else:
#     print("铁定False包含数字和字母")


# 24.字符串内的字符排序（只按字母序不论大小写）

strA="aOLKJUewwefzWESGFSDXAsvwevsdvssdfaegERGEAG"

# x=list(strA)
# x.sort(key=lambda x:x.upper())
# x="".join(x)
# print(x)

# 25.字符串的补位操作
# 1  =》001
# 2  =》002
# 10=》010

# strA="330"
#
# x=strA.rjust(3,"0")
# print(x)