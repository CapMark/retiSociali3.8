import matplotlib.pyplot as plt



def plotFunctions(x1, y1, x2, y2, x3, y3, titolo):
    plt.figure(figsize=(10, 6))
    plt.plot(x1, y1, label='Half degree', color='blue')
    plt.plot(x2, y2, label='random', color='green')
    plt.plot(x3, y3, label='vicinato', color='red')
    plt.title(titolo)
    plt.xlabel('budget')
    plt.ylabel('n influenzati')
    plt.grid(True)
    plt.legend()
    plt.show()


f1x1 = [10, 25, 50, 75, 100, 150]
f1y1 = [10, 11, 35, 56, 75, 132]

f1x2 = [10, 25, 50, 75, 100, 150]
f1y2 = [3, 16, 53, 71, 94, 144]

f1x3 = [10, 25, 50, 75, 100, 150]
f1y3 = [14, 34, 94, 114, 138, 194]

f2x1 = [10, 25, 50, 75, 100, 150]
f2y1 = [12, 22, 38, 49, 67, 94]

f2x2 = [10, 25, 50, 75, 100, 150]
f2y2 = [3, 16, 44, 57, 87, 116]

f2x3 = [10, 25, 50, 75, 100, 150]
f2y3 = [11, 31, 72, 119, 141, 165]

f3x1 = [10, 25, 50, 75, 100, 150]
f3y1 = [0, 13, 41, 54, 74, 131]

f3x2 = [10, 25, 50, 75, 100, 150]
f3y2 = [10, 13, 41, 54, 81, 136]

f3x3 = [10, 25, 50, 75, 100, 150]
f3y3 = [13, 41, 74, 110, 154, 192]


plotFunctions(f1x1, f1y1, f1x2, f1y2, f1x3, f1y3, "Funzione 1")
plotFunctions(f2x1, f2y1, f2x2, f2y2, f2x3, f2y3, "Funzione 2")
plotFunctions(f3x1, f3y1, f3x2, f3y2, f3x3, f3y3, "Funzione 3")
