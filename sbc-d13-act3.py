word = input("Enter > ")

prefixes = ["un", "re", "ful", "less", "dis", "pre", "mis", "ness", "ly", "er"]
broken_word = []
i = 0
back_index = -4

while i < len(word):
    front_part = word[:i]
    front_length = len(front_part)
    back_part = word[back_index:]
    back_length = len(back_part)
    i += 1 
    back_index += 1
    
    if front_part in prefixes:
        broken_word.append(front_part.strip())
        broken_word.append(f"{'#' * front_length}{word[i-1:]}")
        print(broken_word)
        break
    elif back_part in prefixes:
        broken_word.append(f"{word[:back_index - 1]}{'#' * back_length}")
        broken_word.append(word[back_index - 1:])
        print(broken_word)
        break

