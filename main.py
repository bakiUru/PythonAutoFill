from http import cookies
import time
import os
import aiohttp
from bs4 import BeautifulSoup
from requests import request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from twocaptcha import TwoCaptcha
from recaptcha import API_KEY
import requests

os.system('./reconnect.bat')
#CAPTCHA
solver = TwoCaptcha(API_KEY)
#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.page_load_strategy = 'eager'
#Credenciales de ingreso
userNZ = 'MarceRodriguez'
passNZ= 'Marce1990'


###FUNCIONES##
urlCaptcha='https://onlineservices.immigration.govt.nz/rs-captcha?redirect=%2FWorkingHoliday%2FWizard%2FPersonal1.aspx%3FApplicationId%3D2901560%26IndividualType%3DPrimary%26IndividualIndex%3D1%26StatusChanged%3DFalse'
siteKey = '6LeSrCAgAAAAAJfZTH_T47uoIvabVp05FX1grYmD'

def get_csrf_cookie(url):
    response = requests.get(urlCaptcha)
    soup = BeautifulSoup(response.text, 'lxml')
    csrf_element = soup.select_one('[id=recaptcha-token]')
    csrf = csrf_element['value']
    cookies = response.cookies
    return csrf, cookies

def solve(url, sitekey):
    try:
        result = solver.recaptcha(sitekey=siteKey, url=urlCaptcha)
    except:
        print("FILED to solve CAPTCHA")
        
    return result
def post_page(url,csrf, cookie, result):
    payload='key={}&value={}'

def reCaptcha():
    csrf, cookie = get_csrf_cookie(urlCaptcha)
    result = solve(urlCaptcha,siteKey)


#localizacion del wevDriver Chrome
driver_path='./WebDriver/chromedriver.exe'
URL='https://onlineservices.immigration.govt.nz/'


driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.get(URL)

WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.NAME,'username')))\
        .send_keys(userNZ)
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.NAME,'password')))\
        .send_keys(passNZ)
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.CLASS_NAME,'button-large-primary')))\
        .click()
        

###########################################################################
#Selecciono la ruta de Working Holiday
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.XPATH, "/html/body/div/form/div/div[2]/div/div[3]/a")))\
        .click()
############################################################################
""" Cuando se trate de URUGUAY
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr[2]/td/div/div/div[3]/div[44]/a")))\
        .click()
    """
###########################################################################   
#Pruebas con Italia
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr[2]/td/div/div/div[3]/div[19]/a")))\
        .click()

#Button Aply NOW
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_applyNowButton')))\
        .click()
#Recaptcha ---install --> twocaptcha --- BeutifulSoup Lxml
reCaptcha()
#buton Submit----> FORMULARIOS
WebDriverWait(driver,5)\
    .until(EC.presence_of_element_located((By.ID,'ContentPlaceHolder1_submitImageButton')))\
        .click()



##########################
###OTRAS PRUEBAS############

async def login():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            if resp.status == 200:
                elementUser= driver.find_element(By.TAG_NAME,'username')
                elementUser.send_keys(userNZ)
                ElementPass=driver.find_element(By.TAG_NAME,'password')
                ElementPass.send_keys(passNZ)
                WebDriverWait(driver,5)\
                    .until(EC.element_to_be_clickable((By.TAG_NAME,'username')))\
                        .send_keys(userNZ)
                WebDriverWait(driver,5)\
                    .until(EC.element_to_be_clickable((By.TAG_NAME,'password')))\
                        .send_keys(passNZ)
#boton loggin
    time.sleep(10)
    driver.find_element(By.ID, 'next').click()        
#loop = asyncio.get_event_loop()
#loop.run_until_complete(login())


