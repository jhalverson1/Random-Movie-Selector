import random

movie_list = []

# ------------Functions------------
def EnterMovies():
  try:
  
    while True:
      movie = input("\nEnter a Movie: ")
      try:
        weight = int(input("Weight of the movie? "))
      except:
        print("You have entered an invalid value")
      movie_list.extend([movie] * weight)

  except KeyboardInterrupt:
    print("\n")
    pass

# ------------SCRIPT------------
print("Press ctrl-c once finished entering movies")

EnterMovies()

input("Press Enter to see results")
print("\n--------------------------------------\n")

# Select an item from movie_list at random
print("Bucket: ", movie_list)
print("Winner: " + (random.choice(movie_list)))
  