names = [
    "Ava", None, "Olivia", "Emma", None, "Sophia", "Isabella", None, "Mia", "Amelia",
    None, "Harper", "Evelyn", "Abigail", None, "Emily", "Ella", None, "Elizabeth", "Camila",
    "Luna", None, "Sofia", "Avery", None, "Mila", "Aria", None, "Scarlett", "Penelope",
    None, "Layla", "Chloe", None, "Victoria", "Madison", None, "Eleanor", "Grace", None,
    "Nora", "Riley", None, "Zoey", "Hannah", None, "Hazel", "Lily", None, "Ellie",
    "Violet", None, "Lillian", "Zoe", None, "Stella", "Aurora", None, "Natalie", "Emilia",
    None, "Everly", "Leah", None, "Aubrey", "Willow", None, "Addison", "Lucy", None,
    "Audrey", "Bella", None, "Nova", "Brooklyn", None, "Paisley", "Savannah", None, "Claire",
    "Skylar", None, "Isla", "Genesis", None, "Naomi", "Elena", None, "Caroline", "Eliana",
    None, "Anna", "Maya", None, "Valentina", "Ruby", None, "Kennedy", "Ivy", None
]

for name in names:
    if name == None:
        print('Found a Missing Name!')
        break
else:
    print('All Names are Available')