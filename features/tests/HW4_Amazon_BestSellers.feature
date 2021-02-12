# Created by Thinkpad at 2/11/2021
Feature: Amazon BestSellers Test

  Scenario: Verify Amazon BestSellers has 5 links
    Given Open amazon bestsellers page
    Then verify 5 links are displayed
