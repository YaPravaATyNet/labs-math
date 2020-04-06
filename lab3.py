import numpy as np
import matplotlib.pyplot as plt


def numeral(vector):
    cur = vector
    i = 0
    norms = np.array([])
    while True:
        prev = cur
        cur = prev.dot(matrix)
        i += 1
        norm = np.linalg.norm(prev - cur)
        norms = np.append(norms, norm)
        if norm < eps:
            break
    print("Конечное состояние: ", cur)
    print("Переходы: ", i)

    plt.title('Изменение среднеквадратичного отклонения')
    plt.ylabel('Среднеквадратичное отклонение')
    plt.xlabel('Шаг')
    plt.plot(np.array(range(1, i + 1)), norms)
    plt.show()

    return cur

def analytic():
    w, v = np.linalg.eig(matrix.transpose())
    end = v[:, 0] / v[:, 0].sum()
    print("Конечное состояние: ", end)
    return end

matrix = np.array([
    [0.6, 0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.6, 0.2, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.2, 0.0, 0.0, 0.2, 0.4, 0.2],
    [0.8, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0],
    [0.6, 0.0, 0.0, 0.0, 0.4, 0.0, 0.0, 0.0],
    [0.9, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0],
    [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
    [0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3],
])

eps = 1e-6
begin1 = np.array([.1, .0, .3, .2, .0, .1, .2, .1])
begin2 = np.array([.1, .4, .0, .1, .1, .1, .1, .1])

end1 = numeral(begin1)
end2 = numeral(begin2)
end3 = analytic()