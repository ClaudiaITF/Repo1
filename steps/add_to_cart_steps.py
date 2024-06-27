from behave import *


@given('I am on the Cart page')
def step_impl(context):
    context.cart_page.navigate_to_home_page()


@given('I am on the Watches Page')
def step_impl(context):
    context.watches_page.navigate_to_watches_page()


@when('I add to cart the "Luma Analog Watch"')
def step_impl(context):
    context.watches_page.add_luma_analog_watch_to_cart()


@when('I click on "cart" button')
def step_impl(context):
    context.cart_page.click_on_cart_button()


@then('The Cart page contains the text "{no_item_text}"')
def step_impl(context, no_item_text):
    assert no_item_text in context.cart_page.get_cart_no_item_text()


@then('The successful adding to cart message is displayed')
def step_impl(context):
    assert context.watches_page.is_successful_added_to_cart()


@then('The successful message contains "{added_product_text}"')
def step_impl(context, added_product_text):
    assert added_product_text in context.watches_page.get_successful_added_to_cart_message()


@then('I actually am on "{expected_url}"')
def step_impl(context, expected_url):
    assert context.cart_page.is_url_correct(expected_url)


@then('The "{expected_watches}" is actually in the cart')
def step_impl(context, expected_watches):
    assert expected_watches in context.cart_page.get_watches_name()