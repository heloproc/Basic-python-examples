def print_nested_elements(nested_list):
  """Prints each element in a nested list, handling mixed data types."""
  for element in nested_list:
    if isinstance(element, list):  # Check if the element is a list
      for subelement in element:
        print(subelement)
    else:
      print(element)  # Print the element if it's not a list

# Example mixed nested list
nested_list = [1,2, 4, [5, 7]]

# Print each element
print_nested_elements(nested_list)