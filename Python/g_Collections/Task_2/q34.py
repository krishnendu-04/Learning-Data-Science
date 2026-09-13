user1 = {"Song A", "Song B", "Song C"}
user2 = {"Song C", "Song D", "Song E"}
print(user1)
print(user2)
print("Unique songs: ",user1-user2,user2-user1)
print("Common songs: ",user1.intersection(user2))