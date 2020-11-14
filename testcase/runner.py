import allure
import os
import pytest
from web_test.testcase.read_yaml import datas
pytest.main(['-s', 'test01_home_tab.py', '--alluredir', './temp', '-s'])
os.system('allure generate ./temp -o ./report --clean')
