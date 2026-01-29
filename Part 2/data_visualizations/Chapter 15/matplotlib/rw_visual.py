import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))

    plt.plot(
        rw.x_values,
        rw.y_values,
        linewidth = 5
    )

    plt.plot(0, 0, linewidth=5)
    plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth=5)

    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
