# Default size of the grid, given by problem
X_GRID_DIMENSION = 10
Y_GRID_DIMENTION = 10

# create function to generate a grid given an x and y dimension

class Car:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.car_location = (0,0)
        self.total_ticks = 0
        self.pickup_queue = []
        self.drop_off_queue = []

    def handle_pickup_requests(self, requests):
        for request in requests:
            self.pickup_queue.append(request)

    def choose_next_space(self):
        if self.car_location[0] > 0:
            #check left space


car = Car(X_GRID_DIMENSION, Y_GRID_DIMENTION)

car.handle_pickup_requests([1,2])
print(car.pickup_queue)
