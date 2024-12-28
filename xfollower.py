import http.client
import json
import openpyxl

# 连接到API
conn = http.client.HTTPSConnection("api.apidance.pro")

# 请求参数
payload = ''
headers = {
    'apikey': 'your_key'  # 记得替换为实际的apikey
}

# 创建一个新的Excel文件
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Followers List"

# 写入标题
ws.append(["screen_name", "user_id"])

# 初始请求URL
screen_name = "screen_name"
user_id = "user_id"
url = f"/1.1/friends/list.json?screen_name={screen_name}&user_id={user_id}&count=200&cursor=-1"

# 发送请求并处理分页
while True:
    # 发送GET请求
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()

    # 解析JSON数据
    try:
        user_data = json.loads(data.decode("utf-8"))
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        break

    # 获取用户列表并写入Excel
    if 'users' in user_data:
        for user in user_data['users']:
            screen_name = user.get('screen_name', '')
            user_id = str(user.get('id', ''))  # 将 user_id 转换为字符串
            ws.append([screen_name, user_id])

    # 获取分页信息
    next_cursor = user_data.get('next_cursor', 0)
    if next_cursor == 0:
        break  # 如果没有更多数据，停止请求
    else:
        # 构造下一页的URL
        url = f"/1.1/friends/list.json?screen_name={screen_name}&user_id={user_id}&count=200&cursor={next_cursor}"

# 保存Excel文件
wb.save("followers_list.xlsx")

print("Excel文件保存成功！")
