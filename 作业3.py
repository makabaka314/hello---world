count = 1
while count <= 3:
    username = input('请输入用户名:')
    pwd = input('请输入密码:')
    if username == 'zhangsan' and pwd == '123':
        print('登陆成功! ')
        break
    elif count < 3:
        print('用户名或密码错误')
        count += 1
    elif count == 3:
        choice = input('是否继续尝试登录？（Y/N）')
        if choice == 'N':
            break
        elif choice == 'Y':
            count = 1
            continue
        else:
            print('登陆失败! ')

            break