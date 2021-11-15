import pytest


def summ(a,b):
    return a+b

class Testone():
    def setup(self):

        print("测试开始>>>")
    def teardown(self):
        print("测试结束！！")
        print("测试结束！！")




    def test_summ_1(self):
        assert summ(9,4)==13
    def test_summ_2(self):
        assert summ(9,9)==18

    def test_summ_4(self):
        assert summ(9,9)==19
    def test_summ_5(self):
        assert summ(9,9)==18
    def test_summ_7(self):
        assert summ(9,9)==18


if __name__ == '__main__':
    pytest.main(['-s','testadd.py'," --html=report.html"])



