playlist = [
    "Aethu Kari Raavilum", 
    "Pularikalo", 
    "Aaraadhike", 
    "Puthiyoru Pathayil", 
    "Cherathukal", 
    "Nenjodu Cherthu", 
    "Vaathil Melle"
]
print(playlist)
for i in range(-1,-4,-1):
    last3 = playlist.pop(i)
    playlist.insert(0,last3)
# playlist.insert(0,playlist[-3:])
print("Updated playlist: ",playlist)