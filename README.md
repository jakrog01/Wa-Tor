# Wa-tor simulation model
Wa-tor model simulation written in Python. Simple graphical interface of this app allows you to define the initial parameters of the simulation and see its evolution in real time.

# Required packages

You will need pyside6, numpy and matplotlib packages to run the application:
```
pip install pygame
pip install numpy
pip install matplotlib
```

# Application
## Using the application
Upon launching the application, a simple graphical interface is presented. On the left side of the window, there are buttons to activate the simulation and reset parameters to their default values.

![Start Screen](https://github.com/jakrog01/Wator/assets/141222606/76bf8e6c-ff35-4398-839e-1f6c1627bc62)

Users can manipulate the simulation speed via the control panel.
Below the speed slider lies a control panel, where users can adjust the initial simulation parameters. *Once the simulation is initiated, these parameters remain unalterable.*

Upon initiating the simulation, the program undergoes a brief setup period to prepare the area, then a graphic of the area appears in a large window. 
The program draws a phase diagram in real time and the relationship between predator and prey populations in subsequent time steps.
*Prey are marked in blue and predators in red.*

![Simulation Screen](https://github.com/jakrog01/Wator/assets/141222606/55d61a38-2244-4d51-975c-f33dbaf3139a)

## Wa-tor alghoritm
> Somewhere, in a direction that can only be called recreational at a distance limited only by one's programming prowess, the planet Wa-Tor swims among the stars. It is shaped like a torus, or doughnut, and is entirely covered with water.

Wa-tor is a simulation of an ecosystem consisting of only two species of animals: predators and prey.
Wa-Tor model created and presented by [A. K. Dewdney](http://cs.gettysburg.edu/~tneller/cs107/wator_dewdney.pdf) is a translation of the [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) into a discrete, two-dimensional plane.

