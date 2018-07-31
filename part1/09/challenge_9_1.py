fail_obj = open("test.txt", "r", encoding="cp932")
print(fail_obj.read())
fail_obj.close()
