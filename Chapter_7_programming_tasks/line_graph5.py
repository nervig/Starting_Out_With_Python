# This program shows a simple line graph
import matplotlib.pyplot as plt


def main():
    # Create lists for coordinates X and Y of every dots of gata
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Build a line graph
    plt.plot(x_coords, y_coords, marker='o')

    # Add a sample
    plt.title('Sales by years')

    # Add on axis descriptive labels
    plt.xlabel('Year')
    plt.ylabel('Volume of sales')

    # Customize tick marks
    plt.xticks([0, 1, 2, 3, 4],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Add grid
    plt.grid(True)

    # Show a line graph
    plt.show()


main()
