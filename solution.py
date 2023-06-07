text = input("Enter the word: ")
text2 = "inator"
text3 = len(text)
text4 = 1000
text5 = "-inator"
new_text = text + text2
text6 = text3 * text4
new_text2 = text + text5
if text3 <= 8:
    print(f'{text} -->  "{new_text}  {text6}"')
else:
    print(f'{text} -->  "{new_text2} {text6}"')