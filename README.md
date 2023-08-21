# RealWorld


This Python script is designed to test the website (https://realworld.svelte.dev) functionality and verify integrity

### 📋 Requirements
```
Python 3.x or later
Allure report 
```


## ⚙️ Usage

1. Open the directory with the Visual Code.
2. Run the following command int the terminal in order to install de dependencies
```
pip install -r requirements.txt
```
3. Run the script by executing the following command:
```
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
```
 The script will start the test, generate a report in allure, and to display the report use the following commnads when the tests 
 are over.
 ```
allure serve %allure_result_folder%
```

## 🛠️ Features Test

### The script has the following features:


### User Login
```
  As a registered user
  I want to be able to log into my account
  So that I can access my personalized content
```
  
### Post a Article and Add Comment to Post
```
  As a user
  I want to be able to log in Post and add a comment to a post
  So that I can engage with the content on the platform
```
### User Registration
```
  As a new user
  I want to register on the website
  So that I can access the platform's features
```




## ✒️ Writing Scenarios

Scenarios are written in Gherkin syntax and are located in the `features` directory. Each scenario follows the "Given-When-Then" pattern and defines a specific behavior to be tested. For example:

```
Feature: User Registration
  As a new user
  I want to register on the website
  So that I can access the platform's features

  Scenario: Successful User Registration 
    Given I am on the registration page
    When I try to register with this credentials Successful      
    And I click the Sign UP button
    Then I should see the resgistered username in the top of the page  
```


* **Lucas Xavier Ribeiro** 
