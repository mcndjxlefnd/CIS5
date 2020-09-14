guests = ["Nikos & Liz", "Eden & Nikki", "Scottie & Jene", "Nate", "Matthew"]
invitation = f"{guests[0]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[1]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[2]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[3]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[4]}, you are cordially invited to a dinner party at my home."
print(invitation)

print(f"\n{guests [4]} can't make it for dinner")
del guests[4]
guests.append("Rod")

print("\n")
invitation = f"{guests[0]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[1]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[2]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[3]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[4]}, you are cordially invited to a dinner party at my home."
print(invitation)

print("\nHazah! I have found a bigger dinner table and can accommodate more guests!")
guests.insert(0, "Josh")
guests.insert(2, "Shyla")
guests.append("Alexis")

print("\n")
invitation = f"{guests[0]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[1]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[2]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[3]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[4]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[5]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[6]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[7]}, you are cordially invited to a dinner party at my home."
print(invitation)

print("\nMy apologies! I was mistaken, and can only invite two guests to the party :(")
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

invitation = f"\n{guests[0]}, you are cordially invited to a dinner party at my home."
print(invitation)
invitation = f"\n{guests[1]}, you are cordially invited to a dinner party at my home."
print(invitation)

del guests[1], guests[0]
print("\n", guests)
