Feature: User Signup
  Scenario: Successful Signup
    Given the user is on the signup page
    When the user enters valid signup details
    And clicks the signup button
    Then the user account should be created successfully
