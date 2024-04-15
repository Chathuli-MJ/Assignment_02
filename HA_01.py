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
        self.score=0

    # The switch_players method switches the current player.
    def switch_players(self,other_player):
        return other_player

class Intelligence:
    def __init__(self):
        self.computer_intelligence = 'low'  # Default intelligence level
        #self.computer=computer_player

    def set_computer_intelligence(self, intelligence_level):
        self.computer_intelligence = intelligence_level

    def computer_turn(self):
        if self.computer_intelligence == 'low':
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

        elif self.computer_intelligence =='high':
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
        self.total_score1 = 0
        self.player1_scorel=0
        self.player2_score=0
        self.player1_name=None
        self.player2_name=None
        self.dice_hand=DiceHand()

    # The play_two_player_game function plays a two-player game.
    def play_two_player_game(self):
        self.player1_name = input("Enter player 1's name: ")
        self.player2_name = input("Enter player 2's name: ")
        self.player1=Player(self.player1_name)
        self.player2=Player(self.player2_name)
        self.current_player=self.player1
        
        self.play_game()

    # The play_single_player_game function plays a single-player game against the computer.
    def play_single_player_game(self):
        self.player1_name = input("Enter your name: ")
        self.player1=Player(self.player1_name)
        self.player2_name= 'Computer'
        self.player2=Player(self.player2_name)
        self.current_player=self.player1
        while True:
            level = input('Choose the intelligence level(low or high): ')
            if level.lower() == 'low':
                game = Game()
                game.current_player=player1
                break
            elif level.lower() == 'high':
                pass
            else:
                print('Invalid input. Please enter low or high.')
        self.play_game()

    # The play_turn method plays a turn of the game.
    def play_turn(self):
            
            print(f"\nIt's {self.current_player.name}'s turn.")
            Keep_going = True
            while Keep_going:
                input("Press Enter to roll the dice...")
                dice_roll = Dice().roll()
                print(f"\n{self.current_player.name} rolled a {dice_roll}.")
                if dice_roll == 1:
                    if self.current_player ==self.player1:
                            self.player1_score =0
                    else:
                        self.player2_score =0

                    print(f"\n{self.current_player.name} ends the turn with a total score of {0}.\n")
                    self.current_player = self.current_player.switch_players(self.player2 if self.current_player == self.player1 else self.player1)
                    break
                else:
                    if self.current_player ==self.player1:
                        self.player1_score +=dice_roll
                        print(f"{self.current_player.name} accumulated {self.player1_score} points so far this turn.")
                    else:
                        self.player2_score += dice_roll
                        print(f"{self.current_player.name} accumulated {self.player2_score} points so far this turn.")
                    if self.player1_score >= 20 or self.player2_score >= 20:
                        Keep_going =False
                        break
                    
                    choice=input('\nDo you want to roll again? (yes/no): ')
                    if choice.lower() == 'no':
                        if self.current_player == self.player1:
                                print(f"{self.current_player.name} ends the turn with a total score of {self.player1_score}.\n")

                        else:
                                print(f"{self.current_player.name} ends the turn with a total score of {self.player2_score}.\n")
                        self.current_player = self.current_player.switch_players(self.player2 if self.current_player == self.player1 else self.player1)
                        break
                    
               
        

    # The play_game method plays the game until a player wins.
    def play_game(self):
            print("Let's play the game!")
            
            while True:
                self.play_turn()
                if  self.player1_score>= 20 :  # Change the winning score to 20
                    print(f"Congratulations, {self.player1_name}! You've won with a total score of {self.player1_score}!") 
                    break
                elif self.player2_score >= 20:
                    print(f"Congratulations, {self.player2_name}! You've won with a total score of {self.player2_score}!") 
                    break
                    
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
