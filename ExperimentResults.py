import matplotlib.pyplot as plt

# Traffic levels along X-axis
traffic_levels = ["Light", "Medium", "Medium1500", "Heavy", "Intense"]

# Example data for 3 heuristics (extend similarly for all 6)
Boolean = [ 27.43 , 78.46 , None , None , None ]
PSHeuristic = [ 13.31 , 35.02 , 60.00 , None, None ]
CPSHeuristic = [ 13.03 , 21.34 , 21.62 , 54.79 , 130.51 ]
MyHeuristicW0 = [ 9.54 , 20.46 , 21.90 , 50.24 , 127.19 ]
MyHeuristicW05 = [ 8.31 , 19.24 , 20.31 , 50.29 , 122.75 ]
MyHeuristicW1 = [ 8.95 , 21.07 , 21.41 , 47.51 , 121.39 ]
MyHeuristicW2 = [ 11.82 , 24.20 , 25.09 , 54.69 , 127.25 ]


plt.plot(traffic_levels, Boolean, marker='o', label='Boolean Circuit')
plt.plot(traffic_levels, PSHeuristic, marker='o', label='PSHeuristic')
plt.plot(traffic_levels, CPSHeuristic, marker='o', label='CPSHeuristic')
plt.plot(traffic_levels, MyHeuristicW0, marker='o', label='MyHeuristic W=0')
plt.plot(traffic_levels, MyHeuristicW05, marker='o', label='MyHeuristic W=0.5')
plt.plot(traffic_levels, MyHeuristicW1, marker='o', label='MyHeuristic W=1')
plt.plot(traffic_levels, MyHeuristicW2, marker='o', label='MyHeuristic W=2')

# Add more lines for Heuristic 4, Heuristic 5, Heuristic 6 similarly

plt.xlabel('Traffic Level')
plt.ylabel('Average Idle Time (seconds)')
plt.title('Comparison of Heuristic Performance by Traffic Intensity')
plt.legend()
plt.grid(True)
plt.show()
