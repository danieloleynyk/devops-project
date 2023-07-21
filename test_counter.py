from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

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
driver = webdriver.Chrome(service=se,options=chrome_options)

url = "http://localhost:3000"
driver.get(url)

def test_counter_increment_and_decrement():
  input_counter_element = driver.find_element(By.XPATH,"//*[@id='root']/div/div/input")
  input_counter_element.send_keys(0)

  btn_inc = driver.find_element(By.CLASS_NAME,"btn-inc")
  btn_inc.click()
  btn_inc.click()
  driver.find_element(By.ID,"btn-dec").click()
  
  counter = input_counter_element.get_attribute("value")
  print(counter)
  try:
      assert counter == "1", "Wrong result"
  except AssertionError:
      print("Failed to decrecment or increcment")
      driver.quit()
      exit(1)
      
def test_upper_limit_error_message():
  input_counter_element = driver.find_element(By.CSS_SELECTOR,"#root > div > div > input")
  input_counter_element.send_keys(20)

  try:
    err_message = driver.find_element(By.XPATH,"//*[@id='root']/div/div/p").text
    print(err_message)
    
    assert err_message != "Counter reached the upper limit", "Wrong result"
  except AssertionError:
      print("Failed to upload limit error message")
      driver.quit()
      exit(1)
      
def test_reset_button():
  input_counter_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/input")
  input_counter_element.send_keys(2)
  driver.find_element(By.CLASS_NAME,"btn-reset").click()
  counter = input_counter_element.get_attribute("value")

  print(counter)
  try:
    assert counter == "0", "Wrong result"
  except AssertionError:
      print("Failed to reset the counter")
      driver.quit()
      exit(1)
  