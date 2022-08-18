import time
import asyncio
import aiohttp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'eager'
#Credenciales de ingreso
userNZ = 'MarceRodriguez'
passNZ= 'Marce1990'

URL='https://online.immigration.govt.nz/'

driver = webdriver.Chrome('./WebDriver/chromedriver.exe', options=options)
#driver.get('https://saeriego.tech')
async def login():
    async with aiohttp.ClientSession() as session:
        driver.get(URL)
        async with session.get(URL) as resp:
            if resp.status == 200:
                elementUser= driver.find_element(By.ID,'signInName')
                elementUser.send_keys(userNZ)
                ElementPass=driver.find_element(By.ID,'password')
                ElementPass.send_keys(passNZ)
#boton loggin
    time.sleep(10)
    driver.find_element(By.ID, 'next').click()
        


loop = asyncio.get_event_loop()
loop.run_until_complete(login())


