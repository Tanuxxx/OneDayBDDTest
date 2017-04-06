from radish import given, when, then

@given("I have the numbers {number1:g} and {number2:g}")
def have_numbers(step, number1, number2):
    pass

@when("I sum them")
def sum_numbers(step):
    pass

@then("I expect the result to be {result:g}")
def expect_result(step, result):
    pass