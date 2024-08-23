"""Python Collections."""

# print("gg" in "eggs")

lists = [[]] * 3
# print(lists)

# What has happened is that [[]] is a one-element list containing an empty list,
# so all three elements of [[]] * 3 are references to this single empty list.
lists[0].append(8)
# print(lists)

# strings
string1 = "Kyalo"
string2 = "monk"
# print(",".join("4321"))

# hash()
print(hash("demo"))
