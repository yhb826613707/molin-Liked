# 1. 导入Flask类
from flask import Flask, request, render_template
from flask_cors import CORS
import json
from all import *
from config import *
# app = Flask(__name__)
app = Flask(__name__,template_folder='./templates/autotest-web/public',static_folder='./templates/autotest-web/public')
CORS(app, supports_credentials=True)
path = "../../AutoTest/pytestframe/test/cases"


# 实现主页,用例列表和选取用例
@app.route('/')
def index():
    # 获取用例列表
    testcase_list = get_testcase(path)
    # 渲染模板
    return render_template('index.html', title=u"用例筛选", testcases=testcase_list)

@app.route('/getCase')
def get_case():
    # 获取用例列表
    testcase_list = get_testcase(path)
    return testcase_list

# 执行用例
@app.route('/ExecuteCase', methods=['POST'])
def Execute_Case():
    if request.method == 'POST':
        # 获取前端传回来的值
        # testcases = request.values
        data = request.get_data()
        # ['./AutoTest/pytestframe/test/hhh']
        data = json.loads(data)['executeCases']
        # print(data)
        testcases = ""
        for i in data:
            testcases += i+" "
        print("1111111: ",testcases)
        # 启动选择的用例
        main1(testcases)

        return "用例启动中"

    else:
        return " 'it's not a PUT operation! "












if __name__ == '__main__':
    # 运行Flask应用
    # 如何设置， 使得服务器主机的浏览器可以访问?  '0.0.0.0'开放所有的IP， 使得可以访问
    # 如何修改端口?  # 可能会报错:Address already in use
    app.run(host='0.0.0.0', port=5000,debug=True)