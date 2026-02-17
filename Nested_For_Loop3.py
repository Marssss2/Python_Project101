years = [
    2000, 2001, 2002, 2003, 2004,
    2005, 2010, 2015, 2018, 2019,
    2020, 2021, 2022, 2023, 2024,
    2025, 2026, 2027, 2030, 2035
]
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')