T = int(input())

results = []


def biggest_multiple(multiple_of, biggest):
    rest = biggest % multiple_of
    return biggest - rest


for t in range(1, T + 1):
    line1 = input().split()
    N, D = [int(x) for x in line1]

    line2 = input().split()
    xes = [int(x) for x in line2]

    biggest = float("inf")
    for i in range(0, len(xes)):
        if i == 0:
            biggest = biggest_multiple(xes[i], D)
            print(f"i={i}, set initial biggest to {biggest}")
        if i != 0:
            biggest_candidate = biggest_multiple(xes[i], D)
            times = 0
            while biggest_candidate > biggest:
                print(
                    f"i={i}, biggest candidate {biggest_candidate} > {biggest}, calculating new..."
                )
                times += 1
                biggest_candidate -= xes[i]
                print(f"i={i}new biggest candidate is {biggest_candidate}")
            biggest = biggest_candidate
            print(f"i={i}, set biggest to {biggest}")

    print(biggest)

    # latests = []
    # for index, mults_of_x in reversed(list(enumerate(mults))):
    #     i = -1
    #     latest = mults_of_x[i]

    #     while latests and latest > latests[-1]:
    #         i -= 1
    #         latest = mults_of_x[i]

    #     latests.append(latest)

    # ans = latests[-1]
    # results.append("Case #" + str(t) + ": " + str(ans))

for res in results:
    # print(res)
    pass
