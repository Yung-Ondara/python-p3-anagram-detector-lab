# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        matches = []
        for candidate in words:
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        return matches
