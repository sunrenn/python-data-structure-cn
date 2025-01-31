## 6.5.Hash查找

在前面的部分中，我们通过利用关于项在集合中相对于彼此存储的位置的信息，改进我们的搜索算法。例如，通过知道列表是有序的，我们可以使用二分查找在对数时间中搜索。在本节中，我们将尝试进一步建立一个可以在 $$O(1)$$ 时间内搜索的数据结构。这个概念被称为 `Hash 查找`。

为了做到这一点，当我们在集合中查找项时，我们需要更多地了解项可能在哪里。如果每个项都在应该在的地方，那么搜索可以使用单个比较就能发现项的存在。然而，我们看到，通常不是这样的。

`哈希表` 是以一种容易找到它们的方式存储的项的集合。哈希表的每个位置，通常称为一个槽，可以容纳一个项，并且由从 0 开始的整数值命名。例如，我们有一个名为 0 的槽，名为 1 的槽，名为 2 的槽，以上。最初，哈希表不包含项，因此每个槽都为空。我们可以通过使用列表来实现一个哈希表，每个元素初始化为`None` 。Figure 4 展示了大小 m = 11 的哈希表。换句话说，在表中有 m 个槽，命名为 0 到 10。

![6.5.Hash查找.figure4](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure4.png)

*Figure 4*

项和该项在散列表中所属的槽之间的映射被称为 `hash 函数`。 hash 函数将接收集合中的任何项，并在槽名范围内（0和 m-1之间）返回一个整数。假设我们有整数项 `54,26,93,17,77` 和 `31` 的集合。我们的第一个 hash 函数，有时被称为 `余数法` ，只需要一个项并将其除以表大小，返回剩余部分作为其散列值`（h(item) = item％11）`。 Table 4 给出了我们的示例项的所有哈希值。注意，这种余数方法（模运算）通常以某种形式存在于所有散列函数中，因为结果必须在槽名的范围内。

![6.5.Hash查找.table4](assets/5.5.Hash%E6%9F%A5%E6%89%BE.table4.png)

*Table 4*

一旦计算了哈希值，我们可以将每个项插入到指定位置的哈希表中，如 Figure 5 所示。注意，11 个插槽中的 6 个现在已被占用。这被称为负载因子，通常表示为 `λ=项数/表大小`, 在这个例子中，`λ = 6/11` 。
![6.5.Hash查找.figure5](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure5.png)

*Figure 5*

现在，当我们要搜索一个项时，我们只需使用哈希函数来计算项的槽名称，然后检查哈希表以查看它是否存在。该搜索操作是 $$O(1)$$，因为需要恒定的时间量来计算散列值，然后在该位置索引散列表。如果一切都正确的话，我们已经找到了一个恒定时间搜索算法。

你可能已经看到，只有每个项映射到哈希表中的唯一位置，这种技术才会起作用。 例如，如果项 44 是我们集合中的下一个项，则它的散列值为`0（44％11 == 0）`。 因为 77 的哈希值也是 0，我们会有一个问题。根据散列函数，两个或更多项将需要在同一槽中。这种现象被称为碰撞（它也可以被称为“冲突”）。显然，冲突使散列技术产生了问题。我们将在后面详细讨论。

### 5.5.1.hash 函数

给定项的集合，将每个项映射到唯一槽的散列函数被称为完美散列函数。如果我们知道项和集合将永远不会改变，那么可以构造一个完美的散列函数。不幸的是，给定任意的项集合，没有系统的方法来构建完美的散列函数。幸运的是，我们不需要散列函数是完美的，仍然可以提高性能。

总是具有完美散列函数的一种方式是增加散列表的大小，使得可以容纳项范围中的每个可能值。这保证每个项将具有唯一的槽。虽然这对于小数目的项是实用的，但是当可能项的数目大时是不可行的。例如，如果项是九位数的社保号码，则此方法将需要大约十亿个槽。如果我们只想存储 25 名学生的数据，我们将浪费大量的内存。

我们的目标是创建一个散列函数，最大限度地减少冲突数，易于计算，并均匀分布在哈希表中的项。有很多常用的方法来扩展简单余数法。我们将在这里介绍其中几个。

