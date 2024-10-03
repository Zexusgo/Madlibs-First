#code 2

#importing function from the file
from type_error import check_string

def variable(sentances):


    while True:


        var1 = input(sentances)

        if check_string(var1):
        
            return var1

sports_player = variable("Favorite sports player: ")
game = variable("Sports which he play's: ")
antagonist = variable("His opponent: ")

#printing them out with f-string
print(f"""Hey! What is your name? Huh, {sports_player}, kind of heard that one somewhere, do you play {game},
heard that someone strong is out here, my name is {antagonist}""")