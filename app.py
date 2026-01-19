# from db_config import User
from tool import display_all_user, add_new_user, find_name, delete_user_name, update_user

welcome = open("welcome.txt", "r").read()
print(welcome)

while True:
    cmd = input("\nYour command > ").upper()  # コマンドを受け取る

    if cmd == "S":
        display_all_user()
    elif cmd == "A":
        new_name = input("New user name > ")
        new_age = input("New user age > ")
        # ブランクの場合
        if not new_name:
            print("User name can't be blank")
            continue
        elif not new_age:
            print("User name can't be blank")
            continue
        # ユーザー名は1文字以上20文字以下であること
        elif not (1 <= len(new_name) <= 20):
            print("User name is too long(maximun is 20 characters)")
            continue
        # 年齢は正の整数であること
        elif isinstance(new_age, str) and "." in new_age:
            print("Age is not positive integer")
            continue
        # 年齢は0以上120以下であること
        elif not (0 <= int(new_age) <= 120):
            print("Age is grater than 120")
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
