#AI论文助手权限检测系统
#目标：模拟一个期刊平台判断用户能不能使用AI检查

user_name = input("Enter your name: ")
is_login = True
has_paper = True
is_banned = False
quota = int(input("请输入AI剩余检查次数: "))
if is_login and has_paper and not is_banned and quota > 0:
    print(user_name,"可以使用论文检查","剩余次数：",quota)#错误：字符串的“剩余次数”和变量quota没有连接
else:
    print("暂时无法使用论文检查")