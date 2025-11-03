class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)



class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return
        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            friends_str = ", ".join(friend_names)
            print(f"{name} is friends with: {friends_str}")
    
# Testing Code 
if __name__ == "__main__":
    network = SocialNetwork()
    
    
    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    network.add_person("Alex") # To see if it will tell me he is already in the network 

    
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  # This should let me see if there is an error 
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()

#
# I think a graph is correct here because it's a model that shows how these people are connected. 
# Each person is a node, and every friendship is a two way connection. This allows you to easily see who is friends with who. 
# With a list you would just have group of people but no clear correlation.  
# With a Tree you would have some correlation but only from one person exending out, which would not fit the need for this assignment. 
#
#
# A list or a tree wouldn't work well here because a list could only store these people in order not showing who is friends with who
# It doesn't show how each node is connected. A tree wouldn't work because it wouldnt't show which friends are connected to who.
# A tree has a parent-child structure which doesn't show how friendships work because friendships are mutual and can connect
# in more ways that just one direction
#
# When adding friends, I noticed that checking if both people exist is important to avoid errors.
# Mistyping a name can create errors, leading you to think that person might not be added yet. 
# Adding a friendship is fast but printing the whole network takes longer if there are many people because
# we have to list all their friends. Using a dictionary for people helps find them quickly by name which is efficient.