`分组求和法` 将项划分为相等大小的块（最后一块可能不是相等大小）。然后将这些块加在一起以求出散列值。例如，如果我们的项是电话号码 `436-555-4601`，我们将取出数字，并将它们分成2位数`（43,65,55,46,01）`。`43 + 65 + 55 + 46 + 01`，我们得到 210。我们假设哈希表有 11 个槽，那么我们需要除以 11 。在这种情况下，`210％11` 为 1，因此电话号码 `436-555-4601` 散列到槽 1 。一些分组求和法会在求和之前每隔一个反转。对于上述示例，我们得到 `43 + 56 + 55 + 64 + 01 = 219`，其给出 `219％11 = 10` 。

用于构造散列函数的另一数值技术被称为 `平方取中法`。我们首先对该项平方，然后提取一部分数字结果。例如，如果项是 44，我们将首先计算 `44^2 = 1,936` 。通过提取中间两个数字 `93` ，我们得到 `5（93％11）`。Table 5 展示了余数法和中间平方法下的项。

![6.5.Hash查找.table5](assets/5.5.Hash%E6%9F%A5%E6%89%BE.table5.png)

*Table 5*

我们还可以为基于字符的项（如字符串）创建哈希函数。 词 `cat` 可以被认为是 ascii 值的序列。

```bash
>>> ord('c')
99
>>> ord('a')
97
>>> ord('t')
116
```

然后，我们可以获取这三个 ascii 值，将它们相加，并使用余数方法获取散列值（参见 Figure 6）。 Listing 1 展示了一个名为 hash 的函数，它接收字符串和表大小 作为参数，并返回从 `0` 到 `tablesize-1` 的范围内的散列值。

![6.5.Hash查找.figure6](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure6.png)

*Figure 6*

```python
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize
```

*Listing 1*

有趣的是，当使用此散列函数时，字符串总是返回相同的散列值。 为了弥补这一点，我们可以使用字符的位置作为权重。 Figure 7 展示了使用位置值作为加权因子的一种可能的方式。

![6.5.Hash查找.figure7](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure7.png)

*Figure 7*

你可以思考一些其他方法来计算集合中项的散列值。重要的是要记住，哈希函数必须是高效的，以便它不会成为存储和搜索过程的主要部分。如果哈希函数太复杂，则计算槽名称的程序要比之前所述的简单地进行基本的顺序或二分搜索更耗时。 这将打破散列的目的。

### 5.5.2.冲突解决

我们现在回到碰撞的问题。当两个项散列到同一个槽时，我们必须有一个系统的方法将第二个项放在散列表中。这个过程称为冲突解决。如前所述，如果散列函数是完美的，冲突将永远不会发生。然而，由于这通常是不可能的，所以冲突解决成为散列非常重要的部分。

解决冲突的一种方法是查找散列表，尝试查找到另一个空槽以保存导致冲突的项。一个简单的方法是从原始哈希值位置开始，然后以顺序方式移动槽，直到遇到第一个空槽。注意，我们可能需要回到第一个槽（循环）以查找整个散列表。这种冲突解决过程被称为开放寻址，因为它试图在散列表中找到下一个空槽或地址。通过系统地一次访问每个槽，我们执行称为线性探测的开放寻址技术。

Figure 8展示了在简单余数法散列函数`（54,26,93,17,77,31,44,55,20）` 下的整数项的扩展集合。上面的 Table 4 展示了原始项的哈希值。Figure 5 展示了原始内容。当我们尝试将 `44` 放入槽 0 时，发生冲突。在线性探测下，我们逐个顺序观察，直到找到位置。在这种情况下，我们找到槽 1。

再次，`55` 应该在槽 0 中，但是必须放置在槽 2 中，因为它是下一个开放位置。值 20 散列到槽 9 。由于槽 9 已满，我们进行线性探测。我们访问槽`10,0,1`和 `2`，最后在位置 3 找到一个空槽。

![6.5.Hash查找.figure8](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure8.png)

*Figure 8*

一旦我们使用开放寻址和线性探测建立了哈希表，我们就必须使用相同的方法来搜索项。假设我们想查找项 `93` 。当我们计算哈希值时，我们得到 `5` 。查看槽 5 得到 `93`，返回 True。如果我们正在寻找 `20`， 现在哈希值为 `9`，而槽 `9` 当前项为 `31` 。我们不能简单地返回 False，因为我们知道可能存在冲突。我们现在被迫做一个顺序搜索，从位置 `10` 开始寻找，直到我们找到项 `20` 或我们找到一个空槽。

