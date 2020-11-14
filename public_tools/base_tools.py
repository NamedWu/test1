import os

from selenium.common.exceptions import NoSuchElementException
import allure
import logging
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

log = logging.getLogger(__name__)


class base_tools:
    """
    启动浏览器相关操作
    """

    def __init__(self):
        """
        构造函数，创建必要的实例变量
        """
        self.driver = None

    def open_browser(self, br='gc'):
        """
        打开浏览器
        :param br: 默认是gc 谷歌浏览器
        :return:
        """
        log.info('打开浏览器')
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.firefox()
        elif br == 'ie':
            self.driver = webdriver.ie
        else:
            print("浏览器不支持！请选择谷歌浏览器，Firefox浏览器，IE浏览器")
            pass
        # 默认隐式等待
        self.driver.implicitly_wait(11)

    def get_url(self, url=None):
        """
        打开浏览器
        :param url:网站地址
        :return:
        """
        log.info('打开网址')
        self.driver.get(url)

    def __find_ele(self, locator, type=1):
        """
        元素定位方法
        :param locator: 元素定位值
        :param type: 元素定位方法，默认是Xpath , 1:Xpath 2:css_selector
        :return:
        """
        log.info('元素定位')
        ele = None
        self.ele = None
        try:
            if type == 1:
                ele = self.driver.find_element_by_xpath(locator)
            elif type == 2:
                ele = self.driver.find_element_by_css_selector(locator)
                pass
            elif type == 3:
                ele = self.driver.find_element_by_id(locator)
            elif type == 4:
                ele = self.driver.find_element_by_name(locator)
            elif type == 5:
                ele = self.driver.find_element_by_partial_link_text(locator)
            elif type == 6:
                ele = self.driver.find_elements_by_class_name(locator)
            elif type == 7:
                ele = self.driver.find_element_by_link_text(locator)
            else:
                ele = self.driver.find_element_by_tag_name(locator)
        except Exception as e:
            print(e)
        self.ele = ele
        return self.ele

    def click(self, locator=None, type=1):
        """
        创建点击事件
        :return:
        """
        log.info('元素点击')
        ele = self.__find_ele(locator, type)
        ele.click()

    def input(self, locator, type, value=None):
        """
        创建输入事件
        :param value: 输入的值
        :param locator: 默认Xpath定位
        :return:
        """
        log.info('元素输入')
        ele = self.__find_ele(locator, type)
        ele.send_keys(str(value))

    def quit(self):
        """
        退出浏览器
        :return:
        """
        log.info('关闭浏览器')
        self.driver.quit()

    def is_element_present(self, locator, type):
        """
        判断页面元素是否存在
        :param locator: 元素查找方法
        :param type: 元素
        :return:true
        """
        log.info('判断元素是否存在')
        try:
            self.__find_ele(locator, type)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True

    def save_image_to_allure(self):
        """
        页面截图并保存截图
        :param img_doc: 截图说明
        :return:
        """
        # 截取图片并保存至本地
        log.info("截图并保存")
        with allure.step("截图并保存"):
            picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
            print(os.getcwd())
            # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
            try:

                file_path = os.getcwd() + '/' + directory_time
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                else:
                    pass
            except BaseException as msg:
                print("新建目录失败：%s" % msg)

            try:
                file_url = file_path+ '/' + picture_time + '.png'
                self.driver.save_screenshot(file_path + '/' + picture_time + '.png')
                print("%s ：截图成功！！！" % file_url)
            except BaseException as pic_msg:
                print("截图失败：%s" % pic_msg)
            with open(file_url, mode="rb") as f:
                file = f.read()
                allure.attach(file, "用例截图", allure.attachment_type.PNG)


    # 浏览器前进操作
    def browser_forward(self):
        log.info('继续下一页')
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        log.info('返回前一页')
        self.driver.back()

    def find_case_locator(self, recommended):
        """
        读取
        :param recommended:
        :return:
        """
        log.info('读取用例中的cases')
        cases2 = recommended['cases']
        return cases2

    def find_case_title(self, recommended):
        """
        读取用例title
        :return:
        """
        log.info('读取用例title')
        title = recommended['title']
        return title

    def find_case_browser(self, recommended):
        """
        读取浏览器
        :return:
        """
        browser = recommended['browser']
        log.info('选择的浏览器是{}'.format(browser))
        return browser

    def run_case_list(self, list):
        for dict_ele in list:
            method = dict_ele['method']
            locator = dict_ele['locator']
            type = dict_ele['type']
            new_page_ele = dict_ele['new_page_ele']
            if method == 'input':
                value = dict_ele['value']
            else:
                value = None
            self.run_single(new_page_ele, type, value, method, locator)

    def run_single(self, new_page_ele, type, value, method, locator):
        log.info('执行单个用例')
        self.case_operate(method, locator, type, value)
        res = self.is_element_present(new_page_ele, type)
        if res is True:
            print("用例执行成功")
        else:
            print("页面中没有查找到所需要的元素")
        # self.save_image_to_allure()

    def case_operate(self, method, locator, type, value):
        log.info("读取用例操作，并进行相应操作")
        if method == 'input':
            self.input(locator, type, value)
        else:
            self.click(locator, type)

    def select_option(self):
        sel = Select(self.driver.find_element_by_id('com.p1.mobile.putong:id/ccode'))
        for option in sel.options:
            print(option.text)
