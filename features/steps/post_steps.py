from behave import given, when, then
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



class comments:
    @given(u'I enter in the login page')
    def step_impl(context):
        global driver 
        driver= webdriver.Firefox()
        driver.get('https://realworld.svelte.dev/login')

    @when(u'I enter valid credentials for background')
    def step_impl(context):
        email = "testJPMC@test.com.br"
        password = "12345678"
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
        btn_sign_in = driver.find_element(By.CSS_SELECTOR,'button.btn.btn-lg.btn-primary.pull-xs-right[type="submit"]')
        btn_sign_in.click()

    @then(u'I should be logged')
    def step_impl(context):
        time.sleep(2) # Delay to wait for page load
        expected_home_url = "https://realworld.svelte.dev/" 
        actual_url = driver.current_url
        assert actual_url == expected_home_url, f"Expected URL: {expected_home_url}, Actual URL: {actual_url}"

    @given(u'I am on the home page')
    def step_impl(context):
               
        expected_home_url = "https://realworld.svelte.dev/" 
        actual_url = driver.current_url
        assert actual_url == expected_home_url, f"Expected URL: {expected_home_url}, Actual URL: {actual_url}"

    @when(u'I click New Post button')
    def step_impl(context):
        time.sleep(2)
        btn_post = driver.find_element(By.CSS_SELECTOR, "body > div > nav > div > ul > li:nth-child(2) > a")
        btn_post.click()
       
    @when(u'I am on the editor page')
    def step_impl(context):   
        time.sleep(2)             
        expected_editor_url = "https://realworld.svelte.dev/editor" 
        actual_url = driver.current_url
        assert actual_url == expected_editor_url, f"Expected URL: {expected_editor_url}, Actual URL: {actual_url}"

    @when(u'I go to a post')
    def step_impl(context):
        driver.get("https://realworld.svelte.dev/article/Try-to-transmit-the-HTTP-card-maybe-it-will-override-the-multi-byte-hard-drive!-120863")

    @when(u'I enter a comment in the comment box')
    def step_impl(context):
        comment_box = driver.find_element(By.NAME, "comment")
        comment_text = "Test comment"
        comment_box.clear()
        comment_box.send_keys(comment_text)
        context.comment_text = comment_text

    @when(u'I write a post')
    def ste_impl(context):   
        title = "Test Selenium"
        description= "Test using the selenium to write and post a article"
        body= "Selenium is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms."
        
        title_input = driver.find_element(By.NAME, "title")      
        title_input.clear()        
        title_input.send_keys(title)
        
        description_input = driver.find_element(By.NAME,"description")       
        description_input.clear()        
        description_input.send_keys(description)

        body_input = driver.find_element(By.NAME,"body")       
        body_input.clear()        
        body_input.send_keys(body)

    @when(u'I click the Publish Article')
    def step_impl(context):
        time.sleep(2)
        btn_publish_article = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.pull-xs-right.btn-primary")
        btn_publish_article.click()

    @then(u'the Article should be added')
    def step_impl(context):
        time.sleep(2)
        author = "test JPMC"
        author_elementget = driver.find_element(By.CLASS_NAME, "author").text
        assert author == author_elementget, f"Expected author: {author}, Actual author: {author_elementget}"


    @when(u'I click the Post comment button')
    def step_impl(context):
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary[type='submit']")
        submit_button.click()

    @then(u'the comment should be added to the post')
    def step_impl(context):
        time.sleep(2)
        p_element = driver.find_element(By.CSS_SELECTOR, "p.card-text").text
        comment_text = "Test comment"
        assert comment_text == p_element, f"Expected comment: {comment_text}, Actual comment: {p_element}"
    # Clean up after all scenarios
    def after_all(context):
        driver.quit()