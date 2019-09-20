def simpl1(clause):
    positive_atoms = clause[0]
    i = len(positive_atoms)
    positive_res = []
    for x in range(0,i):
        to_add = True
        for y in range(x+1,i):
            if(positive_atoms[x]==positive_atoms[y]):
                to_add = False
        if(to_add):
            positive_res.append(positive_atoms[x])
    return (positive_res,clause[1])               





clause1 = (["A","A"],[])
clause2 = (["A","B","C","A"],[])
clause3 = ([],[])
clause4 = (["A","A","A"],[])




print(simpl1(clause1))

print(simpl1(clause2))

print(simpl1(clause3))

print(simpl1(clause4))





def simpl2(clause):
    negative_atoms = clause[1]
    i = len(negative_atoms)
    negative_res = []
    for x in range(0,i):
        to_add = True
        for y in range(x+1,i):
            if(negative_atoms[x]==negative_atoms[y]):
                to_add = False
        if(to_add):
            negative_res.append(negative_atoms[x])
    return (clause[0], negative_res)  





clause1 = ([],["A","A"])
clause2 = ([],["A","B","C","A"])
clause3 = ([],[])
clause4 = ([],["A","A","A"])





print(simpl2(clause1))

print(simpl2(clause2))

print(simpl2(clause3))

print(simpl2(clause4))





def resolution_check(clause1, clause2):
    combined = False
    #positive of clause1 & negative of clause2
    pos_atoms1 = clause1[0]
    neg_atoms2 = clause2[1]
    for x in pos_atoms1:
        for y in neg_atoms2:
            if(x==y):
                combined = True
    #positive of clause2 & negative of clause1
    pos_atoms2 = clause2[0]
    neg_atoms1 = clause1[1]
    for x in pos_atoms2:
        for y in neg_atoms1:
            if(x==y):
                combined = True
    return combined





def universal(clause):
    pos_atoms = clause[0]
    neg_atoms = clause[1]
    pos_res = []
    neg_res = []
    for x in pos_atoms:
        if(x not in neg_atoms):
            pos_res.append(x)
    for y in neg_atoms:
        if(y not in pos_atoms):
            neg_res.append(y)
    return (pos_res,neg_res)



print(universal((["A","B","c"],["D","c"])))





def resolution(clause1,clause2):
    pos_res = clause1[0]+clause2[0]
    neg_res = clause1[1]+clause2[1]
    clause = (pos_res, neg_res)
    clause = simpl1(clause)
    clause = simpl2(clause)
    clause = universal(clause)
    return clause





clause1 = (["A"],[])
clause2 = ([],["A"])
clause3 = ([],["B"])
clause4 = (["A","B"],[])
clause5 = ([],["A","B"])
clause6 = (["B"],["C"])
clause7 = (["C"],[])
clause8 = (["C"],["A","B"])
clause9 = (["B"],["A"])
clause10 = ([],["C"])
clause11 = (["A","A","B"],[])
clause12 = ([],["A","A"])
clause13 = ([],["B","B"])
clause14 = (["C"],["C"])





print(resolution(clause1,clause2))

print(resolution(clause3,clause4))

print(resolution(clause1,clause5))

print(resolution(clause6,clause7))

print(resolution(clause8,clause10))

print(resolution(clause9,clause1))

print(resolution(clause4,clause2))




def satisfiable(clause):
    pos_atoms = clause[0]
    neg_atoms = clause[1]
    for x in pos_atoms:
        if(x in neg_atoms):
            return True
    return False


def search_solution(clauses):
    for x in clauses:
        if(satisfiable(x)):
            clauses.remove(x)
    if(len(clauses)!=0):
        cur_clause = clauses[0]
        for x in clauses[1:]:
            if(resolution_check(cur_clause,x)):
                clauses.remove(cur_clause)
                clauses.remove(x)
                cur_clause = resolution(cur_clause,x)
                if(cur_clause==([],[])):
                    print("Unsatisfiable")
                else:
                    clauses.append(cur_clause)
                    return search_solution(clauses)



clause15 = (["B"],[])
clause16 = (["C"],["A"])

print(search_solution([clause10,clause14]))

print(search_solution([clause4,clause9]))

print(search_solution([clause1,clause3]))

print(search_solution([clause11,clause12,clause13,clause14]))

print(search_solution([clause8,clause9,clause1,clause10]))

print(search_solution([clause1,clause5,clause6,clause7]))

print(search_solution([clause2,clause3,clause4]))

print(search_solution([clause1,clause2]))

print(search_solution([clause14]))

print(search_solution([clause8,clause16,clause1,clause15]))


