import kociemba

def Up():
    return [["U"]*3 for i in range(3)]

def Down():
    return [["D"]*3 for i in range(3)]
def Left():
    return [["L"]*3 for i in range(3)]

def Front():
    return [["F"]*3 for i in range(3)]
def Right():
    return [["R"]*3 for i in range(3)]
def Back():
    return [["B"]*3 for i in range(3)]
def solving(puzzel):
    try:
        return kociemba.solve(puzzel)
    except:
        return "Wrong Move! Try Again."