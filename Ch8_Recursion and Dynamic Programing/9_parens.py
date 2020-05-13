
def parens(n, sol):
    if n == 1:
        return ["()"]

    else:
        # sol.append(parens(n-1, sol))
        # return "()"+sol
        for j in range(len(sol)):
            part = ["()"+sol[j], "("+sol[j]+")", sol[j]+"()"]
            new.append(part)
        return parens(n-1, new)

n = 1
new = []
print(parens(n, []))
