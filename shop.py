#import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium import webdriver
#driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
#driver.maximize_window()
#driver.get("https://practice.automationtesting.in/")
#Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
#Shop.click()
#driver.execute_script("window.scrollBy(0,300);")
#Book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=165']")
#Book.click()
#time.sleep(5)
#Basket = driver.find_element_by_css_selector("span[class='cartcontents']")
#Basket.click()
#proceed_to_checkout_btn = WebDriverWait(driver, 20).until(
#EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='checkout-button button alt wc-forward']")))
#proceed_to_checkout_btn.click()
#some_element = WebDriverWait(driver, 10).until(
#EC.text_to_be_present_in_element((By.CSS_SELECTOR, "label[for='billing_first_name']"), "First Name "))
#First_Name = driver.find_element_by_id("billing_first_name")
#First_Name.send_keys("Steven")
#Last_Name = driver.find_element_by_id("billing_last_name")
#Last_Name.send_keys("Gerrard")
#Company_Name = driver.find_element_by_id("billing_company")
#Company_Name.send_keys("CD RED PROJECT")
#Email = driver.find_element_by_id("billing_email")
#Email.send_keys("derley63@yandex.ru")
#Phone = driver.find_element_by_id("billing_phone")
#Phone.send_keys("89295183502")
#Selector = driver.find_element_by_css_selector("[role='presentation']>b")
#Selector.click()
#Search = driver.find_element_by_id("s2id_autogen1_search")
#Search.send_keys("Russia")
#Select = driver.find_element_by_id("select2-result-label-394")
#Select.click()
#Address = driver.find_element_by_id("billing_address_1")
#Address.send_keys("Novgorodskaya")
#City = driver.find_element_by_id("billing_city")
#City.send_keys("Moscow")
#State = driver.find_element_by_id("billing_state")
#State.send_keys("Colorado")
#ZIP = driver.find_element_by_id("billing_postcode")
#ZIP.send_keys("127576")
#driver.execute_script("window.scrollBy(0,600);")
#time.sleep(5)
#Check_Payments_btn = driver.find_element_by_id("payment_method_cheque")
#Check_Payments_btn.click()
#Place_Order_btn = driver.find_element_by_id("place_order")
#Place_Order_btn.click()
#some_element_1 = WebDriverWait(driver, 10).until(
#EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-thankyou-order-received']"), "Thank you. Your order has been received. "))
#some_element_2 = WebDriverWait(driver, 10).until(
#EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='method']>strong"), "Check Payments"))


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
Account.click()
Username = driver.find_element_by_id("username")
Username.send_keys("Voldemort.volodyan@yandex.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("Insert1989@")
Login = driver.find_element_by_name("login")
Login.click()
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
Book = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product/android-quick-start-guide/']")
Book.click()
book_old_price = driver.find_element_by_css_selector("del:nth-child(1)>span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector("ins:nth-child(2)>span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
img_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>a")))
close_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='pp_close']")))



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe') # вызываем драйвер браузера, после этой команды вы должны увидеть новое открытое окно браузера
driver.maximize_window() # раскрываем окно браузера на весь экран
driver.get("https://practice.automationtesting.in/")
Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
Account.click()
Username = driver.find_element_by_id("username")
Username.send_keys("Voldemort.volodyan@yandex.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("Insert1989@")
Login = driver.find_element_by_name("login")
Login.click()
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
HTML = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product-category/html/']")
HTML.click()
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li:nth-child(2) >span"), "(3)"))

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
Account.click()
Username = driver.find_element_by_id("username")
Username.send_keys("Voldemort.volodyan@yandex.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("Insert1989@")
Login = driver.find_element_by_name("login")
Login.click()
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
element = driver.find_element_by_name("orderby")
select = Select(element)
select.select_by_value("menu_order")
driver.find_element_by_tag_name("select").click()
driver.find_element_by_css_selector("option:nth-child(6)").click()
driver.find_element_by_tag_name("select").click()
driver.find_element_by_css_selector("option:nth-child(1)").click()
element = driver.find_element_by_name("orderby")
select = Select(element)
select.select_by_value("price-desc")



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Account = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/']")
Account.click()
Username = driver.find_element_by_id("username")
Username.send_keys("Voldemort.volodyan@yandex.ru")
Password = driver.find_element_by_id("password")
Password.send_keys("Insert1989@")
Login = driver.find_element_by_name("login")
Login.click()
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
Book = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product/android-quick-start-guide/']")
Book.click()
book_old_price = driver.find_element_by_css_selector("del:nth-child(1)>span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector("ins:nth-child(2)>span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
img_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>a")))
close_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='pp_close']")))



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
Book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=165']")
Book.click()
time.sleep(3)
element = driver.find_element_by_css_selector(".cartcontents")
element_get_text = element.text
assert element_get_text == "1 Item"
book_price = driver.find_element_by_css_selector("span[class='amount']")
book_price_text = book_price.text
assert book_price_text == "₹350.00"
Basket = driver.find_element_by_css_selector("span[class='cartcontents']")
Basket.click()
some_element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td:nth-child(2) >span"), "350.00"))
some_element_2 = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong:nth-child(1)>span"), "357.00"))



import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
Shop = driver.find_element_by_css_selector("li[id='menu-item-40']")
Shop.click()
driver.execute_script("window.scrollBy(0,300);")
Book = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=165']")
Book.click()
time.sleep(3)
Basket = driver.find_element_by_css_selector("span[class='cartcontents']")
Basket.click()
time.sleep(3)
Delete_btn = driver.find_element_by_css_selector("[class='remove']")
Delete_btn.click()
time.sleep(3)
link = driver.find_element_by_link_text("Undo?")
link.click()
Quantity = driver.find_element_by_css_selector("input[type='number']").clear()
Quantity_2 = driver.find_element_by_css_selector("[type='number']")
Quantity_2.send_keys("3")
Basket = driver.find_element_by_css_selector("input[name='update_cart']")
Basket.click()
time.sleep(5)
Coupon_btn = driver.find_element_by_css_selector("input[name='apply_coupon']")
Coupon_btn.click()
some_element= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class='woocommerce-error']"), "Please enter a coupon code."))









