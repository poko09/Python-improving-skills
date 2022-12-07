from collections import Counter


def generate_words(file):  # przesłonięcie symbolu wbudowanego
    with open(file) as opened_file:
        for line in opened_file:
            tokens = \
                line.lower().replace(',', '').replace('.', '').replace('!', '')\
                    .replace('?', '').replace('-', '').replace('(', '')\
                    .replace(')', '').replace(':', '').split()  # polecam re.sub albo regex.sub
            yield from tokens


def count_sigle_word(file):  # returns a dictionary of elements and its occurring
    return Counter(generate_words(file))

    # alternative code for 'Counter' function  # Counter to nie funkcja, tylko klasa


def count_all_words(file):  # a nie szybciej zsumować wartości trzymane w Counterze?
    list_of_words = list(generate_words(file))  # pakowanie wartości z generatora do listy, trochę zabija jego sens
    return len(list_of_words)


def rank_all_the_words(file):
    all_words = count_sigle_word(file)
    return all_words.most_common()


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

    return dict_of_words  # za dużo zwraca


if __name__ == '__main__':
    file = 'potop.txt'
    print(show_ranks_with_draws(file, 10))

