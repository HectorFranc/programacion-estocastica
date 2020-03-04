import random
import collections

SUITS = ['spade', 'diamond', 'club', 'heart']
VALUES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


def create_deck():
    deck = []
    for suite in SUITS:
        for value in VALUES:
            deck.append((suite, value))
    return deck


def get_stack_of_cards(deck, stack_size):
    stack_size = min(stack_size, len(deck))  # Population <= stack_size

    stack = random.sample(deck, stack_size)
    return stack


def main(stack_size, n_iterations):
    deck = create_deck()
    stacks = []

    for _ in range(n_iterations):
        stack = get_stack_of_cards(deck, stack_size)
        stacks.append(stack)

    pairs = 0
    for stack in stacks:
        values = [card[1] for card in stack]

        counter = dict(collections.Counter(values))
        if 2 in counter.values():
            pairs += 1
    prob_of_get_a_pair = pairs / n_iterations
    print(f'Probability of get a pair in a stack of {stack_size} cards: {prob_of_get_a_pair * 100}%')


if __name__ == "__main__":
    stack_size = int(input('Stack size:\n>> '))
    n_iterations = int(input('Number of iterations:\n>> '))

    main(stack_size, n_iterations)
