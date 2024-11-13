f = "Walt Whitman - O Captain! My Captain!.txt"


class WordsFinder:
    def __init__(self, *file_names ):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        if isinstance(self.file_names, str):
            with open(self.file_names, encoding='utf-8') as file:
                mini_word = file.read().lower()
                sim = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for y in sim:
                    word_new = mini_word.replace(y, '')
                with open(self.file_names, 'w', encoding='utf-8') as file_w:
                    word_end = file_w.write(word_new)
                all_words[self.file_names] = word_end
            return all_words

        elif isinstance(self.file_names, tuple):
            for i in self.file_names:
                with open(i, "r", encoding='utf-8') as file:
                    mini_word = file.read().lower()
                    sim = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for y in sim:
                        mini_word = mini_word.replace(y, '')
                    word_new = mini_word
                with open(i, 'w', encoding='utf-8') as file_w:
                    file_w.write(word_new)
                with open(i, encoding='utf-8') as file:
                    word_end = file.read().split()
                all_words[i] = word_end
            return all_words

    def find(self, word):
        num = 0
        res = {}

        for k, v in self.get_all_words().items():
            for i in v:
                num += 1
                if i == word.lower():
                    res[k] = num
                    return res

    def count(self, word):
        count_num = 0
        result = {}

        for k, v in self.get_all_words().items():
            for i in v:
                if i == word.lower():
                    count_num += 1
                    result[k] = count_num
        return result


fin = WordsFinder("Walt Whitman - O Captain! My Captain!.txt")
print(fin.get_all_words()) # Все слова
print(fin.find('you')) # 85 слово по счёту
print(fin.count('yOu')) # 5 слова you в тексте всего