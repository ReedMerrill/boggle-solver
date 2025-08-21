import pytest

import pprint

import trie_gen


def test_filter_lexicon():

    input = ["a", "aa", "aaa", "aaaa", "aaaaaaaaaaaaaaaaaa"]

    result = trie_gen.filter_lexicon(input)

    assert result == ["aaa", "aaaa"]


def test_make_trie():

    input = ["squirm", "ant", "arms", "elegant", "elephant"]

    result = trie_gen.make_trie(input)

    pprint.pp(result)

    correct = {
        "s": {"q": {"u": {"i": {"r": {"m": {"_end_": "_end_"}}}}}},
        "a": {"n": {"t": {"_end_": "_end_"}}, "r": {"m": {"s": {"_end_": "_end_"}}}},
        "e": {
            "l": {
                "e": {
                    "g": {"a": {"n": {"t": {"_end_": "_end_"}}}},
                    "p": {"h": {"a": {"n": {"t": {"_end_": "_end_"}}}}},
                },
            }
        },
    }

    assert result == correct
