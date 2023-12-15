# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()

day_one_deliveries = open("um-deliveries-day-1.txt")
day_two_deliveries = open("um-deliveries-day-2.txt")
day_three_deliveries = open("um-deliveries-day-3.txt")


def day_one(day_one_deliveries):
    for line in day_one_deliveries:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        
day_one(day_one_deliveries)

def day_two(day_two_deliveries):
    for line in day_two_deliveries:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        
day_two(day_two_deliveries)

def day_three(day_three_deliveries):
    for line in day_three_deliveries:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        
day_three(day_three_deliveries)

def day_three(day_three_deliveries):
    for line in day_three_deliveries:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

