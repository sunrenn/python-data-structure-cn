# 总数不到
most = 51

# 小朋友给
boys_num = 8

# 剩下8块
left = 2

# 每人分得
per = 0

# 求确切的总数
totle = 0


# while ((per*boys_num+left) < most):
#     per = per+1
#     totle = per*boys_num+left

# print("1.总数是: ",totle, "每人份:",per)

per = (most - left)//boys_num

totle = per*boys_num+left

print("2.总数是: ",totle, "每人份:",per)

