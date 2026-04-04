"""
Общие шаги: открытие страницы, логин, проверка заголовка и формы.
"""
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers


@given('Пользователь открывает главную страницу')
def open_login_page(page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_url("https://www.saucedemo.com/")


@given('Пользователь залогинился как standard_user')
def login_as_standard_user(page):
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=10000)


# Проверка заголовка
@then('заголовок страницы содержит "Swag Labs"')
def check_title(page):
    expect(page).to_have_title("Swag Labs")


# Проверка видимости формы логина
@then('поле username видно')
def username_visible(page):
    expect(page.locator('[data-test="username"]')).to_be_visible()


@then('поле password видно')
def password_visible(page):
    expect(page.locator('[data-test="password"]')).to_be_visible()


@then('кнопка Login видна')
def login_button_visible(page):
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


# Шаги ввода логина вручную
@when(parsers.parse('вводит username "{username}"'))
def enter_username(page, username):
    page.locator('[data-test="username"]').fill(username)


@when(parsers.parse('вводит password "{password}"'))
def enter_password(page, password):
    page.locator('[data-test="password"]').fill(password)


@when('нажимает кнопку Login')
def click_login(page):
    page.locator('[data-test="login-button"]').click()


@then('пользователь попадает на страницу товаров')
def on_products_page(page):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@then(parsers.parse('отображается сообщение об ошибке "{message}"'))
def error_message_visible(page, message):
    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_have_text(message)
