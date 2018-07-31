answers = ["15", "22", "30", "41", "55", "69", "70", "87", "94"]

while True:
    select_num = input("2桁の数字を当てよう！\n'q'で終了できるよ").rstrip()
    if select_num == "q":
        break
    elif select_num in answers:
        print("正解")
    else:
        print("不正解")
    print("数字を入力するか、qで終了します")
