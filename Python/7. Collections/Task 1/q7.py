def movie_library(movies):
    count = 0
    for i in movies:
        if i[0]=="A":
            count+=1
    print("Movies starting with A: ",count)
    movies[0] = "Baby's Day Out"
    print("After updation: ",movies)
    movies.sort(reverse=True)
    print("After reversal: ",movies)
    
n = int(input("Enter the number of movies: "))
movies = []
for i in range(n):
    movies.append(input("Enter the movie name: "))
movie_library(movies)