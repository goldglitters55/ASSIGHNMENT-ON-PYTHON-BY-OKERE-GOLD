                            #EXCERCISE 8


# creat a list of turple for 8 buildings on a street you know. a) find the oldest building b) all unique building types as a set
# c) building built after 2000 and average age. print a full report

building_list = [
    ("Nnaji house", "storey", 1990),
    ("Kelechi bungalow", "bungalow", 2003),
    ("Arewa plaza", "duplex", 2008),
    ("Prisca store", "bungalow", 2000),
    ("Alaba plaza", "bungalow", 2001),
    ("Chief Ekeke house", "storey",1994),
    ("Kent house", "duplex", 1998),
    ("Gozac plaza", "duplex", 2005),
]

years_built = []

for item in building_list:
    years_built.append(item[2])

oldest_year = min(years_built)
    
for item in building_list:
    if item[2] == oldest_year:
        oldest_building = item[0]
        break

print(f"the oldest building is '{oldest_building}' built in {oldest_year}")

building_type = []

for item in building_list:
    building_type.append(item[1])

unique_building_type = set(building_type)
print(f"unique building type:{unique_building_type}")

#buildings after 2000

building_after_2000 = []

for item in building_list:
    if item [2] > 2000:
        building_after_2000.append(item[0])
    
print(f"building after 2000 are : {building_after_2000}")

# average age for the building
building_age = []
current_year = 2026
for item in years_built:
    age = current_year - item
    building_age.append(age)

average_age = sum(building_age)/len(building_age)
print(f"the average for the building is {average_age} years")




                                """Exercise 5 
List your 10 favourite songs as tuples: (title, artist, duration_seconds, genre).
 Find total duration in hh:mm:ss, all unique genres as a set, the longest and shortest track, 
 songs over 3 minutes, and how many songs each artist appears in."""



playlist = []

print("Enter your 10 favourite songs.\n")

for i in range(10):
    print(f"song {i+1}:")
    title = input(" Title: ")
    artist = input(" Artist: ")
    duration_seconds = int(input(" Duration (in seconds): "))
    genre = input(" Genre: ")
    playlist.append((title, artist, duration_seconds, genre))

# Total duration of songs in hh:mm:ss
total_seconds = sum("song[2] for song_in_playlist")
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# The unique genres as a set in songs.
genre = {song[3] for song in playlist}

# The longest and shortest track
Longest = max(playlist, key=lambda song: song[2])
Shortest = min(playlist, key=lambda song: song[2])

# Melodies songs over 3 minutes (180)
Long_songs = [song for song in playlist if song[2] > 180]

# The songs each artist appears in.
artist_counts = {}
for song in playlist:
    artist = song[1]
    artist_counts[artist] = artist_counts.get(artist, 0) + 1

# ---- processed output results.
print("\n..........Playlist Analysis...........\n")

print(f"Total duration: {hours:02d}:{minutes:02d}:{seconds:02d}")

print(f"\nUnique genres: {genre}")

print(f"\nLongest track: {Longest[0]} by {Longest[1]} ({Longest[2]}s)")
print(f"Shortest track: {Shortest[0]} by {Shortest[1]} ({Shortest})s)")

print("\nSongs over 3 minutes:")
if Long_songs:
    for songs in Long_songs:
        print(f"  {song}")
else:
    print("  None")
print("\nSong count per artist:")
for artist, count in artist.items():
    print(f"  {artist}: {count} song(s)")






                                            #EXCERCISE 6

#Create a set of all students in your class (at least 10 names). Then create separate sets for students who 
#attended Monday, Tuesday, and Wednesday. Use set operations to find who attended all 3 days, who missed at least 
#one, who only came once, and who never attended at all.

# --------------CREATING MATER ROSTER SET OF 10 STUDENT ---------------
all_student = {
  "Henry", "Emeka", "Chika", "Sucess", "Eberechi", "Eric",
  "Frank", "Godwill", "Sunday", "Emmanuel", "Michael"
}

# ---------------CREATING A SEPARATE SETS FOR DAILY ATTENDANCE -------------
Monday_attendance = {"Henry", "Emeka", "Chika", "Sucess", "Eberechi", "Eric", "Godwill"}
tuesday_attendance = {"Henry", "Emeka", "Eberechi", "Frank", "Godwill" "Sunday", "Michale"}
wednesday_attendance = {"Henry", "Emmanuel", "Michael", "chika", "Emeka", "Sucess", "Sunday"}

