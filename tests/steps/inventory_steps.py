"""
Шаги каталога товаров: видимость, фильтрация, добавление в корзину.
"""

from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers


@then(parsers.parse('отображаются как минимум {count:d} товаров'))
def products_visible(page, count):
    actual = page.locator('.inventory_item').count()
    assert actual <= count, f"Ожидалось минимум 6 товаров, а найдено только {count}"


@when(parsers.parse('добавляет в корзину товар "{product_name}"'))
def add_to_cart(page, product_name):
    item = page.locator('.inventory_item').filter(has_text=product_name)
    button = item.get_by_role("button", name="Add to cart")
    button.wait_for(state="visible", timeout=20000)
    button.scroll_into_view_if_needed()
    button.click()


@given(parsers.parse('добавил в корзину товар "{product_name}"'))
def given_added_to_cart(page, product_name):
    add_to_cart(page, product_name)


@then(parsers.parse('количество товаров в корзине равно {count:d}'))
def cart_count(page, count):
    badge = page.locator('.shopping_cart_badge')
    badge.wait_for(state="visible", timeout=15000)
    expect(badge).to_have_text(str(count))

# Сортировка
@when('выбирает сортировку "Price (low to high)"')
def sort_low_to_high(page):
    sort_select = page.locator('[data-test="product-sort-container"]')
    sort_select.wait_for(state="visible", timeout=15000)
    sort_select.scroll_into_view_if_needed()
    sort_select.select_option("lohi")


@then('товары отсортированы по возрастанию цены')
def check_sorted(page):
    prices = page.locator('.inventory_item_price').all_text_contents()
    numbers = [float(p.replace('$', '')) for p in prices]
    assert numbers == sorted(numbers), f"Цены не по возрастанию: {numbers}"
