def solution(number):
    n_3 = (number - 1) // 3
    n_5 = (number - 1) // 5
    n_15 = (number - 1) // 15

    n_3_sum = (n_3 * (n_3 + 1) // 2) * 3
    n_5_sum = (n_5 * (n_5 + 1) // 2) * 5
    n_15_sum = (n_15 * (n_15 + 1) // 2) * 15

    return n_3_sum + n_5_sum - n_15_sum