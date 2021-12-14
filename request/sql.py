import pymysql.cursors
import flask,json
class Sql():
    server=flask.Flask(__name__)
    @server.route('/',methods=['POST'])
    def index():
        global i
        try:
            res={'msg':'接口调用成功','msg_code':200}
            id=flask.request.values.get('id')
            modu=flask.request.values.get('modu')
            print(id)
            print(modu)
        except:
            print("接口调用失败")
        try:
            connect = pymysql.connect(
                host="192.168.111.128",
                port=3306,
                user="admin",
                passwd="054926wd",
                db='admin',
                charset='utf8'
                )
            print("数据库连接成功")
        except:
            print("数据库连接失败")
        cursor = connect.cursor()
        try:
            inputname = "SELECT inputname,hash,classhash FROM `_avinput` where id = '%id'"
            cursor.execute(inputname)
            data = cursor.fetchall()
            for i in data[:]:
                print(i)
            modu = "select modulename from _avmodule where hash = '%modu'"
            cursor.execute(modu)
            tata = cursor.fetchall()
            for a in tata[:]:
                print(a)
            print("数据查询成功")
            req = {"id":i,"modu":a}
            return json.dumps(req)
        except:
            print("数据查询失败")
    server.run(port=8084, debug=True, host='192.168.1.104')
