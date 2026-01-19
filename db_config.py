import os
from dotenv import load_dotenv
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField

# .envの読み込み
load_dotenv(override=True)

# データベースへの接続設定
db = connect(os.environ.get("DATABASE"))


# ユーザーのモデル
class User(Model):
    """User Model"""

    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])
