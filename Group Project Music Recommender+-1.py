import os.path
#Russell Fish, Michael Lazieh Rahul Swaminathan
# We pledge our honor that we have abided by the stevens honor code system
PREF_FILE = open("musicrecplus.txt", 'a')


def loadUsers(): #all
    ''' Reads in a file of stored users' preferences
    stored in the file 'fileName'.
    Returns a dictionary containing a mapping
    of user names to a list preferred artists
    '''
    file = open("musicrecplus.txt", "r")
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict


def getPreferences(userName, userMap):#all
    ''' Returns a list of the user's preferred artists.
    If the system already knows about the user,
    it gets the preferences out of the userMap
    dictionary and then asks the user if she has
    additional preferences. If the user is new,
    it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        #print("Your music preferences include:")
        #for artist in prefs:
            #print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
    while newPref != "":
        if newPref not in prefs:
            prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs



def getRecommendations(currUser, prefs, userMap):#all
    ''' Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary)
    and the user's preferences in pref (a list).
    Returns a list of recommended artists. '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations



def findBestUser(currUser, prefs, userMap):#all
    ''' Find the user whose tastes are closest to the current
    user. Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser



def drop(list1, list2):#all
    ''' Return a new list that contains only the elements in
    list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3



def numMatches(userPrefs, storedUserPrefs):#all
    """Returns the number of elements that the lists
        userPrefs and storedUserPrefs have in common"""
    x = list(userPrefs)
    x.sort()
    y = list(storedUserPrefs)
    y.sort()
    i,j, cnt = 0,0,0
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            cnt+=1
            i+=1
            j+=1
        elif x[i] > y[j]:
            j += 1
        else:
            i += 1
    return cnt



def BestMatch(CurrentUser, prefs, userMap):#Mike
    """Finds the user with taste most like the current user and returns the best match's
        name as a string."""
    bestUser = None
    bestScore = -1
    for user in userMap.keys():
        score = numMatches(prefs, userMap[user])
        if user==CurrentUser:
            continue
        if score>bestScore:
            bestScore = score
            bestUser = user
    return bestUser



def SongstoRecommend(prefs1, prefs2):#Mike
    """Returns a list with all the songs on the best matches list that aren't
        on the original users list."""
    L=[]
    i=0
    j=0
    while i < len(prefs1) and j < len(prefs2):
        if prefs1[i]==prefs2[j]:
            i+=1
            j+=1
        elif prefs1[i] < prefs2[j]:
            i+=1
        else:
            L.append(prefs2[j])
            j+=1
    while j < len(prefs2):
        L.append(prefs2[j])
        j+=1
    return L



def getRecommendations(CurrentUser, prefs1, userMap):#Mike
    """Returns list of recommended artists."""
    user2=BestMatch(CurrentUser, prefs1, userMap)
    L=SongstoRecommend(prefs1,userMap[user2])
    return L


def Recs():#Mike
    """"Prints out list of recommend artists"""
    L = getRecommendations(userName, userMap[userName], userMap)
    for i in L:
        print(i)
    

def saveUserPreferences(userName, prefs, userMap, fileName): #Russell/Rahul
    ''' Writes all of the user preferences to the file.
    Returns nothing. '''
    userMap[userName] = prefs
    file = open("musicrecplus.txt", "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + "\n"
        file.write(toSave)
    file.close()



def listToDict(L): #this is a helper function that creatrs a temporary list that will be used for the popular
    artistDict = {}
    for i in L:
        artistDict[i] = 0
    return artistDict #Russell/Rahul


#Russell/Rahul
def artistList(userMap):# another helper function that makes two listst that are used for pulling things out of the uer map and artlist list
    artistList = []
    filterList = []
    for user in userMap:
        artistList += userMap[user]
    for artist in artistList:
        if artist not in filterList:
            filterList += [artist]
    return filterList
#Russell/Rahul
def howPopular():#this uses both of the helpers to look into the list and pick out the name that appears most values in the library
    artDict = listToDict(artistList(loadUsers()))
    userMap = loadUsers()
    for user in userMap:
        for artist in userMap[user]:
            artDict[artist] += 1
    a = 0
    for artist in list(artDict.keys()):
        if artDict[artist] > a:
            a = artDict[artist]
    return a

#Russell/Rahul
def mostLikes(userMap): #most likes counts how many of each value there are and picks the most common one. it uses a simple if statment with len()
    #userMap = loadUsers()
    a = 0
    for user in userMap:
        if user[-1] != '$':
            if len(userMap[user]) > a:
                a = len(userMap[user])
                s = user
    return s


#Russell/Rahul
def mostPopular(): #this is very similar to how popular but puts the number of the most values in the library
    artList = listToDict(artistList(loadUsers()))
    userMap = loadUsers()
    for user in userMap:
        if user[-1] != '$':
            for artist in userMap[user]:
                artList[artist] += 1
    a = 0
    s = ''
    for artist in list(artList.keys()):
        if artList[artist] > a:
            a = artList[artist]
            s = artist
    return s



# MAIN
#____________________________________________________________________________








prefs = []
#Russell/Rahul
userMap = loadUsers()
print("Welcome to the music recommender system!\n")

userName = input('Enter your name:  put a $ symbol after your name if you wish your preferences to remain private:')
print ("\nWelcome,", userName, '\n')
#Russell/Rahul
if userName not in userMap: #checks the keys and sees if the user name is arleady tehre if not it will create a new one
    prefs = getPreferences(userName, userMap)
    saveUserPreferences(userName, prefs, userMap, PREF_FILE)
while True:
    option = input('Enter a letter to choose an option:' + '\n' + '\t' + 'e - enter preferences' + '\n' + '\t' 'r - get recommendations' + '\n' + '\t' \
            + 'p - show most popular artists'  + '\n' + '\t' + 'h - how popular is the most popular' + \
           '\n' + '\t' + 'm - which user has the most likes ' + '\n' + '\t' + 'q - save and quit\n')
    if option == 'e':
        prefs = getPreferences(userName, userMap)
        saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            
    if option =='r':# calls the r functionm with the failsafe that if the there are no recomendations
        if len(userMap)<2:
            print("I'm sorry, we have no recommendations right now")
        else:#mike
            Recs()
            
    if option == 'p': 
        count1 = 0
        for user in userMap:#Russell/Rahul
            if not userMap[user] == [] and not userMap[user] == ['']:
                count1 += 1
        if(count1 == 0):
            print("Sorry, no artist found.")
        else:
            print(mostPopular())
        
    if option == 'h':# calls the h fucntion and if ther are no vaules it will say no artist found
        count2 = 0
        for user in userMap:#Russell
            if not userMap[user] == [] and not userMap[user] == ['']:
                count2 += 1
        if(count2 == 0):
            print("Sorry, no artist found.")
        else:
            print(howPopular())
            
    if option == 'm':# calls the m fucntion and if ther are no keys it will say no user found
        count3 = 0
        for user in userMap:#Rahul
            if not userMap[user] == [] and not userMap[user] == ['']:
                count3 += 1
        if(count3 == 0):
            print("Sorry, no users found.")
        else:
            print(mostLikes(userMap))
            
    if option == 'q': #ends the code and allows you to chekc the list after
        break#Russell
    
    if option not in ['e', 'r', 'p', 'h', 'm', 'q']: #this is super simple and checks if the user puts one of the available options
            print("That is not an option.") #Russell

