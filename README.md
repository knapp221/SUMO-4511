# SUMO-4511 Project - Improving Traffic Intersection Heuristics in SUMO with TraCI

Corey Knapp
CSCI 4511W 
Prof. A. Exley
December 2024
University of Minnesota

How to use:
The following repository was designed to be used with Simulation of Urban MObility (SUMO) and executed from the command line in Linux.

Therefore, in order to run any simulations from this repository, there are the following dependencies:
SUMO - Be sure to add it to PATH.
Python 3 - Python 3.12 specifically was used for this project environment.
TraCI - SUMO doesn't always come with TraCI installed, but should be contained in the sumo-tools installation.

Using the following command should capture both sumo and TraCI, with only install sumo-tools being necessary if 
SUMO is installed, but the import appears to be missing.

sudo apt-get install sumo sumo-tools sumo-doc 

Once all dependencies are set up, the python files can be ran, and should automatically open SUMO when executed. 
However, you will need to change the PATH at the top of each python file to match where Simulation.sumocfg and the
.xml files are located. Don't forget to add /Simulation.sumocfg at the end of the path or SUMO will not open. 
Once setup, typing the following into command line:

python3 MyHeuristic.py

Should open the SUMO simulation environment. Pressing the run button at the top will run the simulation
beginning at timestep 0 and will end on timestep 1000, as per the Simulation.sumocfg file. Feel
free to modify the start and end times of the simulation, though the .rou.xml vehicle behavior
only works as intended until timestep 7000. It is also recommended to add delay for visualization
purposes, but this isn't necessary.



GAI NOTICE: As mentioned in the GAI footnote of the writeup, many of the python files contain code
written by a GAI--some more than others. Please refer to each python file for more specifics.
In the general case, I do not take any credit for the code contained in Boolean.py, PSHeuristic.py,
CPSHeuristic.py, and a large subsection of MyHeuristic.py, which is a progression of CPSHeuristic.py.

3x3.net.xml and 3x3.rou.xml were provided by Lucas Alegre’s github.com repository:
https://github.com/LucasAlegre/sumo-rl .

Please see the sources cited page of the writeup for further information about sources used in this
project.













