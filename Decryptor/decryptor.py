
import random
import textAnalyzer
import experiment


def ask4instructions():    
    # let text analyzer prepare probabilities
    analyzer = textAnalyzer.TextAnalyzer()
    print('enter file name for analyzer:')
    filename = input()
    f = open(filename, 'r')
    analyzer.analyze(f)
    f.close()
    # testAnalyzer(analyzer) # test that analyzer works without any errors

    exp = experiment.Experiment(analyzer)

    while True:
        print('')
        print('1 - decrypt text')
        print('q - quit')
        print('')
        print('your input:')
        inp  = input()
        if inp == 'q':
            break
        elif inp == '1':
            print('')
            print('enter text you want to decrypt:')
            text  = input()
            exp.launch(text)
        else:
            print('invalid input')
            print(' ')


if __name__ == '__main__':
    ask4instructions()