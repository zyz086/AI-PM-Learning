#条件语句复习 AI论文自动推荐系统
score = int(input("请输入分数："))
has_paper = True
is_login = True
if has_paper and is_login and score >= 90:#优先级搞错了，应该优先判断是否登录和是否上传论文
    print("推荐顶刊")
elif has_paper and is_login and score >= 70:
    print("推荐普刊")
elif has_paper and is_login and score < 70:
    print("建议修改")
elif not has_paper and is_login:
    print("请登录")#条件变量写反了
else:
    print("请上传论文")

score = int(input("请输入分数："))
has_paper = True
is_login = True
if not is_login:
    print("先登录")
elif not has_paper:
    print("先上传论文")
elif score >= 90:
    print("推荐顶刊")
elif score >= 70:
    print("推荐普刊")
else:
    print("建议修改")