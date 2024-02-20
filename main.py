def sort(width, height, length, mass):
    volume = width * height * length
    
    if volume >= 1000000 or max(width, height, length) >= 150:
        if mass >= 20:
            return "REJECTED"
        else:
            return "SPECIAL"
    elif mass >= 20:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example usage:
result = sort(10, 20, 30, 15)  # Assuming dimensions in cm and mass in kg
print(result)  # Output: "STANDARD"
