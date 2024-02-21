import random


class Ecosystem:
    def __init__(self, river_length, num_fish, num_bears):
        # Initialize the river
        self.river = [None] * river_length

        # Populate the river with fish and bears
        # Fish are represented by 'F', bears are represented by 'B', 'N' represents an empty space
        # Todo: randomly place the fish and bears in the river

        # display the initial river
        print(self.display_river())

    def simulate(self, steps):
        for _ in range(steps):
            # Create a copy of the river to update animals' positions
            new_river = self.river.copy()

            # Todo: move the animals in the river

            # Update the river state
            self.river = new_river

            # desplay the river
            print(self.display_river())

    def display_river(self):
        return ''.join(['N' if x is None else x for x in self.river])


if __name__ == '__main__':
    # Test 1
    ecosystem = Ecosystem(river_length=3, num_fish=1, num_bears=1)
    ecosystem.simulate(steps=2)

    # Test 2
    ecosystem = Ecosystem(river_length=10, num_fish=3, num_bears=2)
    ecosystem.simulate(steps=5)

    # Test 3
    ecosystem = Ecosystem(river_length=8, num_fish=2, num_bears=1)
    ecosystem.simulate(steps=10)

    # Test 4
    ecosystem = Ecosystem(river_length=10, num_fish=2, num_bears=3)
    ecosystem.simulate(steps=10)
