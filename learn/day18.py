#一直在跑面试，没有敲代码，本次任务时完成会之前的复习摸底，找一下哪些知识忘记了
#if 语句
score = 85
if score > 90:
    print("推荐投稿")
elif score > 70:
    print("建议修改")
else:
    print("继续优化")
#for 循环
papers = ["AI教育研究", "智能审稿系统", "大模型应用"]
for paper in papers:
    print("正在检查",paper)
#词典
paper = {
    "title": "AI教育研究",
    "score": 85
}
paper["score"] = 90
paper["status"] = "pass"
print("title")#字典查询语法写错，print(paper,["title"])
#for+dict
result = {
    "逻辑": 85,
    "创新": 90,
    "引用": 80
}
#这个忘记了for key, value in result.items():

#函数参数
def check_direction(title):
    if "AI" in title:
        print("检测到AI方向")
    else:
        print("未检测到AI方向")
check_direction("AI教育研究")