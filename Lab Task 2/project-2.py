# Average of movies

old_data_set = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

user_data_set = []

user = input("Do you want to user your own dataset (yes,no) : ").strip().lower()

if user == 'yes':
    try : n = int(input("How many movies do you want to add : "))
    except : raise ValueError("Enter Numbers only")
    for i in range(n):
        movie_name = input("\nEnter Movie name : ")
        try : budget = int(input("Enter budget of movie in numbers : "))
        except : raise ValueError("Enter Numbers only")
        user_data_set.append((movie_name,budget))
    
movies = user_data_set if user_data_set else old_data_set

total_budget = 0
for i in movies:
    total_budget += i[1]

average_budget = total_budget / len(movies)

print("Average budget of moies is : ",average_budget)

print("\n","-"*20)
print("All movies are ")
for name , budget in movies:
    print(f"Movie name : {name} is having {budget}$ budget")

print("-"*20,"\n")


count_higer_avg = 0
max_movie_budget = 0
max_movie_name = ""
print("\n","-"*20)
print("Movies Above the budget are : ")
for name , budget in movies:
    if budget > average_budget:
        diffrence = budget - average_budget
        print(f"Movie : {name} is above over average budget by {diffrence}$")
        count_higer_avg +=1
    if budget > max_movie_budget:
        max_movie_budget = budget
        max_movie_name = name

print(f"\nNumber of total movies above the average is {count_higer_avg}")
print(f"Movie : {max_movie_name} have the highest bidget of {max_movie_budget}$")




