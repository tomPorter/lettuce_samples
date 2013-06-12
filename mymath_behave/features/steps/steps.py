from behave import *
import factorial

@given('I have the number {number:d}')
def have_the_number(context, number):
    context.number = int(number)

@when('I compute its factorial')
def compute_its_fatorial(context):
    context.number = factorial.factorial(context.number)

@then('I see the number {expected:d}')
def check_number(context, expected):
    expected = int(expected)
    assert context.number == expected, \
        "Got %d" % context.number

