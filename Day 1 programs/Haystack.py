def find_needle(haystack, needle):
    return haystack.find(needle)
haystack = "hello world"
needle = "world"
index = find_needle(haystack, needle)
print(f"The index of '{needle}' in '{haystack}' is: {index}")
