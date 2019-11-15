import random

movie_list = []

print("Press ctrl-c once finished entering movies")

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

input("Press Enter to see results")
print("\n--------------------------------------\n")

# Select an item from movie_list at random
print("Bucket: ", movie_list)
print("Winner: " + (random.choice(movie_list)))
  