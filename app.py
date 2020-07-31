import pymysql
import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# 新增 一筆 資料
@app.route('/restfulapi', methods=['POST'])
def add_product():
    name = request.json['name']
    try:
        connect_database = pymysql.connect(host='database-test-two.cqiihvqn7gdj.us-east-1.rds.amazonaws.com',
                                           user='admin',
                                           passwd='7M4fjqWx3pVPd7luDHSS',
                                           db='utf8_schema',
                                           charset='utf8'
                                           )
        print(':: 成功連線mySQL')

        cursor = connect_database.cursor()
        # 新增資料
        cursor.execute('INSERT INTO `restfualAPI`(`name`)' + 'VALUES(%s)',
                       [name])
        connect_database.commit()

        connect_database.close()
        print(':: 結束連線mySQL')
        return f'{name} - 新增成功'
    except Exception as e:
        return e


# 查詢 所有 資料
@app.route('/restfulapi', methods=['GET'])
def search_all():
    try:
        connect_database = pymysql.connect(host='database-test-two.cqiihvqn7gdj.us-east-1.rds.amazonaws.com',
                                           user='admin',
                                           passwd='7M4fjqWx3pVPd7luDHSS',
                                           db='utf8_schema',
                                           charset='utf8'
                                           )
        print(':: 成功連線mySQL')

        cursor = connect_database.cursor()
        # 搜尋資料 fetchall
        cursor.execute('SELECT * FROM `restfualAPI`')
        r = cursor.fetchall()
        return_list = []
        for ele in r:
            #print(list(ele))
            return_list.append(list(ele))

        connect_database.close()
        print(':: 結束連線mySQL')
        return str(return_list)
    except Exception as e:
        return e

# 查詢 一筆 資料
@app.route('/restfulapi/<id>', methods=['GET'])
def search_one(id):
    try:
        connect_database = pymysql.connect(host='database-test-two.cqiihvqn7gdj.us-east-1.rds.amazonaws.com',
                                           user='admin',
                                           passwd='7M4fjqWx3pVPd7luDHSS',
                                           db='utf8_schema',
                                           charset='utf8'
                                           )
        print(':: 成功連線mySQL')

        cursor = connect_database.cursor()
        # 搜尋資料 fetchall
        cursor.execute('SELECT * FROM `restfualAPI`WHERE `id`=%s',[id])
        r = cursor.fetchall()
        return_list = []
        for ele in r:
            #print(list(ele))
            return_list.append(list(ele))

        connect_database.close()
        print(':: 結束連線mySQL')
        return str(return_list)
    except Exception as e:
        return e


# 更新 一筆 資料
@app.route('/restfulapi/<id>', methods=['PUT'])
def update_product(id):
    name = request.json['name']
    try:
        connect_database = pymysql.connect(host='database-test-two.cqiihvqn7gdj.us-east-1.rds.amazonaws.com',
                                           user='admin',
                                           passwd='7M4fjqWx3pVPd7luDHSS',
                                           db='utf8_schema',
                                           charset='utf8'
                                           )
        print(':: 成功連線mySQL')

        cursor = connect_database.cursor()
        # 新增資料
        cursor.execute('UPDATE `restfualAPI` SET `name`=%s WHERE `id`=%s',
                       [name, id])
        connect_database.commit()

        connect_database.close()
        print(':: 結束連線mySQL')
        return f'{name} - 新增成功'
    except Exception as e:
        return e


# 刪除 一筆 資料
@app.route('/restfulapi/<id>', methods=['DELETE'])
def DELETE(id):
    try:
        connect_database = pymysql.connect(host='database-test-two.cqiihvqn7gdj.us-east-1.rds.amazonaws.com',
                                           user='admin',
                                           passwd='7M4fjqWx3pVPd7luDHSS',
                                           db='utf8_schema',
                                           charset='utf8'
                                           )
        print(':: 成功連線mySQL')

        cursor = connect_database.cursor()
        # 刪除資料
        cursor.execute('SELECT * FROM `restfualAPI`WHERE `id`=%s',[id])
        r = cursor.fetchone()
        return_list = list(r)

        cursor.execute('DELETE FROM `restfualAPI` WHERE `id`=%s', [id])
        connect_database.commit()

        connect_database.close()
        print(':: 結束連線mySQL')
        return '已經刪除下列資料:\n'+str(return_list)
    except Exception as e:
        return e


# heroku專用，偵測heroku給我們的port
app.run(host='0.0.0.0', port=os.environ['PORT'])