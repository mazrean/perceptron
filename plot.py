import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(r_dates, r_min_temp, r_max_temp, b_dates, b_min_temp, b_max_temp):
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.set_xlabel("wet")
    ax.set_ylabel("cloud")
    ax.set_zlabel("sun")

    ax.plot(r_dates, r_min_temp, r_max_temp,marker="o",linestyle='None', color="m")
    ax.plot(b_dates, b_min_temp, b_max_temp,marker="o",linestyle='None', color="c")

    plt.show()

def graph(times, teacher_rates, random_rates):
    x = list(range(times))

    plt.xlabel("times(回)")
    plt.ylabel("accuracy rate")
    plt.plot(x, teacher_rates, color="red")
    plt.plot(x, random_rates, color="blue")

    plt.show()