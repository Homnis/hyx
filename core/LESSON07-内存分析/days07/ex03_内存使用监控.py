# coding:gbk
'''
author: ���� Ĳ�ı�
version: V1.0.0
time: 2018/10/16 9:42
desc: TODO
'''
import memory_profiler

@memory_profiler.profile
def test(a):
    a.append(10)

@memory_profiler.profile
def test2(b):
    b = 20

@memory_profiler.profile
def main():
    x = [100]
    y = 200

    test(x)
    test2(y)

    print(x, y)


if __name__ == "__main__":
    main()

'''
�ڴ洦��ļ��ʹ��
1. �������еĴ��룬ȫ����װ�ɺ���
    ��˾��׼���򣺳���ִ�е���ڣ�һ�������ĵ���

2. ģ���ʹ�����Ž̳�
    ERROR���鿴�ٷ��ֲᡢ�鿴�ٶȽ�����鿴�������ϣ��õ�һ����ʹ�����̣�Ȼ����ȥʹ���������
    --> ��ѯ��Ӧ�Ĺٷ������ֲ�[����]��
        --> �����ֲ�[1~2ҳ]
    --> �鿴�������Ĳ�������[ͨ��]
        --> ���ģ������Ĵ��벿��
'''
