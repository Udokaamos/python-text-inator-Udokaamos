word = input("Enter the word: ")
text2 = "inator"
text3 = len(word)
text4 = '000'
text5 = "-inator"
new_text = word + text2
text6 = str(text3) + text4
new_text2 = word + text5
if text3 <= 8:
    print(f'{word} ➞ "{new_text}  {text6}"')
else:
    print(f'{word} ➞  "{new_text2} {text6}"')