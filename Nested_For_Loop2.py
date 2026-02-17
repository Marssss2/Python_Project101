colors = [
    "Red", "Blue", "Green", "Yellow", "Orange",
    "Purple", "Pink", "Brown", "Black", "White",
    "Gray", "Cyan", "Magenta", "Lime", "Maroon",
    "Navy", "Olive", "Teal", "Silver", "Gold"
]
sizes = [
    "XS", "S", "M", "L", "XL",
    "XXL", "XXXL", "4XL", "5XL", "6XL",
    "Small", "Medium", "Large", "Extra Large", "Extra Small",
    "One Size", "Tiny", "Mini", "Maxi", "Jumbo"
]
for color in colors:
    for size in sizes:
        print(f'{color} -Size {size}')