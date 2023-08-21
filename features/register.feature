Feature: User Registration
  As a new user
  I want to register on the website
  So that I can access the platform's features

  Scenario: Successful User Registration 
    Given I am on the registration page
    When I try to register with this credentials Successful      
    And I click the Sign UP button
    Then I should see the resgistered username in the top of the page  

  Scenario Outline: Failed User Registration - Email already exist
    Given I am on the registration page
    When I try to register with this credentials - Email already <Username> <Email> <Password>     
    And I click the Sign UP button
    Then I should see that stay on registration page with a alert

    Examples: Credentials
        |  Username   |         Email        | Password  |
        |  testJPMC  | testJPMC@test.com.br | 12345678  |
        |  testJPMC1 | testJPMC1@test.com.br| 87654321  |
  

  Scenario Outline: Failed User Registration - Missing Email
    Given I am on the registration page
    When I try to register with this credentials Missing Email <Username> <Password>     
    And I click the Sign UP button
    Then I should see that stay on registration page with a alert

    Examples: Credentials
        | Username  |  Password    |
        | test      |  secret123   |
        | test1     | secret123    |
        | test2     | secret123    |

  Scenario Outline: Failed User Registration - Missing Password
    Given I am on the registration page
    When I try to register with this credentials Missing Password <Username> <Email>      
    And I click the Sign UP button
    Then I should see that stay on registration page with a alert

    Examples: Credentials
        | Username  | Email            | 
        | test1     | test1@example.com|  
        | test2     | test2@example.com|  

Scenario Outline: Failed User Registration - Missing Name
    Given I am on the registration page
    When I try to register with this credentials Missing Username <Email> <Password>      
    And I click the Sign UP button
    Then I should see that stay on registration page with a alert

    Examples: Credentials
        | Email             | Password    |
        | test1@example.com  | secret123   |
        | test2@example.com  | secret123   |
        | test3@example.com  | secret123   |
