from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    print('\n\t\tTEST#1 "Guest can go to login page"')
    page = MainPage(browser, link) 
    page.open()
    page.go_to_login_page()