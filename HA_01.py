import random

class Dice:
    def roll(self):
        return random.randint(1,6)
    
class DiceHand:
    def __init__(self):
        self.full_score=0

    def add_roll(self,value):
        self.full_score += value
        return self.full_score

    def reset(self):
        self.full_score=0

    def total(self):
        return self.full_score

class HighScore:
    def __init__(self, file_name="highscores.txt"):
        self.file_name = file_name
        self.scores = self.load_scores()

    def load_scores(self):
        try:
            with open(self.file_name, "r") as file:
                scores = {}
                for line in file:
                    player, score = line.strip().split(":")
                    if player in scores:
                        scores[player].append(int(score))
                    else:
                        scores[player]= [int(score)]
                return scores
        except FileNotFoundError:
            print("File is not found.")

    def update_score(self, player, score):
        if player in self.scores:
            self.scores[player].append(score)
        else:
            self.scores[player] = [score]
        self.save_scores()

    def save_scores(self):
        with open(self.file_name, "w") as file:
            for player, scores_list in self.scores.items():
                for score in scores_list:
                    file.write(f"{player}:{score}\n")

    def display_player_scores(self, player_name):
        if player_name in self.scores:
            print(f"Scores for {player_name}:")
            for score in self.scores[player_name]:
                print(score)
        else:
            print(f"No scores found for {player_name}.")
    #use this to display score of a specific player 
    #high_scores.display_player_scores("Alice")


class Player:
    def __init__(self,name):
        self.name=name 

    # The switch_players method switches the current player.
    def switch_players(self,other_player):
        return other_player

class Intelligence:
    def __init__(self):
        self.computer_intelligence = 1  # Default intelligence level
        #self.computer=computer_player

    def set_computer_intelligence(self, intelligence_level):
        self.computer_intelligence = intelligence_level

    def computer_turn(self):
        if self.computer_intelligence == 1:
            # Simple strategy: Always roll until reaching 20 points or rolling a 1
            while self.computer.turn_total < 20:
                roll = Dice().roll()
                print(f"Computer rolled: {roll}")
                if roll == 1:
                    print("Computer rolled a 1. Turn over!")
                    break
                else:
                    self.computer.turn_total += roll
                    print(f"Computer's current turn total: {self.computer.turn_total}")

        elif self.computer_intelligence ==2:
             # Decision point: Hold if the computer has more than 15 points
                if self.computer.turn_total < 15:
                    roll=Dice().roll()
                    print(f"Computer rolled: {roll}")
                    if roll == 1:
                        print("Computer rolled a 1. Turn over!") #break
                    else:
                        self.computer.turn_total += roll
                        print(f"Computer's current turn total: {self.computer.turn_total}")
                else: 
                    Dice().roll()
                    print("Computer chose to hold.")
                    self.computer.score += self.computer.turn_total
                    print(f"Computer's score: {self.computer.score}")
                    self.computer.switch_players()#(self.computer)


class Game:
    def __init__(self):
        self.current_player =None
        self.total_score = 0
        self.player1_name=None
        self.player2_name=None
        self.dice_hand=DiceHand()

    # The play_two_player_game function plays a two-player game.
    def play_two_player_game(self):
        self.player1_name = input("Enter player 1's name: ")
        self.player2_name = input("Enter player 2's name: ")
        self.player1=Player(self.player1_name)
        self.player2=Player(self.player2_name)
        self.play_game()

    # The play_single_player_game function plays a single-player game against the computer.
    def play_single_player_game(self):
            player_name = input("Enter your name: ")
            
            while True:
                level = input('Choose the intelligence level(low or high): ')
                if level.lower() == 'low':
                    game = Game()
                    game.current_player=player1
                    break
                elif level.lower() == 'high':
                    intelligence_level = input('Choose the intelligence level for the computer (1 or 2): ')
                    if intelligence_level.isdigit() and int(intelligence_level) in [1, 2]:
                        game = Game()  # Creating an instance of Game
                        game.current_player = Player(Intelligence().set_computer_intelligence(int(intelligence_level)))
                        break
                    else:
                        print('Invalid input. Please choose 1 or 2.')
                else:
                    print('Invalid input. Please enter y or n.')
            game.play_game()

    # The play_turn method plays a turn of the game.
    def play_turn(self):
            self.current_player=self.player1
            print(f"It's {self.current_player.name}'s turn.")
            turn_score=0
            while True:
                input("Press Enter to roll the dice...")
                dice_roll = Dice().roll()
                print(f"{self.current_player.name} rolled a {dice_roll}.")
                if dice_roll == 1:
                    print(f"{self.current_player.name} rolled a 1 and lost all points for this turn.")
                    self.dice_hand.reset()
                    self.current_player=self.current_player.switch_players(self.player2 if self.current_player == self.player1 else self.player1)                   
                    break
                else:
                    turn_score=self.dice_hand.add_roll(dice_roll)
                    print(f"{self.current_player.name} accumulated {turn_score} points so far this turn.")
                    choice=input('Do you want to roll again? (yes/no): ')
                    if choice.lower() == 'no':
                        break
                
            total_score=self.dice_hand.total()
            print(f"{self.current_player.name} ends the turn with a total score of {total_score}.\n")

    # The play_game method plays the game until a player wins.
    def play_game(self):
            print("Let's play the game!")
            while True:
                self.play_turn()
                if  self.total_score>= 20:  # Change the winning score to 20
                    print(f"Congratulations, {self.current_player.name}! You've won with a total score of {self.total_score}!")
                    break
                else:
                    self.current_player.switch_players(self.player2 if self.current_player == self.player1 else self.player1)
                    

    def view_rules(self):
        game_rules ='''
            The objective is to be the first player to reach a certain score, usually 100 points.

            Rules:
            1. Players take turns rolling a single dice.
            2. Roll a 1, and you lose all points for that turn. 
            3. Roll any other number, and you can choose to roll again or end your turn, banking the points.
            4. The first player to reach or exceed the winning score wins the game.

            Good luck and have fun!'''
        print(game_rules)
   
def main():
    #The main function that runs the game.
    print("Welcome to the Pig Game!")
    game_over= False
    while not game_over:
        
        print("1. Play against the computer")
        print("2. Play as a two-player game")
        print("3. Rules for the Game")
        print("4. View High scores")
        print("5. Test game")
        print("6. Quit the game")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            Game().play_single_player_game()
        elif choice == 2:
            Game().play_two_player_game()
        elif choice == 3:
            Game().view_rules()
        elif choice == 4:
            player_name=input('Enter the player for Highscores:')
            HighScore().display_player_scores(player_name)
        elif choice == 5:
            pass#testing
        elif choice == 6:
            game_over= True
        
if __name__=="__main__":
    main()