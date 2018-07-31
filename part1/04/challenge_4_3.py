def calculation(a, b, c, multiplication=3, division=2):
    """
    Returns (a+b+c) * multiplication / division
    :params all : int
    :params a, b, c is must
    :params multiplication, division is option
    """
    return (a+b+c) * multiplication / division

text = input("カンマ区切りで数値を入力してください:")
array = text.split(",")
if len(array) < 3:
    print("引数が足りません")
elif len(array) == 3:
    print(calculation(int(array[0]), int(array[1]), int(array[2])))
elif len(array) == 4:
    print(calculation(int(array[0]), int(array[1]), int(array[2]), int(array[3])))
else:
    print(calculation(int(array[0]), int(array[1]), int(array[2]), int(array[3]), int(array[4])))
