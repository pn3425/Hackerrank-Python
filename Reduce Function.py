def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs))# complete this line with a reduce statement
    return t.numerator, t.denominator
