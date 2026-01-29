import matplotlib.pyplot as plt

x_axis = list(x for x in range(1, 5001))
y_axis = [x**3 for x in x_axis]

plt.scatter(x_axis, y_axis, c=y_axis, cmap=plt.cm.Reds, edgecolor="none", s=40)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.axis([0, 5100, 0, 5100**3])

plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
