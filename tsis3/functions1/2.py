def to_Cel(gradus):
    Cgradus = (5/9 * (gradus - 32))
    return Cgradus
print(to_Cel(int(input())))