from behave import *
from restaurant import *
from car import *


@given('I am a restaurant owner')
def step_impl(context):
    context.restaurant = Restaurant('Midas', 'Italian')


@when('I launch my restaurant')
def step_impl(context):
    context.restaurant.open_restaurant()


@then('my customers should see details about my restaurant')
def step_impl(context):
    assert (context.restaurant.describe_restaurant(), "The name of the restaurant is Pie Hole and we serve "
                                                      "Italian-cuisines")


@given('I just acquired a new car in the show room')
def step_impl(context):
    context.car = Car('Audi', 'a4', 2019)


@when('I check the details of the car')
def step_impl(context):
    context.car.get_description()


@then('I should see the odometer reading')
def step_impl(context):
    assert (context.car.read_odometer(), "This car has 0 miles on it" )
