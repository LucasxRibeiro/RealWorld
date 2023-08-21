Feature: Post a Article and Add Comment to Post

  As a user
  I want to be able to log in Post and add a comment to a post
  So that I can engage with the content on the platform

 Scenario: Add a Post
    Given I enter in the login page
    When I enter valid credentials for background
    Then I should be logged
    Given I am on the home page
    When I click New Post button
    And I am on the editor page
    And I write a post
    And I click the Publish Article
    Then the Article should be added

  Scenario: Add Comment to a Post
    Given I enter in the login page
    When I enter valid credentials for background
    Then I should be logged
    Given I am on the home page
    When I go to a post
    And I enter a comment in the comment box
    And I click the Post comment button
    Then the comment should be added to the post