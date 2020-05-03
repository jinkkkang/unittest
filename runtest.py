# -*- coding: UTF-8 -*-
import unittest
from lib import HTMLTestRunner
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':


    # 组织用例的方式

    #一：  使用dicver 查找所有用例
    suites = unittest.defaultTestLoader.discover("./testcases/", pattern='test*.py')


    #二: 使用addTests 精准添加
    from testcases.testwangwu import WanguuTestCase
    from testcases.testzhangsan import ZhangsanTestCase
    from testcases.testlisi import LisiTestCase
    suites = unittest.TestSuite()
    suites.addTests(unittest.makeSuite(ZhangsanTestCase))
    suites.addTests(unittest.makeSuite(LisiTestCase))
    suites.addTests(unittest.makeSuite(WanguuTestCase))

    # 执行测试的方式
    #一直接运行测试
    runner = unittest.TextTestRunner()
    runner.run(suites)

    #二使用HTMLTestRunner来运行测试,生成测试报告
    file = "report/report.html"
    fp = open(file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Python Test Report', description='This is Python Report')
    runner.run(suites)
    fp.close()

    #三 python3可以使用BeautifulReport来生成测试报告
    result = BeautifulReport(suites)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')

