1. Generate the grid to hold the data. A list of lists.

# Features to add
* Create two different modes of determining who to be picked up next. Lyft Shared/UberPool vs Lyft/UberX. One is a shared ride and continuously picks up/drops off people. The other has a queue system that picks up one fare and waits to drop them off to pick up the next fare.

* An issue I ran into when there was a lot of the same value spaces between nodes, it could go in an endless loop. I decided break this tie by finding the path to the nearest node
