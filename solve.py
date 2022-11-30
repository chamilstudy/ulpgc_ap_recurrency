#t(p,q) = max(t(p+1,q),SUM^q-1_k=p (t(p,k) + t(k+1,q)))

# Resuelve aqui el ejercicio
mem = {}

def getKey(p,q):
    return str(p) + '|' + str(q)

def solve(p, q):
    key = getKey(p,q)

    if key not in mem:
        if p == q:
            return 1
            
        sum = 0
        for k in range(p, q):
            sum += solve(p,k) + solve(k+1,q)

        mem[key] = max(solve(p+1,q), sum)
        return mem[key]
    else:
        return mem[key]