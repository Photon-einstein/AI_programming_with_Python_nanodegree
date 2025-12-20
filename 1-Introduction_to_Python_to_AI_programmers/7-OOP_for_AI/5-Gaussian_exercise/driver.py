from Gaussiandistribution import Gaussian


if __name__ == "__main__":
    filename = "numbers.txt"
    gaussian = Gaussian()
    gaussian.read_data_file(filename)
    gaussian.plot_histogram()
    gaussian.plot_histogram_pdf()