def gauss_seidel(iterations):
    a0, a1, a2 = 0.0, 0.0, 0.0
    for i in range(1, iterations + 1):
        a0 = (485 - 25 * a1 - 135 * a2) / 5
        a1 = (2785 - 25 * a0 - 775 * a2) / 135
        a2 = (16751 - 135 * a0 - 775 * a1) / 4659
        print(f"Iterasi {i}: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}")

gauss_seidel(2)
