#Eusi/lab 3/intro to python

#Ticket 1
username = "BroMeanie1995"
#predict: 13 characters
print(len(username))
#len() did indeed count every character

#Ticket 2
#predict: "B" and "5" will print
print(username[0])
print(username[12])
#indexes start at 0, so the first character has index 0 and the last one has index 12

#Ticket 3
#predict: unless I did something wrong, they should be identical...
welcome = "Welcome to Loop, "
welcome_banner = welcome + "@" + username + "!"
print (welcome_banner)
print (f"Welcome to Loop, @{username}!")
#using an f-string definitely was easier because I didn't have to create new variables

#Ticket 4
#predict: since username's 0 index is actually B, an error message will pop up that prolly says something like "wrong index found"
#username[0] = "X"
print(username.upper())
#TypeError: 'str' object does not support item assignment
#Immutable means that you can't change the value of a string after you make it



#Ticket 5
#predict: the count will print 3, and "Happy Father's Day..." will print first
feed = ["Happy Father's Day from a proud dad of 2!", "Can anyone recommend some effective arthritis cream?", "My boss personally hired me, but still won't give me any benefits."]
print(len(feed))
print(feed[0])
#I used index of 0 because indexes always start from 0

#Ticket 6
#predict: this post's index will be 3
feed.append("No, I will not reveal where I got my boots.") 
print(feed)
#index starts at 0, so the most recent entry's index will always be len -1

#Ticket 7
#predict:  "Happy Father's Day..." will get removed, while "Can anyone..." will now be first, "My boss..." will be second, and "No, I..." will be last
feed.pop(0)
feed.sort
print(feed)
#.pop(0) removed the post at index 0, and .sort sorted everything alphabetically by the first letter of the entry


#Ticket 8
#predict: 33550336 will print, profile[0] will crash bc dictionaries don't use indexes
profile = {"username": "BroMeanie1995", "followers": 33550336, "verified": True}
print(profile["followers"]) 
#profile[0]
#KeyError: 0
#dictionaries probably don't use indexes because the data isnt ordered in a sequence

#Ticket 9
#predict: It won't print anything
profile["followers"]= 33550336 + 50
profile["bio"] = "Comedian turned explorer turned chessmaster. AMA."
print(profile)
print(profile.get("age"))
#.get doesnt cause a crash

#Ticket 10
#predict: @BroMeanie has 33550386 followers and 3 posts. Top post: Can anyone recommend some effective arthritis cream? 
print(f"@{profile['username']} has {profile['followers']} and {len(feed)} posts. Top post: {feed[0]}")
#this line uses a dictionary and a list