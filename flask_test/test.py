from click import confirm
from flask import Flask
from flask import render_template
from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os.path

app = Flask(__name__)
  

def insert(data):
    #db initial
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "test.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    print('sqltest')
    cursor.execute('insert into username(name) values (?)', (data,))
    connection.commit()

def list():
    #db initial
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "test.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * from username")
    data_rows = cursor.fetchall()#資料陣列
    #for row in data_rows:
        #data_list = list(row)
        #text_str = "("+str(data_list[0])+"  "+str(data_list[1])+")"      
        #print(data_list)
    print(data_rows)
    connection.close()



@app.route("/")
def home():
    return render_template("css_test.html")

#建立一名為 page 之路由
@app.route('/page')
def pageAppInfo():
    #建立字典
    appInfo = {  # dict
        'id': 5,
        'name': 'Python - Flask',
        'version': '1.0.1',
        'author': 'Enoxs',
        'remark': 'Python - Web Framework'
    }
    #將資料傳給前端之語法 appInfo(html)=appInfo(python)
    return render_template('page.html', appInfo=appInfo)

@app.route('/data')
def pageData():
    data = {  # dict
        '01': 'Text Text Text',
        '02': 'Text Text Text',
        '03': 'Text Text Text',
        '04': 'Text Text Text',
        '05': 'Text Text Text'
    }
    return render_template('data.html', data=data)

@app.route('/form')
def formPage():
    return render_template('Form.html')
#多表格提交判斷
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if  request.method == 'POST' :
        if request.values['send']=='submit_01':
            user = request.form['user']
            print("post : user => ", user)
            # sql insert 存入 sqlite 語法
            #data = [user]
            insert(user)
            return redirect(url_for('success', name=user, action="post", confirm = "01"))
        elif request.values['send']=='submit_02':
            user = request.form['user']
            print("post : user => ", user)
            #data = [user]
            insert(user)
            return redirect(url_for('success', name=user, action="post", confirm = "02"))  
    else:
        user = request.args.get('user')
        print("get : user => ", user)
        insert(user)
        return redirect(url_for('success', name=user, action="get", confirm = "03"))

    # else:
    #     user = request.args.get('user')
    #     print("get : user => ", user)
    #     return redirect(url_for('success', name=user, action="get"))

@app.route('/success/<action>/<name>/<confirm>')
def success(name, action,confirm):
    #db initial
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "test.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * from username")
    data_rows = cursor.fetchall()#資料陣列
    #for row in data_rows:
        #data_list = list(row)
        #text_str = "("+str(data_list[0])+"  "+str(data_list[1])+")"      
        #print(data_list)
    print(data_rows)
    connection.close()
    return render_template("result.html",data_rows=data_rows)

    #return '{} : Welcome {} ~ !!!'.format(action, name)



app.run(host='0.0.0.0',port=5000,debug=True)