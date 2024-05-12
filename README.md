# Wa-tor simulation model
Wa-tor model simulation written in Python. Simple graphical interface of this app allows you to define the initial parameters of the simulation and see its evolution in real time.
The project was inspired by this [simulation](http://www.alife.pl/drapiezniki-i-ofiary-model-Lotki-Volterry).

# Required packages

You will need pyside6, numpy and matplotlib packages to run the application:
```
pip install pyside6
pip install numpy
pip install matplotlib
```

# Application
## Using the application
Upon launching the application, a simple graphical interface is presented. On the left side of the window, there are buttons to activate the simulation and reset parameters to their default values.

![Start Screen](https://github.com/jakrog01/Wator/assets/141222606/76bf8e6c-ff35-4398-839e-1f6c1627bc62)

Users can manipulate the simulation speed via the control panel.
Below the speed slider lies a simulation parameters panel, where users can adjust the initial simulation parameters. *Once the simulation is initiated, these parameters remain unalterable.*

Upon initiating the simulation, the program undergoes a brief setup period to prepare the area, then a graphic of the area appears in a large window. 
The program draws a phase diagram in real time and the relationship between predator and prey populations in subsequent time steps.
*Prey are marked in blue and predators in red.*

![Simulation Screen](https://github.com/jakrog01/Wator/assets/141222606/55d61a38-2244-4d51-975c-f33dbaf3139a)

## Wa-tor alghoritm
> Somewhere, in a direction that can only be called recreational at a distance limited only by one's programming prowess, the planet Wa-Tor swims among the stars. It is shaped like a torus, or doughnut, and is entirely covered with water.

Wa-tor is a simulation of an ecosystem consisting of only two species of animals: predators and prey.
Wa-Tor model created and presented by [A. K. Dewdney](http://cs.gettysburg.edu/~tneller/cs107/wator_dewdney.pdf), is a translation of the [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) into a discrete, two-dimensional plane.

$$\begin{equation}
\begin{cases}
\dot{V} = aV(t) - bV(t)P(t)  \newline \\
\dot{P} = bdP(t) -cP(t)
\end{cases}
\end{equation}$$

### Algorithm used in the simulation
1. Simulation initialization
   - Random distribution of prey in the ecosystem area.
   - Random distribution of predators in the ecosystem area.
2. Run simulation based on discrete time steps
   - Prey movement
     - Each prey moves to a random, empty adjacent field (PBCs).
     - If there are no free squares, the prey doesn't move.
     - After completing a set number of steps _(parameter a)_, the prey reproduces (leaving another prey on its field).
   - Predators movement
     - Each predator moves to an adjacent field occupied by prey (PBCs).
     - If there is no prey in any adjacent field, the predator moves as the prey.
     - After completing a set number of steps _(parameter d)_, the predator reproduces (leaving another predator on its field).
     - If a predator hunts its prey (moves to its field), it has a certain percentage of chance of successful hunting _(parameter b)_
     - If the predator does not hunt (or the hunt is unsuccessful), the predator uses energy to move. If the energy lost by it is equal to the parameter _(parameter c)_, the predator dies. A successful hunt resets the energy consumed by the predator.
    

     
