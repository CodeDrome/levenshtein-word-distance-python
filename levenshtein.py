import math

# ANSI terminal codes for colours
BLUE = "\x1B[94m"
RESET = "\x1B[0m"

class Levenshtein(object):
    """
    Implements the Levenshtein Word Distance Algorithm for calculating
    the minimum number of changes needed to transform one word into another.
    """

    def __init__(self):
        """
        Just creates costs, and other attributes with default values.
        """

        self.insert_cost = 1
        self.delete_cost = 1
        self.substitute_cost = 1

        self.grid = []

        self.source_word = ""
        self.target_word = ""

        self.minimum_cost = -1

    def calculate(self):
        """
        Creates a grid for the given words and iterates rows and columns,
        calculating missing values.
        """

        self.__init_grid()

        for sourceletter in range(0, len(self.source_word)):

            for targetletter in range(0, len(self.target_word)):

                if self.target_word[targetletter] != self.source_word[sourceletter]:
                    total_substitution_cost = self.grid[sourceletter][targetletter] + self.substitute_cost
                else:
                    total_substitution_cost = self.grid[sourceletter][targetletter]

                total_deletion_cost = self.grid[sourceletter][targetletter+1] + self.delete_cost

                total_insertion_cost = self.grid[sourceletter+1][targetletter] + self.insert_cost

                self.grid[sourceletter+1][targetletter+1] = min(total_substitution_cost, total_deletion_cost, total_insertion_cost)

        self.minimum_cost = self.grid[len(self.source_word)][len(self.target_word)]

    def print_grid(self):
        """
        Prints the target and source words and all transformation costs in a grid
        """

        print("        ", end="")

        for t in self.target_word:

            print(BLUE + "%5c" % t + RESET, end="")

        print("\n")

        for row in range(0, len(self.grid)):

            if row > 0:
                print(BLUE + "%3c" % self.source_word[row - 1] + RESET, end="")
            else:
                print("   ", end="")

            for column in range(0, len(self.grid[row])):

                print("%5d" % self.grid[row][column], end="")

            print("\n")

    def print_cost(self):
        """
        This is a separate function to allow printing just the cost if you are not
        interested in seeing the grid
        """

        if self.minimum_cost >= 0:
            print("Minimum cost of transforming \"%s\" to \"%s\" = %d" % (self.source_word, self.target_word, self.minimum_cost))
        else:
            print("Costs not yet calculated")

    def __init_grid(self):
        """
        Sets values of first row and first column to 1, 2, 3 etc.
        Other values initialized to 0
        """

        del self.grid[:]

        # Don't forget we need one more row than the letter count of the source
        # and one more column than the target word letter count
        for row in range(0, (len(self.source_word) + 1)):

            self.grid.append([0] * (len(self.target_word) + 1))

            self.grid[row][0] = row

            if row == 0:

                for column in range(0, (len(self.target_word) + 1)):

                    self.grid[row][column] = column

        self.minimum_cost = -1
