music = {"Rahul", "Anjali", "Siddharth", "Meera"}
dance = {"Siddharth", "Meera", "Arjun", "Kavya"}
recitation = {"Meera","Rahul", "Kavya", "Vishnu", "Parvathy"}
print("Music: ",music)
print("Dance: ",dance)
print("Recitation: ",recitation)
print("Student(s) participating for all 3 events: ",music.intersection(dance.intersection(recitation)))