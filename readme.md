# Autonomous Driving Car

## Table of Contents
1. About
2. How to Run
3. The Challenge
4. The Methodology
5. The Next Steps

## 1. About
This project the solution to a coding challenge posed by a self driving car firm. They asked this problem to be written in c++ pr Python. Please see "The Challenge" section to see the original challenge. Please see the "Methodology" section to take a look at my methodology for this problem.

## 2. How to Run
### Running the sample data
1. Clone this repo.
2. Make sure you have the latest version of Python install on your computer.
3. Make "Autonomous-Vehicle-Route-Coding-Challenge" your current directory.
4. In the terminal run `python runme.py`. This is execute the program with the standard test case data. The output at each time interval is displayed in the terminal.

At each time interval, the car's current location, any actions (drop off, pickup, or queue add), who is currently in the car, and a rendering of the grid of nodes is displayed

[ ] - an empty node (street intersection)  
[C] - the node where the car is current at  
[P] - a node with a pickup request  
[D] - a node with a drop off request

### Running different data (custom ride requests)
All custom data can be configured in the `runme.py` file. Edit this file.

#### Custom Requests
If you want to run your own set of pick/drop off requests, edit the `requests` variable. This takes a list of JSON lists which can have as many requests as desired.

n = number of time intervals

##### A blank request
```
requests_time_n = []
```

This will advance the simulation by one time unit and not add any pickup requests.

##### A list of requests with one request
```
requests_time_n = [
  {
    "name": "Name of the passenger",
    "start": [9,9],
    "end": [1,3]
  }
]
```
"start" is a location of `[x,y]` where the passenger should be picked up  
"end" is a location of `[x,y]` where the passenger wants to be dropped off

#### Custom Grid
If you want to change the custom grid size, the first two parameters of the Car object initialization call are the X and Y sizes of the grid respectfully. The third parameter is the starting location of the car given a tuple with an x and y location. Edit any of these parameters.

```
car = Car(X_GRID_DIMENSION, Y_GRID_DIMENSION, (0,0))
```

## 3. The Challenge
https://github.com/joeSzaf/Autonomous-Vehicle-Routing-Coding-Challenge.git

Challenge from the company:

We encourage you to spend no more than 3-4 hours on this challenge.  Please make sure you read the prompt carefully and allot yourself time to properly write up a summary of what you did and what your next steps would be if you had more time.

Autonomous Vehicle Routing Coding Challenge
Ride-hailing companies like Uber and Lyft have become ubiquitous means to get around cities. Efficient vehicle routing, or figuring out the fastest and most efficient way to direct vehicles to pick up and drop off multiple passengers at a time, has become a crucial component of their success.

In the near future you are the proud owner of an autonomous vehicle!  You want to let some friends use it whenever they want so you make an app to let them call the vehicle to come pick them up.  In this problem you will develop a system to keep track of the state of your car and your friends.

Here are some more constraints to help you code your solution:

The city is a grid of perpendicular blocks.  At initialization your code should take as user inputs the number of streets in both the x and y directions (ex. x=10, y=10).

The car can move in any direction exactly 1 block at a time.  For our purposes, we only care about when the car is at a vertex of two intersecting streets, so continuing our example, a car can be at the intersection [0, 0] in the upper-left corner of our city, or [9, 9] in the bottom-right corner.

There should be a function to advance time by one time-step (and hence the vehicle by one block in any direction).  This function should accept a list of ride requests from your friends.  These ride requests come in the form of a list of JSON elements.  For example at time=0, the incoming request list could look like:

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

while at time=1 the request list could be empty:

	requests_time_1 = []

and at time=2 the request list could be:

	requests_time_2 = [
		{
  	   "name": "Nancy",
        "start": [9,9],
        "end": [1,3]
    }
	]

At each time-step this list of requests can be an empty list (ex. []), or infinitely long.  At each time step you should print out the current position of the vehicle and the names of all of the passengers currently in the vehicle, as well as anybody being dropped off or being picked up at this intersection.  (We will assume your car can fit infinitely many people at a time.)

Your goal is to schedule your car to get people where they want to go as fast as possible.  Of course, you will likely have to make some trade-offs in the process.  There is no right answer, just make sure you explain your decisions clearly in your write-up.

Submission:  Please return all of your code, as well as a write up of your solution, as well as any tests you have written in a zip file with your name in the title.

Feel free to code your solution in either Python or C++.

## 4. The Methodology
### Choosing which direction to go
After every tick of the program, the program will calculate the desirability of each adjacent square (up, down, left, right) that the car can move. The program checks if the car is current at the end of the grid and does not calculate an adjacent spot that is off the grid.

It is important that this is checked every tick because a new ride request can be added at any tick. Also, the program checks if the car is at an intersection for a pickup (removes a pickup node and adds a new drop off node) or at a drop off point (removes a drop off node).

The desirability of a space is the total number of square away from the nearest pickup and drop off nodes the space is from. Since the nodes are ordered in a simple grid, the "Manhattan Distance" (the absolute distance x and y between the node and the space) can just be calculated for all the nodes then summed up.

The program will choose the space with the lowest score (the lowest number of spaces away from all the nodes). This translates to the space that is closest to the average center of all the pickup/drop off nodes.

### Trade offs
In the event of a tie in desirability (which is common when the car is in the middle of all the pick-up drop off nodes), there is a built-in tie breaker that determines the nearest pickup or drop off node and goes in that direction. This was chosen for several reasons. First, this eliminate the need to backtrack when a further node is chosen. Next, by picking up a passenger this would add more information regarding the drop off location of that passenger. Since the car can be assumed to be able to hold an infinite number of passengers, we do not have to worry about running our of space. For safety reasons, it would be desirable to pick up any person nearby to get them safe inside a car to protect them from weather or other risks. Patrons in the car would also be miffed if they were driven close to their destination and had to wait to be dropped off.

In the event of a tie in the closest node, I structured the check nearest node method to first check the drop off distance of the oldest ride request. It is only fair for the people who have been waiting longer, to be dropped up first. This check goes through the drop off queue first then the pickup queue.

This method could potentially lead to a long wait time for passengers with further destinations that have the personal misfortune of having many close-by ride requests. I thought it would be a fair compromise for all the riders as a whole to have the car move towards the most destinations, but give the edge to people who have been waiting in the car the longest.

## 5. Next Steps
Here are the features that would be added if there was more time.
### Immediate Items
-Cleaner way to handle user input of custom data.  
-More comprehensive test suite that checks more complex pickup request situations, different grid sizes, etc.  
-Refactor the code, especially the `choose_next_space` class method.  
-Add functionality to the pathfinding algorithm to take into account the drop off locations of the passengers requesting rides that have not been picked up yet.  
-Implement a passenger limit feature.  

### Wish List
-Create a visual GUI (not in the terminal) that displays the grid where the user can see the time automatically tick and/or control the flow of time.  
-Create two different modes of determining who to be picked up next. Lyft Shared/UberPool vs Lyft/UberX. One is a shared ride and continuously picks up/drops off people. The other has a queue system that picks up one fare and waits to drop them off to pick up the next fare (First In First Out).  
-Take into account the different traffic considerations like turning, main/side roads, traffic lights, one-way roads, etc.  
