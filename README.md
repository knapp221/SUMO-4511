# SUMO-4511 Project - Improving Traffic Intersection Heuristics in SUMO with TraCI

======3x3 Trivial (Boolean Circuit)======
Light Traffic 1000
26.08
28.17
28.20

Med Traffic 1000 <Approaches Gridlock by 1500 timesteps>
84.53
72.26
77.53

Med Traffic 1500
150.85
151.08
142.41



======3x3 Primitive Sensor Phase Shift Heuristic PSHeuristic.py======
Light Traffic 1000
13.41
13.15
13.78

Med Traffic 1000 <Approaches Gridlock by 1500 timesteps>
31.79
31.87
36.26

Med Traffic 1500
76.26
56.56
53.55



======3x3 Cross-Traffic Comparison Sensor Phase Shift Heuristic CPSHeuristic.py======
Light Traffic 1000
12.74
12.65
13.50

Med Traffic 1000
20.54
22.64
19.64

Med Traffic 1500
21.43
21.55
23.33

Heavy Traffic 1000
113.51
121.75
166.79
125.89
124.61

======Primitive greedy Phase Shift Heuristic MyHeuristic.py======
Weight = 0

Light Traffic 1000
9.10
9.78
9.56
9.65
9.59

Med Traffic 1000
20.96
21.35
19.28
19.72
20.99

Med Traffic 1500
22.29
24.07
21.41

Heavy Traffic 1000
108.84
124.83
156.50
125.07
120.75



Weight = 0.5

Light Traffic 1000
8.11
8.43
8.33
8.44
8.26

Med Traffic 1000
18.57
20.57
17.52
20.71
18.82

Med Traffic 1500
19.53
20.13
21.05

Heavy Traffic 1000
114.27
133.54
140.45


Weight = 1.0

Light Traffic 1000
8.32
8.39
9.29
9.77
8.96


Med Traffic 1000
19.75
21.11
18.89
24.38
21.22

Med Traffic 1500
21.04
23.89
20.08

Heavy Traffic 1000
117.67
112.38
117.61


Weight = 2.0

Light Traffic 1000
11.24
11.92
12.43

Med Traffic 1000
24.09
21.66
23.53

Med Traffic 1500
25.68
24.30
24.22

Heavy Traffic 1000
115.21
125.11



