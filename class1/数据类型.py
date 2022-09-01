s2 = 'It took me six months to write this Python tutorial. \
Please give me more support. \
I will keep it updated.'
print(s2)

str1 = """It took me 6 months to write this Python tutorial.
Please give me a to 'thumb' to keep it updated.
The Python tutorial is available at http://c.biancheng.net/python/."""
print(str1)

strname = "hello" " world"
print(strname)

strA = "Hello"
strB = " World"
strname1 = strA + strB
print(strname1)

age = 20
strname2 = "年龄：" + str(age)
print(strname2)

print("hello".startswith('hell'))
print("hello".endswith('lo'))
print("This is Tom".find("hist", 0)) # 不存在返回-1
print("This is Tom".rfind("is"))
print("This is Tom".index("is")) # 如果查找字符不存在会抛出异常
print("This is Tom".rindex("is"))
print("This is Tom".replace("is","'s",1))
print("hello chris".capitalize())
print("hello china".title())
print("You are perfice".lower())
print("you are my sunshine".upper())
print("My mother is good".swapcase())

print("hello".ljust(10))
print("haha".rjust(10))
print("nihao".center(10))

print("   abcd".lstrip())
print("abcd  ".strip())
print("   abcd  ".strip())

print("helloworld".partition('llo')) # 字符串分成三个元素 (llo前, llo, llo后)
print("sunshine".rpartition('n'))
print("MY,HOBBY,IS,COMPER".split(","))
print("Hello\nChris\nHe".splitlines())
print(" ".join(["I", "like", "c++"]))

print(len('cpianchen'))
print('cbiancheng'.count('f')) # 如果检索的字符串不存在，则返回 0，否则返回出现的次数。

print(b"http://www.cighte.com")
b4 = bytes("C语言中文网8岁了", encoding="UTF-8")
print(b4)
b5 = "C语言中文网8岁了".encode("UTF-8")
print(b5)

strb = "C语言中文网8岁了"
bytes = strb.encode()
print(bytes)
print(bytes.decode())