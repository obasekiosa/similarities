from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    set_a = set(a.split('\n'))
    set_b = set(b.split('\n'))

    out = list(set_a.intersection(set_b))
    return out


def sentences(a, b):
    """Return sentences in both a and b"""

    set_a = set(sent_tokenize(a, language='english'))
    set_b = set(sent_tokenize(b, language='english'))


    out = list(set_a.intersection(set_b))
    return out


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    len_a = len(a)
    len_b = len(b)
    set_a = set([a[i:i+n] for i in range(len_a - n + 1)])
    set_b = set([b[i:i+n] for i in range(len_b - n + 1)])

    out = list(set_a.intersection(set_b))

    return out
