interview = [["I1",8,12],["I2",11,14],["I3",9,10],["I4",10,12],["I6",15,16],["I5",11,13]]

def select_interiver(interview):
    interview.sort(key = lambda x: x[2])
    end = 0
    selected = []

    for i in range(len(interview)):
        if interview[i][1] >= end:
            selected.append(interview[i])
            end = interview[i][2]
    return selected

print(select_interiver(interview))