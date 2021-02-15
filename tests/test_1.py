from pages.main_page import MainPage

def test_calc_1(browser):
    url = 'https://www.google.com/'
    page = MainPage(browser, url)
    page.open()
    page.go_to_calculator()
    page.test_1()
    page.check_result_test_1()