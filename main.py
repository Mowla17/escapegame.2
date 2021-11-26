import time  #'time' module sleep function 
def wrapper(header,border):
    '''It returns a centred header 
       with a border around it
    '''
    wrap = border*80

    return (f"""
            {wrap}
            {header.center(80)}
            {wrap}"""
        )


def intro():
    '''
    Introduce the storyline
    
    '''
    title = "\t E S C A P E  T H E  I S L A N D "
    g = title.center(60)
    print(g)
    time.sleep(2)
    plot_title = "A Bell rings !....."
    print(plot_title)
    time.sleep(2)
    plot = """                          
           As soon as you open your eyes you are in an empty white room, 
           ...With no idea where you are or how you arrived 
           You look AROUND, searching for any clue of what's going on
           ...But all you see is a box of candies and a strange orb lying on the ground 
           

           Startled by the sudden noise you scramble to your feet
           ...That sound... you recognize It !
           a cold realization settles in ...
           ... ... ... ... ... ... ... ... 

           you start craving as soon as you look into that lying box of candy

           """


    alpha =  plot.center(50)
    print(alpha)
    print(wrapper("Search your surroundings for a way to escape !","="))


intro()
