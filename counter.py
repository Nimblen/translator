def wr(number):
    with open('count.txt', 'w', encoding='utf-8') as file:
        return file.write(number)
def r():
    with open('count.txt', 'r', encoding='utf-8') as file:
        return file.read()



print(r())