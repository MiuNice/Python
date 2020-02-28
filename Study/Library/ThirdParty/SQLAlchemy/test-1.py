from sqlalchemy import Column, String, create_engine, Integer, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

db_parameter = {
    "username": "root",
    "password": "root",
    "host": "localhost",
    "port": 3306,
    "db": "test_db",
    "charset": "utf8"
}
db_url = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset={charset}".format(
    username=db_parameter["username"], password=db_parameter["password"], host=db_parameter["host"],
    port=db_parameter["port"], db=db_parameter["db"], charset=db_parameter["charset"]
)


# engine = create_engine(db_url)
# conn = engine.connect()
# # result = conn.execute("select 1")
# sql = "insert into t1 (name, age) values ('tom1', 18)"
# result = conn.execute(sql)


class User(Base):
    __tablename__ = "t1"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)


engine = create_engine(db_url, pool_size=20, max_overflow=0, echo=True)
db_session = sessionmaker(bind=engine)
session = db_session()

# user = User(id=1, name='1', age=None)
# # 添加
# session.add(user)
# # 提交
# session.commit()
# # 关闭
# session.close()


# 插入
# [[name, age],[name, age],...]
# t = [{"id": 2, "name": "1", "age": 18}, {"id": 3, "name": "1", "age": 18}, {"id": 4, "name": "1", "age": 18},
#      {"id": 5, "name": "1", "age": 18}, {"id": 6, "name": "1", "age": 18}]
# for i in t:
#     user = User(id=i["id"], name=i["name"], age=i["age"])
#     session.add(user)
# session.commit()
# session.close()

# 查询
t1 = session.query(User)
for i in t1.all():
    print(i.id, i.name, i.age)

for i2 in t1.filter(User.id > 4).all():
    print(i2.id)

# 更新
t1.filter(User.id == 6).update({User.name: "2"})
# 删除
t1.filter(User.id == 5).delete()
session.commit()

for i in t1.all():
    print(i.id, i.name, i.age)

from sqlalchemy.orm import aliased

# 表别名
user_alias = aliased(User, name="user_alias")
for i in session.query(user_alias):
    print(i.name)

# 字段别名
for i in session.query(user_alias.name.label("user_name")).all():
    print(i.user_name)

from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=engine)
session = Session_class()
# query = session.query(User, User).join(User, User.name == User.name).all()

u1 = aliased(User)
u2 = aliased(User)
q = session.query(u1.name.label("u1_name"), u2.name).join(u2, u1.name == u2.name, isouter=True).all()
print(*q)

q2 = session.query(u1.name, u1.id).all()
print(*q2)
# session.query(u1.name.label(creatorname),modifier.name).join(creator,creator.id==ap.id,isouter=true)(isouter=true表示左连接).join(modifier,modifier.id==ap.id,isouter=true)
p = session.query(u1.id).limit(3).all()
print(p)

p2 = session.query(u1.id).limit(2).offset(0).all()
print(p2)

q3 = session.query(func.concat(u1.id, u1.name)).all()
print(q3)

q4 = session.query(func.ifnull(u1.age, 0)).all()
print(q4)

# import time
# start_time = time.time()
# for _ in range(100000):
#     session.query(u1.name.label("u1_name"), u2.name).join(u2, u1.name == u2.name, isouter=True).all()
# print(time.time() - start_time)
