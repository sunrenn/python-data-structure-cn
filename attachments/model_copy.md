# 浅拷贝与深拷贝

事关数据类型的可变性
深浅拷贝只对可变数据有意义

## python数据类型的可变性
<!-- https://realpython.com/python-mutable-vs-immutable-types/ -->
* 利用集合中只能存放不可变类型的数据来判断 "可变"(Mutable) 和 "不可变"(Immutable)

| 不可变   | 可变      |
| -------- | --------- |
| 数值     | 列表[]    |
| 字符串"" | 字典{k:v} |
| 元组()   | 集合{}    |



```python

import copy

def testcopy(source_data,func):
    aa = source_data
    bb = aa
    cc = copy.copy(bb)
    dd = copy.deepcopy(bb)
    print("aa原始数据,bb,cc浅拷贝,dd深拷贝")

    print("\r\naa:",type(aa),aa)
    print("id(aa):",id(aa),id(aa)-id(aa))
    print("id(bb):",id(bb),id(bb)-id(aa))
    print("id(cc):",id(cc),id(cc)-id(aa))
    print("id(dd):",id(dd),id(dd)-id(aa))

    # 浅拷贝, 只能拷贝可变数据类型中第一层数据, 再深层的就不行了
    # 列表, 字典, 集合, 这三种可变数据, 都自带一个内置的浅拷贝函数: `.copy()`
    print()
    aa[0] = [456]
    print("aa:",type(aa),aa)
    print("bb:",type(bb),bb)
    print("cc:",type(cc),cc)
    print("dd:",type(dd),dd)

    # 深拷贝, 多深都行
    # 只有标准库copy模块里有这个函数, deepcopy(data)
    aa[0][0] = 789
    print("aa:",type(aa),aa)
    print("bb:",type(bb),bb)
    print("cc:",type(cc),cc)
    print("dd:",type(dd),dd)

testdata = [
    ["不可变数据",(lambda ss:ss)],
    [["浅层数组"],(lambda ss:ss)],
    [[[[[[[[[["深层数组"]]]]]]]]],(lambda ss:[ss])],
]

for itm in testdata:
    testcopy(*itm)

```



