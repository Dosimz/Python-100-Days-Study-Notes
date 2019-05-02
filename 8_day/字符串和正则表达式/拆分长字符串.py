import re

def main():
    poem = '窗前名月光,意识地上霜. 巨头望明月,低头死故乡.'
    sentence_list = re.split(r'[,.,.]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == "__main__":
    main()