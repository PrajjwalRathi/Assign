Feature: User Login
  Scenario: Successful Login
    Given the user is on the login page
    When the user enters valid login credentials
    And clicks the login button
    Then the user should be logged in successfully
