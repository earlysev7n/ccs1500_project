import random

class Arcade:
    
    def __init__(self):
        self.money = 0
        self.tokens = 0
        self.tickets = 0
        self.games = [Basketball(), LuckyNine(),Fishing()]
        self.token_prices = [1, 3, 5]  
    
    def add_money(self, amount):
        if self.money + amount > 100:
            print("Invalid Amount!")
            return False
        
        self.money += amount
        return True
    
    def buy_token(self, token_price_index=0):
        num_tokens = int(input("How many tokens do you want to buy?: "))
        token_price = self.token_prices[token_price_index]
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

class Basketball(Game):
    def __init__(self):
        super().__init__(1)
    
    def play(self):
        points = random.choice([0, 0, 0, 1, 2, 3])
        if points > 0:
            return "You won! You scored {} points.".format(points), points
        else:
            return "You lost! Better luck next time.", 0
        
class LuckyNine(Game):
    def __init__(self):
        super().__init__(3)
    
    def play(self):
        user_card = random.randint(1, 9)
        computer_card = random.randint(1, 9)
        if user_card > computer_card:
            return f"You won! Your card ({user_card}) is higher than the computer's card ({computer_card}).", 5
        elif user_card < computer_card:
            return f"You lost! Your card ({user_card}) is lower than the computer's card ({computer_card}).", 0
        else:
            return f"It's a draw! Your card and the computer's card are both {user_card}.", 0

class Fishing(Game):
    def __init__(self):
        super().__init__(5)
        self.fish_types = ['Trash', 'Worm', 'Salmon', 'Bass', 'Catfish','Tilapia', 'Legendary Bangus']
    
    def play(self):
        fish = random.choice(self.fish_types)
        if fish in ['Trash', 'Worm']:
            return f"You lost! You caught a {fish}.", 0
        else:
            tickets_won = 1 if fish in ['Salmon', 'Bass'] else 2 if fish == 'Catfish' else 5 if fish == 'Tilapia' else 50
            return f"You won! You caught a {fish}.", tickets_won

class TicketBooth:
    def __init__(self):
        self.prizes = {1: "Toy Car", 2: "Teddy Bear", 3: "iPhone"}
        self.prize_costs = {1: 5, 2: 10, 3: 100}
    
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

#usage
arcade = Arcade()
ticket_booth = TicketBooth()

while True:
    print("\nWelcome to the Arcade!")
    print("Money: $", arcade.money)
    print("Tokens: ", arcade.tokens)
    print("Tickets: ", arcade.tickets)
    print("1. Add money")
    print("2. Buy token")
    print("3. Play game")
    print("4. Go to Ticket Booth")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter the amount to add: "))
        arcade.add_money(amount)
    elif choice == 2:
        if arcade.buy_token(2):
            print("Token bought successfully!")
    elif choice == 3:
        while True:
            print("\nGames:")
            for i, game in enumerate(arcade.games):
                print(f"{i+1}. {game.__class__.__name__} - Token Price: ${arcade.token_prices[i]}")
            print(f"{len(arcade.games)+1}. Exit")
            game_choice = int(input("Enter the game number: ")) - 1
            if game_choice == len(arcade.games):
                break
            if arcade.play_game(game_choice):
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != 'y':
                    break
    elif choice == 4:
        arcade.tickets = ticket_booth.exchange_tickets(arcade.tickets)
        while True:
            buy_more = input("Do you want to buy more prizes? (y/n): ")
            if buy_more.lower() == 'n':
                break
            elif buy_more.lower() == 'y':
                arcade.tickets = ticket_booth.exchange_tickets(arcade.tickets)
            else:
                print("Invalid choice! Please enter 'y' or 'n'.")
    elif choice == 5:
        print("Thank you for playing!")
        break

