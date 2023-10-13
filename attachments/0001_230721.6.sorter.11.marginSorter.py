# ϣ���������������ĶԱ�

from lib_monitor import time_mem
from lib_array import MyArray
# import copy


class SortTester():

    def __init__(self):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0

    ## ��������
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
        print("�Ƚϴ���: ",self.number_of_comparisons)
        print("��������: ",self.number_of_exchanges)
        return(alist)


    ## ϣ������
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
        
        print("�Ƚϴ���: ",self.number_of_comparisons)
        print("��������: ",self.number_of_exchanges)
        return(alist)

    def _gapInsertionSort(self,alist,start,gap):
        ## ϣ��������Ҫʹ�õĲ�������
        for i in range(start+gap,len(alist),gap):

            current_value = alist[i]
            position = i

            self.number_of_comparisons += 1
            while position>=gap and alist[position-gap]>current_value:
                self.number_of_exchanges += 1
                alist[position]=alist[position-gap]
                position = position-gap

            alist[position]=current_value


    ## �鲢����
    @time_mem
    def mergeSortWrapper(self,alist):
        self.number_of_comparisons = 0
        self.number_of_exchanges = 0
        self.mergeSortReal(alist)
        print("�Ƚϴ���: ",self.number_of_comparisons)
        print("��������: ",self.number_of_exchanges)
        return(alist)

    def mergeSortReal(self, alist, level=0):
        # �����ʵ�ʵĹ鲢����, �Ǹ��ݹ� (������ǵݹ�, ��Ӧ�ý�"��������")
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
    print("������Ŀ: ",title)
    # print("����Ϊ: ",input)
    # print("ʵ�������: ",result)
    # print("���Ӧ����: ",output)
    # print("�����ȷ��" if (result == output) else "�������")

    result = fun(**input)
    print()
    return result

def tst1(**tmp):
    # �ر� (����) ���Ժ���tst
    pass



# ������������
llst = MyArray(3333)
llst.fill_randint()
tstarray1 = llst.array.copy()
tstarray2 = llst.array.copy()
tstarray3 = llst.array.copy()

ster = SortTester()


r1 = tst (
    fun=ster.insertionSort,
    title = str("��������, �����������ݳ���: ")+str(len(tstarray2)),
    output = True,
    alist = tstarray1
) if False else None

r2 = tst (
    fun=ster.shellSort,
    title = str("ϣ������, �����������ݳ���: ")+str(len(tstarray1)),
    output = True,
    alist = tstarray2
)

r3 = tst (
    fun=ster.mergeSortWrapper,
    title = str("�鲢����, �����������ݳ���: ")+str(len(tstarray3)),
    output = True,
    alist = tstarray3
)

print("�����ȷ��" if (r2 == r3) else "�������")


"""

## ����1 3ǧ������

������Ŀ:  ϣ������, �����������ݳ���: 3333
�Ƚϴ���:  33335
��������:  35279
peek_memory:  1.7412109375 KiB - Execution time: 0.08046388626098633 seconds


������Ŀ:  �鲢����, �����������ݳ���: 3333
�Ƚϴ���:  6673
��������:  6685
peek_memory:  60.5712890625 KiB - Execution time: 0.04673123359680176 seconds

�����ȷ��


## ���� 2  3��������

������Ŀ:  ϣ������, �����������ݳ���: 33313
�Ƚϴ���:  466386
��������:  368320
peek_memory:  1.7431640625 KiB - Execution time: 0.9187932014465332 seconds


������Ŀ:  �鲢����, �����������ݳ���: 33313
�Ƚϴ���:  66371
��������:  66654
peek_memory:  531.4697265625 KiB - Execution time: 0.6896300315856934 seconds

�����ȷ��


## ���� 3  30��������

������Ŀ:  ϣ������, �����������ݳ���: 333113
�Ƚϴ���:  5662930
��������:  3496796
peek_memory:  1.7451171875 KiB - Execution time: 10.78674864768982 seconds


������Ŀ:  �鲢����, �����������ݳ���: 333113
�Ƚϴ���:  663016
��������:  666255
peek_memory:  5217.6455078125 KiB - Execution time: 9.709290742874146 seconds

�����ȷ��

"""
