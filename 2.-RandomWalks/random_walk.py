from walker import NormalWalker
from system import System
from coordinate import Coordinate
from bokeh.plotting import figure, show


def walking(system, walker, distance):
    start = system.get_coordinate(walker)

    for _ in range(distance):
        system.move_walker(walker)

    return start.distance(system.get_coordinate(walker))


def simulate_walk(distance, n_iterations, walker_class):
    '''
    Walk simulation

    ## Params:
    - distance, int:

        Number of steps

    - n_iterations, int:

        Number of simulations

    - walker_class, Walker:

        walker class that will be used for simulation

    ## Returns
        List of distances to origin for each walk simulation
    '''
    walker = walker_class()
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(n_iterations):
        system = System()
        system.add_walker(walker, origin)
        walk_simulation = walking(system, walker, distance)

        distances.append(round(walk_simulation, 1))

    return distances


def graph(x, y):
    '''
    Graphs, using Bokeh, a line graph

    Params:
    - x, list:

        x coordinates

    - y, list:

        y coordinates
    '''
    actual_graph = figure(title='Random walk', x_axis_label='Steps', y_axis_label='Distance')
    actual_graph.line(x, y, legend_label='Mean distance')

    show(actual_graph)


def main(walks_distances, n_iterations, walker_class):
    walks_distances = sorted(walks_distances)
    mean_distances_per_walk = []

    for distance in walks_distances:
        simulated_distances = simulate_walk(distance, n_iterations, walker_class)

        mean_distance = round(sum(simulated_distances) / len(simulated_distances), 4)
        max_distance = max(simulated_distances)
        min_distance = min(simulated_distances)

        mean_distances_per_walk.append(mean_distance)

        print(f'{walker_class.__name__} walked a distance of {distance}')
        print(f'- Mean: {mean_distance}')
        print(f'- Max distance: {max_distance}')
        print(f'- Min distance: {min_distance}')

    graph(walks_distances, mean_distances_per_walk)


if __name__ == "__main__":
    distances = list(range(1, 1502, 50))
    n_tries = 150

    main(distances, n_tries, NormalWalker)
