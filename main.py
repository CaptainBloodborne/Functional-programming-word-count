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
        names = ['Alexey', 'Ivan', 'Petr']
        hash_names(names)
        [-6913778901462750956, 4044914442677255742, -8154646851311137882]
        """
    from functools import reduce

    return sum(string.count(word) for string in sentences)
