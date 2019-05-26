# Kickstart 2019 Round C Wiggle Walk Solution (Python)
## Question
### Problem
Banny has just bought a new programmable robot. Eager to test his coding skills, he has placed the robot in a grid of squares with R rows (numbered 1 to R from north to south) and C columns (numbered 1 to C from west to east). The square in row r and column c is denoted (r, c).

Initially the robot starts in the square (SR, SC). Banny will give the robot N instructions. Each instruction is one of N, S, E or W, instructing the robot to move one square north, south, east or west respectively.

If the robot moves into a square that it has been in before, the robot will continue moving in the same direction until it reaches a square that it has not been in before. Banny will never give the robot an instruction that will cause it to move out of the grid.

Can you help Banny determine which square the robot will finish in, after following the N instructions?

### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing the five integers N, R, C, SR and SC, the number of instructions, the number of rows, the number of columns, the robot's starting row and starting column, respectively.

Then, another line follows containing a single string of N characters; the i-th of these characters is the i-th instruction Banny gives the robot (one of N, S, E or W, as described above).

### Output
For each test case, output one line containing Case #x: r c, where x is the test case number (starting from 1), r is the row the robot finishes in and c is the column the robot finishes in.

### Limits
Memory limit: 1GB.<br />
1 ≤ T ≤ 100.<br />
1 ≤ R ≤ 5 × 10<sup>4</sup>.<br />
1 ≤ C ≤ 5 × 10<sup>4</sup>.<br />
1 ≤ SR ≤ R.<br />
1 ≤ SC ≤ C.<br />
The instructions will not cause the robot to move out of the grid.<br />

Test set 1 (Visible)<br />
Time limit: 20 seconds.<br />
1 ≤ N ≤ 100.<br />
<br />
Test set 2 (Hidden)<br />
Time limit: 60 seconds.<br />
1 ≤ N ≤ 5 × 104.<br /><br />

### Sample

Input <br />
 	
Output <br />
 
3<br />
5 3 6 2 3<br />
EEWNS<br />
4 3 3 1 1<br />
SESE<br />
11 5 8 3 4<br />
NEESSWWNESE<br /><br />

  
Case #1: 3 2<br />
Case #2: 3 3<br />
Case #3: 3 7<br />

  
Sample Case #1<br /> corresponds to the top-left diagram, Sample Case #2 corresponds to the top-right diagram and Sample Case #3 corresponds to the lower diagram. In each diagram, the yellow square is the square the robot starts in, while the green square is the square the robot finishes in.

