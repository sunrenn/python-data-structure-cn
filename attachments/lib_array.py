import random
class MyArray:
    # 手动仿造list练习

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def fill_randint(self,maxvalue=100):
        for i in range(self.capacity):
            self.array[i] = random.randint(0,maxvalue)
    
    def insert(self, idx, itm):
        # idx: index, 插入位置
        # itm: 插入内容


        if idx>self.size or idx<0:
            raise Exception("超出数组长度范围！")
        
        # 从右向左右移一位
        # for ii in range(self.size, 1, -1):
        #     self.array[ii] = self.array[ii-1]
        
        for ii in range(self.size-1, -1, -1):
            self.array[ii+1] = self.array[ii]
        
        self.array[idx] = itm
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])





if __name__ == "__main__":

    # testarray1 = MyArray(6)

    # testarray1.insert(0,11)
    # testarray1.insert(0,22)
    # testarray1.insert(0,33)
    # testarray1.insert(2,77)

    # testarray1.output()

    # print(testarray1.array)

    testarray2 = MyArray(100)
    testarray2.fill_randint(1111)
    print(testarray2.array)
