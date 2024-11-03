def words_sorting(*args):
    words_values_dict = {}
    sum_of_values = 0
    for curr_word in args:
        if curr_word not in words_values_dict:
            words_values_dict[curr_word] = 0
            for letter in curr_word:
                words_values_dict[curr_word] += ord(letter)
    for curr_value in words_values_dict.values():
        sum_of_values += curr_value

    sorted_dict = sorted(words_values_dict.items(), key=lambda kvp: -kvp[1] if sum_of_values % 2 != 0 else kvp[0])
    result = ''
    for word, value in sorted_dict:
        result += f'{word} - {value}\n'
    return result
