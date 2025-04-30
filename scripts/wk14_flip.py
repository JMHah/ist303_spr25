# flip a 

from random import randint

def coinflip(numflips=1):
  result_list = [] #store all results for later calcs
  current_streak = []
  longest_streak = []
  count = 0
  while count < numflips:
    flip_result = randint(0,1)
    if flip_result == 1:
      flip_result_str = "Heads"
      print(flip_result_str)
    else:
      flip_result_str = "Tails"
      print(flip_result_str)
    count += 1
    result_list.append(flip_result)
    if len(result_list) <= 1:
      current_streak.append(flip_result)
      longest_streak.append(flip_result)
    else:
      if flip_result == result_list[-2]:
        current_streak.append(flip_result)
        if len(current_streak) > len(longest_streak):
          longest_streak = current_streak
      else:
        current_streak = [flip_result]
  else:
    print(f'average coin flip result is {round(sum(result_list)/numflips,4)}')
    if sum(longest_streak) == 0:
      streak_type = "Tails"
    else:
      streak_type = "Heads"
    print(f'your longest streak was {len(longest_streak)} {streak_type}')
    print(f'you ended on a streak of {len(current_streak)} {flip_result_str}')