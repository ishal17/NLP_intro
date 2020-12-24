
import math

class TextAnalyzer:

    def __init__(self):
        self.statA = {}
        self.statAGivenB = {} 
        self.words_cnt = -1  
        self.pairsStartingWith = {} 

        alphabet = 'abcdefghijklmnopqrstuwvxyz'
        for c in alphabet:
            self.statA[c] = 1
            for d in alphabet:
                pair = c + d
                self.statAGivenB[pair] = 1

    def analyze(self, f):
        starter = True
        prev = ' '
        while True:
            c = f.read(1)
            if not c:
                break
            if c.isalpha():
                # manually get rid of unusual charachters
                if c in ('æ','é','è','œ'):
                    c = 'e' 
                if c in ('â', 'à'):
                    c = 'a'
                    
                c = c.lower()
                if starter:
                    self.statA[c] += 1
                    starter = False
                else:
                    pair = prev + c
                    self.statAGivenB[pair] += 1
            else:
                starter = True
            prev = c
                

    def _getProbA(self, a):
        return self.statA[a] / self._countWords()

    def _getProbAGivenB(self, a, b):
        pair = b + a
        return self.statAGivenB[pair] / self._countPairsStartingWith(b)

    def scoreDNA(self, dna, text):
        score = 0
        starter = True
        prev = ' '
        for c in text:
            if c.isalpha():
                c = c.lower()
                d = dna[ord(c) - ord('a')]
                if starter:
                    score += math.log(self._getProbA(d))
                    starter = False
                else:
                    score += math.log(self._getProbAGivenB(d, prev))
                prev = d
            else:
                starter = True
                prev = c
        
        return score


    def _countWords(self):
        if self.words_cnt < 0:
            cnt = 0
            for key in self.statA.keys():
                cnt += self.statA[key]
            self.words_cnt = cnt
        return self.words_cnt

    def _countPairsStartingWith(self, b):
        if b not in self.pairsStartingWith:
            cnt = 0
            for key in self.statAGivenB.keys():
                if key[0] == b:
                    cnt += self.statAGivenB[key]
            self.pairsStartingWith[b] = cnt
        return self.pairsStartingWith[b]

