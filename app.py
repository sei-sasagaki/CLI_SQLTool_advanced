# from db_config import User
from tool import display_all_user, add_new_user, find_name, delete_user_name, update_user, valid_user

welcome = open("welcome.txt", "r").read()
print(welcome)

while True:
    cmd = input("\nYour command > ").upper()  # コマンドを受け取る

    if cmd == "S":
        display_all_user()
    elif cmd == "A":
        new_name = input("New user name > ")
        new_age = input("New user age > ")

        # 入力内容のバリデーション（Falseを返したらcontinue）
        if not valid_user(new_name=new_name, new_age=new_age):
            continue

        # バリデーションOKの場合
        add_new_user(new_name=new_name, new_age=new_age)
    elif cmd == "F":
        find_name()
    elif cmd == "D":
        delete_user_name()
    elif cmd == "E":
        update_user()
    elif cmd == "Q":
        print("Bye!")
        break
    else:
        print(f"{cmd.lower()}: command not found")
