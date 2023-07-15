import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
options= [
  "--headless",
  "--disable-gpu",
  "--window-size=1920,1200",
  "--ignore-certificate-errors",
  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage"
]
for option in options:
  chrome_options.add_argument(option)
  
se = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
driver = webdriver.Chrome(service=se,options=options)

def test_inc():
    url = "http://localhost:3000"
    
    driver.get(url)

    driver.find_element(By.CLASS_NAME,"btn-dec").click()
    input_counter_element = driver.find_element(By.XPATH,"//*[@id='root']/div/div/input")
    counter = input_counter_element.get_attribute("value")

    print(counter)
    try:
        assert counter == "-1", "Wrong result"
    except AssertionError:
        print("Failed to decrecment")
        driver.quit()
        exit(1)

