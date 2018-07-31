def division2(num):
    """
    引数を2で割った商を返します
    :params num : int
    """
    return num // 2

def multiplication4(num):
    """
    引数を4倍にして返します
    :params num : int
    """
    return num * 4

num = int(input("数値を入力してください:"))
result = division2(num)
print(result)
print(multiplication4(result))
