import random

print(r"""▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓███████████████████████████████████████████████████████████████████████████▓▓▓▓▓▓▓
▓▓▓▓▓█████████████████████████████████████████████████████████████████████████████████▓▓▓▓
▓▓▓█████████████████████████████████████████████████████████████████████████████████████▓▓
▓██████████████████████████████████▓▒▓▒▓▒▒▓▓█▓▒▓▓▓▒▓▒▓▒▓▓▒████████████████████████████████
▓█████████████████████████████████▓▓▓▓▓▓▒▓▓▓██▓▓█▓▒▓▓▓▓▓▓▓████████████████████████████████
▓███████████████████████████████████████▓████████▓████████████████████████████████████████
▓█████████████████▓▓▒▒▒▒▒▓█▓▒▒▒▒▒▒▒█▓▓▒▒▒▒▒▒▓▓█▓▒▒▒▒▒▒▓█▓▒▒▒▒▒▒▒▓▓█▓▒▒▒▒▒▒▒▓██████████████
▓███████████████▓▒▒▒█▓▒▒▒█▓▒▒▓█▓▒▒▓█▒▒▒███▓▓▓▓█▒▒▒▓█▒▒▒▓█▒▒▒▓██▓▒▒▒█▓▒▒▒▓▓████████████████
███████████████▓▒▒▒▒▓▒▒▒█▓▒▒▒▓▓▒▓▓█▓▒▒▒████████▓▒▒▒▓▒▒▒▒█▓▒▒▒███▓▒▒▒█▓▒▒▒▒▒███████████████
██████████████▒▒▒▒▒▒▒▒▒█▓▒▒▒▒▒▒▒▒▓█▒▒▒▓███▓▒▒▓█▓▒▒▒▒▒▒▒▒██▒▒▒▓███▓▒▒▒█▓▒▒▒▓███████████████
████████████▓▒▒▒▓█▓▒▒▒█▓▒▒▒▓█▓▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒██▒▒▒▒█▓▒▒▒▒▒▒▒▒▒▒▓█▓▒▒▒▒▒▒▒▒▒█████████
███████████▓▒▒▒▓█▓▒▒▒██▒▒▒▓█▓▒▒▒▓███▒▒▒▒▒▒▒▓███▓▒▒▒██▓▒▒▒██▒▒▒▒▒▒▒▒▒▓███▓▒▒▒▒▒▒▒▒▒▓███████
▓████████████████████████████████████████████████████████████████████████████████████████▓
▓████████████████████████████████████████████████████████████████████████████████████████▓
▓▓███████████████████████████████████████████████████████████████████████████████████████▓
▓▓▓█████████████████████████████████████████████████████████████████████████████████████▓▓
▓▓▓▓▓█████████████████████████████████████████████████████████████████████████████████▓▓▓▓
▓▓▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████████▓▓▓▓▓▓▓▓
""")

continue_playing = input("ARE  YOU READY? (y/n): ").lower()
if continue_playing != 'y':
    print("Goodbye!")
    exit()

class Arcade:
    
    def __init__(self):
        self.money = 100
        self.tokens = 0
        self.tickets = 0
        self.games = [MathQuiz(), WordScramble(), IloiloTrivia(), CPUQuiz(), ScienceExperiment()]
        self.token_prices = [1, 2, 3, 4, 5]  
    
    def buy_token(self):
        num_tokens = int(input("How many tokens do you want to buy?: "))
        token_price = 2
        total_cost = num_tokens * token_price
        
        if total_cost > self.money:
            print("Not enough money to buy that many tokens!")
            return False  
        
        if self.tokens + num_tokens > 100:  
            print("Token limit exceeded!")
            return False
        
        self.money -= total_cost
        self.tokens += num_tokens
        return True
    
    def play_game(self, game_choice):
        if game_choice == len(self.games):
            return False
        elif game_choice < len(self.games):
            if self.tokens >= self.token_prices[game_choice]:
                self.tokens -= self.token_prices[game_choice]
                game = self.games[game_choice]
                result, tickets_won = game.play()
                self.tickets += tickets_won
                print(result)
                print(f"You won {tickets_won} tickets!")
                return True
            else:
                print("Not enough tokens to play this game!")
                return False
        else:
            print("Invalid game choice!")
            return False



class Game:
    def __init__(self, ticket_price):
        self.ticket_price = ticket_price
    
    def play(self):
        pass

