from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

tc = input("TC: ")
password = input("Password: ")
req_driver = input("Driver Path: ")

driver = webdriver.Chrome(req_driver)
driver.delete_all_cookies()
driver.get("https://online.spor.istanbul/uyegiris")
driver.maximize_window()
driver.implicitly_wait(10)

tc = driver.find_element(By.XPATH,"//*[@id='txtTCPasaport']")
tc.send_keys(tc)
driver.implicitly_wait(10)
password = driver.find_element(By.XPATH,"//*[@id='txtSifre']")
password.send_keys(password)
driver.implicitly_wait(10)
giris= driver.find_element(By.CSS_SELECTOR,"#btnGirisYap").click()

driver.implicitly_wait(10)
kapat = driver.find_element(By.XPATH,"//*[@id='basic']/div/div[2]/button").click()
driver.implicitly_wait(10)
kiralama = driver.find_element(By.CSS_SELECTOR,"#form1 > div.page-header > div.page-header-menu > div > div > ul > li:nth-child(7) > a").click()
driver.implicitly_wait(10)

brans= Select(driver.find_element(By.XPATH,'//*[@id="ddlBransFiltre"]'))
brans.select_by_visible_text('FUTBOL')
sleep(0.5)

tesis = Select(driver.find_element(By.XPATH,'//*[@id="ddlTesisFiltre"]'))
tesis.select_by_visible_text("TEVFİK AYDENİZ SPOR TESİSİ")

seans = driver.find_element(By.XPATH,'//*[@id="pageContent_rptList_rpChild_4_lbRezervasyon_4"]')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
seans.click()
Alert(driver).accept()
sleep(0.1)
agreeement = driver.find_element(By.XPATH,'//*[@id="pageContent_cboxKiralikSatisSozlesmesi"]').click()
sleep(0.1)
add = driver.find_element(By.XPATH,'//*[@id="pageContent_lbtnSepeteEkle"]').click()

sleep(99999)

