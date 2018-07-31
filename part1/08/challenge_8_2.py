import cubed

num = input("求めたい立方体の辺を入力してください").rstrip()
try:
    num = float(num)
    if num <= 0:
        print("0より大きな数値を入力してください")
    else:
        print(cubed.cube_volume(num))
except ValueError:
    print("数値を入力してください")
