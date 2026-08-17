#用学过的if while for list string dict做一个小项目AI论文助手v2
#功能介绍：用户输入姓名和论文标题，系统会自动检测是否为人工智能方向，然后生成一份论文测评和建议

print("欢迎使用AI论文助手")
user_name = input("请输入你的姓名：")
title = input("请输入你的论文标题：")
if "AI" in title:
    print("检测到AI方向")
else:
    print("暂未检测到AI方向")
paper = {
    "title": title,
    "score": 85,
    "status": "待修改"
}
if paper["score"] >= 90:
    print("推荐投稿")
elif paper["score"] >= 70:
    print("修改后投稿")
else:
    print("不建议投稿")

#升级版加入随机分数和while循环
import random
print("欢迎使用AI论文助手")
user_name = input("请输入你的姓名：")
title = input("请输入你的论文标题：")
paper = {
    "title": title
}
counts = 3
while counts > 0:
   score = random.randint(1,100)
   print(score)
   if score >= 90:
       print("允许投稿")
       break
   else:
       counts -= 1
       print("继续改")
       print("剩余次数：",counts)

#for循环复习
papers = ["AI教育研究", "智能审稿系统", "大模型应用"]
for paper in papers:
    print("正在检查",paper)

scores = [95, 80, 60, 40]
for score in scores:
 if score >= 90:
     print(score,"允许投稿")
 elif score >= 80:
     print(score,"修改后投稿")
 elif score >= 60:
     print(score,"继续优化")
 else:
     print(score,"继续优化")

paper = {
    "title": "AI教育研究",
    "score": 95,
    "status": "通过"
}
for key,value in paper.items():
    print(key,value)

papers = [
    {
        "title": "AI教育研究",
        "score": 95
    },
    {
        "title": "智能审稿系统",
        "score": 80
    },
    {
        "title": "大模型应用",
        "score": 60
    }
]
for paper in papers:
    print(paper["title"])
    print(paper["score"])