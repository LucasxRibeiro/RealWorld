from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class User_Login:
    

   
    @given(u'I am on the login page')
    def step_impl(context):
        global driver 
        driver= webdriver.Firefox()
        driver.get('https://realworld.svelte.dev/')
        btn_sign_in_link = driver.find_element(By.CSS_SELECTOR,'a.nav-link[href="/login"]' )
        btn_sign_in_link.click()

        

    @when(u'I enter valid credentials {email} and {password}')
    def step_impl(context,email,password):
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()
        # Input an email address into the field
        email_input.send_keys(email)
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys(password)

    @when(u'I enter invalid credentials {email} and {password}')
    def step_impl(context,email,password):
        # I find the elemend email
        email_input = driver.find_element(By.NAME,"email")
        # Clear the input field
        email_input.clear()
        # Input an email address into the field
        email_input.send_keys(email)
        # I find the elemend password
        password_input = driver.find_element(By.NAME,"password")
        # Clear the input field
        password_input.clear()
        # Input an email address into the field
        password_input.send_keys(password)


    @when(u'I click the "Log In" button')
    def step_impl(context):
        btn_sign_in = driver.find_element(By.CSS_SELECTOR,'button.btn.btn-lg.btn-primary.pull-xs-right[type="submit"]')
        btn_sign_in.click()

    @then(u'I should be redirected to the home page')
    def step_impl(context):
        time.sleep(2) # Delay to wait for page load
        expected_home_url = "https://realworld.svelte.dev/" 
        actual_url = driver.current_url
        assert actual_url == expected_home_url, f"Expected URL: {expected_home_url}, Actual URL: {actual_url}"
        

    @then(u'I should see an error message indicating invalid login')
    def step_impl(context):
        time.sleep(2) # Delay to wait for page load
        error_messageWeb = driver.find_element(By.CSS_SELECTOR,'h1.svelte-lrm3o6').text        
        error_message = "Something went wrong"
        assert error_message == error_message, f"Expected message: {error_message}, Actual message: {error_messageWeb}"
        driver.quit()


    @then(u'I should see a {username} in the top of the page')
    def step_impl(context,username):        
        usernameWeb = driver.find_element(By.CSS_SELECTOR,'a.nav-link[href="/profile/@'+username+'"]').text
        assert usernameWeb == username, f"Expected username: {username}, Actual username: {usernameWeb}"
        driver.quit()
        
        

   