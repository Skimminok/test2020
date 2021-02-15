import time
from .base_page import BasePage

class MainPage(BasePage):
    def go_to_calculator(self):
        selector = "[class='gLFyf gsfi']"
        input_key = 'Калькулятор'
        search_textfield = self.browser.find_element_by_css_selector(selector)
        search_textfield.send_keys(input_key)
        search_textfield.submit()

    def test_1(self):
        # (1 + 2) × 3 - 40 ÷ 5
        click_left_bracket = self.browser.find_element_by_css_selector('[jsname = "j93WEe"]').click()
        click_1 = self.browser.find_element_by_css_selector('[jsname = "N10B9"]').click()
        click_plus = self.browser.find_element_by_css_selector('[jsname = "XSr6wc"]').click()
        click_2 = self.browser.find_element_by_css_selector('[jsname = "lVjWed"]').click()
        click_right_bracket = self.browser.find_element_by_css_selector('[jsname = "qCp9A"]').click()
        click_multiplication = self.browser.find_element_by_css_selector('[jsname = "YovRWb"]').click()
        click_3 = self.browser.find_element_by_css_selector('[jsname = "KN1kY"]').click()
        click_minus = self.browser.find_element_by_css_selector('[jsname = "pPHzQc"]').click()
        click_4 = self.browser.find_element_by_css_selector('[jsname = "xAP7E"]').click()
        click_0 = self.browser.find_element_by_css_selector('[jsname = "bkEvMb"]').click()
        click_division = self.browser.find_element_by_css_selector('[jsname = "WxTTNd"]').click()
        click_5 = self.browser.find_element_by_css_selector('[jsname = "Ax5wH"]').click()
        click_equal = self.browser.find_element_by_css_selector('[jsname = "Pt8tGc"]').click()
        time.sleep(5)

    def check_result_test_1(self):
        result = self.browser.find_element_by_css_selector("#cwos")
        formula = self.browser.find_element_by_css_selector('[jsname = "ubtiRe"]')
        assert result.text == '1', "Результат неверный"
        assert formula.text == '(1 + 2) × 3 - 40 ÷ 5 =', "Формула неверная"

    def test_2(self):
        #6 ÷ 0
        click_6 = self.browser.find_element_by_css_selector('[jsname = "abcgof"]').click()
        click_division = self.browser.find_element_by_css_selector('[jsname = "WxTTNd"]').click()
        click_0 = self.browser.find_element_by_css_selector('[jsname = "bkEvMb"]').click()
        click_equal = self.browser.find_element_by_css_selector('[jsname = "Pt8tGc"]').click()
        time.sleep(5)

    def check_result_test_2(self):
        result = self.browser.find_element_by_css_selector("#cwos")
        formula = self.browser.find_element_by_css_selector('[jsname = "ubtiRe"]')
        assert result.text == 'Infinity', "Результат неверный"
        assert formula.text == '6 ÷ 0 =', "Формула неверная"

    def test_3(self):
        #sin()
        click_sinus = self.browser.find_element_by_css_selector('[jsname = "aN1RFf"]').click()
        click_equal = self.browser.find_element_by_css_selector('[jsname = "Pt8tGc"]').click()
        time.sleep(5)

    def check_result_test_3(self):
        result = self.browser.find_element_by_css_selector("#cwos")
        formula = self.browser.find_element_by_css_selector('[jsname = "ubtiRe"]')
        assert result.text == 'Error', "Результат неверный"
        assert formula.text == 'sin() =', "Формула неверная"