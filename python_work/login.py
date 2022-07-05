def login():
    """初始化登录界面"""
    try:
        with open('resources/password.txt','r') as p:
            password = p.read()
        with open('resources/users.txt','r') as p:
            username = p.read()
        print('登录：')
        while True:
            username1 = input('用户名:')
            password1 = input('密码:')
            if password == password1 or username1 == username:
                break
            else:
                print('密或用户名错误，请再试一次')
                continue
    except FileNotFoundError:
        print('注册：')
        username = input('用户名:')
        password = input('密码:')
        with open('resources/password.txt','w') as p:
            p.write(password)
        with open('resources/users.txt','w') as p:
            p.write(username)


