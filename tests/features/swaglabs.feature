Feature: Тестирование Swag Labs (saucedemo.com)

  Scenario: 1. Проверка заголовка страницы
    Given Пользователь открывает главную страницу
    Then заголовок страницы содержит "Swag Labs"

  Scenario: 2. Проверка видимости элементов формы логина
    Given Пользователь открывает главную страницу
    Then поле username видно
    And поле password видно
    And кнопка Login видна

  Scenario: 3. Успешный логин
    Given Пользователь открывает главную страницу
    When вводит username "standard_user"
    And вводит password "secret_sauce"
    And нажимает кнопку Login
    Then пользователь попадает на страницу товаров

  Scenario: 4. Проверка видимости товаров после логина
    Given Пользователь залогинился как standard_user
    Then отображаются как минимум 6 товаров

  Scenario: 5. Добавление товара в корзину
    Given Пользователь залогинился как standard_user
    When добавляет в корзину товар "Sauce Labs Backpack"
    Then количество товаров в корзине равно 1

  Scenario: 6. Переход в корзину
    Given Пользователь залогинился как standard_user
    And добавил в корзину товар "Sauce Labs Backpack"
    When нажимает на иконку корзины
    Then открывается страница корзины

  Scenario: 7. Заполнение полей оформления заказа
    Given Пользователь залогинился как standard_user
    And в корзине есть товар
    When переходит в корзину
    And нажимает Checkout
    And заполняет First Name "Иван"
    And заполняет Last Name "Иванов"
    And заполняет Zip Code "12345"
    Then кнопка Continue активна

  Scenario: 8. Завершение оформления заказа
    Given Пользователь залогинился как standard_user
    And в корзине есть товар
    When переходит в корзину
    And нажимает Checkout
    And заполняет First Name "Иван"
    And заполняет Last Name "Иванов"
    And заполняет Zip Code "12345"
    And нажимает Continue
    And нажимает Finish
    Then отображается сообщение "Thank you for your order!"

  Scenario: 9. Фильтрация товаров по цене (low to high)
    Given Пользователь залогинился как standard_user
    When выбирает сортировку "Price (low to high)"
    Then товары отсортированы по возрастанию цены

  Scenario: 10. Удаление товара из корзины
    Given Пользователь залогинился как standard_user
    And добавил в корзину товар "Sauce Labs Backpack"
    When переходит в корзину
    And удаляет товар из корзины
    Then корзина пуста

  Scenario: 11. Логин с неверным паролем
    Given Пользователь открывает главную страницу
    When вводит username "standard_user"
    And вводит password "wrong_password"
    And нажимает кнопку Login
    Then отображается сообщение об ошибке "Epic sadface: Username and password do not match any user in this service"

  Scenario: 12. Логин с заблокированным пользователем
    Given Пользователь открывает главную страницу
    When вводит username "locked_out_user"
    And вводит password "secret_sauce"
    And нажимает кнопку Login
    Then отображается сообщение об ошибке "Epic sadface: Sorry, this user has been locked out."