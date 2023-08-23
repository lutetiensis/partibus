"""
Lemmatizer module
"""


def lemmatize(string):
    """
    Lemmatize words in a string.
    """
    res = []
    for word in string.split():
        print(word)
        res.append({})
    return res
