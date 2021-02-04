# Created by Thinkpad at 2/4/2021
Feature: # Amazon helpsearch Cancel order test
  # Enter feature description here

  Scenario: # User can search for cancel order in Amazon Helpsearch
    Given Open amazon help page
    When Input cancel order into amazon helpsearch field
    And Click on cancel order text
    Then Product results for cancel order are shown



