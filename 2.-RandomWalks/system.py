class System:
    def __init__(self):
        self.coordinates = {}

    def add_walker(self, walker, coordinate):
        self.coordinates[walker] = coordinate

    def move_walker(self, walker):
        delta_x, delta_y = walker.walk()
        actual_coordinate = self.coordinates[walker]
        new_coordinate = actual_coordinate.move(delta_x, delta_y)

        self.coordinates[walker] = new_coordinate

    def get_coordinate(self, walker):
        return self.coordinates[walker]
