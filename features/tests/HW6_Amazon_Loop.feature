# Created by Thinkpad at 2/27/2021
Feature: Amazon Links Test

  Scenario: User sees Amazon top Menu icon
    Given Open amazon Best Sellers top icon page
    Then Verify Best Sellers menu icon is visible
    And Verify New Releases menu icon is visible
    And Verify Movers & Shakers menu icon is visible
    And Verify Most Wished For menu icon is visible
    Then Verify Gift Ideas menu icon is visible