score = int(input("Enter your score: "))
submitted = input("Did you submit your assignment? (yes/no): ").lower()

if score >= 90:
    print('High score!')
else:
    print('Low score!')
    
if submitted == 'yes':
    print('Assignment submitted.')  
else:
    print('Assignment not submitted.')