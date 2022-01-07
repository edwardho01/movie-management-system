# Edward Ho, CS 8 (M21)

movies = [['tdk',['The Dark Knight','2008','Christopher Nolan','https://www.imdb.com/title/tt0468569/']]]  # we have global variable movies where we'll directly refer to whenever we want to add, delete, update, and/or list the movies that are stored in here

def print_menu(movie_menu):  # print_menu() will display the screen with all the options whenever we want to return back to the menu
    """Will display the screen in which the user makes a choice"""
    print((27 * '*') + "\n What would you like to do? \n 1 - List movies \n 2 - Add a movie \n 3 - Update a movie \n 4 - Delete a movie \n Q - Quit the system \n" + (27 * '*')+'\n')

def create_ID(text): # create_ID will be referenced in anything where the user needs to find something via the movie ID
    """Will create the ID of any new or updating title added"""
    movie_ID = ""
    boolean = True # travel through the string with a boolean value
    for letter in range(len(text)):
        if (text[letter] == ' '): # if there's a space within the title, then True
            boolean = True
        elif text[letter] != ' ':  # otherwise if it's not a space within the title and a character/number, then it'll add this first letter to movie_ID with no space
            if boolean == True:
                movie_ID += (text[letter])
                boolean = False  # then it'll set as false and do it over again until the entire range(len()) of string has been traversed
    return movie_ID.lower() 

def add_movie():
    """Will add any new string inputs into the global function movies"""
    print('You\'ll need to add the following info: \n -title \n -year \n -director \n -imdb')
    print("::: Press Enter to Continue \n or type M to return to the menu")
    decision = input("::: ").lower() 
    if decision != 'm':  # if the user types m, then it'll instantly return back to the print_menu to remake a decision
        mov = [] # we'll create a sub-lists which stores the nested list of the movies info
        title = input("title: ")
        for movie in range(len(movies)):  # traverse across the entirety of movies
            if create_ID(title) == movies[movie][0]:  # this will check for the ID that matches the movie with that ID in movies
                print('WARNING: A movie with such key already exists:') # once its checked, it'll print the statements, break out the loop and return to the menu
                print('{} - {}'.format(movies[movie][0],movies[movie][1][0]))
                break
        else: # now if the title doesn't already exist, then we'll proceed to add all the other options
                print('Movie Key: {}'.format(create_ID(title)))
                print('Adding a new movie: {}'.format(title))
                year = input("year: ")   
                director = input("director: ")
                imdb = input("imdb: ")
                mov.append(title)
                mov.append(year)
                mov.append(director)
                mov.append(imdb) 
                KeyValuePair = []  # we create KeyValuePair to store the movies information and ID so it'll have 2 index's, the ID and information correlating
                text = mov[0]
                new_ID = create_ID(text)
                KeyValuePair.append(new_ID)
                KeyValuePair.append(mov)
                movies.append(KeyValuePair) # after we create KeyValuePair, we'll store that value into movies, so it'll be essentially one index, containing all that information inside movies and the more we add the more index's it'll contain

def list_movies():
    """Will display clearly all the nested items which reside within movies"""
    quantity = len(movies)  # determines how many movies exist within movies[]
    if quantity == 1: 
        print('There is {} movie in this collection.'.format(quantity))
        print('-------------------------------------------------')
        for movie in movies: # check's all the index's within movies
            print_movie(movie) # then it'll print each index information that exist by referring to the print_movie() function
            print('-------------------------------------------------')
    else:
        print('There are {} movies in this collection.'.format(quantity))
        print('-------------------------------------------------')
        for movie in movies:
            print_movie(movie)
            print('-------------------------------------------------')

