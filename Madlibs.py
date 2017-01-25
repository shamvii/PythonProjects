#Mad Libs are stories with blank spaces that a reader can fill in with their own words.
print "Hey there! The program is running"
character_name = raw_input("Please give a character name!")
adjective1 = raw_input("Please enter adjective 1!")
adjective2 = raw_input("Please enter adjective 2!")
adjective3 = raw_input("Please enter adjective 3!")
verb1 = raw_input("Please enter verb 1!")
verb2 = raw_input("Please enter verb 2!")
verb3 = raw_input("Please enter verb 3!")
noun1 = raw_input("Please enter noun 1!")
noun2 = raw_input("Please enter noun 2!")
noun3 = raw_input("Please enter noun 3!")
noun4 = raw_input("Please enter noun 4!")
animal = raw_input("Please enter an animal name!")
food = raw_input("Please enter a food!")
fruit = raw_input("Please enter any fruit name!")
number = raw_input("Please enter any number!")
superhero_name = raw_input("Please enter a superhero name!")
country = raw_input("Please enter a country name!")
dessert = raw_input("Please enter a dessert name!")
year = raw_input("Please enter any year!")






#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (adjective1, character_name, verb1, adjective2, noun1, noun2, animal, food, verb2, noun3, fruit, adjective3, character_name, verb3, number, character_name, superhero_name, superhero_name, character_name, country, character_name, dessert, character_name, year, noun4)
print(STORY)