import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

# 注册接口测试
def test_register_success():
    '''注册成功'''
    res = requests.post(f"{BASE_URL}/api/user/register", json={
        "username": "newuser", "password": "123456Abc", "email": "new@qq.com"
    })
    result = res.json()
    assert result["code"] == 200
    assert result["msg"] == "注册成功"

def test_register_username_too_short():
    """用户名太短"""
    res = requests.post(f"{BASE_URL}/api/user/register", json={
        "username": "ab", "password": "123456Abc", "email": "test@qq.com"
    })
    result = res.json()
    assert result["code"] == 400
    assert "用户名长度不能少于3个字符" in result["msg"]

def test_register_username_exists():
    """用户名已存在"""
    res = requests.post(f"{BASE_URL}/api/user/register", json={
        "username": "test01", "password": "123456Abc", "email": "test@qq.com"
    })
    result = res.json()
    assert result["code"] == 400
    assert "用户名已存在" in result["msg"]

#登录接口测试
def test_login_success():
    """正常登录"""
    res = requests.post(f"{BASE_URL}/api/user/login", json={
        "username": "tester001", "password": "123456Abc"
    })
    result = res.json()
    assert result["code"] == 200
    assert result["msg"] == "登录成功"
    assert "token" in result

def test_login_wrong_password():
    """密码错误"""
    res = requests.post(f"{BASE_URL}/api/user/login", json={
        "username": "tester001", "password": "wrong_password"
    })
    result = res.json()
    assert result["code"] == 401
    assert "用户名或密码错误" in result["msg"]



# 商品搜索接口测试
def test_search_success():
    """正常搜索"""
    res = requests.get(f"{BASE_URL}/api/product/search", params={"keyword": "手机"})
    result = res.json()
    assert result["code"] == 200
    assert result["msg"] == "查询成功"

def test_search_empty_keyword():
    """空关键词"""
    res = requests.get(f"{BASE_URL}/api/product/search", params={"keyword": ""})
    result = res.json()
    assert result["code"] == 400
    assert "请输入搜索关键词" in result["msg"]

# 购物车接口测试
def test_add_cart_success():
    """正常添加购物车"""
    res = requests.post(f"{BASE_URL}/api/cart/add", json={
        "product_id": 1, "quantity": 2
    })
    result = res.json()
    assert result["code"] == 200
    assert result["msg"] == "添加购物车成功"

def test_add_cart_overstock():
    """超出库存"""
    res = requests.post(f"{BASE_URL}/api/cart/add", json={
        "product_id": 1, "quantity": 50
    })
    result = res.json()
    assert result["code"] == 400
    assert "库存不足" in result["msg"]

# 结账接口测试
def test_checkout_without_login():
    """未登录拦截"""
    res = requests.post(f"{BASE_URL}/api/order/checkout", json={
        "cart_ids": [1], "address_id": 1
    })
    result = res.json()
    assert result["code"] == 401
    assert "请先登录" in result["msg"]

# 删除地址测试
def test_delete_address():
    '''删除成功'''
    res=requests.delete(f"{BASE_URL}/api/address/delete", json={
        "address_id": 1
    })
    result = res.json()
    assert result["code"] == 200
    assert "删除成功" in result["msg"]

def test_delete_address_unfinsh_order():
    '''有未完成订单，删除失败'''
    res = requests.delete(f"{BASE_URL}/api/address/delete", json={
        "address_id": 101,
    })
    result = res.json()
    assert result["code"] == 400
    assert "当前地址有订单正在处理，不允许删除" in result["msg"]