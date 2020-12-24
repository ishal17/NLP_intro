
import keyFinder

class Experiment:

    def __init__(self, analyzer):
        self.finder = keyFinder.KeyFinder(analyzer)
        self._setDefaultHyperarameters()        

    def launch(self, text):
        while True:
            print('')
            print('1 - enter hyperparameters')
            print('2 - use default hyperparameters')
            print('q - quit')
            print('')
            print('your input:')
            inp  = input()
            if inp == 'q':
                break
            elif inp == '1':
                self._updateHyperparameters()
                self._findKey(text)
            elif inp == '2':
                print('')
                print('using default hyperparameters')
                self._setDefaultHyperarameters()
                self._findKey(text)
            else:
                print('invalid input')
                print(' ')


    def _updateHyperparameters(self):
        print('')
        print('size of initial generation:')
        self.n_parents  = int(input())
        print('')
        print('number of children:')
        self.n_children  = int(input())
        print('')
        print('number of generations:')
        self.n_generations  = int(input())

    def _setDefaultHyperarameters(self):        
        self.n_parents = 20
        self.n_children = 5
        self.n_generations = 200

    def _findKey(self, text):        
        key = self.finder.findBestKey(text, self.n_parents, self.n_children, self.n_generations)
        self._decryptText(text, key)

    def _recoverEncryptionKey(self, key):
        guess = '?' * 26
        l = list(guess)
        for c in key:
            c1 = key[ord(c) - ord('a')]
            l[ord(c1) - ord('a')] = c
        return ''.join(l)

    def _decryptText(self, text, key):
        print('')
        print('found decriprion key:')
        print(key)
        print('')
        print('possible encryption key:')
        print(self._recoverEncryptionKey(key))

        output = ''
        for c in text:
            if c.isalpha():
                c = c.lower()
                output += key[ord(c) - ord('a')]
            else:
                output += c
        print('')
        print('decrypted text is:')
        print(output)
        print('')
        print('you can try decripting the same text with different hyperparameters')
