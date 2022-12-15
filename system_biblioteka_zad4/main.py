import json
import os


class Library:
    path = '/Users/karol/PycharmProjects/system_biblioteka_zad4/list_of_books.json'
    books = [{'id': 1, "Author": "Witkiewicz", "Title": "Szewcy", "Borrowed": False},
             {'id': 2, "Author": "Lem", "Title": "Bajki robotow", "Borrowed": False}] # example of adding books to json list

    if os.path.isfile(path) == True:
        print("istnieje")
        print("list_of_books.json")
    else:
        file = "list_of_books.json"
        with open(file, "w", encoding="utf-8") as infile:
            json_object = json.dumps(books, indent=4)
            infile.write(json_object)

    def open_json(self, file):
        with open(file, mode='r', encoding='utf-8') as read_file:
            sample_load = json.load(read_file)
        return sample_load

    def add_book(self):
        name_of_author = input("Podaj imię autora: ")
        name_of_title = input("Podaj tytuł książki: ")

        sample_load = self.open_json('list_of_books.json')
        num = len(sample_load) - 1
        id_num = sample_load[num].get('id') + 1
        sample_load.append({
            'id': id_num,
            'Author': name_of_author,
            'Title': name_of_title,
            'Borrowed': False})
        with open('list_of_books.json', mode='w') as write_file:
            json.dump(sample_load, write_file)

    def show_all_books(self):
        sample_load = self.open_json('list_of_books.json')
        print(json.dumps(sample_load, indent=3))

    def find_book_by_title(self) -> bool:
        input_value = input("Podaj tytul ksiazki: ")
        sample_load = self.open_json('list_of_books.json')
        input_key = 'Title'
        if not any(_dict[input_key] == input_value for _dict in sample_load if input_key in _dict):
            print("Nie ma takiej pozycji w bibliotece")
            return False
        print ("Taka ksiazka istnieje :)")
        return True

    def find_book_by_author(self) -> bool:
        input_value = input("Podaj autora ksiazki: ")
        sample_load = self.open_json('list_of_books.json')
        input_key = 'Author'
        if not any(_dict[input_key] == input_value for _dict in sample_load if input_key in _dict):
            print("Nie ma takiej pozycji w bibliotece")
            return False
        print("Taka ksiazka istnieje!")
        return True

    def delete_book(self):
        input_value = int(input("Podaj ID ksiazki, ktora chcesz usunac: "))
        sample_load = self.open_json('list_of_books.json')
        new_list = [i for i in sample_load if not (i['id'] == input_value)]
        with open('list_of_books.json', mode='w') as write_file:
            json.dump(new_list, write_file)

    def current_user(self):
        log_name = input("Czytelniku podaj login do zalogowania się do strony: ")
        return log_name

    def user_login(self):
        log_name = input("Czytelniku podaj login do zalogowania się do strony: ")
        input_key = 'Login'
        sample_load = self.open_json('list_of_readers.json')
        while True:
            if not any(_dict[input_key] == log_name for _dict in sample_load if input_key in _dict):
                print("Wprowadzono niepoprawny login! \n")
                input_value = input("Podaj login ponownie: ")
            else:
                print("Zalogowano!")
                break
        return log_name


    def borrow_book(self):
        login = self.user_login()
        path_of_records = '/Users/karol/PycharmProjects/system_biblioteka_zad4/list_of_records.json'
        file = "list_of_records.json"
        input_value = int(input("Uzytkowniku, podaj ID ksiazki, ktora chcesz wypozyczyc: "))
        sample_load = self.open_json("list_of_books.json")
        input_key = "id"
        input_key_second = 'Borrowed'
        input_value_second = False

        place_in_list = 0
        for index in range(len(sample_load)):
            if sample_load[index]['id'] == input_value:
                break
            place_in_list += 1

        while True:

            if not any(_dict[input_key] == input_value for _dict in sample_load if input_key in _dict):
                print("Nie ma takiego ID w książce\n")
                input_value = int(input("Podaj ID ponownie: "))

            elif sample_load[place_in_list][input_key_second] == input_value_second:
                sample_load[place_in_list][input_key_second] = True
                print(sample_load)

                with open('list_of_books.json', mode='w') as write_file:
                    json.dump(sample_load, write_file)

                print("Możesz wypożyczyć książkę")
                break

            else:
                print("Nie możesz wypożyczyć książki, ponieważ jest ona obecnie niedostępna ")
                break


