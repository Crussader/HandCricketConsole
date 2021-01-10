# Import 
import random, os
from time import sleep


class Game:

    # Decorators 
    d1 = "#"*20      # This is Class Property 
    d2 = "*"*20

    # Computer Choice
    lst1 = ("bat", "bowl")
    lst2 = ["odd", "even"]

    # Scoring
    ply_runs = 0
    comp_runs = 0

    def __init__(self, ply_choice, ply_bob_choice, ply_number, comp_bob_choice, comp_number):

        # Player Choice
        self.ply_choice = ply_choice            #This is a Class Attribute
        self.ply_bob_choice = ply_bob_choice
        self.ply_number = ply_number
        
        # Computer Choice
        self.comp_choice = 'odd' if ply_choice == 'even' else 'even'   # Using in-line if 
        self.comp_bob_choice = comp_bob_choice
        self.comp_number = comp_number
    
        
    def toss(self):
        res = int(self.ply_number) + int(self.comp_number)

        self.winner = 'Computer' if self.comp_choice == self.lst2[res&1] else 'Player'
        print(f"{self.d2}\nTotal: {res}\nPlayer(Even or Odd): {self.ply_choice}\nComputer(Even or Odd): {self.comp_choice}\nWinner: {self.winner}\n{self.d1}")

        self.check_start = 'Starting' if self.ply_bob_choice=='bat' or self.comp_bob_choice=='bat' else 'Not Starting'
        print(f"{self.winner} chose {self.ply_bob_choice if self.winner == 'Player' else self.comp_bob_choice} so it is {self.check_start}\n{self.d2}")
        print('Clearing Console... 5 secs')
        sleep(5)
        os.system('cls||clear')     #This Clears the Console 
    
            
    def start_game(self):  

        Game.toss(self)

        def check_ply_value(choice):
            """
            This Function is to Make Sure the user,
            dosent Input the Wrong Input,
            So to do that we Use While Loop To make Work,
            but insead to write the while loop again and again,
            we use a function which will do it and return the Number
            
            1: General Input (1-6)
            2: Flick (1-2)
            """

            if choice == 1:
                
                while True:
                    self.ply_number = int(input("Enter Number (1-6):  "))
                    if -1 < self.ply_number <=6:
                        break
                    return self.ply_number
            
            elif choice == 2:

                while True:
                    flick_ply = input("Enter 1 or 2:  ")
                    if 0 < flick_ply < 3:
                        break
                return flick_ply
                    
        ###########################
        if self.winner == 'Player':
            self.no_of_wickets = int(input("Enter Number of Wickets(1-10): "))
            if 1 < self.no_of_wickets > 11 :
                raise ValueError (f'You Have Entered a Number {"Higher" if self.no_of_wickets > 11 else "Lower"} Than 10 :  "{self.no_of_wickets}"')
            else:
                print(self.d1)
        else:
            self.no_of_wickets = random.randint(1, 11)
        
        self.copy_wickets = self.no_of_wickets
        ##############################
        while self.no_of_wickets > 0:

            if (self.winner == 'Player' and self.ply_bob_choice=='bat') or (self.winner == 'Computer' and self.comp_bob_choice=='bowl'):
                """

                if Player choses batting and wins the toss or,
                Player Wins the Toss and chose Bowl
                Therefore, Only Batting for the 'Player' Only Happens


                """

                self.checkvalue = 1 
                print(self.d2)

                check_ply_value(1)

                self.comp_number = random.randint(1, 7)
                self.ply_runs = ((self.ply_number + self.ply_runs) if (self.ply_number!=self.comp_number) else (self.no_of_wickets-1))

                if self.ply_number == 0 and self.comp_number!=0:

                    self.ply_runs += self.comp_number
                    
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                elif self.ply_number == self.comp_number:
                    print('{0}Out{0}'.format(self.d2))
                    self.no_of_wickets -= 1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')
                    
                elif self.ply_number == self.comp_number == 0:
                    
                    # Flick
                    print("Flick has been triggered!")

                    flick_comp = random.randint(1,3)
                    print(f"{'Player Escaped' if check_ply_value(2) != flick_comp else 'Player lost The Flick'}")
                    self.no_of_wickets -=1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')
                    

                else:
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')
                    

            if (self.winner == 'Computer' and self.ply_bob_choice=='bat') or (self.winner == 'Player' and self.ply_bob_choice=='bowl'):
                """

                if computer Choses batting and wins the toss or,
                Player wins the toss and choses bowl so batting for computer, 
                Therefore, Only Batting For the 'Computer' Happens

                """

                self.checkvalue = 2
                print(self.d2)

                check_ply_value(1)
                self.comp_number = random.randint(1, 7)

                self.comp_number = ((self.comp_number + self.comp_runs) if (self.ply_number!=self.comp_number) else (self.no_of_wickets-1))

                if self.comp_number == 0 and self.ply_number !=0:

                    self.comp_runs += self.ply_number
                    print(f'Runs: {self.comp_runs} | Wickets : {self.no_of_wickets}')
                
                # Out
                elif self.ply_number == self.comp_number:
                    print('{0}Out{0}'.format(self.d2))
                    self.no_of_wickets -= 1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                # Flick
                elif self.ply_number == self.comp_number == 0:
                    
                    print("Flick has been triggered!")

                    check_ply_value(2)

                    flick_comp = random.randint(1,3)
                    print(f"{'Computer Escaped' if check_ply_value(2) != flick_comp else 'Computer lost The Flick'}")
                    self.no_of_wickets -=1
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                else:
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                    
        #################
        print(f"{self.d2}\n{'Computer' if self.checkvalue == 2 else 'Player'} has {(self.ply_runs + 1) if self.checkvalue == 1 else (self.comp_runs + 1)} Runs to Go")
        print(f'All Wickets Out, so {"Computer" if self.checkvalue == 2 else "Player"} is Bowling Now, and {"Computer" if self.checkvalue == 1 else "Player"} is Batting\n{self.d2}') 

        #########################
        # This is the loop for the bat or bowl after the first bat or bowl
        while self.copy_wickets>0:

            if self.checkvalue==2:
                
                """

                self.checkvalue is the aatribute checking what value is assaigned,
                if the computer batting 'if' condition occurs then it will set the value to 2 
                depends on the if condition (1,2)
                2 = Computer Is Batting now

                """

                print(self.d2)
                
                check_ply_value(1)
                self.comp_number = random.randint(1,7)

                self.comp_number = ((self.comp_number + self.comp_runs) if (self.ply_number!=self.comp_number) else (self.no_of_wickets-1))

                if self.comp_number == 0 and self.ply_number !=0:

                    self.comp_runs += self.ply_number
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')
                    
                elif self.ply_number == self.comp_number:
                    print('{0}Out{0}'.format(self.d2))
                    self.no_of_wickets -= 1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')
                    

                
                elif self.ply_number == self.comp_number == 0:
                    
                    print("Flick has been triggered!")
                
                    flick_comp = random.randint(1,3)
                    print(f"{'Computer Escaped' if check_ply_value(2) != flick_comp else 'Computer lost The Flick'}")
                    self.no_of_wickets -=1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                else:
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

            if self.checkvalue == 1:
                """
                Similar To the previous One
                1 = Player is batting now 
                """

                print(self.d2)
                
                check_ply_value(1)
                self.comp_number = random.randint(1, 7)
                self.ply_runs += self.ply_number 

                if self.ply_number == 0 and self.comp_number!=0:

                    self.ply_runs += self.comp_number
                    
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                elif self.ply_number == self.comp_number:
                    print('{0}Out{0}'.format(self.d2))
                    self.no_of_wickets -= 1
                    print(f'\nPlayer: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                elif self.ply_number == self.comp_number == 0:
                    
                    
                    print("Flick has been triggered!")

                    flick_comp = random.randint(1,3)
                    print(f"{'Player Escaped' if check_ply_value(2) != flick_comp else 'Player lost The Flick'}")
                    self.no_of_wickets -=1
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

                
                else:
                    print(f'Player: {self.ply_number}\nComputer: {self.comp_number}\nRuns : {self.ply_runs} | Wickets : {self.no_of_wickets}')

        # Check Results and Prints them
        print(f"{self.d2}\n{'Computer' if self.comp_runs > self.ply_runs else 'Player'} HAS WON !!!\n{self.d2}")

    
args = (
    input("Enter Odd or Even: ").lower(),
    input("Enter Bat or Bowl: ").lower(),
    int(input("Enter Number 1-6: ")),
    random.choice(Game.lst1),
    random.randint(1, 7)
    )
Game(*args).start_game()

