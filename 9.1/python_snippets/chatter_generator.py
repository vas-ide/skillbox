import zipfile
from pprint import pprint
from random import randint

class Chatter:
    analize_count = 5

    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.stat = {}

    def unzip(self):
        zip_file = zipfile.ZipFile(self.zip_file_name, 'r')
        for filename in zip_file.namelist():
            zip_file.extract(filename)
        return filename

    def collect(self, file_name):
        sequence = ' ' * self.analize_count
        with open(file_name, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line[:-1]
                for char in line:
                    if sequence in self.stat:
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char

    def preparation(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
            self.stat_for_generate[sequence].sort(reverse=True)


    def chatter(self, N):
        N = 1000
        printed = 0

        sequence = ' ' * self.analize_count
        spaces_printed = 0
        while printed < N:
            char_stat = self.stat_for_generate[sequence]
            total = self.totals[sequence]
            dice = randint(1, total)
            pos = 0
            for count, char in char_stat:
                pos += count
                if dice <= pos:
                    break
            print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char



chatterer = Chatter(zip_file_name='1984-txt.zip')
file_name = chatterer.unzip()
chatterer.collect(file_name)
chatterer.preparation()
chatterer.chatter(N=10000)






































