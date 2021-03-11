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

def dupes(a, b):
	"""Check for duplicated accounts"""
	if a == b:
		b = get_account()


score = 0
account_a = get_account()
account_b = get_account()

while True:
	followers_a = get_followers(account_a)
	followers_b = get_followers(account_b)

	print(f"Compare A: {format_data(account_a)}")
	print(f"Against B: {format_data(account_b)}\n")

	guess = input("Who have more followers? Type 'A' or 'B': \n").lower()

	checker = check_guess(guess, followers_a, followers_b)



	if checker:
		score = score_control(checker, score)
		print(f"You guessed right ! Current score: {score}\n")
		if checker and guess == 'a':
			account_b = get_account()
			dupes(account_a, account_b)
		else:
			if checker and guess == 'b':
				account_a = account_b
				account_b = get_account()
				dupes(account_a, account_b)
	else:
		score = score_control(checker, score)
		print(f"You guessed wrong ! Final score: {score}\n")	
		
		play_again = input( 'Play again? "Y" or "N" ').lower()
		if play_again == "n":
			break
		else:
			account_a = get_account()
			account_b = get_account()
			dupes(account_a, account_b)
			score = 0
