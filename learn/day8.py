#AI论文检查模拟器
counts = 3
while counts > 0:
    choice = input("是否检查论文：")
    if choice == "是":
        counts -= 1
        print("剩余次数：", counts)
    else:
        break

#升级版
import random
counts = 3
while counts > 0:
    counts -= 1
    score = random.randint(1,100)
    print("AI评分", score)
    if score >= 90:
        print("推荐投稿")
        break
    else:
        print("继续修改")
    print("剩余次数", counts)

#AI论文助手自动优化循环
import random
counts = 3
while counts > 0:
    score = random.randint(1,100)
    print("AI评分", score)
    if score >= 90:
        print("优化成功，可以投稿")
    else:
        print("继续优化")
    counts -= 1
print("结束")