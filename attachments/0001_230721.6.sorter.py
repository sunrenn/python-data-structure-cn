# 希尔排序与插入排序的对比

from lib_monitor import time_mem
from lib_array import MyArray
# import copy


class SortTester():

    def __init__(self):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0


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


    ## 归并排序
    @time_mem
    def mergeSortWrapper(self,alist):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0
        self.mergeSortReal(alist)
        print("比较次数: ",self.number_of_comparisons)
        print("交换次数: ",self.number_of_exchanges)
        return(alist)

    def mergeSortReal(self, alist, level=0):

        level += 1
        self.number_of_comparisons = level
        self.number_of_exchanges = level
        # print("Splitting ",alist)

        self.number_of_comparisons += 1
        if len(alist)>1:
            self.number_of_exchanges += 1
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergeSortReal(lefthalf, level)
            self.mergeSortReal(righthalf, level)

            i=0
            j=0
            k=0
            self.number_of_comparisons += 1
            while i < len(lefthalf) and j < len(righthalf):
                self.number_of_comparisons += 1
                if lefthalf[i] < righthalf[j]:
                    self.number_of_exchanges += 1
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    self.number_of_exchanges += 1
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            self.number_of_comparisons += 1
            while i < len(lefthalf):
                self.number_of_exchanges += 1
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            self.number_of_comparisons += 1
            while j < len(righthalf):
                self.number_of_exchanges += 1
                alist[k]=righthalf[j]
                j=j+1
                k=k+1


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
tstarray3 = llst.array.copy()

ster = SortTester()


r1 = tst (
    fun=ster.insertionSort,
    title = str("插入排序, 测试输入数据长度: ")+str(len(tstarray2)),
    output = True,
    alist = tstarray1
) if False else None

r2 = tst (
    fun=ster.shellSort,
    title = str("希尔排序, 测试输入数据长度: ")+str(len(tstarray1)),
    output = True,
    alist = tstarray2
)

r3 = tst (
    fun=ster.mergeSortWrapper,
    title = str("归并排序, 测试输入数据长度: ")+str(len(tstarray3)),
    output = True,
    alist = tstarray3
)

print("结果正确！" if (r2 == r3) else "结果错误")


"""

## 测试1 3千数据量

测试项目:  希尔排序, 测试输入数据长度: 3333
比较次数:  33335
交换次数:  35279
peek_memory:  1.7412109375 KiB - Execution time: 0.08046388626098633 seconds


测试项目:  归并排序, 测试输入数据长度: 3333
比较次数:  6673
交换次数:  6685
peek_memory:  60.5712890625 KiB - Execution time: 0.04673123359680176 seconds

结果正确！


## 测试 2  3万数据量

测试项目:  希尔排序, 测试输入数据长度: 33313
比较次数:  466386
交换次数:  368320
peek_memory:  1.7431640625 KiB - Execution time: 0.9187932014465332 seconds


测试项目:  归并排序, 测试输入数据长度: 33313
比较次数:  66371
交换次数:  66654
peek_memory:  531.4697265625 KiB - Execution time: 0.6896300315856934 seconds

结果正确！


## 测试 3  30万数据量

测试项目:  希尔排序, 测试输入数据长度: 333113
比较次数:  5662930
交换次数:  3496796
peek_memory:  1.7451171875 KiB - Execution time: 10.78674864768982 seconds


测试项目:  归并排序, 测试输入数据长度: 333113
比较次数:  663016
交换次数:  666255
peek_memory:  5217.6455078125 KiB - Execution time: 9.709290742874146 seconds

结果正确！

"""
