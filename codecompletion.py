def sort_by_key(list_of_dicts, key, reverse=False):
    """
    Sort a list of dictionaries by a specific key.
    
    Args:
        list_of_dicts: List of dictionaries to sort
        key: The dictionary key to sort by
        reverse: If True, sort in descending order
    
    Returns:
        Sorted list of dictionaries
    """
    return sorted(list_of_dicts, key=lambda x: x.get(key), reverse=reverse)

# Example usage
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_data = sort_by_key(data, "age")
print(sorted_data)