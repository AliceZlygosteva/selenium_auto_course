from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def test_auth_positive():
    browser.get('https://www.saucedemo.com/')

    # вводим валидный логин в поле 'Username'
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')

    # вводим валидный пароль в поле 'Password'
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')

    # кликаем на кнопку 'Login'
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()

def test_auth_negative():
    browser.get('https://www.saucedemo.com/')

    # вводим невалидный логин в поле 'Username'
    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('user')

    # вводим невалидный пароль в поле 'Password'
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')

    # кликаем на кнопку 'Login'
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()

def test_cart_add_catalog():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # кликаем на кнопку 'Add to cart'
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(By.XPATH, '// *[@id="shopping_cart_container"]').click()
    # проверяем что перешли на страницу корзины
    assert browser.current_url == 'https://www.saucedemo.com/cart.html', 'url не соответствует ожидаемому'

    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart_item')))
    assert element is not None  # проверяем, что элемент с товаром присутствует

    browser.quit()

def test_cart_delete():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # кликаем на кнопку 'Add to cart'
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    # проверяем что перешли на страницу корзины
    assert browser.current_url == 'https://www.saucedemo.com/cart.html', 'url не соответствует ожидаемому'

    #  кликаем на кнопку 'Remove'
    browser.find_element(By.ID, 'remove-sauce-labs-backpack').click()

    # Проверяем, что товар был удален
    wait = WebDriverWait(browser, 5)
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart_item')))
        assert False, "Элемент с товаром не был удален"
    except:
        assert True

    browser.quit()

def test_cart_add_card():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    browser.find_element(By.ID, 'item_4_title_link').click()

    # кликаем на кнопку 'Add to cart' в карточке товара
    browser.find_element(By.ID, 'add-to-cart').click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
    # проверяем что перешли на страницу корзины
    assert browser.current_url == 'https://www.saucedemo.com/cart.html', 'url не соответствует ожидаемому'

    wait = WebDriverWait(browser, 5)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart_item')))
    assert element is not None  # проверяем, что элемент с товаром присутствует

    browser.quit()

def test_cart_delete_card():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # кликаем на название товара для открытия карточки товара
    browser.find_element(By.ID, 'item_4_title_link').click()

    # кликаем на кнопку 'Add to cart' в карточке товара
    browser.find_element(By.ID, 'add-to-cart').click()

    # Проверяем, что количество товаров в корзине увеличилось
    cart_badge = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert cart_badge == '1', 'Товар не добавлен в корзину'

    # кликаем на кнопку 'Remove'
    browser.find_element(By.ID, 'remove').click()

    # Проверка, что товар удален (кнопка меняется обратно на "Add to cart")
    add_to_cart_button_again = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, 'add-to-cart')))
    assert "Add to cart" in add_to_cart_button_again.text, "Товар не был удален из корзины"

    browser.quit()

def test_card_picture():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # кликаем на картинку товара
    browser.find_element(By.ID, 'item_4_img_link').click()
    # проверяем что произошёл переход на url карточки товара
    assert 'inventory-item.html?id=4' in browser.current_url, "Переход на страницу карточки товара не произошел"

    browser.quit()

def test_card_title():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


    browser.find_element(By.ID, 'item_4_title_link').click()

    assert 'inventory-item.html?id=4' in browser.current_url, "Переход на страницу карточки товара не произошел"

    browser.quit()

def test_checkout():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # кликаем на кнопку 'Add to cart'
    browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()

    # кликаем на иконку тележки для перехода на страницу корзины
    browser.find_element(By.XPATH, '// *[@id="shopping_cart_container"]').click()
    # проверяем что перешли на страницу корзины
    assert browser.current_url == 'https://www.saucedemo.com/cart.html', 'url не соответствует ожидаемому'

    # кликаем на кнопку 'Checkout'
    browser.find_element(By.ID, 'checkout').click()
    # проверяем, что произошёл переход на первый шаг оформления заказа
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-one.html', 'url не соответствует ожидаемому'

    browser.find_element(By.ID, 'first-name').send_keys('Name')
    browser.find_element(By.ID, 'last-name').send_keys('LastName')
    browser.find_element(By.ID, 'postal-code').send_keys('123456')
    browser.find_element(By.ID, 'continue').click()

    # проверяем, что произошёл переход на второй шаг оформления заказа
    assert browser.current_url == 'https://www.saucedemo.com/checkout-step-two.html', 'url не соответствует ожидаемому'

    browser.find_element(By.ID, 'finish').click()

    # проверяем, что произошёл переход на страницу подтверждения оформления заказа
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'url не соответствует ожидаемому'

    browser.find_element(By.ID, 'back-to-products').click()

    # проверяем, что мы вернулись на страницу каталога
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()

def test_sorting_a_z():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем селект
    browser.find_element(By.CLASS_NAME, 'product_sort_container').click()
    # выбираем параметр фильтра 'Name (A to Z)'
    browser.find_element(By.CSS_SELECTOR, 'option:first-child').click()

    browser.quit()

def test_sorting_z_a():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем селект
    browser.find_element(By.CLASS_NAME, 'product_sort_container').click()
    # выбираем параметр фильтра 'Name (Z to A)'
    browser.find_element(By.CSS_SELECTOR, 'option:nth-child(2)').click()

    browser.quit()

def test_sorting_low_high():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем селект
    browser.find_element(By.CLASS_NAME, 'product_sort_container').click()
    # выбираем параметр фильтра 'Price (low to high)'
    browser.find_element(By.CSS_SELECTOR, 'option:nth-child(3)').click()

    browser.quit()

def test_sorting_high_low():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем селект
    browser.find_element(By.CLASS_NAME, 'product_sort_container').click()
    # выбираем параметр фильтра 'Price (high to low)'
    browser.find_element(By.CSS_SELECTOR, 'option:last-child').click()

    browser.quit()

def test_logout():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем бургер-меню
    browser.find_element(By.ID, 'react-burger-menu-btn').click()

    # ждём открытия бургер-меню для нажатия ссылки 'Logout'
    wait = WebDriverWait(browser, 5)
    logout_link = wait.until(EC.visibility_of_element_located((By.ID, 'logout_sidebar_link')))

    # нажимаем 'Logout'
    logout_link.click()

    # проверяем, что произошёл переход на страницу авторизации
    assert browser.current_url == 'https://www.saucedemo.com/', 'url не соответствует ожидаемому'

    browser.quit()

def test_about():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем бургер-меню
    browser.find_element(By.ID, 'react-burger-menu-btn').click()

    # нажимаем 'About'
    browser.find_element(By.ID, 'about_sidebar_link').click()

    assert browser.current_url == 'https://saucelabs.com/', 'url не соответствует ожидаемому'

    browser.quit()

def test_reset_app_state():
    browser.get('https://www.saucedemo.com/')

    browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # раскрываем бургер-меню
    browser.find_element(By.ID, 'react-burger-menu-btn').click()

    # ждём открытия бургер-меню для нажатия ссылки 'Reset App State'
    wait = WebDriverWait(browser, 5)
    reset_link = wait.until(EC.visibility_of_element_located((By.ID, 'reset_sidebar_link')))

    # нажимаем 'Reset App State'
    reset_link.click()

    browser.quit()