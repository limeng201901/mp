import allure
from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage


class Search(BasePage):

    def search(self):

         self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        #self.parse("../page/search.yaml", "search")


    def search2(self):

            self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        # self.parse("../page/search.yaml", "search")

    def cancel(self):
        self.parse("../page/search.yaml", "cancel")
        self.goto_xueqiu()





