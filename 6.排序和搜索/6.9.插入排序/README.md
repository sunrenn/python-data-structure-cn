## 6.9.插入排序

插入排序，尽管仍然是 $O(n^2)$，工作方式略有不同。它始终在列表的较低位置维护一个排序的子列表。然后将每个新项 "插入" 回先前的子列表，使得排序的子列表成为较大的一个项。Figure 4 展示了插入排序过程。 阴影项表示算法进行每次遍历时的有序子列表。

![6.9.插入排序.figure4](assets/5.9.%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.figure4.png)

*Figure 4*

我们开始假设有一个项 (位置0) 的列表已经被排序。在每次遍历时，对于每个项 1 至 n-1，对比当前项和子列表。当我们回顾已经排序的子列表时，我们将那些更大的项移动到右边。当我们到达较小的项或子列表的末尾时，可以插入当前项。

Figure 5 详细展示了第五次遍历。在该算法中的这一点，存在由 `17,26,54,77` 和 `93` 组成的五个项的排序子列表。我们插入 `31` 到已经排序的项。第一次与 93 比较导致 93 向右移位。 77 和 54 也移位。 当遇到 26 时，移动过程停止，并且 31 被置于开放位置。现在我们有一个六个项的排序子列表。

![6.9.插入排序.figure5](assets/5.9.%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.figure5.png)

*Figure 5*

`insertSort` (ActiveCode 1) 的实现展示了 存在 n-1 个遍历以对 n 个排序。从位置 1 开始迭代并移动位置到 n-1，因为这些是需要插回到排序子列表中的项。第 8 行执行移位操作，将值向上移动到列表中的一个位置，在其后插入。请记住，这不是像以前的算法中的完全交换。

插入排序的最大比较次数是 n-1 个整数的总和。同样，是 $O(n^2)$。然而，在最好的情况下，每次通过只需要进行一次比较。这是已经排序的列表的情况。

关于移位和交换的一个注意事项也很重要。通常，移位操作只需要交换大约三分之一的处理工作，因为仅执行一次分配。在基准研究中，插入排序有非常好的性能。

```python
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

```

*ActiveCode 1*