class MathQuiz(Game):
    def __init__(self):
        super().__init__(1)
    
    def play(self):
        print(r"""                          __      __       
                         |  \    |  \      
 ______ ____    ______  _| $$_   | $$____  
|      \    \  |      \|   $$ \  | $$    \ 
| $$$$$$\$$$$\  \$$$$$$\\$$$$$$  | $$$$$$$\
| $$ | $$ | $$ /      $$ | $$ __ | $$  | $$
| $$ | $$ | $$|  $$$$$$$ | $$|  \| $$  | $$
| $$ | $$ | $$ \$$    $$  \$$  $$| $$  | $$
 \$$  \$$  \$$  \$$$$$$$   \$$$$  \$$   \$$""")
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
        
        user_answer = int(input(f"What is {num1} {operator} {num2}? "))
        if user_answer == answer:
            return "Correct answer!", 5
        else:
            return f"Wrong answer! The correct answer is {answer}.", 0

class WordScramble(Game):
    def __init__(self):
        super().__init__(2)
    
    def play(self):
        print(r"""           .---.                                      .--.--.                                          ____              ,--,              
          /. ./|                       ,---,         /  /    '.                                      ,'  , `.  ,---,   ,--.'|              
      .--'.  ' ;   ,---.    __  ,-.  ,---.'|        |  :  /`. /            __  ,-.                ,-+-,.' _ |,---.'|   |  | :              
     /__./ \ : |  '   ,'\ ,' ,'/ /|  |   | :        ;  |  |--`           ,' ,'/ /|             ,-+-. ;   , |||   | :   :  : '              
 .--'.  '   \' . /   /   |'  | |' |  |   | |        |  :  ;_       ,---. '  | |' | ,--.--.    ,--.'|'   |  ||:   : :   |  ' |      ,---.   
/___/ \ |    ' '.   ; ,. :|  |   ,',--.__| |         \  \    `.   /     \|  |   ,'/       \  |   |  ,', |  |,:     |,-.'  | |     /     \  
;   \  \;      :'   | |: :'  :  / /   ,'   |          `----.   \ /    / ''  :  / .--.  .-. | |   | /  | |--' |   : '  ||  | :    /    /  | 
 \   ;  `      |'   | .; :|  | ' .   '  /  |          __ \  \  |.    ' / |  | '   \__\/: . . |   : |  | ,    |   |  / :'  : |__ .    ' / | 
  .   \    .\  ;|   :    |;  : | '   ; |:  |         /  /`--'  /'   ; :__;  : |   ," .--.; | |   : |  |/     '   : |: ||  | '.'|'   ;   /| 
   \   \   ' \ | \   \  / |  , ; |   | '/  '        '--'.     / '   | '.'|  , ;  /  /  ,.  | |   | |`-'      |   | '/ :;  :    ;'   |  / | 
    :   '  |--"   `----'   ---'  |   :    :|          `--'---'  |   :    :---'  ;  :   .'   \|   ;/          |   :    ||  ,   / |   :    | 
     \   \ ;                      \   \  /                       \   \  /       |  ,     .-./'---'           /    \  /  ---`-'   \   \  /  
      '---"                        `----'                         `----'         `--`---'                    `-'----'             `----' """)
        words = ['python', 'computer', 'algorithm', 'variable', 'function']
        word = random.choice(words)
        scrambled_word = ''.join(random.sample(word, len(word)))
        
        print("Unscramble the word:", scrambled_word)
        user_guess = input("Your guess: ")
        if user_guess == word:
            return "Correct guess!", 5
        else:
            return f"Wrong guess! The correct word is {word}.", 0

class IloiloTrivia(Game):
    def __init__(self):
        super().__init__(3)
    
    def play(self):
        print(r"""░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░  
░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░  
                                                                """)
        questions = {
            "What is the capital of Iloilo?": "Iloilo City",
            "Once refered to as the queen city of the south?": "Iloilo",
            "Most famous food?": "Batchoy"
        }
        question = random.choice(list(questions.keys()))
        answer = questions[question]
        
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            return "Correct answer!", 5
        else:
            return f"Wrong answer! The correct answer is {answer}.", 0

