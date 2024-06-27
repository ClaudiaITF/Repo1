Feature: Test the functionality of the Create New Customer Account Page

  Background:
    Given I am on the Create New Customer Account Page

  @register
  Scenario: Check that trying to register without completing any field displays error fields
    When I click on the Create an Account button
    Then First name error is displayed
    Then Last name error is displayed
    Then Email error is displayed
    Then Password error is displayed
    Then Confirm password error is displayed

  @register
  Scenario: Check that the registration is successful when completing all the necessary fields
    When I enter "Ionita" in the First name field
    When I enter "Claudia" in the Last name field
    When I enter "claudyadya03@gmail.com" in the Email field
    When I insert "ITfactory123" in the Password field
    When I insert "ITfactory123" in the Confirm password field
    When I click on the Create an Account button
    Then The successful registration message is displayed
    Then The successful registration message contains "Thank you for registering."
