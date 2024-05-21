import pytest
import requests

def setup_module():
    print("准备测试数据")

def teardown_module():
    print("清理测试数据")

def test_mobile_post():
    canshu = {"shouji":"15656755448","appkey":"0c818521d38759e1"}
    r = requests.post("http://sellshop.5istudy.online/sell/shouji/query",params=canshu)
    print(r.status_code)  # 接口状态返回码
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["province"] == "上海"

def test_mobile_get():
    canshu = {"shouji": "15656755448", "appkey": "0c818521d38759e1"}  # params用字典来写
    r = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=canshu)

    print(r.status_code)  # 接口状态返回码
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["province"] == "上海"

if __name__ =='__main__':
    pytest.main()