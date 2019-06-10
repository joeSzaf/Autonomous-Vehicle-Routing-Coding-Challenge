from app import *

# Default size of the grid, given by problem
X_GRID_DIMENSION = 10
Y_GRID_DIMENTION = 10

# create different requests
requests_time_0 = [
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

requests_time_1 = []

requests_time_2 = [
    {
                "name": "Nancy",
                    "start": [9,9],
                    "end": [1,3]
            }
]

requests_time_3 = []
requests_time_4 = []
requests_time_5 = []
requests_time_6 = []
requests_time_7 = [
    {
                "name": "Bridget",
                    "start": [3,7],
                    "end": [8,2]
            }
]
requests_time_8 = []
requests_time_9 = []
requests_time_10 = []
requests_time_11 = []
requests_time_12 = []
requests_time_13 = []
requests_time_14 = []
requests_time_15 = []
requests_time_16 = []
requests_time_17 = []
requests_time_18 = []
requests_time_19 = []
requests_time_20 = []

# intialize self driving car. beep beep boop.
car = Car(X_GRID_DIMENSION, Y_GRID_DIMENTION, (0,0))

# create queue of JSON requests
requests = [requests_time_0, requests_time_1, requests_time_2,
    requests_time_3,
    requests_time_4,
    requests_time_5,
    requests_time_6,
    requests_time_7,
    requests_time_8,
    requests_time_9,
    requests_time_10,
    requests_time_11,
    requests_time_12,
    requests_time_13,
    requests_time_14,
    requests_time_15,
    requests_time_16,
    requests_time_17,
    requests_time_18,
    requests_time_19,
    requests_time_20
]

car.run(requests)
# let the car drive itself