线性探测的缺点是聚集的趋势;项在表中聚集。这意味着如果在相同的散列值处发生很多冲突，则将通过线性探测来填充多个周边槽。这将影响正在插入的其他项，正如我们尝试添加上面的项 `20` 时看到的。必须跳过一组值为 `0` 的值，最终找到开放位置。该聚集如 Figure 9 所示。

![6.5.Hash查找.figure9](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure9.png)

*Figure 9*

处理聚集的一种方式是扩展线性探测技术，使得不是顺序地查找下一个开放槽，而是跳过槽，从而更均匀地分布已经引起冲突的项。这将潜在地减少发生的聚集。 Figure 10 展示了使用 `加3` 探头进行碰撞识别时的项。 这意味着一旦发生碰撞，我们将查看第三个槽，直到找到一个空。

![6.5.Hash查找.figure10](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure10.png)

*Figure 10*

在冲突后寻找另一个槽的过程叫 `重新散列`。使用简单的线性探测，rehash 函数是 `newhashvalue = rehash(oldhashvalue)`其中 `rehash(pos)=(pos + 1)％sizeoftable`。 `加3`rehash 可以定义为`rehash(pos)=(pos + 3)％sizeoftable`。一般来说，`rehash(pos)=(pos + skip)％sizeoftable`。重要的是要注意，“跳过”的大小必须使得表中的所有槽最终都被访问。否则，表的一部分将不被使用。为了确保这一点，通常建议表大小是素数。这是我们在示例中使用 11 的原因。

线性探测思想的一个变种称为二次探测。代替使用常量 “跳过” 值，我们使用rehash 函数，将散列值递增 `1，3，5，7，9，` 依此类推。这意味着如果第一哈希值是 `h`，则连续值是`h + 1，h + 4，h + 9，h + 16`，等等。换句话说，二次探测使用由连续完全正方形组成的跳跃。Figure 11 展示了使用此技术放置之后的示例值。

![6.5.Hash查找.figure11](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure11.png)

*Figure 11*

用于处理冲突问题的替代方法是允许每个槽保持对项的集合（或链）的引用。链接允许许多项存在于哈希表中的相同位置。当发生冲突时，项仍然放在散列表的正确槽中。随着越来越多的项哈希到相同的位置，搜索集合中的项的难度增加。 Figure 12 展示了添加到使用链接解决冲突的散列表时的项。

![6.5.Hash查找.figure12](assets/5.5.Hash%E6%9F%A5%E6%89%BE.figure12.png)

*Figure 12*

当我们要搜索一个项时，我们使用散列函数来生成它应该在的槽。由于每个槽都有一个集合，我们使用一种搜索技术来查找该项是否存在。优点是，平均来说，每个槽中可能有更少的项，因此搜索可能更有效。我们将在本节结尾处查看散列的分析。

### 5.5.3.实现 map 抽象数据类型

最有用的 Python 集合之一是字典。回想一下，字典是一种关联数据类型，你可以在其中存储键-值对。该键用于查找关联的值。我们经常将这个想法称为 `map`。

map 抽象数据类型定义如下。该结构是键与值之间的关联的无序集合。map 中的键都是唯一的，因此键和值之间存在一对一的关系。操作如下。

* Map() 创建一个新的 map 。它返回一个空的 map 集合。
* put(key，val) 向 map 中添加一个新的键值对。如果键已经在 map 中，那么用新值替换旧值。
* get(key) 给定一个键，返回存储在 map 中的值或 None。
* del 使用 `del map[key]` 形式的语句从 map 中删除键值对。
* len() 返回存储在 map 中的键值对的数量。
* in 返回 True 对于 `key in map` 语句，如果给定的键在 map 中，否则为False。

字典一个很大的好处是，给定一个键，我们可以非常快速地查找相关的值。为了提供这种快速查找能力，我们需要一个支持高效搜索的实现。我们可以使用具有顺序或二分查找的列表，但是使用如上所述的哈希表将更好，因为查找哈希表中的项可以接近 $$O(1)$$ 性能。

在 Listing 2 中，我们使用两个列表来创建一个实现 Map 抽象数据类型的HashTable 类。一个名为 `slots` 的列表将保存键项，一个称 `data` 的并行列表将保存数据值。当我们查找一个键时，`data` 列表中的相应位置将保存相关的数据值。我们将使用前面提出的想法将键列表视为哈希表。注意，哈希表的初始大小已经被选择为 11。尽管这是任意的，但是重要的是，大小是质数，使得冲突解决算法可以尽可能高效。

