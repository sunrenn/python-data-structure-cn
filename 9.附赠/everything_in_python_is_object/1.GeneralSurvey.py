#!/usr/bin/env python3
# everything_is_an_object.py
"""
在终端里优雅地打印 Markdown 文章，并当场用代码验证
‘Python 一切皆对象’ 的六重一致性。
https://www.kimi.com/chat/d1r6t22vtfek8na3kofg
"""

import inspect
import textwrap
from types import FunctionType, ModuleType

# --------------------------------------------------
# 1. 文章正文（Markdown 源码）
# --------------------------------------------------
ARTICLE = """
# 一切皆对象：Python 的宇宙法则

> 2025-07-15

在 Python 的苍穹下，“一切皆对象”并非一句简陋的口号，而是一条贯穿始终的宇宙法则。让我们沿着这条法则，俯瞰整片语言的星系，欣赏六重奏般的和谐与丰盈。

## 1. 统一接口：点号的魔力  
无论是一颗数字原子、一段函数星云，还是一艘模块飞船，只要伸手轻点 `.attr`、`.method()`，它们便应声而动。点号是通用的咒语，万物皆能听懂。

## 2. 引用语义：便签与灯塔  
变量从不占有，只是温柔地贴上一张便签。`a = b = []` 之后，`a.append(1)` 的涟漪即刻荡向 `b`。灯塔与影子的游戏，让内存的海洋波光粼粼。

## 3. 继承体系：血脉的延伸  
自 `object` 以降，所有类型共享同一条 DNA。列表可以被继承、函数亦可被派生。子类像河流汇入大海，既保留自己的歌声，又拥抱上游的旋律。

## 4. 多态消息：不问出身的舞会  
`len(x)` 的邀请发出去，列表、字典、自定义树形贵族同时起舞。舞步各异，却都踩着同一节拍——接口的节拍。

## 5. 动态塑形：橡皮泥时间  
运行时的 Python 是一位顽皮的雕塑家：给实例插上新的羽翼，把类的方法偷偷替换，甚至让对象的类型在指尖化蝶。程序不再僵死，而是会呼吸的陶土。

## 6. 反射之光：镜中观己  
`dir()` 是一面银镜，`getattr()` 与 `setattr()` 是雕刻刀，`inspect` 模块则是一座天文台。程序抬头即可看见自己的骨骼与经络，亦可提笔改写自己的命运。

---

## 尾声：未尽的留白  
当然，宇宙深处仍有暗礁：关键字 `if`、`for` 并非对象，却在幕后默许对象们上演宏大叙事；单例 `None`、`Ellipsis` 看似静默，亦严格遵守同一套引力定律。  
我们无需穷尽每一粒尘埃，只需记得——

> 在 Python 的星空里，所有光点共享同一条引力定律，  
> 那定律的名字，叫做“对象协议”。  

于是，万物对话，万物共舞，宇宙因此丰盈而轻盈。
"""

# --------------------------------------------------
# 2. 优雅的打印函数
# --------------------------------------------------
def print_markdown(md: str):
    """简单地将 Markdown 文本按行输出，保留格式。"""
    for line in md.strip().splitlines():
        print(line)

# --------------------------------------------------
# 3. 六重一致性验证
# --------------------------------------------------
def demonstrate():
    section("1️⃣  统一接口：点号的魔力")
    num = 42
    greet = lambda: "hello"
    # num.greet = greet  # 给数字添加一个方法
    print(f"   42 拥有属性 .real = {num.real}")
    print(f"   函数拥有属性 __name__ = {greet.__name__}")
    print(f"   模块拥有属性 __file__ = {inspect.getfile(FunctionType)}")
    print(f"   模块的 __name__ = {ModuleType.__name__}")
    # print(f"   greet() = {num.greet()}")

    section("2️⃣  引用语义：便签与灯塔")
    a = b = []
    a.append(1)
    print(f"   a = b = [] 后，a.append(1) -> b = {b}")

    section("3️⃣  继承体系：血脉的延伸")
    print(f"   int 的基类链：{int.__mro__}")
    print(f"   自定义类可继承 list：class MyList(list): ...")

    class MyList(list):
        def shout(self):
            return f"I have {len(self)} items!"
    print(f"   MyList([7, 8]).shout() -> {MyList([7, 8]).shout()}")

    section("4️⃣  多态消息：不问出身的舞会")
    class FakeSeq:
        def __len__(self):
            return 99
    print(f"   len([1, 2]) = {len([1, 2])}")
    print(f"   len({'a': 1}) = {len({'a': 1})}")
    print(f"   len(FakeSeq()) = {len(FakeSeq())}")

    section("5️⃣  动态塑形：橡皮泥时间")
    class Elf:
        pass
    e = Elf()
    e.magic = "fireball"
    Elf.shout = lambda self: "I am dynamic!"
    print(f"   实例动态添加属性 e.magic = {e.magic}")
    print(f"   类动态添加方法 e.shout() = {e.shout()}")

    section("6️⃣  反射之光：镜中观己")
    print(f"   dir(e)[:5] = {dir(e)[:5]}")
    print(f"   getattr(e, 'magic') = {getattr(e, 'magic')}")
    print(f"   inspect.isclass(Elf) = {inspect.isclass(Elf)}")

def section(title):
    print(f"\n{title}")
    print("─" * 40)

# --------------------------------------------------
# 4. 主流程
# --------------------------------------------------
if __name__ == "__main__":
    print_markdown(ARTICLE)
    print("\n" + "=" * 60)
    print("现在开始代码验证 —— 让文字落地，让对象说话：\n")
    demonstrate()