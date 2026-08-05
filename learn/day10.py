#论文批量检查 主要练习for循环
papers = ["论文A","论文B","论文C"]
for paper in papers:
    if paper == "论文B":#又忘记在if语句后面加冒号！！！！
        print("发现重点论文")
    else:
        print("检查完成",paper)