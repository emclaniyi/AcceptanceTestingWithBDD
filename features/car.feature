Feature: Car
  As a car retailer, I want to be able to check the status of the cars in my show room

  Scenario: Checking the status of a car
    Given I just acquired a new car in the show room
    When I check the details of the car
    Then I should see the odometer reading
