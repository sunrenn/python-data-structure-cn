## 8.10.广度优先搜索分析

在继续使用其他图算法之前，让我们分析广度优先搜索算法的运行时性能。首先要观察的是，对于图中的每个顶点 $$|V|$$ 最多执行一次 while 循环。因为一个顶点必须是白色，才能被检查和添加到队列。这给出了用于 while 循环的 $$O(V)$$。嵌套在 while 内部的 for 循环对于图中的每个边执行最多一次，$$|E|$$。原因是每个顶点最多被出列一次，并且仅当节点 u 出队时，我们才检查从节点 u 到节点 v 的边。这给出了用于 for 循环的 $$O(E)$$ 。组合这两个环路给出了 $$O(V+E)$$。

当然做广度优先搜索只是任务的一部分。从起始节点到目标节点的链接之后是任务的另一部分。最糟糕的情况是，如果图是单个长链。在这种情况下，遍历所有顶点将是 $$O(V)$$。正常情况将是 $$|V|$$ 的一小部分但我们仍然写 $$O(V)$$。

最后，至少对于这个问题，存在构建初始图形所需的时间。我们把 `buildGraph` 函数的分析作为一个练习。
