from Gaussiandistribution import Gaussian

# Create an instance of the Gaussian class
gaussian_distribution = Gaussian()

# Read data from a file (replace 'your_data.txt' with the actual file name)
gaussian_distribution.read_data_file('numbers.txt')

# Display the histogram and PDF plot
gaussian_distribution.plot_histogram_pdf()
