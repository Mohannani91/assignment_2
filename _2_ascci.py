asciidict= dict()
alfapetTeller = range(97,123)
for i in alfapetTeller:
    asciidict[str(i)] = chr(i)
def get_swap_dict(d):
    return {v: k for k, v in asciidict.items()}
d_swap = get_swap_dict(asciidict)
print(d_swap)