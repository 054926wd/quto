import flask,json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
class Requ():
    server=flask.Flask(__name__)
    @server.route('/',methods=['POST'])
    def index():
            global username, password
            try:
                res = {'msg': '接口调用失败', 'msg_code': 404}
                username=flask.request.values.get('username')
                password=flask.request.values.get('password')
                print(username)
                print(password)
            except:
                print("接口调用失败")
                return res
            try:
                req = {"req":"运行成功","req_code":201}
                req_error = {"req_error":"网站打开失败","req_code":500}
                driver = webdriver.Chrome()
                sleep(2)
                driver.maximize_window()
                driver.get("http://192.168.111.128:90")
                try:
                    # driver.find_element_by_xpath('//*[@id="site-topbar"]/div/div[2]/ul/li[3]/a').click()
                    driver.find_element(By.XPATH, '//*[@id="site-topbar"]/div/div[2]/ul/li[3]/a').click()
                    print("程序正常运行")
                except:
                    print("登陆按钮点击失败")
                # driver.find_element_by_id("loginAccount").send_keys("dlh")
                driver.find_element(By.ID, "loginAccount").send_keys(username)
                sleep(2)
                # driver.find_element_by_id("loginPassword").send_keys("123456")
                driver.find_element(By.ID, "loginPasswor").send_keys(password)
                sleep(2)
                # driver.find_element_by_class_name("btn btn-primary").click()
                try:
                    driver.find_element(By.XPATH, '//*[@id="user-login-form"]/div[4]/div/button[1]').click()
                    print("会员登陆成功")
                except:
                    print("会员登陆失败")
                sleep(5)
                return req
            except:
                print("网站运行失败")
                return req_error
    server.run(port=8083, debug=True, host='192.168.1.105')
