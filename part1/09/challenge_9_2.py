like_color = input("好きな色はなんですか？:").rstrip()

with open("like_color.txt", "w", encoding="utf-8") as fail_obj:
    fail_obj.write(like_color)
print("保存しました")
