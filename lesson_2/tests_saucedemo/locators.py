from selenium.webdriver.common.by import By

# AUTH

USERNAME_FIELD = (By.ID, 'user-name')
PASSWORD_FIELD = (By.ID, 'password')
LOGIN_BUTTON = (By.ID, 'login-button')

# BURGER-MENU

BURGER_MENU = (By.ID, 'react-burger-menu-btn')
LOGOUT = (By.ID, 'logout_sidebar_link')
ABOUT = (By.ID, 'about_sidebar_link')
RESET_APP_STATE = (By.ID, 'reset_sidebar_link')

# CATALOG

DROPDOWN_MENU = (By.XPATH, '//*[@class="product_sort_container"]')
CATALOG_ITEM_NAME = (By.XPATH, '//*[@class="inventory_item_name"]')
CATALOG_ITEM_PRICE = (By.XPATH, '//*[@class="inventory_item_price"]')

# CART

ADD_TO_CART_BUTTON_IN_CATALOG = (By.ID, 'add-to-cart-sauce-labs-backpack')
ITEM_CATALOG_TITLE = (By.ID, 'item_4_title_link')
ITEM_CATALOG_IMG = (By.ID, 'item_4_img_link')
ADD_TO_CART_BUTTON_IN_ITEM = (By.ID, 'add-to-cart')
REMOVE_BUTTON_IN_ITEM = (By.ID, 'remove')
CART_ICON = (By.XPATH, '//*[@id="shopping_cart_container"]')
CART_COUNTER = (By.CLASS_NAME, 'shopping_cart_badge')
CART_REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-backpack')
CART_ITEM = (By.CLASS_NAME, 'cart_item')
CHECKOUT_BUTTON = (By.ID, 'checkout')

# CHECKOUT

FIRST_NAME_FIELD = (By.ID, 'first-name')
LAST_NAME_FIELD = (By.ID, 'last-name')
POSTAL_CODE_FIELD = (By.ID, 'postal-code')
CHECKOUT_CONTINUE_BUTTON = (By.ID, 'continue')
CHECKOUT_FINISH_BUTTON = (By.ID, 'finish')
BACK_TO_PRODUCTS_BUTTON = (By.ID, 'back-to-products')
