from behave import *


@given('I am on the Create New Customer Account Page')
def step_impl(context):
    context.create_new_customer_account_page.navigate_to_create_new_customer_account_page()


@when('I click on the Create an Account button')
def step_impl(context):
    context.create_new_customer_account_page.click_create_an_account_button()


@when('I enter "{first_name}" in the First name field')
def step_impl(context, first_name):
    context.create_new_customer_account_page.set_first_name(first_name)


@when('I enter "{last_name}" in the Last name field')
def step_impl(context, last_name):
    context.create_new_customer_account_page.set_last_name(last_name)


@when('I enter "{email}" in the Email field')
def step_impl(context, email):
    context.create_new_customer_account_page.set_email_input(email)


@when('I insert "{password}" in the Password field')
def step_impl(context, password):
    context.create_new_customer_account_page.set_password_input(password)


@when('I insert "{confirm_password}" in the Confirm password field')
def step_impl(context, confirm_password):
    context.create_new_customer_account_page.set_confirm_password_input(confirm_password)


@then('First name error is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_first_name_error_displayed()


@then('Last name error is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_last_name_error_displayed()


@then('Email error is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_email_name_error_displayed()


@then('Password error is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_password_error_displayed()


@then('Confirm password error is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_confirm_password_error_displayed()


@then('The successful registration message is displayed')
def step_impl(context):
    assert context.create_new_customer_account_page.is_successful_registration_message_displayed()


@then('The successful registration message contains "{expected_message}"')
def step_impl(context, expected_message):
    assert expected_message in context.create_new_customer_account_page.get_successful_registration_message_text()

