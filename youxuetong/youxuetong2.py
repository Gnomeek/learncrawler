# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver = webdriver.Chrome()
    driver.get("http://www.youxuetong.com/main/tologin.do")
    driver.maximize_window()
    elem1 = driver.find_element_by_name("loginName")
    elem1.clear()
    elem1.send_keys("18539122639")
    elem2 = driver.find_element_by_name("loginPwd")
    elem2.clear()
    elem2.send_keys("511236")
    driver.find_element_by_id("cbxRememberPwd").click()
    driver.find_element_by_name("btnLogin").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Openloginstatus")))
    driver.switch_to_frame("Openloginstatus")
    driver.find_element_by_xpath("//a[@class='btn_tea']").click()
    return driver

def send_msg(driver,i):
    while i < 70 :
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "mainIframe")))
        driver.switch_to_default_content()
        driver.switch_to_frame("mainIframe")
        driver.switch_to_frame("iframe")
        driver.find_element_by_xpath("//input[@class='btn5'][2]").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "aui_loading")))
        #time.sleep(5)aui_content aui_state_full
        driver.switch_to_default_content()
        elem7 = driver.find_element_by_xpath("//iframe")
        s = elem7.get_attribute('name')
        driver.switch_to_frame(s)
        driver.find_element_by_xpath("//tbody/tr[last()]/td[1]/input").click()
        driver.switch_to_default_content()
        driver.find_element_by_xpath("//button[3]").click()
        driver.switch_to_frame("mainIframe")
        driver.switch_to_frame("iframe")
        elem10 = driver.find_element_by_xpath("//textarea[@name='content']")
        elem10.send_keys(u"近日天气温差较大，春季请做好流感预防工作。"+str(i))
        driver.find_element_by_class_name('btn_send').click()
        driver.find_element_by_class_name('aui_state_highlight').click()
        i += 1
        driver.refresh()

def main():
    global i
    i = 0
    driver = login()
    try:
        send_msg(driver,i)
    except:
        print i
        driver.refresh()
        send_msg(driver,i)

if __name__=='__main__':
    main()