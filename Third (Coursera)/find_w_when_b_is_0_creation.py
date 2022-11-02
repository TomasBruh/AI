import numpy as np

x_train = np.array([1.0, 2.0, 3.0, 4.0])
y_train = np.array([200.0, 300.0, 700.0, 800.0])
b = 0


def compute_model_output_test(x_inner, w_inner, b_inner, i_inner):
    answer_return = w_inner * x_inner[i_inner] + b_inner
    return answer_return


# (y^-y)2 = (y^-y)*(y^-y)
def function(x_inner):
    w = x_inner
    big_j = 0
    for i in range(x_train.shape[0]):
        y_thing = y_train[i]
        y_hat_thing = compute_model_output_test(x_train, w, b, i)
        thing = (y_hat_thing - y_thing)
        big_j = big_j + thing
        return big_j


not_smallest_it_can_be = True
x = 0
while not_smallest_it_can_be:
    x = x+1
    answer = function(x)
    if answer == 0:
        not_smallest_it_can_be = False