def update_movie():
    """Will grab entered movie ID if it exist within movies and allows user to update any information pertaining to that ID"""
    print('Enter the ID of a movie that you want to update \nor type M to return to the menu.')
    search_ID = input("::: ").lower()
    if search_ID != 'm': # if not m then it'll proceed
        for movie in movies:
            if movie[0] == search_ID:  # if the movie[0] which should be the index of movie ID, it'll compare it to the search input of the user
                print("Updating: '{}'".format(movie[0]))
                print()
                print_movie(movie)
                print('-------------------------------------------------')
                print('Which field would you like to update?')
                print('0 - title')
                print('1 - year')
                print('2 - director')
                print('3 - imdb')
                print('Enter an option for the field \n or type M to return to the menu.')
                edit_option = input('::: ').lower()  # now since we confirmed it's within movies, if not m it'll proceed
                if edit_option != 'm':
                    print('You selected option {} to update {}'.format(edit_option,update_options[edit_option]))  # i reference the dictionary option so it could return what the user has chose to input
                    print('Enter your updated value of {}:'.format(update_options[edit_option]))
                    edit_number = input('::: ')
                    if edit_option == '0':
                        movie[0] = create_ID(edit_number)
                        movie[1][0] = edit_number
                        print('Successfully updated, new infos:')
                        print('-------------------------------------------------')
                        print_movie(movie)
                        break
                    elif edit_option == '1':
                        movie[1][1] = edit_number
                        print('Successfully updated, new infos:')
                        print('-------------------------------------------------')
                        print_movie(movie)
                        break
                    elif edit_option == '2':
                        movie[1][2] = edit_number
                        print('Successfully updated, new infos:')
                        print('-------------------------------------------------')
                        print_movie(movie)
                        break
                    elif edit_option == '3':  # for all these options, I made sure to index specifically what we are searching for since movie[1][3] directly index's the movies imdb
                        movie[1][3] = edit_number
                        print('Successfully updated, new infos:')
                        print('-------------------------------------------------')
                        print_movie(movie)
                        break
                break
        else:
            while movie[0] != search_ID:  # if the search ID the user input isnt in the first index of movie, then it'll print the warning and break the loop
                print("WARNING: No such a movie to update")
                break

def delete_movie():
    """Will grab entered movie ID if it exist within movies and then delete the entire list that is associated with said ID"""
    print('Enter the ID of a movie that you want to delete \nor type M to return to the menu.')
    search_ID = input("::: ").lower()
    if search_ID != 'm': 
        for movie in movies:
            if movie[0] == search_ID: # everything is almost similar to updating the movie, where it'll span across movies, and check if all the ID index's matches the user input
                print("Deleting movie with ID '{}'".format(movie[0]))
                print('-------------------------------------------------')
                print_movie(movie)
                print('::: Are you sure? Type Y or N')
                decision_to_delete = input("::: ").lower()
                if decision_to_delete == 'y': # give the user the choice to edit or not, if yes then proceed
                    movies.remove(movie)  # it'll remove in the movies the index any that matches the ID, which can only be 1
                    print('deleted')
                    break
                else:
                    print("Looks like you aren't 100% sure.\nCancelling the deletion.") # else if another input besides 'y' is entered then it'll exit the loop
                    break # since it exit's the loop, it'll also exit the function and return to the main menu
        else:
            while movie[0] != search_ID:
                print("WARNING: No such movie to delete")
                break

def print_movie(movie):  # an aditional print_movie(movie) is created because whenever I might want to reference or return a movies info, I'll refer to this function
    """Will print the associated movie info of the called list that exist within movies""" # these specifically reference the specific index's within each nested list item which matches what info we want extract which is why we use for movie in movies that match the user input
    print('ID: {}'.format(movie[0]))
    print('title: {}'.format(movie[1][0]))
    print('year: {}'.format(movie[1][1]))
    print('director: {}'.format(movie[1][2]))
    print('imdb: {}'.format(movie[1][3]))

update_options = {  # these are just used to display what the reader entered for clearness
    '0': 'title',
    '1': 'year',
    '2': 'director',
    '3': 'imdb'
}

movie_menu = {  # movie_menu is referred back in the if __name__ == "__main__": system because once the user opens the project, it'll give them the options within its dictionary to choose one of the 4
    '1': list_movies,
    '2': add_movie,
    '3': update_movie,
    '4': delete_movie
}

movie_option = {  # these are also just used to display what the reader entered for clearness
    '1': 'List Movies',
    '2': 'Add a movie',
    '3': 'Update a movie', 
    '4': 'Delete a movie' 
}

if __name__ == "__main__":
    opt = None

    while True:
        print_menu(movie_menu)
        print("::: Enter an option")
        opt = input("::: ")

        if opt == 'q':
            print("Goodbye")
            break # if the user enters q then it'll print goodbye, break out the entire while loop and print see you next time and close the function
        elif opt == 'Q': # created just to read upper case as well
            print("Goodbye")
            break 
        else:
            if opt in movie_menu:  # if it's another option 1,2,3, or 4 then it'll reference the dictionary movie_menu and use whatever number was inputed to reference accordingly the matching option which will return the function that matches
                print("You selected option {} to {}.".format(opt, movie_option[opt]))
                print('-------------------------------------------------')
                selected_action = movie_menu[opt]
                selected_action()
            elif opt not in movie_menu: # BUT if it's not in the movie_menu nor Q/q then it'll read out the print statement below and give the reader to re-enter an appropriate option
                print("Unavalaible Action: Please re-enter 1,2,3,4, or Q to exit")
                print('-------------------------------------------------')
                continue # this continue sends them back to the main loop



    print("See you next time!")

