"""
Шаги корзины: переход, просмотр, удаление товаров.
"""
from playwright.sync_api import expect
from pytest_bdd import given, when, then
from tests.steps.inventory_steps import add_to_cart


@given('в корзине есть товар')
def ensure_item_in_cart(page):
    if not page.locator('.shopping_cart_badge').is_visible():
        add_to_cart(page, "Sauce Labs Backpack")


@when('переходит в корзину')
@when('нажимает на иконку корзины')
@then('открывается страница корзины')
def click_cart_icon(page):
    page.locator('.shopping_cart_link').click()


@when('удаляет товар из корзины')
def remove_from_cart(page):
    page.get_by_text("Remove").first.click()


@then('корзина пуста')
def cart_is_empty(page):
    expect(page.locator('.cart_item')).to_have_count(0)
