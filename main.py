import perceptron
import plot

def main():
    times = 10000
    teacher_rates, random_rates, times = perceptron.culc(times, 0.00000001)
    plot.graph(times, teacher_rates, random_rates)

main()