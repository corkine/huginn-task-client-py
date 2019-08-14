from huginnTask.publisher import get_status, push_data

token = ("corkine", "spring123456")

# 获取状态
groupName = "zsw_g"
print(get_status(groupName, token))

# 提交任务
retry = 3
data = [
	{
	"group":groupName,
	"data":"帮马章竞改英文摘要2"
	},
	{
	"group":groupName,
	"data":"睡觉2"
	}
]
res2 = push_data(groupName, retry, data, token)
print(res2)

# 重新获取状态
print(get_status(groupName, token))