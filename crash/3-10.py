generic_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

print(f"{generic_list[3].title()} is the fourth item in the list, indexed at three.\n")

print(f"{generic_list[-1].title()} is the last item in the list, indexed at 9.\n")

generic_list[0] = "1st"

print(f"{generic_list[0].title()} is the first item in the list, indexed at zero.\n")

generic_list.append('eleventh')

print("\nAppended 'eleventh': ", generic_list)

generic_list.insert(2, '1.5')

print(f"\n{generic_list[2]} should be '1.5' and is the third item in the list, indexed at two. {generic_list[3]} has moved to index 3.")

del generic_list[2]
print("\n 1.5 has been deleted from the list: ", generic_list)

popped_glist = generic_list.pop()

print("\nPopped:", popped_glist, "\ngeneric_list result:", generic_list)

print(f"\nPop out that {generic_list.pop(1)}. Resultng list: {generic_list}")

to_be_removed = 'fifth'

generic_list.remove(to_be_removed)

print("\ngeneric_list with fifth removed", generic_list)

print("\nalphabetically sorted list:", sorted(generic_list))

print("\noriginal list: ", generic_list)

generic_list.reverse()
print("\noriginal list reversed", generic_list)

generic_list.sort()
print("\nalphabetically sorted, permanently: ", generic_list)

generic_list.sort(reverse=1)
print("\nreverse alphabetically sorted in reverse: ", generic_list)

print("\nlength of list after all is said and done: ", len(generic_list))
