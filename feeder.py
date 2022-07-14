#I'm here to calculate short-circuit current based on input short-circuit current as well as the properites of the feeder.

#The input should be a feeder object

class feeder:
    def __init__(self, N, mat, wire_size, len):
        self.sets = int(N)           #integer number of sets
        self.material = str(mat)     #"CU" or "AL" as a string
        self.size = str(wire_size)   #AWG wire size or kcmil as a string
        self.length = float(len)       #float measured in feet
    
    """ def __init__(self):
        self.sets = 1           #integer number of sets
        self.material = "AL"    #CU or AL as a string
        self.size = "10"        #AWG wire size or kcmil as a string
        self.length = 20        #measured in feet """


def outputISC(inputISC,ELL,feederA):
    
    AL600V_dictionary = {
        "14" : 237,
        "12" : 376,
        "10" : 599,
        "8" : 951,
        "6" : 1481,
        "4" : 2346,
        "3" : 2952,
        "2" : 3713,
        "1" : 4645,
        "1/0" : 5777,
        "2/0" : 7187,
        "3/0" : 8826,
        "4/0" : 10741,
        "250" : 12122,
        "300" : 13910,
        "350" : 15484,
        "400" : 16671,
        "500" : 18756,
        "600" : 20093,
        "750" : 21766,
        "1000" : 23478,
    }

    CU600V_dictionary = {
        "14" : 389,
        "12" : 617,
        "10" : 981,
        "8" : 1557,
        "6" : 2425,
        "4" : 3806,
        "3" : 4774,
        "2" : 5907,
        "1" : 7293,
        "1/0" : 8925,
        "2/0" : 10755,
        "3/0" : 12844,
        "4/0" : 15082,
        "250" : 16483,
        "300" : 18177,
        "350" : 19704,
        "400" : 20566,
        "500" : 22185,
        "600" : 22965,
        "750" : 24137,
        "1000" : 25278,
    }

    if feederA.material == "AL":
        C = AL600V_dictionary[feederA.size]
    elif feederA.material == "CU":
        C = CU600V_dictionary[feederA.size]

    I = inputISC
    L = feederA.length
    N = feederA.sets

    f = 1.732 * L * I / (C * N * ELL)
    M = float(1)/float(1.0 + f)
    #print(f"Size = {feederA.size}\nI = {I}\nL = {L}'\nN = {N}\nC = {C}\nf = {f}\nM = {M}")

    output = I * M
    return int(output)

""" fooder = feeder(1,"AL","400",175)

out = outputISC(26056,208,fooder)
print(out) """