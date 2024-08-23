""" Main file for the project."""

import sys


def main():
    print(sys.float_info)


def strings_demo():
    # Strings.
    name = "Kyalo Kitili"

    print(name[0:2000])
    # print(name[200]) can't index an out of bounds index.


def lists_demo():
    # Lists
    name = "Kyalo Kit"

    # a list can contain different data types.
    mixed_list = [
        "demo",
        1,
        2,
        name,
        3.4,
        5,
    ]
    
    mixed_list.append({"name": "Kyalo Kitili"})
    
    # slicing through lists
    list_copy = mixed_list[0:len(mixed_list)]
    list_copy.append(45)
    
    # shallow copy of a list
    print( list_copy)
    print(mixed_list)
    
    # list assignment never creates a copy.
    rgb = ["red", "green", "blue"]
    rgba = rgb
    rgba.append("alph")
    print(id(rgb) == id(rgba))
    
    # slice ops return a shallow copy
    correct_rgba = rgba[:]
    correct_rgba[-1] = "Alpha"
    print(correct_rgba)
    
    # assignment to slices
    correct_rgba[0:len(correct_rgba)] = [23,89,34,0.5]
    print(correct_rgba)
    
    # clear list
    correct_rgba[:] = []
    print(correct_rgba)

# control flow
def control_flow_demo():
    names = ["mary", "jane", "joe", "james", "john"]
    for name in names:
        print(name)
        
    # enumerate
    for i, name in enumerate(names):
        print(i, name)

    # range
    for i in range(len(names)):
        print(i, names[i])
        
    
if __name__ == "__main__":
    """
    Python idiom that is used to determine whether a Python script is 
    being run as the main program or being imported as a module into 
    another script.
    """
    # main()
    # strings_demo()
    # lists_demo()
    control_flow_demo()
    # pass
