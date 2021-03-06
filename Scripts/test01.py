import allure
import pytest


class Test01():
    @allure.step(" 03执行学院新增操作")
    def test01(self):
        print("执行学院新增操作")
    @allure.step("执行学院更新操作")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test02(self):
        allure.attach("断言开始","学院是否更新成功")
        print("执行学院更新操作")
        allure.attach("断言结束","更新成功！")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        print("test03被执行")
        assert 0
    def test04(self):
        print("test04被执行")
    def test05(self):
        print("test05被执行")
