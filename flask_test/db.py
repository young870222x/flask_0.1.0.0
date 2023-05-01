import sqlite3
import os.path

#定義資料庫位置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")
connection = sqlite3.connect(db_path)

cursor = connection.cursor()

nametest = input('please input name \n')
info = input('please input info \n')

cursor.execute('insert into moredata(name,info) values (?,?)', (nametest,info,))
connection.commit()

cursor.execute("SELECT * from moredata")
data_rows = cursor.fetchall()#資料陣列
for row in data_rows:
    print(row[0],row[1],row[2])


# cursor.execute("SELECT * from username")
# data_rows = cursor.fetchall()
# for row in data_rows:
#     print(row)

connection.close()
print(BASE_DIR)
print(db_path)