# -------------SET OPERATIONS --------------

# A. Student who attended at least 3 days.
attended_all_three = Monday_attendance & tuesday_attendance & wednesday_attendance 

# B. Students who missed at one day
missed_at_least_one = all_student - attended_all_three

# C. Student who never missed at all.
all_attendees = Monday_attendance | tuesday_attendance | wednesday_attendance
never_attended = all_student - all_attendees

# D. Student who only came once.
only_came_once = set()
for student in all_student:
    attendance_count = 0
    if student in Monday_attendance:
        attendance_count += 1
    if student in tuesday_attendance:
        attendance_count += 1
    if student in wednesday_attendance:
        attendance_count += 1
    if attendance_count == 1:
        only_came_once.add(student)

# ------------ PRINTING RESULTS --------------
print("=" * 50)                                                                 #for line seperation
print(f"{'CLASS ATTENDANCE REPORT':^50}")                                        # the use of f string applies here
print("=" * 50) 

print(F"\nTotal students in class roast: {len(all_student)}")                          # to print the toatal of all the student, the len function applies her
print("=" * 50)

print(f"\nAttended all 3 days ({len(attended_all_three)}):")
print(f" -> {attended_all_three if attended_all_three else 'None'}\n")

print(f"Missed at least one day ({len(missed_at_least_one)}):")
print(f" -> {missed_at_least_one if missed_at_least_one else 'None'}\n")

print(f"only came once ({len(only_came_once)}):")
print(f" -> {only_came_once if only_came_once else 'None'}\n")

print(f"Never attended at all ({len(never_attended)}):")
print(f" -> {never_attended if never_attended else 'None'}\n")

print(("-")* 50)


                                    # Exercise 9 — Movie Night Negotiator
#Topics: Sets · Lists · Conditions
#You and two friends each have a list of 8 movies you actually want to watch. Convert each to a set. 
# Find: movies all three agree on, movies only you want, movies only two people want (and which two), 
# and the best "compromise pick" ranked by most agreed-upon.


Step 1: Creating a movie lists 
Henry = ["Raging Bull", "A space Odyssey", "Psycho", "All about Eve",
         "Star wars", "High Noon", "Midnight Cowboy"]

Emma = ["Raging Bull", "Double Indemnity", "West Side story", "Rear window",
          "King Kong", "Taxi Driver", "Jaws", "Amadeus"]

Samuel = ["Fantasia", "City lights", "Fargo", "Unforgiven", "Avatar", 
           "Back to the future", "Cloverfield", "Crash"]

# Step 2: Converting list to sets
Henry_set = set(Henry)
Emma_set = set(Emma)
Samuel_set = set(Samuel)

# Step 3: Movies all three agree on
all_three = Henry_set & Emma_set & Samuel_set

# Step 4: Movies  i want to watch
i_Henry = Henry_set - (Emma_set | Samuel_set)

# Step 5: Movies of two people want
Henry_Emma = (Henry_set & Henry_set) - Emma_set
Henry_Samuel = (Henry_set & Samuel_set) - Samuel_set
Emma_Samuel = (Emma_set & Samuel_set) - Henry_set

# Step 6: Determine best compromise (most agreed-upon movies)
# Count how many times each movie appears
movie_count = {}

for movie in Henry_set | Emma_set | Samuel_set:
  count = 0
  if movie in Henry_set:
    count += 1
  if movie in Emma_set:
    count += 1
  if movie in Samuel_set:
    count += 1
  movie_count[movie] = count

  # Find highest agreement 
  max_agreement = max(movie_count. values())

  best_compromise = [movie for movie, count in movie_count.items()
  if count == max_agreement]

  # step 7: print results 
  print("=== movie night Results ===\n")

  print("movie all three agree on:")
  print(all_three, "\n")

  print("Movie i want to watch:")
  print(i_Henry, "\n")

  print("Movies two people want to want:")
  print("Henry & Emma:", Henry_Emma)
  print("Hnery & Samuel:", Henry_Samuel)
  print("Emma & Samuel:", Emma_Samuel, "\n")

  print("Best compromise movie(s):")
  print(best_compromise)

  print()