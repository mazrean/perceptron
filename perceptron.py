from os import times
import read
import numpy as np

def culc(times, lm, rho):
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

    print(w)

    max_i = 0
    max_seccess = 0
    max_w = w
    max_r_i = 0
    max_r_seccess = 0
    max_r_w = w
    teacher_successes = []
    random_successes = []
    for i in range(times):
        rho=1/(10*i+1)
        success = 0
        for v in teacher_data:
            result = np.dot(w, v[0])[0][0]
            if result > -lm and (not v[1]):
                w -= (rho * v[0]).T
            elif result < lm and v[1]:
                w += (rho * v[0]).T
            else:
                success += 1
        teacher_successes.append(success)
        if success > max_seccess:
            max_seccess = success
            max_i = i
            max_w = np.copy(w)

        success = 0
        for v in random_data:
            result = np.dot(w, v[0])[0][0] > 0.0
            if result == v[1]:
                success += 1
        random_successes.append(success)
        if success > max_r_seccess:
            max_r_seccess = success
            max_r_i = i
            max_r_w = np.copy(w)

    print(max_i)
    print(max_w)
    print(max_seccess)
    print(max_r_i)
    print(max_r_w)
    print(max_r_seccess)
    print(w)

    teacher_length = len(teacher_data)
    teacher_rates = list(map(lambda x: x/teacher_length, teacher_successes))

    random_length = len(random_data)
    random_rates = list(map(lambda x: x/random_length, random_successes))

    return teacher_rates, random_rates, times