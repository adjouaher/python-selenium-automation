# Created by Thinkpad at 2/11/2021
Feature: Amazon Add Item Shopping cart test

  Scenario: User can add item to Amazon Shopping cart
    Given Open amazon page
    When Input Key chain into Amazon search field
    And click on Amazon search icon
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 Item
