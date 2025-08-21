import sys
import json

_end_ = "_end_"


def filter_lexicon(words: list) -> list:
    out = []
    for word in words:
        length = len(word)
        if (length >= 3) and (length <= 8):
            out.append(word)
    return out


def make_trie(words: list) -> dict:
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end_] = _end_
    return root


def main():

    # lexicon file user input
    input_path = input("lexicon (input) path:" or "en.txt")
    output_path = input("output path:" or ".")

    # Open the file in read mode
    with open(input_path, "r") as file:
        lexicon = []
        for line in file:
            line = line.strip()
            lexicon.append(line)

    words = filter_lexicon(lexicon)

    trie = make_trie(words)

    sys.setrecursionlimit(999_999_999)

    with open(output_path, "w") as outfile:
        json.dump(trie, outfile)


if __name__ == "__main__":
    main()
