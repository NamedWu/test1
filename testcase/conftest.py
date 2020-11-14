import allure
import pytest
from selenium import webdriver


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('-----------------')
#     driver = webdriver.Chrome()
#     # 获取钩子方法调用结果
#     out = yield
#     # print('用例执行结果', out)
#     # 从钩子方法的嗲用结果中获取测试报告
#     report = out.get_result()
#     print('测试报告：%s' % report)
#     print('步骤：%s' % report.when)
#     print('nodeid：%s' % report.nodeid)
#     print('description:%s' % str(item.function.__doc__))
#     print(('运行结果: %s' % report.outcome))
#     if report.when == call and report.outcome == 'passed':
#         with allure.step("截图并保存"):
#             file_path = '/Users/xiaotaozi/PycharmProjects/auto-qing/web_test/testcase/pic_save/(2).png'
#             driver.get_screenshot_as_file(file_path)
#             with open(file_path, mode="rb") as f:
#                 file = f.read()
#                 allure.attach(file, "用例截图", allure.attachment_type.PNG)