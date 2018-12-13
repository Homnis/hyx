'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 10:37
desc: 正则表达式语法
'''
'''
python中re模块，主要用来进行正则表达式的操作
1. 定义正则表达式 【普通字符串】
2. 从目标字符串中提取数据 【正则规则】

正则规则：语法
1) 普通字符：也是正则表达式的一种字符，匹配当前字符本身

2) ^:表示匹配字符串的开头位置

3) $:表示匹配字符串的结束的位置

4) .:表示匹配任意一个字符[换行、制表符..除外..]

5) *:表示匹配任意一个字符出现了0次~n次

6) +:表示匹配任意一个字符出现1次~n次

7) ?:表示匹配一个字符出现了0次~1次

8) {m}:表示匹配一个字符出现了m次
    {m,n}:表示匹配一个字符至少出现m次最多出现n次
    {m,}:表示匹配任意一个字符至少出现m次
    {,n}:表示匹配任意一个字符最多出现n次
    
9) [0-9]:表示匹配任意一个0~9之间的数字
    [a-z]:表示匹配任意一个小写字母
    [A-Z]:表示匹配任意一个大写字母
    
    [0-3]:表示匹配任意一个0~3的数字
    [a-zA-Z]:表示匹配任意一个字母
    [abc]:表示匹配a或者b或者c
    [^a-z]:尖角符号出现在方括号中，表示取反：匹配非小写字母的字符
    
    [0-120]:表示匹配0~1 或者2 或者0--不能操作数字范围，如果要判断数字范围请使用比较运算符

10) ()表示分组，将一组数据单独区分出来
    (abc)：表示匹配abc字符，并且单独存放为一组

为了更加方便的操作正则表达式，出现了一些特殊符号，用于简化正则表达式的操作
11) \d: 和[0-9]相同的意义,匹配任意一个数字
    \D: 和[^0-9]相同的意义，匹配任意一个非数字
    
12) \s: 匹配任意一个空白字符
    \S: 匹配任意一个非空白字符

13) \b: 匹配任意一个单词边界

14) \w: 匹配任意一个数字、字母或者下划线，和[a-zA-Z0-9_]相同的意义
    
15) \：转义字符
    . -> 匹配-> \. 匹配一个普通的字符.
'''
import re

# 目标字符串
target = "hello, email@qq.com regexp in pythonn with regular on expressionon"

# 1.定义正则表达式
reg = r'l'
# findall(reg, target)：从target字符串中查询符合reg定义规则的字符串
print(re.findall(reg, target))

# 2. 开头匹配
# reg2 = r'^l'
reg2 = r'^h'
print(re.findall(reg2, target))

# 3. 结束位置
reg3 = r'n$'
print(re.findall(reg3, target))

# 4. 匹配任意一个字符
reg4 = r'^...'
print(re.findall(reg4, target))

# 5. 匹配任意一个字符出现0~n次
reg5 = r'l*'
print(re.findall(reg5, target))

# 6.匹配任意一个字符出现1~n次
reg6 = r'l+'
print(re.findall(reg6, target))

# 7. 匹配任意一个字符出现0次/1次
reg7 = r'l?'
print(re.findall(reg7, target))

# 8. 匹配任意一个字符出现指定次数
reg8 = r'l{2}'
print(re.findall(reg8, target))

# 9. 中括号范围：匹配任意一个数字/字符范围
reg9 = r'[a-g]{1}'
print(re.findall(reg9, target))

# 10.圆括号分组
reg10 = r'(on){2}'
print(re.findall(reg10, target))

# 13.单词边界
reg13 = r'\bon\b'
print(re.findall(reg13, target))