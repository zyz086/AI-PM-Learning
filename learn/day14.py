#AI论文助手用户信息
user = {"name":"郑亚舟","专业":"计算机","积分":700,"会员等级":"高级用户"}
user["积分"] = 800
user["AI检查次数"] = 5
print(user["name"])
print(user)

#复习
paper = {
    "title":"AI教育研究",
    "score":95,
    "status":"通过"
}
print(paper["title"])
paper["score"] = 80
paper["author"] = "张三"
print(paper)

check_result = {
    "逻辑":85,
    "创新":90,
    "引用":70
}

print(check_result["创新"])
check_result["引用"] = 80
check_result["总体评价"] = "建议修改"
for key,value in check_result.items():
    print(key,value)

