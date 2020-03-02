fd = open('name.txt', encoding="UTF-8")
try:
    for line in fd:
        print(line)
finally:
    fd.close()

with open('name.txt',encoding="UTF-8") as f:
    for line in f:
        print(line)
