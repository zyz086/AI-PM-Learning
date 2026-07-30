#AI论文助手会员系统v1.2

user_name = input("请输入你的名字: ")
age = input("请输入你的年龄：")
points = int(input("请输入你的积分："))

if points >= 1000:
    level = "专业用户"
elif points >= 500:
    level = "高级用户"
else:
    level = "普通用户"

if level == "专业用户":
    rate = 50
elif level == "高级用户":
    rate = 80
else:
    rate = 100

times,remain = divmod(points,rate)

counts = 3
while counts > 0:
     choice = input("是否需要检查：（是/否：）")
     if choice == "是":
         counts -= 1
         print("检查完成，剩余次数：",counts)
     else:
          break
print("AI检查结束")


print(user_name,"你的等级是：",level)
print("你的积分可以兑换",times,"次检查")
print("剩余积分",remain)
