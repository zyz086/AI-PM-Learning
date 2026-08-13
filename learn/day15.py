#今天是学习python基础语法的半个月，复习一下前面的内容
papers = ["论文A","论文B","论文C"]
print(papers[2])
print(len(papers))

projects = ["AI匹配","智能审稿"]
projects["AI写作助手"]#这是字典的写法不是列表的写法
projects.append("AI写作助手")
#列表的删除有点忘记了
projects.remove("智能审稿")
print(projects)

#切片，获取元素
scores = [95,80,70,60,40]
print((scores 0:2))#切片必须放在[]里面
print(scores -2:-1)
print(scores[0:3])
print(scores[-2:])

#字符串查找
title = input("请输入论文标题：")
if title == "AI":#这里包含关系要用in
if "AI" in title:
    print("检测到AI方向")
else:
    print("暂未检测到AI方向")

#字符串替换
title = "AI教育助手研究"
print(title.replace("AI","人工智能"))

#创建字典
papers = {
    "标题":"AI教育研究",
    "分数": 95,
    "状态":"通过"
}

#修改字典
papers("分数") = 100
#函数和字典搞混了
papers["score"] = 100,
papers("作者","张三")#字段表达形式写错了
paper["author"] = "张三"
print(papers)

#字典遍历 for循环遍历
result = {
    "逻辑": 85,
    "创新": 90,
    "引用": 80
}
for key,value in result.items():
   print(key,value)

papers = [#papers是列表不是字典 列表查询到方式是papers[下标索引]
    {
        "title": "AI教育研究",
        "score": 95
    },
    {
        "title": "智能审稿系统",
        "score": 80
    }
]
print[papers("title")]#print是函数不是列表正确的print()，这里应该先去列表再去字典
print(papers[0]["title"])


paper = {
    "title": "AI教育研究",
    "score": 85,
    "status": "待修改"
}
if paper["score"] >= 90:
    print("允许投稿")
elif paper["score"] >= 70:
    print("建议修改后投稿")
else:
    print("不建议投稿")