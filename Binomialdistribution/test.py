from Binomialdistriburtion import Binomial

# Create an instance of the Gaussian class
Binomialdistriburtion = Binomial()

# Read data from a file (replace 'your_data.txt' with the actual file name)
Binomialdistriburtion.read_data_file('numbers.txt')

# Display the histogram and PDF plot
Binomialdistriburtion.plot_histogram_pdf()
