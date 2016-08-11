# HanoiPython
A simple Tower-of-Hanoi console game in Python

## Description
I created this to demonstrate some programming ideas to my son, who has been teaching himself Python.

The game involves moving disks from one pin to another:

```
TOWER OF HANOI v1.0
by YOUR NAME GOES HERE
     |        |        |    
    [1]       |        |    
   [ 2 ]      |        |    
  [  3  ]     |        |    
 [   4   ]    |        |    
[    A        B        C    ]

Your move?  
```

You can only move a disk onto an empty pin or a larger disk. The game ends once you've moved the entire tower.

## Known Issues
It has room for further work / exercises for the reader.

* The hint feature doesn't work. It could suggest the best next move.
* It is trivial to rank the player's score out of the best possible - computing the maximum number of moves is a fairly simple function.
* There's a bug where an error message will stay visible after it's appeared the first time. Can you find it?
