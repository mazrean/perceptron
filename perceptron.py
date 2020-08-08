from os import times
import read
import numpy as np

def culc(times, ryo=0.00001):
    data = read.read()
    random_data = list(filter(lambda x: x[0]%2!=0, data))
    teacher_data = list(filter(lambda x: x[0]%2==0, data))

    def extend(l):
        l.insert(0, 1.0)
        return l

    random_data = list(map(lambda x: (np.matrix(extend(x[1:4])).T, x[4]), random_data))
    teacher_data = list(map(lambda x: (np.matrix(extend(x[1:4])).T, x[4]), teacher_data))


    w = teacher_data[0][0].T
    if not teacher_data[0][1]:
        w = -teacher_data[0][0].T

    teacher_successes = []
    random_successes = []
    for i in range(times):
        success = 0
        for v in teacher_data:
            result = np.dot(w, v[0])[0][0] > 0.0
            if result and (not v[1]):
                w -= (ryo * v[0]).T
            elif (not result) and v[1]:
                w += (ryo * v[0]).T
            else:
                success += 1
        teacher_successes.append(success)

        success = 0
        for v in random_data:
            result = np.dot(w, v[0])[0][0] > 0.0
            if result == v[1]:
                success += 1
        random_successes.append(success)

    teacher_length = len(teacher_data)
    teacher_rates = list(map(lambda x: x/teacher_length, teacher_successes))

    random_length = len(random_data)
    random_rates = list(map(lambda x: x/random_length, random_successes))

    return teacher_rates, random_rates, times