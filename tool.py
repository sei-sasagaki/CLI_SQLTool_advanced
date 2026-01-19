from db_config import User


def display_all_user():
    """
    要件：ユーザー一覧表示
    """
    users = User.select()
    for user in users:
        print(f"Name: {user.name} Age: {user.age}")


def add_new_user(new_name, new_age):
    """
    要件：新規ユーザー追加
    要件：ユーザー名の重複を許可しない
    要件：バリデーション
    """
    # # ブランクの場合
    # if not new_name:
    #     print("User name can't be blank")
    # if not new_age:
    #     print("User name can't be blank")
    # # ユーザー名は1文字以上20文字以下であること
    # if not (1 <= len(new_name) <= 20):
    #     print("User name is too long(maximun is 20 characters)")
    # # 年齢は正の整数であること
    # if new_age < 0 or isinstance(new_age, str) and "." in new_age:
    #     print("Age is not positive integer")
    # # 年齢は0以上120以下であること
    # if not (0 <= new_age <= 120):
    #     print("Age is grater than 120")
    # バリデーションOKの場合
    if User.get_or_none(User.name == new_name) is None:
        new_user = User(name=new_name, age=new_age)
        new_user.save()
        print(f"Add new user: {new_name}")
    else:
        print(f"Duplicated user name {new_name}")


def Validation(new_name, new_age):
    pass
    # new_name = input("New user name > ")
    # new_age = int(input("New user age > "))
    # ブランクの場合
    # if not new_name:
    #     raise ValueError("User name can't be blank")
    # if not new_age:
    #     raise ValueError("User name can't be blank")
    # # ユーザー名は1文字以上20文字以下であること
    # if not (1 <= len(new_name) <= 20):
    #     raise ValueError("User name is too long(maximun is 20 characters)")
    # # 年齢は正の整数であること
    # if new_age < 0 or isinstance(new_age, str) and "." in new_age:
    #     raise ValueError("Age is not positive integer")
    # # 年齢は0以上120以下であること
    # if not (0 <= new_age <= 120):
    #     raise ValueError("Age is grater than 120")


def find_name():
    """
    要件：ユーザー検索機能を追加
    """
    check_name = input("User name > ")
    user = User.get_or_none(User.name == check_name)
    if user:
        print(f"Name: {user.name} Age: {user.age}")
    else:
        print(f"Sorry, {check_name} is not found")


def delete_user_name():
    """
    要件：ユーザー削除機能を追加
    """
    del_name = input("User name > ")
    user = User.get_or_none(User.name == del_name)
    if user:
        user.delete_instance()
        print(f"User {del_name} is deleted")
    else:
        print(f"Sorry, {del_name} is not found")


def update_user():
    """
    要件：ユーザー編集機能を追加
    """
    update_name = input("User name > ")
    user = User.get_or_none(User.name == update_name)
    if user:
        new_name = input(f"New user name({user.name}) > ")
        new_age = int(input(f"New user age({user.age}) > "))
        user.name = new_name
        user.age = new_age
        user.save()
        print(f"Update user: {new_name}")
    else:
        print(f"Sorry, {update_name} is not found")

# print(f"{cmd.lower()}: command not found")


if __name__ == "__main__":
    new_name = "bob"
    if User.get_or_none(User.name == new_name) is None:
        print(f"{new_name}はありません")
