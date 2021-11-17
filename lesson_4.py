import selenium.webdriver
import selenium.webdriver.common.by
from selenium.webdriver.chrome.options import Options

# 1a
chrome_driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\lenovo\Downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("http://www.walla.co.il")

# 1b
firefox_driver = selenium.webdriver.Firefox(executable_path=r"C:\Users\lenovo\Downloads\firefox.exe")
firefox_driver.get("http://www.ynet.co.il")
#
# # 2a
title = chrome_driver.title
print(title)
# # 2b
chrome_driver.refresh()
# # 2c
if title == chrome_driver.title:
    print("its' equal, but usless")

# 3 - YAP

# 4
try:
    chrome_driver.get("https://translate.google.com")
    tag = chrome_driver.find_element(selenium.webdriver.common.by.By.TAG_NAME, "textarea")
    tag.send_keys("שלום עולם")
except Exception as e:
    pass

# 5
chrome_driver.get("https://www.youtube.com/")
chrome_driver.find_element(selenium.webdriver.common.by.By.ID, "search").send_keys("halo")
chrome_driver.find_element(selenium.webdriver.common.by.By.ID, "search-icon-legacy").click()

# 6
chrome_driver.get("https://translate.google.com")
e1 = chrome_driver.find_element(selenium.webdriver.common.by.By.ID, "tw-target-text-container")
e2 = chrome_driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "tw-data-text tw-text-large XcVN5d tw-ta")
# they have just 2 elements now for that area

# 7
chrome_driver.get("https://www.facebook.com/")
chrome_driver.find_element(selenium.webdriver.common.by.By.NAME, "email").send_keys("a@a.com")
chrome_driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").send_keys("acdfdgb!2@")
chrome_driver.find_element(selenium.webdriver.common.by.By.NAME, "login").click()

# 9
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
browser = selenium.webdriver.Chrome(chrome_options=chrome_options)

# conflict
print("I have a problem here")