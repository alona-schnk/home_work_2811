def password_required(info):
    """
    Запитує у користувача пароль перед викликом кожної з функцій.
    Якщо пароль вірний, то секретні дані виводяться на екран.
    :param info:
    :return: password_verify()
    """
    def password_verify():
        password = input("Enter password: ")
        if password == "zxcv":
            info()
        else:
            print("Default password!")
    return password_verify()


def bank_credentials():
    print("Bank card: 0000-1111-2222-3333-4444")
    print("Bank password: 1234")
    print("amount: 100 000 000$")


def instagram_credentials():
    print("username: snowden")
    print("password: cia")


password_required(bank_credentials)
password_required(instagram_credentials)



