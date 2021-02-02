import matplotlib.pyplot as plt


def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    plt.plot(x_coords, y_coords)

    # Title
    plt.title('Sample of data')

    # The name of axis x and y
    plt.xlabel('This is axis x')
    plt.ylabel('This is axis y')

    # The board of axis
    plt.xlim(xmin=-1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    # The grid of field
    plt.grid(True)

    plt.show()


main()
