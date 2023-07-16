from uzwords import words
from difflib import get_close_matches

def checkWords(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    availble = False

    if word in matches:
        availble = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ','x')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х','ҳ')
        matches.update(get_close_matches(word, words))
    elif 'қ' in word:
        word = word.replace('қ','к')
        matches.update(get_close_matches(word, words))
    elif 'к' in word:
        word = word.replace('к','қ')
        matches.update(get_close_matches(word, words))
    elif 'ц' in word:
        word = word.replace('ц','с')
        matches.update(get_close_matches(word, words))
    elif 'с' in word:
        word = word.replace('с','ц')
        matches.update(get_close_matches(word, words))

    return {'available': availble, 'matches': matches}

if __name__ == '__main__':
        print(checkWords('сирк'))
        print(checkWords('тарих'))
        print(checkWords('цирк'))
        print(checkWords('гайрат'))