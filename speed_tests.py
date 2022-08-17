import timeit


def speed_contest(commands, globals, number=100):

    # commands = [
    #     [ 'sol.removeNthFromEnd(head,3)'],
    #     [ 'sol.secondsol(head, 3)']
    # ]

    commands = [[x] for x in commands]
    for com in commands:
        com.append(timeit.timeit(com[0], globals=globals, number=number))

    sres = sorted(commands, key=lambda i: i[1])
    for i, c in enumerate(sres):
        if i == 0: 
            msg = f"{i+1} -> {c[0]} \n\t {round(100*float(c[1])/float(sres[1][1]))}% of the second time"
            continue
        msg += f"\n{i+1} -> {c[0]} \n\t {round(c[1]/sres[0][1]*10)/10} times slower than the winner"

    print(msg)