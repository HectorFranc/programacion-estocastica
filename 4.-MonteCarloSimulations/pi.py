import random
import math
from statistics import mean, stdev


def generate_random_point():
    return [random.random() * 2 - 1 for _ in range(2)]


def pi_calc(launches=10000):
    '''
    Pi value using Basilea problem solution
    '''
    in_circle = 0
    for _ in range(launches):
        point = generate_random_point()
        distance_to_origin = math.sqrt(point[0] ** 2 + point[1] ** 2)
        if distance_to_origin <= 1:
            in_circle += 1

    return 4 * in_circle / launches


def pi_and_statistics(sigma=0.01, initial_launches=100, incremental_launches_factor=2, max_iterations=100):
    launches = initial_launches
    pi_values = [pi_calc(launches), pi_calc(launches)]
    actual_iteration = 2

    while stdev(pi_values) > sigma:
        if actual_iteration >= max_iterations:
            break
        launches = int(incremental_launches_factor * launches)
        pi_values.append(pi_calc(launches))
        actual_iteration += 1

        print(f'Iter = {actual_iteration}:')
        print(f'\tMean = {str(mean(pi_values))}')
        print(f'\tStdev = {stdev(pi_values)}')

    return (mean(pi_values), stdev(pi_values))


if __name__ == "__main__":
    sigma = float(input('Max sigma\n>> '))

    final_pi_value, final_pi_stdev = pi_and_statistics(sigma, 1000, 1.5, 1000)
    print(f'\n\nFinal PI value: {final_pi_value}')
    print(f'Stdev = {final_pi_stdev}')
