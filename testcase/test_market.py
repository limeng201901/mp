import allure

from ui_framework.page.app import App
from ui_framework.page.basepage import BasePage


class TestMarket():
    def setup(self):
        self.app_main = App().start().goto_main()


    @allure.severity('blocker')
    @allure.feature('搜索1')
    def test_goto_market(self):
       with allure.step('搜索1-1'):
           self.search= self.app_main.goto_market().goto_search()
           self.search.search()
           self.search.cancel()

       #
       with allure.step('搜索1-2'):
           self.app_main.goto_market().goto_search().search2()






