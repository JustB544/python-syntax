def print_upper_words(words, must_start_with=[]):
    """Given list of words return them as uppercase, and optionally exclude words that don't start with a certain letter.

    words: list of words
    must_start_with: list of letters word must start with
    """
    val = True
    for x in words:
        if (len(must_start_with) != 0):
            val = False
            for y in must_start_with:
                if (x[0] == y):
                    val = True
            #print(val)
            if (val == False):
                continue
        print(x.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
