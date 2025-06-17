import csv
movie = [["top gun","Risky Business","Minority Report"],["titanic","The Revenant","Training Day","Man on Fire","Flight"]]

with open("movie.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    for movie_list in movie:
        w.writerow(movie_list)
