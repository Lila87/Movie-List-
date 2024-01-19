#movielist
#1/12/24
#Lila 

#Init 
myList = []
movie = ""
#Functions 


def movieList():
    global movie
    print("Welcome to your movie list!")
    option = int(input("Please select the following options: 1. Add a movie to the list, 2. View the current list, 3. Mark movie as watched, 4. Remove a task from the list, 5. Remove ALL tasks, 6. Sort the list alphabetically, 7. Print number of items in list, 8. Exit the program"))
    movie = (input("Enter movie:"))
    if option==1:
        addTask()
    elif option==2:
        viewList()
    elif option ==3:
        movieWatched()
    elif option==4:
        removeMovie()
    elif option ==5:
        removeALL()
    elif option == 6:
        alphabet()
    elif option ==7:
        count()
    elif option==8:
        quit()
    cont = input("Would you like to continue?")
    if cont== "yes":
        movieList()
    if cont== "no":
        quit()
    movieList()

def addTask(): 
    myList.append(movie)
def viewList ():
    print(myList)
def movieWatched():
    myList.insert(movie, "X")
def removeMovie():
    myList.remove(movie)
def removeALL():
    myList.clear()
def alphabet():
    sorted(myList)
def count():
    myList.count(myList)
#main 
    
movieList()