generic_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

fourth_item_message = ' is the fourth item in the list, indexed at three:'

print(f"{generic_list[3].title()} is the fourth item in the list, indexed at three.\n")

print(f"{generic_list[-1].title()} is the last item in the list, indexed at 9.\n")

generic_list[0] = "1st"

print(f"{generic_list[0].title()} is the first item in the list, indexed at zero.\n")

generic_list.append('eleventh')

print(generic_list)

generic_list.insert(2, '1.5')

print(f"{generic_list[2]} is the third item in the list, indexed at two. {generic_list[3]} has moved to index 3.")

del generic_list[2]
print(generic_list)

popped_glist = generic_list.pop()

print("Popped:", popped_glist, "\ngeneric_list result:", generic_list)

print(f"Pop out that {generic_list.pop(1)}. Resultng list: {generic_list}")

to_be_removed = 'fifth'

generic_list.remove(to_be_removed)

print("generic_list with fifth removed", generic_list)






