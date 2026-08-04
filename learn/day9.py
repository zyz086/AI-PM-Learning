count = 3

while count > 0:

    print("检查", count)

    if count == 2:
        print("发现问题，停止")
        break

    count -= 1

else:
    print("全部检查完成")