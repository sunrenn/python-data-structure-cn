
import copy

def testcopy(source_data,func,actlevel=3):
    """
    source_data: 初始数据
    fun: 对初始数据的处理方法
    actlevel: 修改的层级
    """
    aa = source_data
    bb = aa
    cc = copy.copy(bb)
    dd = copy.deepcopy(bb)

    print()
    print("-"*50)
    print("\r\n\r\naa:",type(aa),aa)
    print("id(aa):",id(aa),id(aa)-id(aa), end=" || ")
    print("id(bb):",id(bb),id(bb)-id(aa), end=" || ")
    print("id(cc):",id(cc),id(cc)-id(aa), end=" || ")
    print("id(dd):",id(dd),id(dd)-id(aa), end=" || ")

    # 浅拷贝, 只能拷贝可变数据类型中第一层数据, 再深层的就不行了
    # 列表, 字典, 集合, 这三种可变数据, 都自带一个内置的浅拷贝函数: `.copy()`
    # 深拷贝, 多深都行
    # 只有标准库copy模块里有这个函数, deepcopy(data)

    # 修改
    try:
        
        if type(aa)!=type("1") :
            evalstr = "aa"
            for ii in range(actlevel):
                evalstr += "[0]"
            evalstr+="='跟随原始变量被修改了' "
            print("\r\n\r\n",actlevel,"层修改: ",evalstr)
            eval(evalstr)
        else :
            aa = "AAA"
    except Exception as e:
        print(e)
    print("aa:",type(aa),aa, end=" || ")
    print("bb:",type(bb),bb, end=" || ")
    print("cc:",type(cc),cc, end=" || ")
    print("dd:",type(dd),dd, end=" || ")
    print()
    print("-"*50)


testdata = [
    ["不可变数据",(lambda ss:ss),0],
    [["浅层数组"],(lambda ss:ss),1],
    [[[[[[[[[["深层数组"]]]]]]]]],(lambda ss:[ss]),9],
]

print("aa原始数据,bb,cc浅拷贝,dd深拷贝")
for itm in testdata:
    testcopy(*itm)

