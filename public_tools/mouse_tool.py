from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class mouse_operation:
    """
    鼠标对应的各种操作
    click(on_element=None) ——单击鼠标左键
    click_and_hold(on_element=None) ——点击鼠标左键，不松开
    context_click(on_element=None) ——点击鼠标右键
    double_click(on_element=None) ——双击鼠标左键
    drag_and_drop(source, target) ——拖拽到某个元素然后松开
    drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
    key_down(value, element=None) ——按下某个键盘上的键
    key_up(value, element=None) ——松开某个键
    move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
    move_to_element(to_element) ——鼠标移动到某个元素
    move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
    perform() ——执行链中的所有动作
    release(on_element=None) ——在某个元素位置松开鼠标左键
    send_keys(*keys_to_send) ——发送某个键到当前焦点的元素send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
    """
    def __init__(self):
        """
        构造函数，创建实例化变量
        """
        self.driver = webdriver.Chrome()

    def mouse_click(self, on_element=None):

        ActionChains(self.driver).click()

    def option_frame_click(self, locator1, locator2, type):
        """
        下拉框元素的点击
        :param locator1: 存在下拉框的元素定位
        :param locator2: 下拉框中的元素定位
        :return:
        """
        ele1 = self.__find_ele(locator1, type)
        ele2 = self.__find_ele(locator2, type)
        ActionChains(self.driver).move_to_element(ele1).click(ele2).perform()