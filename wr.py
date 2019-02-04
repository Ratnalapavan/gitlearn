f=open("employee.txt","a")
lst=["a\n","b\n","c\n","d\n"]
f.writelines(lst)
print(f.tell())
f.seek(0)
f.write("123456789\n")
print(f.tell())
f.close()
