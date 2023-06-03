## 1.10.控制结构

正如我们前面提到的，算法需要两个重要的控制结构：迭代和选择。Python以各种形式支持这两种方法。程序员可以对给定环境选择最有用的语句。

对于迭代，Python提供了一个标准的`while`语句和一个非常强大的`for`语句。只要条件为真，`while`语句就会重复一段代码。 例如，

```python
>>> counter = 1
>>> while counter <= 5:
...     print("Hello, world")
...     counter = counter + 1


Hello, world
Hello, world
Hello, world
Hello, world
Hello, world
```

把“Hello, world”这个短语打印出来五次。在每次重复的开始时评估`while`语句的条件。如果条件为真，则将执行语句主体。由于语言强制执行的强制缩进模式，很容易看到`while`语句的结构。

`while`语句是一个非常通用的迭代结构，我们将在许多不同的算法中使用它。 在许多情况下，将会用复合条件来控制迭代。 片段如

```python
while counter <= 10 and not done:
...
```

只会在条件的两个部分都满足的情况下才会执行语句的主体。 变量`counter`的值需要小于或等于10，并且变量`done`的值需要为`False`（`not False`为`True`），以便`True and True`结果为`True`。

即使这种类型的构造在各种情况下都非常有用，但是另一个迭代结构`for`语句，可以与许多Python集合一起使用。 只要集合是序列，`for`语句就可以用于迭代集合的成员。 所以，例如，

```python
>>> for item in [1,3,6,2,5]:
...    print(item)
...
1
3
6
2
5
```

逐次将列表[1,3,6,2,5]中的每个值赋给变量item。 然后执行迭代的主体。 这适用于任何序列集合（列表，元组和字符串）。

for语句的一个常见用途是在一系列值上实现明确的迭代。 如下

```python
>>> for item in range(5):
...    print(item**2)
...
0
1
4
9
16
>>>
```

该语句将执行五次print功能。 range函数将返回表示序列0,1,2,3,4的范围对象，并且每个值将分配给变量item。 然后将该值平方并打印。

此迭代结构的另一个非常有用的版本用于处理字符串的每个字符。 以下代码片段遍历字符串列表，并且每个字符串通过将每个字符追加到列表上来处理每个字符。 结果为所有单词中所有字母的列表。

```python
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)
```

选择语句允许程序员提出问题，然后根据结果执行不同的操作。 大多数编程语言都提供了这个有用结构的两个版本：`if else`和`if`。 一个简单示例是使用`if else`语句实现二分选择。

```python
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')
```

此片段将通过打印所获得的字母等级对名为score的值进行分类。 如果分数大于或等于90，则语句将打印A.如果不是（else），则询问下一个问题。 如果分数大于或等于80，那么它必须在80到89之间，因为第一个问题的答案是错误的。 在这种情况下，打印B。 您可以看到Python缩进模式有助于理解`if`和`else`之间的关联而无需任何其他语法元素。

此类嵌套选择的替代语法是使用`elif`关键字。 将`else`和下一个`if`组合起来，以消除对额外嵌套级别的需要。 请注意，如果所有其他条件都失败，则仍需要最终的`else`来提供默认情况。

```python
if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')
```

Python也有单向选择构造，即`if`语句。 使用此语句，如果条件为`true`，则执行操作。 在条件为假的情况下，简单地继续执行到if之后的下一个语句。 例如，以下片段将首先检查变量`n`的值是否为负数。 如果是，则由绝对值函数修改。 无论如何，下一步是计算平方根。

```python
if n<0:
   n = abs(n)
print(math.sqrt(n))
```

返回列表，有一种替代方法来创建一个列表，它使用迭代和选择构造，称为list comprehension。列表推导允许您根据某些处理或选择标准轻松创建列表。 例如，如果我们想要创建前10个完美正方形的列表，我们可以使用for语句：

```python
>>> sqlist=[]
>>> for x in range(1,11):
         sqlist.append(x*x)

>>> sqlist
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
```

使用列表推导( 又称列表综合 )，我们可以一步完成

```python
>>> sqlist=[x*x for x in range(1,11)]
>>> sqlist
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>>
```

变量`x`采用`for`构造指定值1到10。 然后计算`x * x`的值并将其添加到正在构造的列表中。 列表推导的一般语法还允许添加选择标准，以便仅添加某些项。 例如，

```python
>>> sqlist=[x*x for x in range(1,11) if x%2 != 0]
>>> sqlist
[1, 9, 25, 49, 81]
>>>
```

此列表推导构造了一个列表，该列表仅包含1到10范围内的奇数的平方。任何支持迭代的序列都可以在列表推导中用于构造新列表。

```python
>>>[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']
>>>
```































