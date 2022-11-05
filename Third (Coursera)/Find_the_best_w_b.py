import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.5, 3.3, 4.0])
y_train = np.array([300.0, 400.0, 770.0, 850.0])


def compute_cost(x_inner, y_inner, w_inner, b_inner):
    # number of training examples
    m_inner = x_inner.shape[0]

    cost_sum = 0
    for i_inner in range(m_inner):
        f_wb_inner = w_inner * x_inner[i_inner] + b_inner
        cost = (f_wb_inner - y_inner[i_inner]) ** 2
        cost_sum = cost_sum + cost
    total_cost = (1 / (2 * m_inner)) * cost_sum

    return total_cost


def find_best_b(w_lowest_in_func):
    w_lowest_in_func = w_lowest_in_func
    b_lowest = 0
    j_value = compute_cost(x_train, y_train, w_lowest_in_func, b_lowest)
    if j_value > compute_cost(x_train, y_train, w_lowest_in_func, b_lowest - 1):
        b_lowest = b_lowest - 1
        b_temp = b_lowest
        while compute_cost(x_train, y_train, w_lowest_in_func, b_temp) <= compute_cost(x_train, y_train,
                                                                                       w_lowest_in_func, b_lowest):
            b_lowest = b_temp
            b_temp = b_temp - 1
    else:
        b_lowest = b_lowest + 1
        b_temp = b_lowest
        while compute_cost(x_train, y_train, w_lowest_in_func, b_temp) <= compute_cost(x_train, y_train,
                                                                                       w_lowest_in_func, b_lowest):
            b_lowest = b_temp
            b_temp = b_temp + 1
    print(b_lowest)
    return b_lowest


def find_best_w():
    w_lowest_in_func = 0
    j_value = compute_cost(x_train, y_train, w_lowest_in_func, find_best_b(w_lowest_in_func))
    if j_value > compute_cost(x_train, y_train, w_lowest_in_func - 1, find_best_b(w_lowest_in_func - 1)):
        w_lowest_in_func = w_lowest_in_func - 1
        while compute_cost(x_train, y_train, w_lowest_in_func, find_best_b(w_lowest_in_func)) > compute_cost(x_train, y_train, w_lowest_in_func - 1, find_best_b(w_lowest_in_func - 1)):
            w_lowest_in_func = w_lowest_in_func - 1
    else:
        w_lowest_in_func = w_lowest_in_func + 1
        while compute_cost(x_train, y_train, w_lowest_in_func, find_best_b(w_lowest_in_func)) > compute_cost(x_train, y_train, w_lowest_in_func + 1, find_best_b(w_lowest_in_func + 1)):
            w_lowest_in_func = w_lowest_in_func + 1
    return w_lowest_in_func


w_lowest = find_best_w()
m = x_train.shape[0]
f_wb = np.zeros(m)
for i in range(m):
    f_wb[i] = w_lowest * x_train[i] + find_best_b(w_lowest)

# Plot our model prediction
plt.plot(x_train, f_wb, c='b', label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')

plt.show()

# Holly shit I made this and it works