```python
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
```

*Listing 2*

hash 函数实现简单的余数方法。冲突解决技术是 `加1` rehash 函数的线性探测。 put 函数（见 Listing 3）假定最终将有一个空槽，除非 key 已经存在于 `self.slots` 中。 它计算原始哈希值，如果该槽不为空，则迭代 rehash 函数，直到出现空槽。如果非空槽已经包含 key，则旧数据值将替换为新数据值。

```python
def put(self,key,data):
  hashvalue = self.hashfunction(key,len(self.slots))

  if self.slots[hashvalue] == None:
    self.slots[hashvalue] = key
    self.data[hashvalue] = data
  else:
    if self.slots[hashvalue] == key:
      self.data[hashvalue] = data  #replace
    else:
      nextslot = self.rehash(hashvalue,len(self.slots))
      while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
        nextslot = self.rehash(nextslot,len(self.slots))

      if self.slots[nextslot] == None:
        self.slots[nextslot]=key
        self.data[nextslot]=data
      else:
        self.data[nextslot] = data #replace

def hashfunction(self,key,size):
     return key%size

def rehash(self,oldhash,size):
    return (oldhash+1)%size
```

*Listing 3*

同样，get 函数（见 Listing 4）从计算初始哈希值开始。如果值不在初始槽中，则 rehash 用于定位下一个可能的位置。注意，第 15 行保证搜索将通过检查以确保我们没有返回到初始槽来终止。如果发生这种情况，我们已用尽所有可能的槽，并且项不存在。

HashTable 类提供了附加的字典功能。我们重载 `__getitem__` 和`__setitem__` 方法以允许使用 `[]` 访问。 这意味着一旦创建了HashTable，索引操作符将可用。 

```python
def get(self,key):
  startslot = self.hashfunction(key,len(self.slots))

  data = None
  stop = False
  found = False
  position = startslot
  while self.slots[position] != None and  \
                       not found and not stop:
     if self.slots[position] == key:
       found = True
       data = self.data[position]
     else:
       position=self.rehash(position,len(self.slots))
       if position == startslot:
           stop = True
  return data

def __getitem__(self,key):
    return self.get(key)

def __setitem__(self,key,data):
    self.put(key,data)
```

*Listing 4*

下面的会话展示了 HashTable 类的操作。首先，我们将创建一个哈希表并存储一些带有整数键和字符串数据值的项。

```bash
>>> H=HashTable()
>>> H[54]="cat"
>>> H[26]="dog"
>>> H[93]="lion"
>>> H[17]="tiger"
>>> H[77]="bird"
>>> H[31]="cow"
>>> H[44]="goat"
>>> H[55]="pig"
>>> H[20]="chicken"
>>> H.slots
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
>>> H.data
['bird', 'goat', 'pig', 'chicken', 'dog', 'lion',
       'tiger', None, None, 'cow', 'cat']
```

接下来，我们将访问和修改哈希表中的一些项。注意，正替换键 20 的值。

```bash
>>> H[20]
'chicken'
>>> H[17]
'tiger'
>>> H[20]='duck'
>>> H[20]
'duck'
>>> H.data
['bird', 'goat', 'pig', 'duck', 'dog', 'lion',
       'tiger', None, None, 'cow', 'cat']
>> print(H[99])
None

```

### 5.5.4.hash法分析

我们之前说过，在最好的情况下，散列将提供 $$O(1)$$，恒定时间搜索。然而，由于冲突，比较的数量通常不是那么简单。即使对散列的完整分析超出了本文的范围，我们可以陈述一些近似搜索项所需的比较数量的已知结果。

我们需要分析散列表的使用的最重要的信息是负载因子 λ。概念上，如果 λ 小，则碰撞的机会较低，这意味着项更可能在它们所属的槽中。如果 λ 大，意味着表正在填满，则存在越来越多的冲突。这意味着冲突解决更困难，需要更多的比较来找到一个空槽。使用链接，增加的碰撞意味着每个链上的项数量增加。

和以前一样，我们将有一个成功的搜索结果和不成功的。对于使用具有线性探测的开放寻址的成功搜索，平均比较数大约为`1/2（1 + 1/(1-λ)）`，不成功的搜索为 1/2(1+(1/1-λ)^2 ) 如果我们使用链接，则对于成功的情况，平均比较数目是 1+λ/2，如果搜索不成功，则简单地是 λ 比较次数。
