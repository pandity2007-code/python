# using string.replace(old word, new word)
# write a program to print name , id,and the date


letter = '''Dear <|Name|>
            branch - xxxxxxx
            You are selected
            <|date|>'''

print(letter.replace("<|Name|>","Yash saraswat").replace("xxxxxxx","CSE").replace("<|date|>"," 05 aug 2025") )
    