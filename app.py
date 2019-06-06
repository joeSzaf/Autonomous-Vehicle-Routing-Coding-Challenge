# Default size of the grid, given by problem
X_GRID_DIMENSION = 10
Y_GRID_DIMENTION = 10

# create function to generate a grid given an x and y dimension

class Car:
    def __init__(self, x_size, y_size, car_start_location=(0,0) ):
        self.x_size = x_size
        self.y_size = y_size
        self.car_location = car_start_location
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

    def find_nearest_node(self, space):
        shortest_distance = self.x_size + self.y_size
        closest_node = None

        for node in self.drop_off_queue:
            node_distance = abs(space[0] - node["end"][0]) + abs(space[1] - node["end"][1])
            if node_distance < shortest_distance:
                closest_node = node
                shortest_distance = node_distance


        for node in self.pickup_queue:
            node_distance = abs(space[0] - node["start"][0]) + abs(space[1] - node["start"][1])
            if node_distance < shortest_distance:
                closest_node = node
                shortest_distance = node_distance

        # in the event of a tie, it returns the first node in the queue for drop off
        return shortest_distance

    def check_pickup(self):
        new_pickup_list = []
        for passenger in self.pickup_queue:
            if passenger["start"][0] == self.car_location[0] and passenger["start"][1] == self.car_location[1]:
                self.drop_off_queue.append(passenger)
            else:
                new_pickup_list.append(passenger)
        self.pickup_queue = new_pickup_list

    def choose_next_space(self):
        # init shortest_distance to be maximum size possible based on grid size and number of ride requests
        shortest_distance = (self.x_size + self.y_size) * (len(self.pickup_queue) + len(self.drop_off_queue))
        next_locations = []

        if self.car_location[0] > 0:
            space = (self.car_location[0] -1, self.car_location[1])
            distance = self.calculate_total_distances(space)
            if distance is shortest_distance:
                next_locations.append(space)
            elif distance < shortest_distance:
                shortest_distance = distance
                next_locations = [space]

        if self.car_location[0] < self.x_size - 1:
            space = (self.car_location[0] +1, self.car_location[1])
            distance = self.calculate_total_distances(space)
            if distance is shortest_distance:
                next_locations.append(space)
            elif distance < shortest_distance:
                shortest_distance = distance
                next_locations = [space]

        if self.car_location[1] > 0:
            space = (self.car_location[0], self.car_location[1] -1)
            distance = self.calculate_total_distances(space)
            if distance is shortest_distance:
                next_locations.append(space)
            elif distance < shortest_distance:
                shortest_distance = distance
                next_locations = [space]

        if self.car_location[1] < self.y_size - 1:
            space = (self.car_location[0], self.car_location[1] +1)
            distance = self.calculate_total_distances(space)
            if distance is shortest_distance:
                next_locations.append(space)
            elif distance < shortest_distance:
                shortest_distance = distance
                next_locations = [space]

        if len(next_locations) is 1:
            return next_locations[0]
        else:
            closest_node_distance = self.x_size + self.y_size
            next_space = None

            for location in next_locations:
                distance = self.find_nearest_node(location)
                if distance < closest_node_distance:
                    closest_node_distance = distance
                    next_space = location

            return next_space





car = Car(X_GRID_DIMENSION, Y_GRID_DIMENTION)

car.drop_off_queue = [
    {
        "name": "Elon",
        "start": [3,5],
        "end": [8,7]
    },
    {
        "name": "George",
        "start": [1,2],
        "end": [4,3]
    }
]

car.pickup_queue = [
    {
        "name": "Nancy",
        "start": [9,9],
        "end": [1,3]
    }
]


print(car.pickup_queue)
car.check_pickup()
print(car.pickup_queue)
print(car.drop_off_queue)
