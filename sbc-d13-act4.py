def custom_tokenization(input_text):
    tokens = []
    current_word = ""
    for char in input_text:
        if char in [' ', ',']:
            if current_word:
                tokens.append(current_word.lower())
                current_word = ""
        else:
            current_word += char
    if current_word:
        tokens.append(current_word.lower())
    return tokens


input_text = input("Enter: ")
token_list = custom_tokenization(input_text)
print(token_list)  
