Feature: Test the functionality of the Login Page

  Background:
    Given I am on the Login Page


  @login
  Scenario: Check that "The account signin was incorrect." message is displayed when the user tries to log in with an unregistered email
    When I insert an unregistered email in the email input
    When I insert a password in the password input
    When I click on the signin button
    Then The main error message is displayed
    Then The error text contains "The account signin was incorrect." message


  @login
  Scenario: Check that error message is displayed when the user enters an email address with an invalid format
    When I insert "emailinvalid" in the email input
    When I insert "parolainvalida" in the password input
    When I click on the signin button
    Then The email error message is displayed
    Then The email error message text contains "enter a valid email address"

  @login
  Scenario: Check that the URL is correct
    Then The actual URL is "https://magento.softwaretestingboard.com/customer/account/login"