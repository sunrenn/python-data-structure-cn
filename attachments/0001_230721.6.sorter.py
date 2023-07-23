# 希尔排序与插入排序的对比

from lib_monitor import time_mem
from lib_array import MyArray
# import copy


class SortTester():

    def __init__(self):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0


    ## 希尔排序
    @time_mem
    def shellSort(self,alist):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0
        sublist_count = len(alist)//2
        while sublist_count > 0:

            for start_position in range(sublist_count):
                self._gapInsertionSort(alist,start_position,sublist_count)

            # print("After increments of size", sublist_count, "The list is",alist)

            sublist_count = sublist_count // 2
        
        print("比较次数: ",self.number_of_comparisons)
        print("交换次数: ",self.number_of_exchanges)
        return(alist)

    def _gapInsertionSort(self,alist,start,gap):
        for i in range(start+gap,len(alist),gap):

            current_value = alist[i]
            position = i

            self.number_of_comparisons += 1
            while position>=gap and alist[position-gap]>current_value:
                self.number_of_exchanges += 1
                alist[position]=alist[position-gap]
                position = position-gap

            alist[position]=current_value


    ## 插入排序
    @time_mem
    def insertionSort(self,alist):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0
        for index in range(1,len(alist)):

            current_value = alist[index]
            position = index

            self.number_of_comparisons += 1
            while position>0 and alist[position-1]>current_value:
                self.number_of_exchanges += 1
                alist[position]=alist[position-1]
                position = position-1

            alist[position]=current_value
        
        # print(alist)
        print("比较次数: ",self.number_of_comparisons)
        print("交换次数: ",self.number_of_exchanges)
        return(alist)


def tst(fun,title,output,**input):
    print()
    print("测试项目: ",title)
    # print("输入为: ",input)
    # print("实际输出是: ",result)
    # print("结果应该是: ",output)
    # print("结果正确！" if (result == output) else "结果错误")

    result = fun(**input)
    print()
    return result

def tst1(**tmp):
    # 关闭 (覆盖) 测试函数tst
    pass

# 测试数据生成
llst = MyArray(3333)
llst.fill_randint()
tstarray1 = llst.array.copy()
tstarray2 = llst.array.copy()

ster = SortTester()

r1 = tst (
    fun=ster.shellSort,
    title = str("希尔排序, 测试输入数据长度: ")+str(len(tstarray1)),
    output = True,
    alist = tstarray1
)

r2 = tst (
    fun=ster.insertionSort,
    title = str("插入排序, 测试输入数据长度: ")+str(len(tstarray1)),
    output = True,
    alist = tstarray2
)

# print("结果正确！" if (r1 == r2) else "结果错误")



