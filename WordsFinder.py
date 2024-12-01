import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = line.lower()
                        line = line.translate(str.maketrans('', '', string.punctuation))
                        words.extend(line.split())
                all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1  # Нумерация с 1

        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}

        # Перебираем все файлы и считаем вхождения слова
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())

        return result


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())

print(finder2.find('TEXT'))

print(finder2.count('teXT'))
