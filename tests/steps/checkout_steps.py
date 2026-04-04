"""
Шаги оформления заказа: заполнение формы, подтверждение.
"""

from playwright.sync_api import expect
from pytest_bdd import when, then, parsers


@when('нажимает Checkout')
def click_checkout(page):
    page.get_by_text("Checkout").click()


@when(parsers.parse('заполняет First Name "{value}"'))
def fill_first_name(page, value):
    page.locator('[data-test="firstName"]').fill(value)


@when(parsers.parse('заполняет Last Name "{value}"'))
def fill_last_name(page, value):
    page.locator('[data-test="lastName"]').fill(value)


@when(parsers.parse('заполняет Zip Code "{value}"'))
def fill_zip(page, value):
    page.locator('[data-test="postalCode"]').fill(value)


@then('кнопка Continue активна')
def continue_button_enabled(page):
    expect(page.get_by_text("Continue")).to_be_enabled()


@when('нажимает Continue')
def click_continue(page):
    btn = page.get_by_text("Continue")
    btn.wait_for(state="visible", timeout=10000)
    btn.click()


@when('нажимает Finish')
def click_finish(page):
    btn = page.get_by_text("Finish")
    btn.wait_for(state="visible", timeout=10000)
    btn.click()


@then('отображается сообщение "Thank you for your order!"')
def thank_you_message(page):
    expect(page.get_by_text("Thank you for your order!")).to_be_visible(timeout=10000)