<svg version="1.1" viewBox="0.0 0.0 960.0 720.0" fill="none" stroke="none" stroke-linecap="square" stroke-miterlimit="10" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg"><clipPath id="p.0"><path d="m0 0l960.0 0l0 720.0l-960.0 0l0 -720.0z" clip-rule="nonzero"></path></clipPath><g clip-path="url(#p.0)"><path fill="#000000" fill-opacity="0.0" d="m0 0l960.0 0l0 720.0l-960.0 0z" fill-rule="evenodd"></path><path shape-rendering="crispEdges" fill="#ffff00" d="m235.50919 128.35957l76.80054 0l0 76.80054l-76.80054 0l0 -76.80054z" fill-rule="nonzero"></path><path shape-rendering="crispEdges" fill="#00ff00" d="m158.70866 205.16011l76.80052 0l0 76.80052l-76.80052 0l0 -76.80052z" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m81.908134 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m158.70866 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m235.50919 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m312.30972 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m389.11023 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m465.91077 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m542.7113 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m79.908134 51.559055l464.80316 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m79.908134 128.35957l464.80316 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m79.908134 205.16011l464.80316 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m79.908134 281.96063l464.80316 0" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m272.6063 153.16536l74.77167 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m272.6063 153.16536l56.771667 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m329.37796 158.12054l13.614288 -4.955185l-13.614288 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m352.9685 153.16536l78.39371 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m352.9685 153.16536l60.393707 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m413.3622 158.12054l13.614288 -4.955185l-13.614288 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m430.15485 172.46194l-220.25195 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m430.15485 172.46194l-202.25195 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m227.9029 167.50674l-13.614304 4.9552l13.614304 4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m201.8924 173.6693l0 -80.8189" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m201.8924 173.6693l0 -62.8189" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m206.84758 110.850395l-4.955185 -13.614296l-4.9552 13.614296z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m182.5958 92.86352l0 154.36221" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m182.5958 92.86352l0 136.36221" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m177.64061 229.22572l4.955185 13.614288l4.9552 -13.614288z" fill-rule="evenodd"></path><path shape-rendering="crispEdges" fill="#ffff00" d="m635.5696 51.559055l76.800476 0l0 76.80052l-76.800476 0l0 -76.80052z" fill-rule="nonzero"></path><path shape-rendering="crispEdges" fill="#00ff00" d="m789.1706 205.16011l76.80054 0l0 76.80052l-76.80054 0l0 -76.80052z" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m635.5696 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m712.37006 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m789.1706 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m865.9711 49.559055l0 234.40158" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m633.5696 51.559055l234.40155 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m633.5696 128.35957l234.40155 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m633.5696 205.16011l234.40155 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m633.5696 281.96063l234.40155 0" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m673.4514 99.173225l0 62.110237" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m673.4514 99.173225l0 44.110237" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m668.4962 143.28346l4.9552 13.614288l4.9552 -13.614288z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m750.7703 176.6798l0 62.11023" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m750.7703 176.6798l0 44.11023" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m745.8151 220.79002l4.9552 13.614288l4.9552 -13.614288z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m682.79395 166.75984l55.77954 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m682.79395 166.75984l37.77954 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m720.5735 171.71504l13.614319 -4.9552l-13.614319 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m765.88055 238.78871l55.77954 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m765.88055 238.78871l37.77954 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m803.6601 243.74391l13.614319 -4.9552l-13.614319 -4.9552z" fill-rule="evenodd"></path><path shape-rendering="crispEdges" fill="#ffff00" d="m309.99213 472.01575l76.80054 0l0 76.80054l-76.80054 0l0 -76.80054z" fill-rule="nonzero"></path><path shape-rendering="crispEdges" fill="#00ff00" d="m540.3937 472.01575l76.80054 0l0 76.80054l-76.80054 0l0 -76.80054z" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m79.59055 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m156.39108 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m233.1916 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m309.99213 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m386.79266 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m463.59317 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m540.3937 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m617.1942 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m693.99475 316.4147l0 388.0026" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 318.4147l618.4042 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 395.2152l618.4042 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 472.01575l618.4042 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 548.8163l618.4042 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 625.6168l618.4042 0" fill-rule="nonzero"></path><path stroke="#000000" stroke-width="4.0" stroke-linecap="butt" d="m77.59055 702.4173l618.4042 0" fill-rule="nonzero"></path><path fill="#000000" fill-opacity="0.0" d="m357.79266 510.7467l0 -72.346436" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m357.79266 510.7467l0 -54.346436" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m362.74783 456.40027l-4.9551697 -13.614288l-4.9552 13.614288z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m364.2651 435.37796l69.95273 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m364.2651 435.37796l51.95273 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m416.21783 440.33316l13.614319 -4.9552l-13.614319 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m445.06824 434.77954l48.251984 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m445.06824 434.77954l30.251984 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m475.32022 439.7347l13.614288 -4.9551697l-13.614288 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m504.16272 436.58267l0 86.834625" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m504.16272 436.58267l0 68.834656" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m499.20752 505.41733l4.9552 13.614288l4.9552 -13.614288z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m504.16272 531.8609l0 54.2677" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m504.16272 531.8609l0 36.2677" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m499.20752 568.1286l4.9552 13.614319l4.9552 -13.614319z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m495.13123 588.54333l-74.17322 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m495.13123 588.54333l-56.173218 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m438.958 583.58813l-13.614288 4.9552l13.614288 4.955139z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m404.063 588.54333l-62.70865 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m404.063 588.54333l-44.70865 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m359.35434 583.58813l-13.614288 4.9552l13.614288 4.955139z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m335.3176 585.2126l0 -224.91336" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m335.3176 585.2126l0 -206.91336" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m340.2728 378.29922l-4.9552 -13.614319l-4.9552 13.614319z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m342.55643 360.60367l63.905518 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m342.55643 360.60367l45.905518 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m388.46194 365.55887l13.614288 -4.9552l-13.614288 -4.9552z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m406.46194 371.4567l0 124.22046" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m406.46194 371.4567l0 106.22046" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m401.50674 477.67715l4.9552 13.614319l4.9552 -13.614319z" fill-rule="evenodd"></path><path fill="#000000" fill-opacity="0.0" d="m416.12335 495.67715l154.39374 0" fill-rule="evenodd"></path><path stroke="#ff0000" stroke-width="3.0" stroke-linejoin="round" stroke-linecap="butt" d="m416.12335 495.67715l136.39374 0" fill-rule="evenodd"></path><path fill="#ff0000" stroke="#ff0000" stroke-width="3.0" stroke-linecap="butt" d="m552.5171 500.63235l13.614258 -4.9552l-13.614258 -4.9552z" fill-rule="evenodd"></path></g></svg>