## 8.4.邻接矩阵

实现图的最简单的方法之一是使用二维矩阵。在该矩阵实现中，每个行和列表示图中的顶点。存储在行 v 和列 w 的交叉点处的单元中的值表示是否存在从顶点 v 到顶点 w 的边。 当两个顶点通过边连接时，我们说它们是相邻的。 Figure 3 展示了 Figure 2 中的图的邻接矩阵。单元格中的值表示从顶点 v 到顶点 w 的边的权重。

![8.4.邻接矩阵.figure3](assets/7.4.%E9%82%BB%E6%8E%A5%E7%9F%A9%E9%98%B5.figure3.png)

*Figure 3*

邻接矩阵的优点是简单，对于小图，很容易看到哪些节点连接到其他节点。 然而，注意矩阵中的大多数单元格是空的。 因为大多数单元格是空的，我们说这个矩阵是“稀疏的”。矩阵不是一种非常有效的方式来存储稀疏数据。 事实上，在Python中，你甚至要创建一个如 Figure 3所示的矩阵结构。

当边的数量大时，邻接矩阵是图的良好实现。但是什么是大？填充矩阵需要多少边？ 由于图中每个顶点有一行和一列，填充矩阵所需的边数为 $$|V|^2$$。 当每个顶点连接到每个其他顶点时，矩阵是满的。有几个真实的问题，接近这种连接。 我们在本章中讨论的问题都涉及稀疏连接的图。
