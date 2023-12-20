# # importing required package of webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.opera.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
#
# if __name__ == '__main__':
#     # Instantiate the webdriver with the executable location of MS Edge
#     browser = webdriver.Edge()
#     # Simply just open a new Edge browser and go to lambdatest.com
#     browser.maximize_window()
#     browser.get('https://www.lambdatest.com')
#     browser.find_element(By.LINK_TEXT,"Platform ").click()
#     browser.find_element(By.LINK_TEXT,"Selenium Testing").click()
#     browser.find_element(By.LINK_TEXT,"Login").click()
#     browser.find_element(By.ID,"email").send_keys("Hello@gmail.com")
#     browser.find_element(By.CSS_SELECTOR,"#password").send_keys("123456")
#     browser.find_element(By.XPATH,"//button[@id='login-button']").click()


# from selenium import webdriver
# # from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
#
# # Setup chrome driver
# driver = webdriver.Edge()
#
# # Navigate to the url
# driver.get('https://thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python')
#
# # Find elements by Link Text
# driver.find_element(By.LINK_TEXT,'Sign Up').click()
#
#
#
# # Close the driver
# driver.quit()












# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Create a new instance of the Chrome driver
# driver = webdriver.Edge()
#
# # Open the Bstack Demo website
# driver.get("https://bstackdemo.com/")
#
# # Find the sign-in button and click on it
# signin_btn = driver.find_element(by=By.CSS_SELECTOR,value="#signin").click()
#
# #Add implicit wait for element to be found
# driver.implicitly_wait(10)
#
# #Find the Username, Password and Login Button
# username =driver.find_element(by=By.ID,value="username")
# password =driver.find_element(by=By.ID,value="password")
# login_btn= driver.find_element(by=By.ID,value="login-btn")
#
# #Select demouser as Username
# username.click()
# username_input= driver.find_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0")
# username_input.click()
#
# #Select testingisfun99 as Password
# password.click()
# password_input =driver.find_element(by=By.CSS_SELECTOR,value="#react-select-3-option-0-0")
# password_input.click()
#
# # Submit the form
# login_btn.click()
# driver.implicitly_wait(10)
#
# #Assert User is successfully Logged In
# logout_btn= driver.find_element(by=By.CSS_SELECTOR,value="#logout")
# assert logout_btn.is_displayed()
#
# #Closer the browser
# driver.close()
# from selenium import webdriver
#
# # from webdriver_manager.chrome import ChromeDriverManager
#
# from selenium.webdriver.common.by import By
#
#
# class WebAutomation:
#
#     def __init__(self):
#         self.driver = webdriver.Edge()
#
#     # Add implicit wait for element to be found
#
#     def apply_wait(self):
#         self.driver.implicitly_wait(10)
#
#     # Navigate to Signup Page
#
#     def open_signup_page(self):
#         self.driver.get("https://bstackdemo.com/")
#
#         signin_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#signin")
#
#         signin_btn.click()
#
#     # Select demouser as Username
#
#     def fill_username(self):
#         username = self.driver.find_element(by=By.ID, value="username")
#
#         username.click()
#
#         username_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#react-select-2-option-0-0")
#
#         username_input.click()
#
#     # Select testingisfun99 as Password
#
#     def fill_password(self):
#         password = self.driver.find_element(by=By.ID, value="password")
#
#         password.click()
#
#         password_input = self.driver.find_element(by=By.CSS_SELECTOR, value="#react-select-3-option-0-0")
#
#         password_input.click()
#
#     # Submit the form
#
#     def submit_form(self):
#         login_btn = self.driver.find_element(by=By.ID, value="login-btn")
#
#         login_btn.click()
#
#     # Assert User is successfully Logged In
#
#     def login_success(self):
#         logout_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="#logout")
#
#         assert logout_btn.is_displayed()
#
#         self.driver.close()
#
#
# b1 = WebAutomation()
#
# b1.open_signup_page()
#
# b1.apply_wait()
#
# b1.fill_username()
#
# b1.fill_password()
#
# b1.submit_form()
#
# b1.apply_wait()
#
# b1.login_success()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()















