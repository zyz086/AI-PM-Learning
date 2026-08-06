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

papers = ["深度学习论文", "AI教育研究", "智能审稿系统", "大模型应用"]
position = papers.index("智能审稿系统")
backup = papers.copy()
backup[0] = "深度学习优化"
last_two = papers[2:]
sorted_papers = papers.copy()
sorted_papers.sort()
print("原论文：",papers)
print("备份",backup)
print("智能审稿系统位置：",position)
print("最后两篇：",last_two)
print("排序后：",sorted_papers)