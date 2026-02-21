students = [['Maria', 85],
            ['Kumar', 90],
            ["Max", 60],    
            ]

print(list(filter(lambda row: row[0].startswith('M'), students))) #it will print the list of students whose names start with 'M' which is [['Maria', 85], ['Max', 60]]