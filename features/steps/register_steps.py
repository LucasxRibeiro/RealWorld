from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.common.alert import Alert 
class Register_User:
    

   
    @given(u'I am on the registration page')
    def step_impl(context):
        global driver 
        driver= webdriver.Firefox()
        driver.get('https://realworld.svelte.dev/')
        btn_sign_in_link = driver.find_element(By.CSS_SELECTOR,'a.nav-link[href="/register"]' )
        btn_sign_in_link.click()
        driver.get_full_page_screenshot_as_png
    @when(u'I try to register with this credentials Successful')
    def step_impl(context):

        current_time = datetime.datetime.now()
        formato = "%Y%m%d%H%M%S"
        global data_hora_formatada 
        data_hora_formatada = current_time.strftime(formato)
        time.sleep(2)
        # I find the elemend username
        username_input = driver.find_element(By.NAME,"username")
        # Clear the input field
        username_input.clear()
        # Input an username into the field
        username_input.send_keys(data_hora_formatada)
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()        
        # Input an email address into the field
        email_input.send_keys(data_hora_formatada+"test@hotmail.com")
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys("secret123")

    @when(u'I try to register with this credentials - Email already {Username} {Email} {Password}')
    def step_impl(context,Username,Email,Password):
        time.sleep(2)
        # I find the elemend username
        username_input = driver.find_element(By.NAME,"username")
        # Clear the input field
        username_input.clear()
        # Input an username into the field
        username_input.send_keys(Username)
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()        
        # Input an email address into the field
        email_input.send_keys(Email)
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys(Password)

    @when(u'I try to register with this credentials Missing Username {Email} {Password}')
    def step_impl(context,Email,Password):
        time.sleep(2)
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()        
        # Input an email address into the field
        email_input.send_keys(Email)
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys(Password)
    
    @when(u'I try to register with this credentials Missing Email {Username} {Password}')
    def step_impl(context,Username,Password):
        time.sleep(2)
        # I find the elemend username
        username_input = driver.find_element(By.NAME,"username")
        # Clear the input field
        username_input.clear()
        # Input an username into the field
        username_input.send_keys(Username)       
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys(Password)

    
    
    @when(u'I try to register with this credentials Missing Password {Username} {Email}')
    def step_impl(context,Username,Email):
        time.sleep(2)
        # I find the elemend username
        username_input = driver.find_element(By.NAME,"username")
        # Clear the input field
        username_input.clear()
        # Input an username into the field
        username_input.send_keys(Username)
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()        
        # Input an email address into the field
        email_input.send_keys(Email)
       
    
    @when(u'I click the Sign UP button')
    def step_impl(context):
        btn_sign_in = driver.find_element(By.CSS_SELECTOR,'button.btn.btn-lg.btn-primary.pull-xs-right')
        btn_sign_in.click()
        


    @then(u'I should see the resgistered username in the top of the page')
    def step_impl(context):     
        time.sleep(2)
        usernameWeb = driver.find_element(By.CSS_SELECTOR,'a.nav-link[href="/profile/@'+data_hora_formatada+'"]').text
        assert usernameWeb == data_hora_formatada, f"Expected username: {data_hora_formatada}, Actual URL: {usernameWeb}"
        driver.quit()

    @then(u'I should see that stay on registration page with a alert')
    def step_impl(context):    
        time.sleep(2) 
        expected_register_url = "https://realworld.svelte.dev/register" 
        current_register_url = driver.current_url
        assert current_register_url == expected_register_url, f"Expected username: {expected_register_url}, Actual URL: {current_register_url}"     
        driver.quit()
    
    