import matplotlib.pyplot as plt
y = [3.0, 6.25, 6.92, 7.86, 8.88, 9.63, 10.08, 10.35, 11.61, 12.05, 13.2, 14.34, 15.22, 15.53, 16.9, 17.13, 18.91, 19.91, 20.06, 22.01, 23.43, 24.33, 25.73, 27.76, 29.13, 29.86, 32.51, 34.61, 36.93, 38.88, 41.41, 45.16, 49.73, 52.5, 54.87, 61.92, 68.66, 71.28, 80.66, 86.85, 99.16, 109.14, 130.41, 146.71, 177.0, 219.79, 275.61, 360.33, 618.87, 1609.4, 2500.0, 2500.0, 2500.0, 2500.0, 2500.0] 
y_error = [0.0, 0.6837397165588672, 1.0361467077590893, 1.3417898494175606, 1.4783774890061063, 1.8902645317521038, 1.921874085365636, 1.8728320800328042, 2.077955726188602, 2.108909670896314, 2.723967694375247, 2.9773142259425693, 3.0350617786134104, 2.812312215953271, 3.398529093593286, 2.8342723934018763, 4.1571504663651515, 3.8028804872096624, 3.804786459185325, 4.477711469043086, 4.93812717535707, 5.12260675828235, 4.374597124307563, 5.486565410163266, 6.2139439971728105, 5.03193799643835, 6.5673358373087645, 6.67666833083687, 6.817998239952838, 8.211309274409288, 8.056171547329413, 9.03296186198082, 10.010849114835365, 9.745255255764212, 11.751302055517083, 13.627677718525636, 13.565559332368126, 15.051963327087932, 14.976127670395975, 15.683988650850269, 22.373967015261282, 20.159871031333505, 31.719109382200504, 31.56304643091348, 40.40841496520248, 54.78107246120689, 80.89683491954429, 104.52837461665614, 188.5286002175797, 527.4204394977502, 0.0, 0.0, 0.0, 0.0, 0.0]

threshold = 0
max = 0

for index,b in enumerate(y):
    if b == 2500.0:
        threshold = index
        break
    elif b > max:
        max = b
        threshold = index

xs = [x for x in range (len(y))]
plt.axvline(threshold, linestyle='-.', linewidth = 1, label = f"Threshold value= {round(threshold,2)}%", color = "grey")
plt.errorbar(xs, y, yerr=y_error)
plt.xlabel("Hunting efficiency [%]")
plt.ylabel("Number of stable iterations")
plt.legend(loc='upper left')
plt.show()
print(max)
