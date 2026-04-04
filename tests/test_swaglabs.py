"""
Привязки сценариев к .feature файлу.
Сами шаги — в папке steps/.
"""
from pytest_bdd import scenario

from tests.steps.common_steps import *
from tests.steps.inventory_steps import *
from tests.steps.cart_steps import *
from tests.steps.checkout_steps import *


@scenario('features/swaglabs.feature', '1. Проверка заголовка страницы')
def test_check_title():
    pass


@scenario('features/swaglabs.feature', '2. Проверка видимости элементов формы логина')
def test_login_form_visible():
    pass


@scenario('features/swaglabs.feature', '3. Успешный логин')
def test_successful_login():
    pass


@scenario('features/swaglabs.feature', '4. Проверка видимости товаров после логина')
def test_products_visible_after_login():
    pass


@scenario('features/swaglabs.feature', '5. Добавление товара в корзину')
def test_add_to_cart():
    pass


@scenario('features/swaglabs.feature', '6. Переход в корзину')
def test_go_to_cart():
    pass


@scenario('features/swaglabs.feature', '7. Заполнение полей оформления заказа')
def test_fill_checkout_fields():
    pass


@scenario('features/swaglabs.feature', '8. Завершение оформления заказа')
def test_complete_order():
    pass


@scenario('features/swaglabs.feature', '9. Фильтрация товаров по цене (low to high)')
def test_sort_by_price():
    pass


@scenario('features/swaglabs.feature', '10. Удаление товара из корзины')
def test_remove_from_cart():
    pass


@scenario('features/swaglabs.feature', '11. Логин с неверным паролем')
def test_wrong_password():
    pass


@scenario('features/swaglabs.feature', '12. Логин с заблокированным пользователем')
def test_locked_out_user():
    pass
