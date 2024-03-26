import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


class TestYandexMarket(unittest.TestCase):

    def setUp(self):
        # запускаем браузер yandex
        service = Service(executable_path='./yandexdriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.maximize_window()

    def test_search_in_yandex_market(self):
        #поиск товара
        self.driver.get("https://market.yandex.ru/")
        search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        search_box.send_keys("умная колонка алиса")
        search_box.submit()
        self.assertIsNotNone(self.wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='SerpStatic']")))

    def test_add_to_cart_in_yandex_market(self):
        #добавление товара в корзину
        self.driver.get("https://market.yandex.ru/")
        search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        search_box.send_keys("умная колонка алиса")
        search_box.submit()

        #считаем ссылку, чтобы открыть в том же окне
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-auto='snippet-link']"))).get_attribute("href")
        self.driver.execute_script("window.location.href = arguments[0];", first_product)
        time.sleep(10)
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[variant='yellow']")))
        add_to_cart_button.click()


    def test_add_in_favourites_yandex_market(self):
        #добавление товара в избранное
        self.driver.get("https://market.yandex.ru/")
        search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        search_box.send_keys("Смартфоны")
        search_box.submit()
        favourites_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='_2VECW']")))
        favourites_product.click()


    def test_search_catalog_in_yandex_market(self):
        self.driver.get("https://market.yandex.ru/")

        catalog_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='_30-fz button-focus-ring Hkr1q _1pHod _2rdh3 _3rbM-']")))
        catalog_button.click()
        time.sleep(5)

        #Ноутбуки и компьютеры
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div/div/div/div/div/div[1]/div/ul/li[6]/a/span")))
        search_input.click()
        time.sleep(5)

        #Ноутбуки
        open_search_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/a")))
        open_search_input.click()
        time.sleep(5)


    def test_compare_in_yandex_market(self):
        #Сравнение товаров
        self.driver.get("https://market.yandex.ru/")
        search_box = self.wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        search_box.send_keys("Ноутбуки")
        search_box.submit()

        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='SerpStatic']/div[1]/div/div/div/div/div/div/div[2]/div/div/div/article/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/button")))
        first_product.click()
        time.sleep(5)

        second_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='SerpStatic']/div[1]/div/div/div/div/div/div/div[3]/div/div/div/article/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/button")))
        second_product.click()
        time.sleep(5)

        open_compare = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[5]/div/div/div[3]/a")))
        open_compare.click()
        time.sleep(5)

    def test_sign_in_yandex_market(self):
        self.driver.get("https://market.yandex.ru/")
        sign_in = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='USER_MENU_ANCHOR']/div/div/a")))
        sign_in.click()

        sign_in_login = "text"
        sign_in_password = "text"

        search_input_login = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='passp-field-login']")))
        search_input_login.send_keys(sign_in_login)
        time.sleep(3)
        button_input_login = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='passp:sign-in']")))
        button_input_login.click()

        search_input_password = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='passp-field-passwd']")))
        search_input_password.send_keys(sign_in_password)
        time.sleep(3)
        button_input_password = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='passp:sign-in']")))
        button_input_password.click()
        time.sleep(15)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()