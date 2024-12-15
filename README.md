# SUMO-4511 Project - Improving Traffic Intersection Heuristics in SUMO with TraCI

======3x3 Trivial (Boolean Circuit)======
Light Traffic 1000
26.08
28.17
28.20
27.85
26.87
avg: 27.43

Med Traffic 1000 <Approaches Gridlock by 1500 timesteps>
84.53
72.26
77.53
84.76
73.20
avg:78.46



======3x3 Primitive Sensor Phase Shift Heuristic PSHeuristic.py======
Light Traffic 1000
13.41
13.15
13.78
13.25
12.97
avg: 13.31

Med Traffic 1000 <Approaches Gridlock by 1500 timesteps>
31.79
31.87
36.26
36.41
38.76
avg: 35.02

Med Traffic 1500
76.26
56.56
53.55
55.71
57.94
avg:60.00


======3x3 Cross-Traffic Comparison Sensor Phase Shift Heuristic CPSHeuristic.py======
Light Traffic 1000
12.74
12.65
13.50
13.33
12.94
avg:13.03

Med Traffic 1000
20.54
22.64
19.64
23.26
20.61
avg:21.34

Med Traffic 1500
21.43
21.55
23.33
19.72
22.07
avg:21.62

Heavy Traffic 1000
52.56
57.54
49.03
66.05
48.78
avg: 54.79

Intense Traffic 1000
113.51
121.75
166.79
125.89
124.61
avg:130.51

======Proto A* Search Phase Shift Heuristic MyHeuristic.py======
Weight = 0

Light Traffic 1000
9.10
9.78
9.56
9.65
9.59
avg:9.54

Med Traffic 1000
20.96
21.35
19.28
19.72
20.99
avg:20.46

Med Traffic 1500
22.29
24.07
21.41
21.97
19.75
avg:21.90

Heavy Traffic 1000
46.96
59.24
39.30
62.89
42.83
avg:50.24

Intense Traffic 1000
108.84
124.83
156.50
125.07
120.75
avg:127.19


Weight = 0.5

Light Traffic 1000
8.11
8.43
8.33
8.44
8.26
avg:8.31

Med Traffic 1000
18.57
20.57
17.52
20.71
18.82
avg:19.24

Med Traffic 1500
19.53
20.13
21.05
19.97
20.87
avg:20.31

Heavy Traffic 1000
50.31
59.33
37.49
62.61
41.69
avg:50.29

Intense Traffic 1000
114.27
133.54
140.45
115.41
110.09
avg:122.75


Weight = 1.0

Light Traffic 1000
8.32
8.39
9.29
9.77
8.96
avg:8.95


Med Traffic 1000
19.75
21.11
18.89
24.38
21.22
avg:21.07

Med Traffic 1500
21.04
23.89
20.08
20.46
21.60
avg:21.41

Heavy Traffic 1000
41.25
53.08
39.34
59.30
44.58
avg: 47.51


Intense Traffic 1000
117.67
112.38
117.61
124.26
135.04
avg:121.39


Weight = 2.0

Light Traffic 1000
11.24
11.92
12.43
12.21
11.31
avg:11.82

Med Traffic 1000
24.09
21.66
23.53
28.19
23.53
avg:24.20

Med Traffic 1500
25.68
24.30
24.22
25.07
26.16
avg:25.09

Heavy Traffic 1000
40.02
59.89
45.81
81.03
46.68
avg:54.69


Intense Traffic 1000
115.21
125.11
137.92
128.62
129.37
avg:127.25



