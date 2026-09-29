from flask import Flask, request, jsonify

app = Flask(__name__)


# 1. 注册接口 @为装饰器
@app.route('/api/user/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    email = data.get('email', '')

    if len(username) < 3:
        return jsonify({"code": 400, "msg": "用户名长度不能少于3个字符"})

    if len(password) < 6:
        return jsonify({"code": 400, "msg": "登录密码不能少于6个字符"})

    if username == "test01":
        return jsonify({"code": 400, "msg": "用户名已存在"})

    return jsonify({"code": 200, "msg": "注册成功"})


# 2. 登录接口
@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')

    # 模拟正确登录
    if username == "tester001" and password == "123456Abc":
        return jsonify({"code": 200, "msg": "登录成功", "token": "fake-token-123"})
    else:
        return jsonify({"code": 401, "msg": "用户名或密码错误"})


# 3. 商品搜索接口
@app.route('/api/product/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword', '')

    if not keyword:
        return jsonify({"code": 400, "msg": "请输入搜索关键词！"})

    return jsonify({"code": 200, "msg": "查询成功", "data": [{"id": 1, "name": f"搜索到的商品：{keyword}"}]})


# 4. 添加购物车接口
@app.route('/api/cart/add', methods=['POST'])
def add_cart():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    # 模拟库存只有10件
    if quantity > 10:
        return jsonify({"code": 400, "msg": "库存不足，该商品目前只有10个"})

    return jsonify({"code": 200, "msg": "添加购物车成功"})


# 5. 结账接口（未登录拦截）
@app.route('/api/order/checkout', methods=['POST'])
def checkout():
    # 模拟：如果请求头里没有 token，说明没登录
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"code": 401, "msg": "请先登录后再结算"})

    return jsonify({"code": 200, "msg": "订单创建成功"})


@app.route('/api/address/delete', methods=['DELETE'])
def delete_address():
    data = request.json
    address_id = data.get('address_id')

    # 模拟：如果没传地址ID，报错
    if not address_id:
        return jsonify({"code": 400, "msg": "请选择要删除的地址"})

    # 模拟：如果地址ID是 101（假设这个地址有未完成订单），拦截删除
    if address_id == 101:
        return jsonify({"code": 400, "msg": "当前地址有订单正在处理，不允许删除"})

    # 其他情况都删除成功
    return jsonify({"code": 200, "msg": "删除成功"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)