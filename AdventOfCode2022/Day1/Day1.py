class Elf:
    def __init__(self, text):
        split = text.split('\n')
        self.calories = sum([int(i.strip()) for  i in split])

def maximums(items, number_of_maximums):
    maximum = []
    while len(maximum) < number_of_maximums:
        indices = [index for index, item in enumerate(items) if item == max(items)]
        for i in indices:
            maximum.append(items[i])
        for i in indices:
            items.pop(i)
    return maximum[:number_of_maximums]
                        

elves = []
with open("Day1-input.txt",'r') as fp:
    text = fp.read()
    for i in text.split('\n\n'):
        elf = Elf(i)
        elves.append(elf.calories)

print("part 1 answer:")
print(max([i for i in elves]))

print("\npart 2 answer:")
maximum_list = maximums(elves,3)
print(sum(maximum_list))
