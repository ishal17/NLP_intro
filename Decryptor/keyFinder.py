
import random
import heapq

class KeyFinder:

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.identityKey = 'abcdefghijklmnopqrstuwvxyz'

    def findBestKey(self, text, n_parents, n_children, n_generations):
        print('')
        print('using parameters: n_parents =', n_parents, ', n_children =', n_children, ', n_generations =', n_generations)
        print('')
        print('trying to decrypt:')
        print(text)

        currentGeneration = [self._randomDNA() for i in range(n_parents)]
        for i in range(n_generations):
            print('')
            print('-- start of generation #', i, ' --')
            offspring = currentGeneration.copy() # keep current dna's and add children
            for dna in currentGeneration:
                for _ in range(n_children):
                    offspring.append(self._mutate(dna))

            filtered_offspring = [gene for gene in set(list(offspring))]
            # for _ in range(n_parents - len(filtered_offspring)):
            #     filtered_offspring.append(self._randomDNA())
            currentGeneration = self._chooseBestDNA(text, filtered_offspring, n_parents)
            print('')
            print(currentGeneration)
            print('')
            score = self.analyzer.scoreDNA(currentGeneration[0], text)
            print('current best loss is: ', score)

        return self._chooseBestDNA(text, currentGeneration)[0]

    def _chooseBestDNA(self, text, offspring, num = 1):
        h = []
        for dna in offspring:
            heapq.heappush(h, (self.analyzer.scoreDNA(dna, text), dna))

        chosen = heapq.nlargest(num, h)
        return [elem[1] for elem in chosen]

    def _mutate(self, dna):
        i = random.randrange(0, 25, 1)
        j = random.randrange(0, 25, 1)
        l = list(dna)
        l[i], l[j] = l[j], l[i]
        return ''.join(l)

    def _randomDNA(self):
        key = self.identityKey
        l = list(key)
        random.shuffle(l)
        key = ''.join(l)
        return key
        
