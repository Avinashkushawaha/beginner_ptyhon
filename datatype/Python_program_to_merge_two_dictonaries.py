dict1 = {"john": 40, "peter": 45}
dict2 = {"john": 466, "peter": 45}

print(dict1 | dict2)

# Solution 2: Using ** Operator

dict1 = {"john": 40, "peter": 45}
dict2 = {"john": 466, "peter": 45}

print({**dict1, **dict2})

