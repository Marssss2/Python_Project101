def clean_name(name):
    up_clean = name.strip().upper()
    down_clean = name.strip().lower()
    return up_clean,down_clean

up_clean,down_clean = clean_name('  Angelo')
print(up_clean, down_clean) 

print(up_clean)
print(down_clean)