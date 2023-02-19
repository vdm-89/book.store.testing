#import time
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
#driver.maximize_window() # раскрываем окно браузера на весь экран
#driver.get("https://practice.automationtesting.in/")
#Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
#Account.click()
#Email = driver.find_element_by_name("email")
#Email.send_keys("Voldemort.volodyan@yandex.ru")
#Password = driver.find_element_by_id("reg_password")
#Password.send_keys("Insert1989@")
#Register = driver.find_element_by_name("register")
#Register.click()



#import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
#driver.maximize_window() # раскрываем окно браузера на весь экран
#driver.get("https://practice.automationtesting.in/")
#Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
#Account.click()
#Username = driver.find_element_by_id("username")
#Username.send_keys("Voldemort.volodyan@yandex.ru")
#Password = driver.find_element_by_id("password")
#Password.send_keys("Insert1989@")
#Login = driver.find_element_by_name("login")
#Login.click()
#some_element= WebDriverWait(driver, 10).until(
#EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li[class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']"), "Logout"))


