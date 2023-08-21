Feature: User Login
  As a registered user
  I want to be able to log into my account
  So that I can access my personalized content

    Scenario Outline: Successful User Login
      Given I am on the login page
      When I enter valid credentials <email> and <password>
      And I click the "Log In" button
      Then I should be redirected to the home page
      And I should see a <username> in the top of the page

      Examples: Credentials
        |  username   |         email        | password  |
        |  test JPMC  | testJPMC@test.com.br | 12345678  |
        |  test JPMC1 | testJPMC1@test.com.br| 87654321  |

    Scenario Outline: Unsuccessful User Login - Invalid Credentials
      Given I am on the login page
      When I enter invalid credentials <email> and <password>
      And I click the "Log In" button
      Then I should see an error message indicating invalid login

      Examples: Credentials
        |         email        | password   |
        | testJPMC@test.com.br | 123456789  |
        | testJPMC1@test.com.br| 876543219  |