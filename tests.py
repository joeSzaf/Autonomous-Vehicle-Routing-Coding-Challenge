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


unittest.main()
