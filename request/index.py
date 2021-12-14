from time import sleep
from request import main
from selenium import webdriver
from selenium.webdriver.common.by import By
class Test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.111.128:90")
    try:
        # driver.find_element_by_xpath('//*[@id="site-topbar"]/div/div[2]/ul/li[3]/a').click()
        driver.find_element(By.XPATH, '//*[@id="site-topbar"]/div/div[2]/ul/li[3]/a').click()
        print("程序正常运行")
    except:
        print("登陆按钮点击失败")
    # driver.find_element_by_id("loginAccount").send_keys("dlh")
    driver.find_element(By.ID,"loginAccount").send_keys(main.Requ.username)
    # driver.find_element_by_id("loginPassword").send_keys("123456")
    driver.find_element(By.ID,"loginPassword").send_keys(main.Requ.password)
    # driver.find_element_by_class_name("btn btn-primary").click()
    try:
        driver.find_element(By.XPATH,'//*[@id="user-login-form"]/div[4]/div/button[1]').click()
        print("会员登陆成功")
    except:
        print("会员登陆失败")
        print(main.Requ.username)
        print(main.Requ.password)

