import datetime

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] + [20] * 90


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -9999
    for i in range(1, n + 1):
        q = max(q, p[i-1] + cut_rod((p, n-1)))
    return q


start_t = datetime.datetime.now()
cut_rod(p, 25)
print(f"소요시간: {datetime.datetime.now() - start_t}")

start_t = datetime.datetime.now()
cut_rod(p, 26)
print(f"소요시간: {datetime.datetime.now() - start_t}")










def cut_rod(p, n):
    r = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = -9999
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]
