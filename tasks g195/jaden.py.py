def to_jaden_case(string):
    w = string.split()
    return ' '.join(z.capitalize() for z in w)
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
