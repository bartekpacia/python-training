T = int(input())

results = []


def generate_mults_mult_lower_than(x, D):
    mults = []
    m = 0
    while m <= D:
        mults.append(m)
        m += x

    return mults


for t in range(1, T + 1):
    line1 = input().split()
    N, D = [int(x) for x in line1]

    line2 = input().split()
    xes = [int(x) for x in line2]

    mults = []
    for index, x in enumerate(xes):
        mults_of_x = generate_mults_mult_lower_than(x, D)

        mults.append(mults_of_x)

    latests = []
    for index, mults_of_x in reversed(list(enumerate(mults))):
        i = -1
        latest = mults_of_x[i]

        while latests and latest > latests[-1]:
            i -= 1
            latest = mults_of_x[i]

        latests.append(latest)

    ans = latests[-1]
    results.append("Case #" + str(t) + ": " + str(ans))

for res in results:
    print(res)
