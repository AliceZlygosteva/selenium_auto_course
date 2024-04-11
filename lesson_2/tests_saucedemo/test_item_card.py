from locators import ITEM_CATALOG_IMG, ITEM_CATALOG_TITLE


# Успешный переход к карточке товара после клика на картинку товара
def test_transition_to_card_from_img(browser, auth):
    # кликаем на картинку товара
    browser.find_element(*ITEM_CATALOG_IMG).click()

    # проверяем что произошёл переход на url карточки товара
    assert 'inventory-item.html?id=4' in browser.current_url, "Переход на страницу карточки товара не произошел"


# Успешный переход к карточке товара после клика на название товара
def test_transition_to_card_from_title(browser, auth):
    # кликаем на название товара
    browser.find_element(*ITEM_CATALOG_TITLE).click()

    assert 'inventory-item.html?id=4' in browser.current_url, "Переход на страницу карточки товара не произошел"
