#AI论文版本管理系统
papers = ["论文A","论文B","论文C","论文D"]
position = papers.index("论文C")
backup = papers.copy()
backup[0] = "论文Av2"
last_papers = papers[2:]
print("原论文列表：",papers)
print("备份列表：",backup)
print("论文c位置：",position)
print("后两篇论文：",last_papers)