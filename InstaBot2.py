from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

name = input("Enter your username: ")
passW = input("Enter your password: ")
tar = input("Enter person you want to follow and dm: ")
msg = input("Enter message to be sent: ")

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
driver.set_window_size(1024, 600)
driver.maximize_window()

driver.get("https://www.instagram.com/" + tar)
driver.implicitly_wait(5)
assert "Instagram" in driver.title

#going to log in page
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div/div/div/a").click()
driver.implicitly_wait(15)
assert "Instagram" in driver.title

#log in
elemUser = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
elemUser.send_keys(name)

elemPass = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
elemPass.send_keys(passW)

driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
driver.implicitly_wait(15)
assert "Instagram" in driver.title

#remove pop up
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
driver.implicitly_wait(15)
assert "Instagram" in driver.title

#follow
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/button").click()
time.sleep(3)

#go to dms
driver.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg").click()
#dm = driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg/path")
#action = ActionChains(driver)
#action.click(on_element=dm)
#action.perform()
time.sleep(2)

#remove another pop up
driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
time.sleep(2)

#search for person needed
driver.find_element_by_css_selector("#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.oNO81 > div.S-mcP > div > div._2NzhO.EQ1Mr > button > div > svg").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input").click()
time.sleep(2)
target = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
target.send_keys(tar)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div").click()

#send the dm
time.sleep(5)
dm = driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
dm.send_keys(msg)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()