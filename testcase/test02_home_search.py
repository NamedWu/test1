import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def test_select():
    driver = webdriver.Chrome()
    path = 'https://www.hibobi.com/'
    driver.get(path)
    # 通过显示等待的方法判断元素是否出现
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='c-header']/div[2]/div[3]/div/input")))
    select = driver.find_element_by_xpath('//*[@id="c-header"]/div[2]/div[3]/div/input')
    Select(select).select_by_visible_text('Boy')
    time.sleep(2)


if __name__ == '__main__':
    pytest.main()




# # 根据下标进行选择，从0开始
# Select(select).select_by_index(1)
# time.sleep(2)
# # 根据value的值选择
# Select(select).select_by_value('daily')
# time.sleep(2)
# # 根基text选择
#
#
# # 判断选择是否预期
# WebDriverWait(driver,20).until(EC.element_located_to_be_selected((By.XPATH,'//*[contains(text(),"关注了")]')))