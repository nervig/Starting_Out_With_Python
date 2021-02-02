# The program show a simple circle diagram
import matplotlib.pyplot as plt

def main():
    # Create a list of value of sales
    sales = [100, 400, 300, 600]

    # Create a list of beat labels
    slice_labels = ['1st qrt', '2st qrt', '3st qrt', '4st qrt']

    # Create a circle diagram from that values
    plt.pie(sales, labels=slice_labels, colors=('g', 'b', 'm', 'r'))

    # Add a title
    plt.title('Sales by quarters')

    # Show a circle diagram
    plt.show()


main()
