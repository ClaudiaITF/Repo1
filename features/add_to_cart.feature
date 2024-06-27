Feature: Test the functionality of the Add to cart page

  @cart
  Scenario: Check that the cart is empty
    Given I am on the Cart page
    Then The Cart page contains the text "no items in your shopping cart"

  @cart
  Scenario: Check that the "The product has been added to your cart" message is displayed when adding a product to cart
    Given I am on the watches Page
    When I add to cart the "Luma Analog Watch"
    Then The successful adding to cart message is displayed
    Then The successful message contains "The product has been added to your cart"

  @cart
  Scenario: Check that a product which was added to cart is actually in the cart
    Given I am on the watches Page
    When I add to cart the "Luma Analog Watch"
    When I click on "cart" button
    Then I actually am on "https://magento.softwaretestingboard.com/checkout/cart/"
    Then The "Luma Analog Watch" is actually in the cart