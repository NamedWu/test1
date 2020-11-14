import allure
import pytest
from web_test.testcase.read_yaml import datas
from web_test.public_tools.base_tools import base_tools
from selenium import webdriver


class Test_home_tab:
    def setup(self):
        """"
        构造函数，实例化变量
        """
        self.driver = base_tools()
        self.driver.open_browser('gc')
        self.driver.get_url('https://www.hibobi.com/')

    @allure.feature('首页tab点击')
    @allure.story('recommended按钮点击')
    @pytest.mark.parametrize('recommended', datas['homepage'])
    def test01_recommended(self, recommended):
        """
        测试按钮recommended按钮点击
        :param recommended:
        :return:
        """
        with allure.step('读取完用例，开始执行'):
            self.driver.run_case_list(self.driver.find_case_locator(recommended))
            self.driver.save_image_to_allure()
            pic = '/Users/xiaotaozi/PycharmProjects/auto-qing/web_test/testcase/2020-11-14/2020-11-14-16_20_04.png'
            allure.attach('在fixture后置操作里面添加一个附件txt', 'fixture后置附件',
                          allure.attachment_type.TEXT)



    @allure.step('关闭浏览器')
    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
