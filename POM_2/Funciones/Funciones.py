import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# https://www.lambdatest.com/blog/handling-errors-and-exceptions-in-selenium-python/

class Funciones_Globales:

    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Welcome a Page Object Model")

    def Tiempo_sleep(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def Navegar(self, URL):
        self.driver.get(URL)
        self.driver.maximize_window()

    def Navegar_T(self, URL, Tiempo):
        self.driver.get(URL)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def Texto_XPath(self, xpath, texto, tiempo):
        try:
            value = self.driver.find_element(By.XPATH, xpath)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + xpath)

    def Texto_ID(self, ID, texto, tiempo):
        try:
            value = self.driver.find_element(By.ID, ID)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + ID)

    def Texto_NAME(self, NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.NAME, NAME)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + NAME)

    def Texto_CLASS_NAME(self, CLASS_NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + CLASS_NAME)

    def Texto_CSS_SELECTOR(self, CSS_SELECTOR, texto, tiempo):
        try:
            value = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + CSS_SELECTOR)

    def Texto_TAG_NAME(self, TAG_NAME, texto, tiempo):
        try:
            value = self.driver.find_element(By.TAG_NAME, TAG_NAME)
            value.send_keys(texto)
            t = time.sleep(tiempo)
            return t
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + TAG_NAME)

    def Button_XPATH(self, XPATH):
        try:
            value = self.driver.find_element(By.XPATH, XPATH)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + XPATH)

    def Button_ID(self, ID):
        try:
            value = self.driver.find_element(By.ID, ID)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + ID)

    def Button_NAME(self, NAME):
        try:
            value = self.driver.find_element(By.NAME, NAME)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + NAME)

    def Button_CLASS_NAME(self, CLASS_NAME):
        try:
            value = self.driver.find_element(By.CLASS_NAME, CLASS_NAME)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + CLASS_NAME)

    def Button_CSS_SELECTOR(self, CSS_SELECTOR):
        try:
            value = self.driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + CSS_SELECTOR)

    def Button_TAG_NAME(self, TAG_NAME):
        try:
            value = self.driver.find_element(By.TAG_NAME, TAG_NAME)
            value.click()
        except NoSuchElementException as ex:
            print(ex.msg)
            print("No se encontró el elemento" + TAG_NAME)

    