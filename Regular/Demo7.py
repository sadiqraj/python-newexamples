import re
st = input("Enter a String : ")
res = re.findall(r"\w\w",st)
print(res)
print("------------------")
res = re.findall(r"\b\w\w",st)
print(res)
print("------------------")
res = re.findall(r"\b\w.",st)
print(res)
print("------------------")