def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height1))  # Output: 49

height2 = [1, 1]
print(max_area(height2))  # Output: 1

