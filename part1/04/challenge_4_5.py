def str_to_float(text):
    """
    文字列をfloat型に変換して返します
    :params text : str
    """
    try:
        return float(text)
    except ValueError:
        print("数値に変換できません")

text = input("数値に変換する文字を入力してください:")
print(str_to_float(text))
