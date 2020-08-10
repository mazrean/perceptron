import perceptron
import plot

def main():
    times = 50000
    teacher_rates, random_rates, times = perceptron.culc(times, 20.0, 0.001)
    plot.graph(times, teacher_rates, random_rates)