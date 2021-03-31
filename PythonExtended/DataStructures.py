#region Sorting
#TODO - sorting functions
#endregion

#region Lists
#endregion

#region Dicts
def Map(a, b):
    """New dict with the values of a and b mapped together using the keys"""
    out = {}
    for key, value in a.items():
        if key in b:
            out[value] = b[key]
    return out

def strip(a, b):
    """Removes keys not in b from a"""
    out = {}
    for key, value in a.items():
        if key in b:
            out[key] = value
    return out
#endregion