from typing import List


def count_words(sentences: List[str], word: str) -> int:
    """
        Take a list of strings and return the list of their hashes

        Parameters
        ----------
        sentences: List[str]
            List of some random strings, which contain or don't contain
            parameter word
        word: str
            Word which entries to sentences we need to count.

        Returns
        ---------
        int
            Number of "word" entries to "sentences" .

        Examples
        --------
        sentences_test = ['test string',
        'with two test words: test and test',
        'and some without ** string'
        ]
        count_words(sentences_test, 'test')
        4
        """
    from functools import reduce
    if sentences:
        return reduce(
            lambda num1, num2: num1 + num2,
            map(lambda string: string.count(word), sentences)
        )
    return 0
