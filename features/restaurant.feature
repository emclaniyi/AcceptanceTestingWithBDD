Feature: Open restaurant
  As a restaurant owner, I want to launch my restaurant so I can cater to customer needs.

  Scenario: Opening my restaurant
    Given I am a restaurant owner
    When I launch my restaurant
    Then my customers should see details about my restaurant
