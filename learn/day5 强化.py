#AI论文助手权限检测系统v1.1
#目标：模拟一个期刊平台判断用户能不能使用AI检查

user_name = input("Enter your name: ")
is_login = True
has_paper = True
is_banned = False
quota = int(input("请输入AI剩余检查次数: "))
if not is_login:
    print("请先登录")
elif not has_paper:
    print("请上传论文")
elif is_banned:#错误：is_banned表示的是被封禁的用户
    print("账号异常")
elif quota <= 0:#忘记写等号了
    print("额度用完了")
else:
    print(user_name,"可以使用检查")