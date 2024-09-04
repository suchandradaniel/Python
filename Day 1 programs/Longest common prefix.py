strs = ["flower", "flow", "flight"]

if not strs:
    prefix = ""
else:
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                break

print(prefix)
