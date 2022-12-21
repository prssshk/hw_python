from scipy.stats import norm

for a, b in [(0.1, 0.9), (0.05, 0.95), (0.01, 0.99)]:
    t_a = norm.ppf(a, loc=0, scale=1)
    t_b = norm.ppf(b, loc=0, scale=1)
    print(t_a, t_b)
