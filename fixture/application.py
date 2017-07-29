from selenium.webdriver.firefox.webdriver import WebDriver

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_homepage(self):
        wd = self.wd
        wd.get("https://doska.io/")

    def search_kw(self, search_item):
        wd = self.wd
        wd.find_element_by_name("search_text").click()
        wd.find_element_by_name("search_text").clear()
        wd.find_element_by_name("search_text").send_keys(search_item.keyword)
        wd.find_element_by_xpath("//form[@id='form-search']/fieldset/input").click()

    def select_first(self):
        wd = self.wd
        wd.find_element_by_link_text("Продам iPhone 5 16GB MD297CS/A").click()

    def destroy(self):
        self.wd.quit()