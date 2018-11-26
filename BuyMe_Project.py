### BUYME Automation TEST ###
#By Michael Masas
#Please Create a folder - C:\BuyMeAutomation - make sure All Project Files - Chromedriver.exe , Michael.jpeg and py files exists in the folder
import time
import os
from selenium import webdriver                          ##Import Web Driver Module for Web Automation
from selenium.webdriver.common.keys import Keys         ##Import Send Keys Module from selenium library

#STEP A
driver = webdriver.Chrome(executable_path='C:\BuyMeAutomation\chromedriver.exe')                                       #Define Web Driver Path
driver.get("https://buyme.co.il")                                                                                      #Surf to WebSite
time.sleep(5)                                                                                                          #Wait for Site to Load - 5 Seconds
driver.find_element_by_xpath("//*/div/header[1]/div[2]/ul/li[5]/a/span").click()                                        #Click on "הרשמה \ כניסה"
driver.find_element_by_xpath("//*/div/span/strong").click()                                                             #Click on "עוד לא נרשמתי"
first_name_form = driver.find_element_by_id("ember901").click()                                                         #Click on "שם פרטי" Text Area
driver.find_element_by_id("ember901").send_keys("מיכאל")                                                                #Fill in Personal Name
driver.find_element_by_id("ember901").send_keys(Keys.TAB)                                                               #Move To Email Text Area
email_address_form = driver.find_element_by_id("ember902").click()                                                      #Click on "מייל" Text Area
driver.find_element_by_id("ember902").send_keys("CHANGE-TO-WHATEVER444@email2.com")                                        #Fill in  Email Address
driver.find_element_by_id("ember902").send_keys(Keys.TAB)                                                               #Move To Password Area
driver.find_element_by_id("valPass").send_keys("1PassPasss112")                                                         #find Password text area and Send Password
driver.find_element_by_id("ember904").send_keys("1PassPasss112")                                                        #confirm password
driver.find_element_by_xpath("//*/div[5]/div/label").click()                                                            #Click "אני מסכים לתנאים"
driver.find_element_by_id("ember904").send_keys(Keys.ENTER)                                                             #Click On " הרשם ל BUYME" By Pressing enter
time.sleep(3)
#STEP B
driver.find_element_by_xpath(""'//*[@id="ember617_chosen"]/a/span'"").click()           #Open "בחר סכום" dropdown menu
driver.find_element_by_xpath(""'//*[@id="ember617_chosen"]/div/ul/li[4]'"").click()     #Pick "200-299" can change the brackets number for a different picking
driver.find_element_by_xpath(""'//*[@id="ember632_chosen"]/a/span'"").click()           #Open "בחר איזור" dropdown menu
driver.find_element_by_xpath(""'//*[@id="ember632_chosen"]/div/ul/li[4]'"").click()     #Pick "איזור" can change the brackets number for a different picking
driver.find_element_by_xpath(""'//*[@id="ember641_chosen"]/a/span'"").click()           #Open "קטוגריה" dropdown menu
driver.find_element_by_xpath(""'//*[@id="ember641_chosen"]/div/ul/li[3]'"").click()     #Pick "איזה סוג גיפט קארד " can change the brackets number for a different picking
driver.find_element_by_xpath(""'//*[@id="ember676"]/button'"").click()                  #Click "תמצאו לי"
time.sleep(3)
#STEP C
driver.find_element_by_xpath(""'//*[@id="ember1019"]'"").click()                         #Pick a Gift Card By Rows and columns
time.sleep(3)
driver.find_element_by_id("ember1068").send_keys("200")                                  #Insert a Price
driver.find_element_by_xpath(""'//*[@id="ember1067"]/div[2]/div/button'"").click()          #Click "לבחירה"

time.sleep(3)

#STEP D
driver.find_element_by_xpath(""'//*[@id="ember1161"]'"").click()                                                                      #Click - To Who
driver.find_element_by_xpath(""'//*[@id="ember1161"]'"").send_keys("דניאל גוטליב")                                                    #Fill in To Who
driver.find_element_by_xpath(""'//*[@id="ember1171_chosen"]/a/span'"").click()                                      #Open "סוג אירוע"
driver.find_element_by_xpath(""'//*[@id="ember1171_chosen"]/div/ul/li[2]'"").click()                                #Choose event type By Brackets
driver.find_element_by_id("ember1194").send_keys(os.getcwd()+"/Michael.jpeg")                                       #Upload a Picture - uses os Module
driver.find_element_by_xpath(""'//*[@id="ember1121"]/div[4]/div/div[1]/div[2]/div/button'"").click()                #Pick Email Button
driver.find_element_by_xpath(""'//*[@id="ember1635"]'"").send_keys("danielGotlibsmail@email.com")                  #Fill in Email Address
driver.find_element_by_xpath(""'//*[@id="ember1635"]'"").send_keys(Keys.ENTER)                                      #Click Save
#driver.find_element_by_xpath(""'//*[@id="ember1121"]/div[5]/button'"").click()                                      #Click "תשלום"



#comment

#more comments
#more Comments

















