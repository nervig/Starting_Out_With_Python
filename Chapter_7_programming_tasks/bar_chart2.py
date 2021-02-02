# The program show a simple pillar chart
import matplotlib.pyplot as plt

def main():
    # Create a list with coordinates X of left edge every pillar
    left_edges = [0, 10, 20, 30, 40]

    # Create a list with heights every pillar
    heights = [100, 200, 300, 400, 500]

    # Create a variable for a length pillar
    bar_width = 5

    # Build a pillar chart
    plt.bar(left_edges, heights, bar_width, color=('k', 'g', 'b', 'm', 'r'))

    # Show a pillar chart
    plt.show()


main()
