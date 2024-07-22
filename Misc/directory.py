def main(): 

    rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 
             'NT110':1244, 'CM241':1411} 
 
    instructors = {'CS101':'Haynes', 'CS102':'Alvarado', 
                   'CS103':'Rich', 'NT110':'Burke', 
                   'CM241':'Lee'} 
 
    times = {'CS101':'8:00am', 'CS102':'9:00am', 
             'CS103':'10:00am', 'NT110':'11:00am', 
             'CM241':'1:00pm'} 
 
    course = input('Enter a class name:') 
 
    if course not in rooms: 
        print(course, 'is invalid.') 
    else: 
        print('Class:', course,) 
        print('Room:', rooms[course]) 
        print('Instructor:', instructors[course]) 
        print('Time:', times[course]) 
 

main()