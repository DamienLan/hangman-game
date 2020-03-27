"""
Define the word class
"""


def build_occurence(string):
    """
    return a dictionnary wich represent the occurencer of each letter
    :param string:
    :return: dictionnary
    """
    occurence = {}
    for i in range(len(string)):
        try:
            occurence[string[i]].append(i)
        except KeyError:
            occurence[string[i]] = [i]

    return occurence


def build_word_in_process(string):
    word_in_process = '_' * len(string)
    return word_in_process


class Word:
    """
    Word class
    """

    def __init__(self, string):
        """
        init function
        :param string: word chosen
        """

        self.occurence = build_occurence(string)
        self.word_in_process = build_word_in_process(string)
        self.found = False

    def upgrade(self, char):
        """
        Check if the word is found
        :param char: character given by user
        :return: None
        """

        for i in self.occurence[char]:
            self.word_in_process = self.word_in_process[:i] + char + self.word_in_process[i + 1:]

    def display(self):
        """
        Display the word with reveal and not reveal letter
        :return: string
        """

        word_display = self.word_in_process.replace("", " ").center(30)
        return word_display


if __name__ == '__main__':
    word = Word('test')
    print(word.occurence)
    print(word.word_in_process)
    word.upgrade('e')
    print(word.word_in_process)
    print(word.display())
