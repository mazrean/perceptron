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