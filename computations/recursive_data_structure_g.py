import argparse


def main(n):

    # constructor cases
    if n == 0 or n == 1:
        return

    # induction hypothesis
    assert 5*(3**(n-1) - 2**(n-1)) - 6*(3**(n-2) - 2**(n-2)) == 3**n - 2**n

    # quotient rule
    assert 5*(3**(n-1)) == 5*(3**n / 3)
    assert 5*(-2**(n-1)) == 5*(-2**n / 2)
    assert -6*(3**(n-2)) == -6*(3**n / 3**2)
    assert -6*(-2**(n-2)) == -6*(-2**n / 2**2)
    assert 5*(3**n / 3) - 5*(2**n / 2) - 6*(3**n / 3**2) - 6*(-2**n / 2**2) == 3**n - 2**n

    # multiply up to common factor
    assert (12*5*3**n) / 36 - (18*5*2**n) / 36 - (4*6*3**n) / 36 - (9*6*-2**n) / 36 == 3**n - 2**n

    # remove double negative
    assert (12*5*3**n) / 36 - (18*5*2**n) / 36 - (4*6*3**n) / 36 + (9*6*2**n) / 36 == 3**n - 2**n

    # simplify
    assert (60*3**n - 90*2**n - 24*3**n + 54*2**n) / 36 == 3**n - 2**n
    assert (36*3**n - 36*2**n) / 36 == 3**n - 2**n

    print('QED')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, nargs='+')
    args = parser.parse_args()

    for n_ in args.n:
        main(n_)
