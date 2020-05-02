from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
username="uday.zzz"
pwd="Uday1024"
time.sleep(3)
driver.maximize_window()#fullscreen_window()
text_area = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
text_area.send_keys(username)
text_area = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
text_area.send_keys(pwd)
submit_butn = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')[0]
submit_butn.click()

time.sleep(4)
submit_butn = driver.find_elements_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')[0] #optional
submit_butn.click()
# submit_butn = driver.find_element_by_class_name('_8-yf5')[1] #feed
# submit_butn.click()

submit_butn = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[3]/div[1]/a/div')[0] #optional
submit_butn.click()
try:
    for j in range(1,10):
        for i in range(1,81):
            submit_butn = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(i)+']/div[3]/button')[0]
            print('//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(i)+']/div[3]/button')
            submit_butn.click()
            time.sleep(2)
        driver.refresh()
        time.sleep(180)
except:
    pass

#content.click()
#print(content)
