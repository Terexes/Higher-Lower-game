from game_data import data
import random



def get_account():
  """Get a account from game_data"""
  return random.choice(data)


def format_data(account):
  """Format data to give it more readability"""
  name = account['name']
  description = account['description']
  country = account['country']
  return f"{name} is a {description} from {country}."


def get_followers(account):
  return account['follower_count']


def check_guess(guess, followers_a, followers_b):
  """Check guessed answer returning a boolean value"""
  if followers_a > followers_b:
    return guess == 'a'
  else:
    if followers_b > followers_a:
      return guess == 'b'


def score_control(guess, score = 0):
  """Gives feedback of score based on right guesses"""
  if guess:
    score += 1
    return score
  else:
    return score

def game(account_a, account_b, score):
  """Runs the game"""
  if account_a == account_b:
    account_b = get_account()
  
  followers_a = get_followers(account_a)
  followers_b = get_followers(account_b)

  # Get user guess:
  print(f"Compare A: {format_data(account_a)}\n")
  print(f"Against B: {format_data(account_b)}\n")
  guess = input("Who have more followers? Type 'A' or 'B': ").lower()


  # Give feedback from guesses:
  ## Check guess:
  checker = check_guess(guess, followers_a, followers_b)
  if not checker:
   # Gives player feedback  
    print(f"You guessed wrong ! Final score: {score}")
    return
  else:
   # Score keeping:
   ## Temporary variable (temp) to store score_control value 
   temp = score_control(guess)
   score += temp
   print(f'Score: {score}')      
  
   continue_game = input('Keep playing? "Y" or "N": \n').lower   
   if continue_game == 'n':
    print("Thanks for playing !")
    return
   else:
    account_a = account_b
    account_b = get_account()
    return game(account_a, account_b, score)
  

account_a = get_account()
account_b = get_account()


keep_playing = False
score = 0
game(account_a, account_b, score)
