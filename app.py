# Default size of the grid, given by problem
X_GRID_DIMENSION = 10
Y_GRID_DIMENTION = 10

# create function to generate a grid given an x and y dimension

class Car:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.car_location = (4,7)
        self.total_ticks = 0
        self.pickup_queue = []
        self.drop_off_queue = []

    def handle_pickup_requests(self, requests):
        for request in requests:
            self.pickup_queue.append(request)

    def calculate_total_distances(self, space):
        total_blocks = 0

        for destination in self.drop_off_queue:
            total_blocks += abs(space[0] - destination["end"][0])
            total_blocks += abs(space[1] - destination["end"][1])

        for location in self.pickup_queue:
            total_blocks += abs(space[0] - location["start"][0])
            total_blocks += abs(space[1] - location["start"][1])

        return total_blocks

'''
    def choose_next_space(self):
        # init shortest_distance to be maximum size possible based on grid size and number of ride requests
        shortest_distance = (self.x_size + self.y_size) * (len(self.pickup_queue) + len(self.drop_off_queue))
        best_location = None

        if self.car_location[0] > 0:
            distance = self.calculate_total_distances((self.car_location[0] -1, self.car_location[1]))
            if distance < shortest_distance:
                shortest_distance = distance
                best_location = (self.car_location[0] -1, self.car_location[1])

        if self.car_location[0] < self.x_size - 1:
            distance = self.calculate_total_distances((self.car_location[0] +1, self.car_location[1]))
            if distance < shortest_distance:
                shortest_distance = distance
                best_location = (self.car_location[0] +1, self.car_location[1])

        if self.car_location[1] > 0:
            distance = self.calculate_total_distances((self.car_location[0], self.car_location[1] -1))
            if distance < shortest_distance:
                shortest_distance = distance
                best_location = (self.car_location[0], self.car_location[1] -1)

        if self.car_location[1] < self.y_size - 1:
            distance = self.calculate_total_distances((self.car_location[0], self.car_location[1] +1))
            if distance < shortest_distance:
                shortest_distance = distance
                best_location = (self.car_location[0], self.car_location[1] +1)

        return best_location
'''

car = Car(X_GRID_DIMENSION, Y_GRID_DIMENTION)

car.handle_pickup_requests([1,2])
