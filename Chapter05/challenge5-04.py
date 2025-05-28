personal_dir={"身長":170,"体重":58}
keys=input("キーを入力してください:")
if keys in personal_dir:
    b = personal_dir[keys]
    print(b)
else:
    print("そんなキーはありません。")

