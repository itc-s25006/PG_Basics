answer = input("好きなひらがなを記入して")
with open("b.txt","w") as f:
    f.write(answer)
