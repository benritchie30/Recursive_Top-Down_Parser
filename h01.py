import sys


def tokenizer(inpt):
    inpt = inpt.splitlines()
    nums = inpt[0].split()
    num_nonterm = int(nums[0])
    num_terms = int(nums[1])
    num_productions = int(inpt[int(num_nonterm + num_terms + 1)])
    terminals = inpt[1:num_nonterm+1]
    non_terminals = inpt[num_nonterm+1:num_nonterm+num_terms+1]
    productions = {x: [] for x in terminals}
    for i in range(num_nonterm+num_terms + 2, num_nonterm+num_terms + 2 + num_productions * 2, 2):
        productions[inpt[i]].append(inpt[i+1])

    return terminals, non_terminals, productions


def parser(curr, i):
    ret = False
    if i >= len(curr) or i >= len(target):
        return False

    is_nt, end_nt = is_nonterminal(curr, i)

    if curr[i] == target[i] and not is_nt:
        if i == len(target) - 1 and curr == target:
            return True
        ret = parser(curr, i+1)

    if is_nt:
        for p in productions[curr[i:end_nt]]:
            new_curr = curr[:i] + p + curr[end_nt:]
            ret = parser(new_curr, i)
            if ret:
                break
    return ret


def is_nonterminal(curr, i):
    if len(curr) == 1:
        return curr in non_terminals, 1
    if i != 0:
        if curr[i-1] != " ":
            return False, 1
    if i == len(curr) - 1:
        return curr[i:] in non_terminals, i+1
    count = i
    while curr[count] != " " and count < len(curr) - 1:
        count += 1
    return curr[i:count] in non_terminals, count


def main():
    g = "grammar-grm"
    if g[0] == '\'' and g[-1] == '\'' or g[0] == '\"' and g[-1] == '\"':
        print("ahh")
        g = g[1:-1]

    print(g)
    # grammar = open(g).read()
    # global terminals
    # global non_terminals
    # global productions
    # global target
    # target = open(t).read().split()
    # target = " ".join(target)
    # non_terminals, terminals, productions = tokenizer(grammar)
    #
    # if parser(non_terminals[0], 0):
    #     print("string is valid\n")
    # else:
    #     print("string is invalid\n")


if __name__ == '__main__':
    main()
