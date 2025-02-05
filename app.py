class Car:
    def __init__(self, x_size, y_size, car_start_location=(0,0) ):
        self.x_size = x_size
        self.y_size = y_size
        self.car_location = car_start_location
        self.total_ticks = 0
        self.pickup_queue = []
        self.drop_off_queue = []
        self.dropped_off_passengers = []

    def handle_pickup_requests(self, requests):
        for request in requests:
            self.pickup_queue.append(request)
            print('-> %s has been added to the pickup queue.'%(request["name"]))

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
                print(' + %s has been picked up.'%(passenger["name"]))
            else:
                new_pickup_list.append(passenger)
        self.pickup_queue = new_pickup_list

    def check_drop_off(self):
        new_drop_off_list = []
        for passenger in self.drop_off_queue:
            if passenger["end"][0] == self.car_location[0] and passenger["end"][1] == self.car_location[1]:
                self.dropped_off_passengers.append(passenger)
                print(' - %s has been dropped off.'%(passenger["name"]))
            else:
                new_drop_off_list.append(passenger)
        self.drop_off_queue = new_drop_off_list

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
            next_space = next_locations[0]

            for location in next_locations:
                distance = self.find_nearest_node(location)
                if distance < closest_node_distance:
                    closest_node_distance = distance
                    next_space = location

            return next_space

    def print_board(self):
        # create joining row
        join_row = []
        for col in range(self.x_size):
            join_row.append(" | ")
        join_row_string = "\n" + " ".join(join_row)+"\n"

        # create base grid
        grid = []
        for row in range(self.y_size):
            current_row = []
            for space in range(self.x_size):
                current_row.append("[ ]")
            grid.append(current_row[:])

        # add car location
        grid[self.car_location[1]][self.car_location[0]] = "[C]"

        # add pickup locations
        for passenger in self.pickup_queue:
            grid[passenger["start"][1]][passenger["start"][0]] = "[P]"

        # add drop off locations
        for passenger in self.drop_off_queue:
            grid[passenger["end"][1]][passenger["end"][0]] = "[D]"

        grid_string =[]
        for row in grid:
            grid_string.append("-".join(row))

        print(join_row_string.join(grid_string))

    def tick(self, requests):
        self.total_ticks += 1

        self.car_location = self.choose_next_space()


        print('The car is currently at: (%s, %s)'%(self.car_location[0],self.car_location[1]))
        print("-----------------")

        self.handle_pickup_requests(requests)
        self.check_pickup()
        self.check_drop_off()
        print("-----------------")

        print('Current passengers:')
        for passenger in self.drop_off_queue:
            print("  <> %s"%(passenger["name"]))
        print('')

        self.print_board()
        print('')

    def run(self, request_list):
        for requests in request_list:
            print("Current time: %s tick(s)"%(self.total_ticks))
            self.tick(requests)
