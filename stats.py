def word_count(text):
    word_list = text.split()
    word_num = len(word_list)
    return word_num

def char_count(text):
    counts = {}
    text = text.lower()
    
    for char in text:  
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts


def sort_chars(char_dict):
    formatted_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    
    # Define a function that returns the value to sort by
    def sort_on(dict):
        return dict["num"]
    
    # Sort the list in-place
    formatted_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return formatted_list