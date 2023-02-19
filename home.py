import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
Read_more = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product/selenium-ruby/']")
Read_more.click()
Reviews = driver.find_element_by_css_selector("a[href='#tab-reviews']")
Reviews.click()
Five_star = driver.find_element_by_css_selector("a[class='star-5']")
time.sleep(5)
Five_star.click()
Comment = driver.find_element_by_id("comment")
Comment.send_keys("Nice book!")
Name = driver.find_element_by_id("author")
Name.send_keys("Vladimir")
Email = driver.find_element_by_id("email")
Email.send_keys("milliganb43@gmail.com")
Submit = driver.find_element_by_name("submit")
Submit.click()
driver.quit()



