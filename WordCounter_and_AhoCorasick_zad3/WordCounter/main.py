from collections import Counter


def generate_words(file):
    with open(file) as opened_file:
        for line in opened_file:
            tokens = \
                line.lower().replace(',', '').replace('.', '').replace('!', '')\
                    .replace('?', '').replace('-', '').replace('(', '')\
                    .replace(')', '').replace(':', '').split()
            for token in tokens:
                yield token


def count_sigle_word(file):  # returns a dictionary of elements and its occurring
    list_of_words = list(generate_words(file))
    counter = Counter(list_of_words)

    # alternative code for 'Counter' function
    # for element in list_of_words:
    #     if element not in dict_of_words:
    #         dict_of_words[element] = 0
    #     dict_of_words[element] +=1
    return counter


def count_all_words(file):
    list_of_words = list(generate_words(file))
    return len(list_of_words)


def rank_all_the_words(file):
    all_words = count_sigle_word(file)
    return all_words.most_common()


def words_with_same_position(file):  # first function (misunderstood the assignment instructions)
    dict_of_words = dict(count_sigle_word(file))
    test_list = list(dict_of_words.values())
    test_dict = list(dict_of_words)
    test_list.append(' ')
    test_list.append(' ')
    counter = 0
    list_of_draws = []
    for element in dict_of_words:
        if dict_of_words[element] == test_list[counter + 1] and dict_of_words[element] == test_list[counter + 2]:
            list_of_draws.extend([element, (test_dict[test_dict.index(element) + 1]),
                                  (test_dict[test_dict.index(element) + 2])])
        counter += 1
    return list_of_draws


def show_ranks_with_draws(file, num):
    dict_of_words = dict(rank_all_the_words(file))
    list_of_occurrences = list(dict_of_words.values())
    list_of_occurrences.extend([0, 0])

    i = 0  # shows position in a list
    while num > 0:
        while list_of_occurrences[i] == list_of_occurrences[i + 1]:
            i = i + 1

        while list_of_occurrences[i] != list_of_occurrences[i + 1]:
            i = i + 1
            num -= 1
            break

    dict_of_words = {element: dict_of_words[element] for element in list(dict_of_words)[:i]}

    return dict_of_words


if __name__ == '__main__':
    file = 'potop.txt'
    print(show_ranks_with_draws(file, 10))

