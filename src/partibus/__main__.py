"""
main() function of the module.
"""

import argparse

from partibus.lemmatize import lemmatize


def main():
    """
    Main function.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='+', type=str,
                        help='word or list of words to lemmatize')
    args = parser.parse_args()
    print(lemmatize(' '.join(args.words)))


if __name__ == "__main__":
    main()
