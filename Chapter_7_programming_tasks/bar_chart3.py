# The program show a diagram of volume of sales
import matplotlib.pyplot as plt


def main():
    # Create a list with coordinate X left edge every pillar
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with heights every pillar
    heights = [100, 200, 300, 400, 500]

    # Create a variable for width of pillar
    bar_width = 10

    # Build a diagram bar
    plt.bar(left_edges,heights, bar_width,
            color=('k', 'g', 'b', 'm', 'r'))

    # Add title
    plt.title('Sales by years')

    # Add to axis describe labels
    plt.xlabel('Year')
    plt.ylabel('Volume of sales')

    # Customize tick marks
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Show a bar diagram
    plt.show()


main()
