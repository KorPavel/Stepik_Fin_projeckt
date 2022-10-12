from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

def test_guest_can_go_to_login_page(browser):
    print('\n\t\tTEST#1 "Guest can go to login page"')
    page = MainPage(browser, link) 
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    print('\n\t\tTEST#2 "Guest should see login link"')
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()