#AI论文关键词检测器 学习字符串的查找、替换、布尔判断等
title = input("请输入论文标题：")
if "AI" in title:
    print("检测到AI方向")#多余重复了一次if循环的操作
    print(title.replace("AI","人工智能"))

#若字符串要进行in的布尔比较是需要每个字符串都和标题比较的，比如：
title = input("请输入论文标题：")
if "AI" in title or "人工智能" in title or "机器学习" in title:#复杂一点～
    print("检测到人工智能相关论文")
else:
    print("暂未检测到AI方向")

keywords = ["AI","人工智能","机器学习","大模型"]
title = input("请输入论文标题：")
for word in keywords:
    if word in title:
        print("检测到人工智能相关论文")
        break
    else:
        print("暂未检测到AI方向")