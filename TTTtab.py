case=["1","2","3","4","5","6","7","8","9"]
def tab(case):
    espace="|         |         |         |"
    ligne="+---------+---------+---------+"
    print(ligne)
    for i in range(0,7,3):
        print(espace)
        print(f"|    {case[i]}    |    {case[i+1]}    |    {case[i+2]}    |")
        print(espace)
        print(ligne)
tab(case)
