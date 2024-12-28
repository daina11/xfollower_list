import tweepy

# 设置认证
bearer_token = 'xxxxx'  # 使用 Bearer Token 进行身份验证

# 创建 API 客户端
client = tweepy.Client(bearer_token)

# 你需要知道用户的用户名或ID，这里我们使用用户名
user_username = "user_name"

try:
    # 获取用户信息
    user = client.get_user(username=user_username)
    user_id = user.data.id
    print(f"获取用户 {user_username} 的 ID: {user_id}")



except tweepy.TweepyException as e:
    print(f"发生错误: {e}")

