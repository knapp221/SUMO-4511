import matplotlib.pyplot as plt

# Traffic levels along X-axis
traffic_levels = ["Light", "Medium", "Medium1500", "Heavy", "Intense"]

# Example data for 3 heuristics (extend similarly for all 6)
Boolean = [12, 25, 110]
PSHeuristic = [10, 22, 110]
CPSHeuristic = [8, 20, 110]
MyHeuristicW0 = [8, 20, 110]
MyHeuristicW05 = [8, 20, 110]
MyHeuristicW1 = [8, 20, 110]
MyHeuristicW2 = [8, 20, 110]


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
