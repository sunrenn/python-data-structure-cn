# 2.1. 写一个优秀的python类

当你写一个类的时候，有很多事情要考虑。特别是当您打算将您的类发布给其他人使用时。在本节中，我们将构建一个简单的类来表示一个可以滚动的骰子，以及一个包含一堆骰子的杯子。我们将考虑以下方面来设计一个在Python生态系统中良好工作的类, 并逐步改进我们的实现。

每个类都应该有一个文档字符串 (docstring)，以提供有关如何使用该类的某种级别的文档。

每个类都应该有一个`__str__`魔术方法来给它一个有意义的字符串表示。

每个类都应该有一个适当的`__repr__`魔术方法，用于在交互式shell、调试器和其他不发生字符串转换的情况下进行表示。

每个类都应该具有可比性，这样就可以对其进行排序，并与其他实例进行有意义的比较。这至少意味着实现`__eq__`和`__lt__`。

您应该考虑对每个实例变量进行访问控制。您希望将哪些属性设为公共属性，哪些属性设为只读属性，以及哪些属性在允许更改之前要受到控制或检查。

如果类是其他类的容器 (container)，那么还有一些进一步的考虑:

您应该能够使用`len`找出容器容纳了多少东西

您应该能够遍历容器中的项。

您可能希望允许用户使用方括号索引表示法访问容器中的项。

## 2.1.1. `MSDie`类的基本实现

让我们从MSDie类的一个非常简单的实现开始，我们将一步一步地改进它。我们想让我们的骰子更灵活一些，这样构造函数将允许我们指定面(sides)的数量。

```python
import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)

```

这就是一个不错的起点。甚至对某些任务来说这就足够了。我们有了一个类，可以构造出一个骰子，然后可以滚动它，然后可以输出出当前的值。不过, 如果我们可以只需 `print(my_die)` , 而不必通过名为current_value的实例属性就可以显示骰子的值, 那就更好了. 

于是为使得色子的输出和交互更方便。我们将实现`__str__`和`__repr__`魔术方法以让类的表示更加直接。

```python

import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)


my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)

```
注意，当我们打印一个对象列表时，repr用于显示这些对象。良好的repr使调试和简单的状态输出 (print statements) 变得更加容易。
