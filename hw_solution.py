"""This method is able to use one function by taking in to parameters instead of one"""

def melon_count(day_number, path):
    """Given day number & path to the deliveries, produce report.

    Opens the deliveries file at [path], processes each line,
    and generates report in all uppercase.
    """

    print("Day", day_number)
    
    # Create a file object from the string passed in as path
    delivery_log = open(path)
    
    # Iterate over each line in the file object
    for line in delivery_log: 
        line = line.rstrip()  # Remove extra whitespace to the right of the line
        words = line.split('|')  # Create a list of strings
        
        # Assign a meaningful variable name to each item from the words list
        melon = words[0]
        count = words[1]
        amount = words[2]

        # Or you could do this with "list unpacking":
        #
        # melon, count, amount = words

        # Display information 
        print(f"Delivered {count} {melon}s for total of ${amount}")

    delivery_log.close()

# Function calls for existing reports
melon_count(1, "um-deliveries-day-1.txt")
melon_count(2, "um-deliveries-day-2.txt")
melon_count(3, "um-deliveries-day-3.txt")