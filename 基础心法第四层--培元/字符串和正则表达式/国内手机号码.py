import re

def main():
    # 创建正则表达式对象
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123445467遍,我的手机号是13512346789这个良好号,
    不是15600998765,也是110或119,王打吹的手机号才是 15600989765
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线---------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------华丽的分隔线-----------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == "__main__":
    main()