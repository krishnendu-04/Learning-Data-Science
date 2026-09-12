ratings = [4.5, 3.0, 5.0, 2.5, 4.0, 3.5, 1.5, 4.8]
print(ratings)
for i in range(len(ratings)):
    if ratings[i]<3:
        ratings[i] = 3
print("Updated ratings: ",ratings)