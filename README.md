ECShop B2C商城接口自动化与Mock实战

项目简介

本项目基于《ECShop需求规格说明书》，在无后端源码的情况下，使用 Flask 搭建 Mock 服务，并使用 Python + Requests + Pytest 编写接口自动化测试脚本。



&#x20;技术栈

编程语言：Python



自动化框架：Requests, Pytest

Mock服务：Flask

测试报告：pytest-html



项目文件说明

app.py：基于 Flask 搭建的 Mock 服务，模拟了注册、登录、购物车增删改查、地址删除等 12+ 接口。



test\_ecshop\_api.py：接口自动化测试脚本，包含正常流、边界值等断言场景。



report.html：自动化测试执行后生成的可视化测试报告。



如何运行

安装依赖：pip install flask requests pytest pytest-html



启动 Mock 服务：python app.py



执行自动化测试：pytest test\_ecshop\_api.py -v



实战收获

在测试过程中，结合 HTTP 状态码与后端日志排查异常，成功定位了 500 除零异常、405 请求方法不匹配等后端缺陷，实现了缺陷定位、修复与回归验证的完整闭环。

