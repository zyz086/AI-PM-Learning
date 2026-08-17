from learn.day16 import score


def ai_check():
    title = input("请输入你的论文标题:")
    if "AI" in title:
        print("检测到AI方向")
    else:
        print("暂未检测到AI方向")

ai_check()

def recommend():
    score = int(input("请输入论文分数的："))
    if score >= 90:
        print("推荐投稿")
    elif score >= 70:
        print("修改后投稿")
    else:
        print("继续优化")

recommend()

def welcome_user(name):
    print("欢迎你",name)

welcome_user("亚舟")

def check_direction(title):
    if "AI" in title:
        print("检测到AI方向")
    else:
        print("未检测到AI方向")

check_direction("AI数学教育")