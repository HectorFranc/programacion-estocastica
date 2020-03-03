import random


def launch_dice(n_launches):
    launch_sequence = []

    for _ in range(n_launches):
        lauch = random.randint(1, 6)
        launch_sequence.append(lauch)

    return launch_sequence


def main():
    n_tries = int(input('Times simulation will run:\n>> '))
    n_launches = int(input('Number of coin launches:\n>> '))

    lauches = []
    for _ in range(n_tries):
        launch_sequence = launch_dice(n_launches)
        lauches.append(launch_sequence)

    launches_with_1 = 0
    for launch in lauches:
        if 1 in launch:
            launches_with_1 += 1
    prob_launches_with_1 = launches_with_1 / n_tries
    print(f'Probality of get at least a 1 in {n_launches} launches = {prob_launches_with_1 * 100}%')


if __name__ == '__main__':
    main()
