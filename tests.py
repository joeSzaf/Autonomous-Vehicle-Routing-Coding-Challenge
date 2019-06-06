import unittest

from app import *

class myTest(unittest.TestCase):
    def test_handle_pickup_requests(self):
        car = Car(10,10)
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

        self.assertEqual( len(car.pickup_queue), 0 )

        car.handle_pickup_requests(requests_time_0)

        self.assertEqual( len(car.pickup_queue), 2 )
        self.assertEqual( car.pickup_queue[0]["name"], "Elon" )
        self.assertEqual( car.pickup_queue[-1]["end"], [4,3] )

        car.handle_pickup_requests(requests_time_1)
        self.assertEqual( len(car.pickup_queue), 2 )

        car.handle_pickup_requests(requests_time_2)
        self.assertEqual( len(car.pickup_queue), 3 )
        self.assertEqual( car.pickup_queue[-1]["name"], "Nancy" )

    def test_calculate_total_distances(self):
        car = Car(10,10)
        car.pickup_queue = [
    		{
            	"name": "Nancy",
                "start": [9,9],
                "end": [1,3]
            }
    	]
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

        self.assertEqual( car.calculate_total_distances((0,0)), 40)
        self.assertEqual( car.calculate_total_distances((3,5)), 20)

    def test_choose_next_space(self):
        car = Car(10, 10)
        car.pickup_queue = [
    		{
            	"name": "Nancy",
                "start": [9,9],
                "end": [1,3]
            }
    	]
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

    def test_check_pickup(self):
        car1 = Car(10, 10, (8,9))
        car1.pickup_queue = [
    		{
            	"name": "Nancy",
                "start": [9,9],
                "end": [1,3]
            }
    	]
        car1.drop_off_queue = [
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

        car1.check_pickup()
        self.assertEqual( len(car1.pickup_queue), 1)
        self.assertEqual( len(car1.drop_off_queue), 2)

        car2 = Car(10, 10, (9,9))
        car2.pickup_queue = [
    		{
            	"name": "Nancy",
                "start": [9,9],
                "end": [1,3]
            }
    	]
        car2.drop_off_queue = [
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

        car2.check_pickup()
        self.assertEqual( len(car2.pickup_queue), 0)
        self.assertEqual( len(car2.drop_off_queue), 3)

    def test_check_drop_off(self):
        car = Car(10, 10, (8,6))
        car.pickup_queue = [
    		{
            	"name": "Nancy",
                "start": [9,9],
                "end": [1,3]
            }
    	]
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

        car.check_drop_off()
        self.assertEqual( len(car.drop_off_queue), 2)
        self.assertEqual( len(car.dropped_off_passengers), 0)

        car.car_location = (8,7)
        car.check_drop_off()
        self.assertEqual( len(car.drop_off_queue), 1)
        self.assertEqual( len(car.dropped_off_passengers), 1)
        self.assertEqual( car.dropped_off_passengers[0]["name"], "Elon")





unittest.main()
