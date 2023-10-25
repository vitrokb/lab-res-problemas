amount_of_lines = int(input())
lines = []

answer = []

for i in range(0, amount_of_lines):
    line = input()
    lines.append(line)

for text in lines:
    if text == " " or "":
        print(" ")
    else:
        word = ""
        text_in_list = text.split()
        for i in text_in_list:
            word = word + i[0]
        print(word)