class CPUQuiz(Game):
    def __init__(self):
        super().__init__(4)
    
    def play(self):
        print(r"""       _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\        
       /::::\    \              /::::\    \              /:::/    /        
      /::::::\    \            /::::::\    \            /:::/    /         
     /:::/\:::\    \          /:::/\:::\    \          /:::/    /          
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/    /           
   /:::/    \:::\    \      /::::\   \:::\    \      /:::/    /            
  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/    /      _____  
 /:::/    /   \:::\    \  /:::/\:::\   \:::\____\  /:::/____/      /\    \ 
/:::/____/     \:::\____\/:::/  \:::\   \:::|    ||:::|    /      /::\____\
\:::\    \      \::/    /\::/    \:::\  /:::|____||:::|____\     /:::/    /
 \:::\    \      \/____/  \/_____/\:::\/:::/    /  \:::\    \   /:::/    / 
  \:::\    \                       \::::::/    /    \:::\    \ /:::/    /  
   \:::\    \                       \::::/    /      \:::\    /:::/    /   
    \:::\    \                       \::/____/        \:::\__/:::/    /    
     \:::\    \                       ~~               \::::::::/    /     
      \:::\    \                                        \::::::/    /      
       \:::\____\                                        \::::/    /       
        \::/    /                                         \::/____/        
         \/____/                                           ~~           """)
        questions = {
            "Who is the president of CPU?": "Ernest Howard B. Dagohoy",
            "What year was CPU built?": "1905",
            "CPU first Filipino president?": "Rex D. Drilon"
        }
        question = random.choice(list(questions.keys()))
        answer = questions[question]
        
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            return "Correct answer!", 5
        else:
            return f"Wrong answer! The correct answer is {answer}.", 0

class ScienceExperiment(Game):
    def __init__(self):
        super().__init__(5)
    
    def play(self):
        print(r"""  _____   __  ____    ___  ____     __    ___ 
 / ___/  /  ]|    |  /  _]|    \   /  ]  /  _]
(   \_  /  /  |  |  /  [_ |  _  | /  /  /  [_ 
 \__  |/  /   |  | |    _]|  |  |/  /  |    _]
 /  \ /   \_  |  | |   [_ |  |  /   \_ |   [_ 
 \    \     | |  | |     ||  |  \     ||     |
  \___|\____||____||_____||__|__|\____||_____|""")
        experiments = {
            "What happens when you mix vinegar and baking soda?": "Fizzing",
            "What is the primary function of chlorophyll in plants?": "Photosynthesis",
            "What happens when you heat water?": "Boil"
        }
        question = random.choice(list(experiments.keys()))
        answer = experiments[question]
        
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            return "Correct answer!", 5
        else:
            return f"Wrong answer! The correct answer is {answer}.", 0

class TicketBooth:
    def __init__(self):
        self.prizes = {1: "Pen", 2: "Book", 3:"Calculator", 4:"Scientific Calculator", 5: "iPhone"}
        self.prize_costs = {1: 10, 2: 20, 3: 30,4: 40, 5:100}
    
    def exchange_tickets(self, tickets):
        print("Available prizes:")
        for prize_num, prize_name in self.prizes.items():
            print(f"{prize_num}: {prize_name} ({self.prize_costs[prize_num]} tickets)")
        
        choice = int(input("Enter the prize number you want to exchange tickets for: "))
        if choice in self.prizes.keys():
            if tickets >= self.prize_costs[choice]:
                print(f"Congratulations! You've exchanged {self.prize_costs[choice]} tickets for a {self.prizes[choice]}!")
                tickets -= self.prize_costs[choice]
            else:
                print("Not enough tickets to exchange for this prize.")
        else:
            print("Invalid prize number.")
        return tickets

# usage
arcade = Arcade()
ticket_booth = TicketBooth()

while True:
    print("\nWelcome to the Arcade!")
    print("Money: ", arcade.money)
    print("Tokens: ", arcade.tokens)
    print("Tickets: ", arcade.tickets)
    print("1. Buy token")
    print("2. Play game")
    print("3. Go to Ticket Booth")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if arcade.buy_token():
            print("Token bought successfully!")
    elif choice == 2:
        while True:
            print("\nGames:")
            for i, game in enumerate(arcade.games):
                print(f"{i+1}. {game.__class__.__name__} - Token Price: {arcade.token_prices[i]}")
            print(f"{len(arcade.games)+1}. Exit")
            game_choice = int(input("Enter the game number: ")) - 1
            if game_choice == len(arcade.games):
                break
            if arcade.play_game(game_choice):
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != 'y':
                    break
    elif choice == 3:
        arcade.tickets = ticket_booth.exchange_tickets(arcade.tickets)
        while True:
            buy_more = input("Do you want to buy more prizes? (y/n): ")
            if buy_more.lower() == 'n':
                break
            elif buy_more.lower() == 'y':
                arcade.tickets = ticket_booth.exchange_tickets(arcade.tickets)
            else:
                print("Invalid choice! Please enter 'y' or 'n'.")
    elif choice == 4:
        print("Thank you for playing!")
        break
