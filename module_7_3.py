import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                words_list = content.split()
                all_words[file_name] = words_list
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                positions[file_name] = words.index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)
        return counts


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


