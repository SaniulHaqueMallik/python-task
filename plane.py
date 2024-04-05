def minimum_planes_needed(planes):
    if not planes:
        return -1
    
    n = len(planes)
    planes_needed = 0
    current_fuel = planes[0]
    max_reachable = planes[0]
    
    for i in range(1, n):
        max_reachable = max(max_reachable, i + planes[i])
        
        if i > current_fuel:
            current_fuel = max_reachable
            planes_needed += 1
        
    if current_fuel >= n - 1:
        return planes_needed
    else:
        return -1

# Example usage
planes = [2, 1, 2, 3, 1]
print(minimum_planes_needed(planes))  # Output: 2
