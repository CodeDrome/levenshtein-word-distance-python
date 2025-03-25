import levenshtein


def main():

    print("-----------------------------")
    print("| codedrome.com             |")
    print("| Levenshtein Word Distance |")
    print("-----------------------------\n")

    source_words = ["banama", "banama", "levinstein"]
    target_words = ["banana", "elephant", "levenshtein"]

    lp = levenshtein.Levenshtein()

    for i in range(0, len(source_words)):

        lp.source_word = source_words[i]
        lp.target_word = target_words[i]

        lp.calculate()

        lp.print_grid()
        lp.print_cost()

        print("")


if __name__ == "__main__":

    main()
