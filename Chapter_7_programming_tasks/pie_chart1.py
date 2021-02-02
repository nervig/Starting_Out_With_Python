# The program show a simple circle diagram
import matplotlib.pyplot as plt

def main():
    # Create a list of values
    values = [20, 60, 80, 40]

    # Create a circle diagram from that values
    plt.pie(values)

    # Show a circle diagram
    plt.show()


main()
