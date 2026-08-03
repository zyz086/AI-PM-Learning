#AI论文投稿权限检查
is_login = True
has_paper = True
ai_check_done = False
if is_login:#这里的is_login是布尔值所以不需要写is_login == True
    if has_paper:
        if ai_check_done:
            print("允许投稿")
        else:
            print("先完成AI检查")
    else:
        print("请先上传论文")
else:
    print("先登录")
