
def shellSort(alist):

    sublist_count = len(alist)//2

    while sublist_count > 0:

        for startposition in range(sublist_count):
            gapInsertionSort(alist,startposition,sublist_count)

        print("After increments of size",sublist_count, "The list is",alist)

        sublist_count = sublist_count // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]

shellSort(alist)
print(alist)
