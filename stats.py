def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents  


def count_characters(text_to_count):
    count_dict = {}
    split = list(text_to_count.lower())

    for char in split:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    return count_dict

def sort_on(dict):
    return dict[1]

def sort_dict(dict_to_sort):
    sorted_dict = dict(sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=True)) 
    return(sorted_dict)