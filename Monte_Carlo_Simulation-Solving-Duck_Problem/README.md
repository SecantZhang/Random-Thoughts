# Approximating the Duck-Problem using Monte-Carlo Simulation

Link to full description and thought process for this script: [MC Blog](https://secantzhang.github.io/blog/monte-carlo-method-solving-duck-problem)

## Problem Definition: 

> Suppose I have four ducks randomly located inside a round pool, what is the probability that the four ducks happen to be in the same semi-circle? 

## Dependencies: 

* Python 3
* random
* tqdm
* math
* numpy

## How to Run: 

Change the parameters of the ```main()``` function in line ```75```, the first parameter is the ```canvas_size``` and the second parameter is the number of simulations. Basically, the default parameters given in the code have a pretty good running time and convergence guarantee. But you can play around if you like. 

### In Terminal (Mac): 

```
python mc_duck_simulation.py
```