#AI论文助手会员系统v1
user_name = input("请输入你的名字: ")
age = input("请输入你的年龄：")
points = int(input("请输入你的积分："))

if points >= 1000:
    level = "专业用户"
elif points < 1000:
    level = "高级用户"
else:
    level = "普通用户"

print(user_name, "你的等级是", level)