class Reader:

    path = '/Users/karol/PycharmProjects/system_biblioteka_zad4/list_of_readers.json'

    def __init__(self):
        self.first_name = input("Podaj imie czytelnika: ")
        self.second_name = input("Podaj nazwisko czytelnika: ")
        self.login = input("Podaj login uzytkownika: ")

        input_key = 'Login'
        input_value = self.login

        user_list = [{
            'id': 1,
            'FirstName': self.first_name,
            'LastName': self.second_name,
            "Login": self.login
        }]
        if os.path.isfile(self.path) == False:
            file = "list_of_readers.json"
            with open(file, "w", encoding="utf-8") as infile:
                json_object = json.dumps(user_list, indent=5)
                infile.write(json_object)
        else:
            sample_load = Library().open_json('list_of_readers.json')
            if not any(_dict[input_key] == input_value for _dict in sample_load if input_key in _dict):
                num = len(sample_load) - 1
                id_num = sample_load[num].get('id') + 1
                sample_load.append({
                    'id': id_num,
                    'FirstName': self.first_name,
                    'LastName': self.second_name,
                    'Login': self.login})
                with open('list_of_readers.json', mode='w') as write_file:
                    json.dump(sample_load, write_file)

            print('Zarejestrowano uzytkownika')

    def __str__(self) -> str:
        return f"{self.first_name}, {self.second_name}, {self.login}"


class Librarian:

    def __init__(self):
        self.library_worker = [{'id': 1, "FirstName": "Guido", "LastName": "van Rossum", 'Login': 'Monty'}]
        self.path = '/Users/karol/PycharmProjects/system_biblioteka_zad4/list_of_workers.json'
        self.login = input("Podaj login bibliotekarza: ")
        input_key = 'Login'
        input_value = self.login

        if os.path.isfile(self.path) == False:
            file = "list_of_workers.json"
            with open(file, "w", encoding="utf-8") as infile:
                json_object = json.dumps(self.library_worker, indent=4)
                infile.write(json_object)
        else:
            sample_load = Library().open_json('list_of_workers.json')
            while True:

                if not any(_dict[input_key] == input_value for _dict in sample_load if input_key in _dict):
                    print("Wprowadzono niepoprawny login! \n")
                    input_value = input("Podaj login ponownie: ")
                else:
                    print("Zalogowano!")
                    break


    def add_new_reader(self):
        reader = Reader()

    def show_all_readers(self):
        sample_load = Library().open_json('list_of_readers.json')
        print(json.dumps(sample_load, indent=4))



class Menu:

    def main_menu(self):
        library = Library()
        while True:

            welcome = int(input("System biblioteczny, podaj jako kto chcesz sie zalogowac: \n"
                                "1) Czytelnik\n"
                                "2) Bibliotekarz\n"
                                "3) Wyjscie\n"
                                ">> "))
            if welcome == 1:
                library.user_login()

                while True:

                    reader_menu = int(input("Wybierz opcje dla czytelnika biblioteki: \n"
                                            "1) Zobacz wszystkie ksiazki \n"
                                            "2) Znajdz ksiazke po nazwie autora \n"
                                            "3) Znajdz ksiazke po tytule \n"
                                            "4) Wypożycz książkę \n"
                                            "5) Wyjscie \n"
                                            ">> "))
                    if reader_menu == 1:
                        library.show_all_books()
                        continue
                    if reader_menu == 2:
                        library.find_book_by_author()
                        continue
                    if reader_menu == 3:
                        library.find_book_by_title()
                        continue
                    if reader_menu == 4:
                        library.borrow_book()
                        continue
                    else:
                        break




            elif welcome == 2:
                librarian = Librarian()

                while True:

                    librarian_menu = int(input("Wybierz opcje dla pracownika biblioteki: \n"
                                               "1) Dodaj nowego czytelnika\n"
                                               "2) Dodaj nowa ksiazke\n"
                                               "3) Usun ksiazke\n"
                                               "4) Wyswietl wszystkie ksiazki\n"
                                               "5) Znajdz ksiazke po nazwie autora\n"
                                               "6) Znajdz ksiazke po tytule\n"
                                               "7) Wyjscie\n"
                                               ">> "))
                    if librarian_menu == 1:
                        reader = Reader()
                    elif librarian_menu == 2:
                        library.add_book()
                    elif librarian_menu == 3:
                        library.delete_book()
                    elif librarian_menu == 4:
                        library.show_all_books()
                    elif librarian_menu == 5:
                        library.find_book_by_author()
                    elif librarian_menu == 6:
                        library.find_book_by_title()
                    else:
                        break
            else:
                exit()


if __name__ == '__main__':
    menu = Menu()
    menu.main_menu()
