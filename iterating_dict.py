## Iterate over the dictionary created in Assignment 1 and print each key-value pair.
d1={i:i**2 for i in range(1,11)}
for key,values in d1.items():
    print(f"{key}:{values}")