safe_count = 0
unsafe_count = 0

with open('input.txt', 'r') as file:
    input_arrays = file.readlines()

for line in input_arrays:
    line = line.strip()
    if not line:  # Skip empty lines
        continue
        
    items = [int(x) for x in line.split()]
    if len(items) < 2:
        continue

    # Check if sequence is ascending or descending
    is_ascending = items[0] < items[1]
    is_valid = True

    # Check each adjacent pair
    for i in range(len(items) - 1):
        diff = items[i + 1] - items[i]
        
        if is_ascending:
            if not (0 < diff <= 3):
                is_valid = False
                break
        else:
            if not (-3 <= diff < 0):
                is_valid = False
                break

    if is_valid:
        safe_count += 1
        
print(safe_count)
            

        

        
