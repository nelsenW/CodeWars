import numpy
def greek_comparator(lhs, rhs):
    # the tuple greek_alphabet is defined in the global namespace
    return numpy.sign(greek_alphabet.index(lhs) - greek_alphabet.index(rhs))