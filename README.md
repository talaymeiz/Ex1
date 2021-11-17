# Ex1
The current project is a solution to the problem of inlaying a call to a building elevator.<br>
Given a list of calls, their source and destination floors and the time the call is received,<br>
we would like to allocate each call to the suitable elevator so that the average waiting time of all passengers<br>
from the moment the button is pressed until reaching the destination floor is as minimal as possible.<br>
In the previous project we implemented an **online algorithm** that received every call at a given moment.<br>
In the current project we have implemented an **offline algorithm** in which all calls and times are already given and the suitable inlay needs to be returned.<br>
<br>
While searching for information about suitable algorithms we came across the following articles written on the subject:
* /https://www.geeksforgeeks.org/scan-elevator-disk-scheduling-algorithms <br>
A simple algorithm of old elevators and an example of running, a comparison to running SCAN ie on a disk.

* http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf <br>
An article written by James Dong and Hasim Zafar, in which they explain the basis of elevator movement and give ideas for optimizing the algorithm such as
dividing into segments according to the number of elevators and sending the calls to the nearest elevator by calculating distance.

* https://www.quora.com/What-algorithm-is-used-in-modern-day-elevators <br>
Four motion algorithms are presented for optimization purposes such as Elevator Nearest, division into segments by elevators,<br>
division into segments by calls and division into dynamic segments.

* https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-
 /elevators <br>
 A paragraph from the article talks about new elevators where the calls are made before entering the elevator.<br>
 Brings the algorithm called estimated time of arrival control.
 

### *Offline Algorithm:*

1. Save the building details from the jason file in the building class and the elevators details in the elevator class
2. Read the calls file and save each call in the Call class
3. Go through the given list of calls
4. For each call, check whether the call is suitable for the same elevator as that of the previous call, using the 'worth' function that checks:
    - If the calls are in the same direction
    - If the calls time difference is contained in the time it takes the elevator to go up the floor difference
    - If the calls time difference is small
  if so, the current call elevator will be the previous call elevator.
5. If the current call does not match the elevator of the previous call, the current call elevator will be the next elevator
6. Move on to the next call in the list.

### *Average Waiting Time:*


Average Waiting Time | B1 | B2 | B3 | B4 | B5
--- | --- | --- | --- |--- |---
Calls a | 112.92 | 46.06 | 34.16 | 22.99 | 18.42
Calls b | -- | -- | 544.05 | 240.119 | 70.634 
Calls c | -- | -- | 568.46 | 251.971 | 74.342 
Calls d | -- | -- | 554.016 | 247.884 | 72.108 

<br>

Uncompleted Calls | B1 | B2 | B3 | B4 | B5
--- | --- | --- | --- |--- |---
Calls a | 0 | 0 | 0 | ? | 0
Calls b | -- | -- | 160 | 31 | 0 
Calls c | -- | -- | 121 | 31 | 0
Calls d | -- | -- | 66 | 14 | 0 

