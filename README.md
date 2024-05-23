# Wa-Tor simulation model
Wa-Tor model simulation written in Python. Simple graphical interface of this app allows you to define the initial parameters of the simulation and see its evolution in real time. You can also use Wa-Tor Analyzer to analyze the impact of one of the parameters on the stability of the ecosystem.
The project was inspired by this [simulation](http://en.alife.pl/predators-and-prey-the-Lotka-Volterra-model).

## Required packages

You will need pyside6, numpy and matplotlib packages to run the application:
```
pip install pyside6
pip install numpy
pip install matplotlib
```

# Wa-Tor Simulator Application
## Using the application
Upon launching the application, a simple graphical interface is presented. On the left side of the window, there are buttons to activate the simulation and reset parameters to their default values.

![Start Screen](https://github.com/jakrog01/Wator/assets/141222606/76bf8e6c-ff35-4398-839e-1f6c1627bc62)

Users can manipulate the simulation speed via the control panel.
Below the speed slider lies a simulation parameters panel, where users can adjust the initial simulation parameters. *Once the simulation is initiated, these parameters remain unalterable.*

Upon initiating the simulation, the program undergoes a brief setup period to prepare the area, then a graphic of the area appears in a large window. 
The program draws a phase diagram in real time and the relationship between predator and prey populations in subsequent time steps.
*Prey are marked in blue and predators in red.*

![Simulation Screen](https://github.com/jakrog01/Wator/assets/141222606/55d61a38-2244-4d51-975c-f33dbaf3139a)

## Wa-Tor alghoritm
> Somewhere, in a direction that can only be called recreational at a distance limited only by one's programming prowess, the planet Wa-Tor swims among the stars. It is shaped like a torus, or doughnut, and is entirely covered with water.

Wa-Tor is a simulation of an ecosystem consisting of only two species of animals: predators and prey.
Wa-Tor model created and presented by [A. K. Dewdney](http://cs.gettysburg.edu/~tneller/cs107/wator_dewdney.pdf), is a translation of the [Lotka-Volterra equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) into a discrete, two-dimensional plane.

$$\begin{equation}
\begin{cases}
\dot{V} = \alpha (a)V(t) - \beta (b)V(t)P(t)  \newline \\
\dot{P} = \delta (b,d) V(t) P(t) - \gamma (c) P(t)
\end{cases}
\end{equation}$$

### Algorithm used in the simulation
1. Simulation initialization
   - Random distribution of prey in the ecosystem area.
   - Random distribution of predators in the ecosystem area.
2. Run simulation based on discrete time steps
   - Prey movement
     - Each prey moves to a random, empty adjacent field ([PBCs](https://en.wikipedia.org/wiki/Periodic_boundary_conditions)).
     - If there are no free squares, the prey doesn't move.
     - After completing a set number of steps _(parameter a)_, the prey reproduces (leaving another prey on its field).
   - Predators movement
     - Each predator moves to an adjacent field occupied by prey ([PBCs](https://en.wikipedia.org/wiki/Periodic_boundary_conditions)).
     - If there is no prey in any adjacent field, the predator moves as the prey.
     - After completing a set number of steps _(parameter d)_, the predator reproduces (leaving another predator on its field).
     - If a predator hunts its prey (moves to its field), it has a certain percentage of chance of successful hunting _(parameter b)_
     - If the predator does not hunt (or the hunt is unsuccessful), the predator uses energy to move. If the energy lost by it is equal to the parameter _(parameter c)_, the predator dies. A successful hunt resets the energy consumed by the predator.

### Result
<p align="center">
  <img src="https://github.com/jakrog01/Wa-Tor/assets/141222606/b764269e-f7e0-4c66-838e-4d6c08036a7b" alt="animated" />
</p>

# Wa-Tor Analizayer Application
Wa-Tor Analyzer is a console-based application used to analyze the Wa-Tor model. The algorithm used in this application is exactly the same as in Wa-Tor Simulator.

The entire application is devoted to drawing charts. In the application code, you can specify how many threads the application should run on (after entering 0, the program works on all possible threads). You can determine the number of iterations in a given step that interests you and the number of measurements "in one sample" from which the average is calculated. You can also assign the **strategy variable** to one of the following strategies:
1. **Plot oscilation in time strategy**: it plots changes in prey and predator populations
2. **Respect to strategy**: it plots the dependence of the number of iterations for which the ecosystem was stable on the changing parameter. Each of the initial simulation parameters has its own strategy that prepares graphs for it.

For convenience of use, the results are presented in the form of ready-made charts (AnalysisResults\png folder) and txt files with the results (AnalysisResults\txt folder). The graph also shows the threshold value for which balance occurred in the ecosystem. Charts can be created with or without marked standard deviation.

### Example result
As an example of using the program, I created a raport examining the relationship between the balance in the ecosystem and the effectiveness of hunting. The [example raport](Wa_TorRaportExample.pdf) is available on this repository.
