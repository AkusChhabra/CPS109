import math

# Problem 1 ––––––––––––––––––––––––

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = "" 
    return "DCB"[tens - 5] + adjust


# Problem 2 ––––––––––––––––––––––––
# 6-7 seconds

def is_ascending(items):
  
  con = False

  for i in range(1, len(items)):

    if not items:
      con = True
    elif ( items[i] > items[i-1] ):
      con = True
    elif ( items[i] < items[i-1] ):
      con = False
      break
    elif ( items[i] == items[i-1]):
      con = False
      break
    else:
      break

  return con


# Problem 3 ––––––––––––––––––––––––
# 0 seconds

def riffle(items, out=True):

  l1 = items[0:len(items)//2]
  l2 = items[len(items)//2:len(items)]
  l3 = list(range(len(items)))

  count, j = 0, 0

  for i in range(0, len(items)):
    if i%2 == 1 and out == True:
      l3[i] = l2[j]
      count += 1
    if i%2 == 0 and out == True:
      l3[i] = l1[j]
      count += 1
    if i%2 == 1 and out == False:
      l3[i] = l1[j]
      count += 1
    if i%2 == 0 and out == False:
      l3[i] = l2[j]
      count += 1
    if count%2 == 0:
      j += 1

  return l3


# Problem 4 ––––––––––––––––––––––––
# 3-4 seconds

def only_odd_digits(n):

  numList = [int(i) for i in str(n)]
  con = True

  for i in range(len(numList)):
    if numList[i]%2 == 0:
      con = False

  return con


# Problem 5 ––––––––––––––––––––––––
# 2-3 seconds

def is_cyclops(n):

  numList = [int(i) for i in str(n)]

  if len(numList)%2 == 0:
    return False
  if numList[len(numList)//2] != 0:
    return False

  count = 0

  for i in range(0, len(numList)):
    if numList[i] == 0:
      count += 1

  if count >= 2:
    return False
  else:
    return True


# Problem 6 ––––––––––––––––––––––––
# 3-4 seconds

def domino_cycle(tiles):

  con = True

  if not tiles: # Empty Tuple
    return True
  if tiles[0][0] != tiles[len(tiles)-1][1]: # End Case
    return False

  # Test Inner Tile Equivalence
  for i in range(1, len(tiles)):
      if tiles[i][0] != tiles[i-1][1]:
        con = False
        break

  return con


# Problem 7 –––––––––––––––––––––––– 

def count_dominators(items):

  if not items:
    return 0

  check, counter, result, temp = 0, 0, False, 0

  for i in range(1, len(items)): 
    if items[i] == items[0]:
      temp += 1
    if temp == len(items):
      return 1

  for i in range(0, len(items)):
    mx = items[i]
    if i == len(items)-1:
      counter += 1
      break
    if i < len(items):
      listNew = items[i+1:len(items)]
      testMax = max(listNew)

      if mx > testMax:
        result = True
      if mx <= testMax:
        result = False
      if result == True:
        check = 1
      if result == False:
        check = 0

    counter += check

  return counter


# Problem 8 ––––––––––––––––––––––––
# 

def extract_increasing(digits): 

  if digits == '':
    return ''
  if len(digits) == 1:
    return digits

  mx, extract, d, current, test, j = int(digits[0]), [], 0, -1, 1, 0

  for i in range(1, len(digits)):
    
#    print('\nmx:',  mx)
#    print('current:', current)
#    print('digits[i]:', int(digits[i]))
#    print('test:', test)

    if i+1 == len(digits):
      extract.append(mx)
      break
    if mx < int(digits[i]) and test == 1:
      extract.append(mx)
      mx = int(digits[i])
    elif mx >= current:
      if j > 0:
        d = int(digits[i+1])
        current = 10*current + d
      if j == 0:
        d = int(digits[i+1])
        current = 10*int(digits[i]) + d
        j += 1
      test = 0
    elif mx < current:
      extract.append(mx)
      mx = current
      current = -1
      test = 1
      j = 0
  
  if current > mx:
    extract.append(current)

  return extract


# Problem 9 ––––––––––––––––––––––––
# 32 seconds

def words_with_letters(words, letters):
  extract, i = [], 0

  for i in range(len(words)):
    testIter = iter(words[i])
    if all(k in testIter for k in letters):
      extract.append(words[i])

  return extract


# Problem 10 ––––––––––––––––––––––––
# 

def taxi_zum_zum(moves):
  # key: + rotation = CCW
  # +x and +y right and up respectively

  x, y, dir, coord = 0, 0, 90, ()
# print(moves)
  for i in range(len(moves)):
# print(dir)
    while dir > 360 or dir < -360:
      if dir > 360:
        dir = dir - 360
      if dir < -360:
        dir = 360 + dir 

    if moves[i] == 'R':
      dir -= 90
    if moves[i] == 'L':
      dir += 90
    elif moves[i] == 'F':
      if dir == 0 or dir == 360 or dir == -360:
        x += 1
        y += 0
      if dir == 90 or dir == -270:
        x += 0
        y += 1
      if dir == 180 or dir == -180:
        x += -1
        y += 0
      if dir == 270 or dir == -90:
        x += 0
        y += -1

  return (x, y)


# Problem 11 ––––––––––––––––––––––––
# 

def give_change(amount, coins):

  extract = []

#  print('\n\n')
#  print(amount, coins)

  for i in range(len(coins)):
#    print('\ncoin[i]:', coins[i])
#    print('Difference:', amount - coins[i])
    if amount == 0:
      break
    while amount >= coins[i] or amount - coins[i] == 0:
#      print('Interloop Amount:', amount)
#      print('Interloop Difference:', amount - coins[i])
      amount -= coins[i]
      extract.append(coins[i])
      if amount < coins[i]:
#        print('Amount (broke loop):', amount)
        break

  return extract


# Problem 12 ––––––––––––––––––––––––
# 1 second

def safe_squares_rooks(n, rooks):

  if rooks == []:
    return n**2

  total, row, col = n**2, set(), set()

  for i in range(len(rooks)):
    for j in range(len(rooks[i])):
      if j % 2 == 0:
        row.add(rooks[i][j])
      if j % 2 == 1:
        col.add(rooks[i][j])
  
  return (n - len(row))*(n-len(col))




# Problem 13 ––––––––––––––––––––––––
# 

def pancake_scramble(text):

  n, current = len(text), text

  for i in range(2, n):
    if i % 2 == 0: # odd
      tempList = current[0:i]
      remain = current[i:]
      tempRev = tempList[::-1]
      current = ''
      current = tempRev + remain
#      print('Current:', current)
#      print('TempRev:', tempRev)
#      print('Remain:', remain)

    if i % 2 == 1: # even
      if i == n:
        remain = current[:]
        tempList = current[0:i//2] + current[i//2:]
      else:
        remain = current[i:]
        tempList = current[0:i//2] + current[i//2:i]
      tempRev = tempList[::-1]
      current = ''
      current = tempRev + remain
#      print('Current2:', current)
#      print('TempRev2:', tempRev)
#      print('Remain2:', remain)
  return current[::-1]



# Problem 14 ––––––––––––––––––––––––
# 40 seconds

def words_with_given_shape(words, shape):

  n, result = len(shape)+1, []

  for i in range(0, len(words)):
    check = []
    if n == len(words[i]):
      for j in range(1, len(words[i])):
        lower, upper = words[i][j-1], words[i][j]
        if lower > upper:
          check.append(-1)
        elif lower < upper:
          check.append(1)
        else:
          check.append(0)
        if check[j-1] != shape[j-1]:
          break
        if check[-1] == shape[-1] and len(check) == len(shape):
          result.append(words[i]) 
        else:
          continue

  return result


# Problem 15 ––––––––––––––––––––––––
# 0 seconds

def is_left_handed(pips):

  pips = list(pips)

  opp, hold, k = [], [], 0
  leftDice = [[4,4,4,4],[6,5,1,2], [3,3,3,3]]

  if 3 in pips:
    while pips[0] != 3:
      pips = pips[-1:] + pips[:-1]
  if 4 in pips:
    while pips[0] != 4:
      pips = pips[-1:] + pips[:-1]

  for i in range(len(pips)):
    for j in range(len(leftDice[0])):
      if pips[i] == leftDice[1][j]: # other numbers
        hold.append(1)
      if pips[i] == leftDice[2][j]: # number 3
        hold.append(2)
        break
      if pips[i] == leftDice[0][j]: # number 4
        hold.append(0)
        break

  if 3 in pips:
    for j in range(len(leftDice[1])):
      if pips[1] == leftDice[1][j]:
        k = j
  if 4 in pips:
    for j in range(len(leftDice[1])):
      if pips[1] == leftDice[1][j]:
        k = j

  # Three (3)
  if 3 in pips:
    if pips[2] == leftDice[1][k-1] and hold[0] == 2:
      return False
    elif k == 3 and pips[2] == leftDice[1][0] and hold[0] == 2:
      return True
    elif k == 0 and pips[2] == leftDice[1][3] and hold[0] == 2:
      return True
    elif pips[2] == leftDice[1][k+1] and hold[0] == 2:
      return True

  # Four (4)
  if 4 in pips:
    if pips[2] == leftDice[1][k-1] and hold[0] == 0:
      return True
    elif k == 3 and pips[2] == leftDice[1][0] and hold[0] == 0:
      return False
    elif k == 0 and pips[2] == leftDice[1][3] and hold[0] == 0:
      return False
    elif pips[2] == leftDice[1][k+1] and hold[0] == 0:
      return False
    else:
      False


# Problem 16 ––––––––––––––––––––––––
# 1-3 seconds

def winning_card(cards, trump=None):

  deck, numbers, iterNum, count, suit = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace'], [], [], 0, trump

  if trump == None:
    suit = cards[0][1]

  for i in range(len(cards)):
    if cards[i][1] == suit:
      numbers.append(cards[i][0])
    if cards[i][1] != suit:
      count += 1

  if count == 4:
    suit = cards[0][1]
    for i in range(len(cards)):
      if cards[i][1] == suit:
        numbers.append(cards[i][0])

  for i in range(len(numbers)):
    for j in range(len(deck)):
      if numbers[i] == deck[j]:
        iterNum.append(j)

  return (deck[max(iterNum)], suit)


# Problem 17 ––––––––––––––––––––––––
#

def create_zigzag(rows, cols, start=1):
  grid, n, = [], start

  for i in range(rows):
    grid.append(list(range(n, n + cols)))
    n = n + cols
  
  for i in range (1, rows, 2):
    grid[i].reverse()
  
  return grid





# Problem 20 ––––––––––––––––––––––––
# 0.5 seconds

def can_balance(items):

  for i in range(len(items)):
    current_sum = 0
    for j in range(len(items)):
      current_sum += (i-j) * items[j]
    if current_sum == 0:
      return i
  return -1


# Problem 21 –––––––––––––––––––––––– 
# 1.4 seconds

def josephus(n, k):
#  print('\n\n\nn:', n)
#  print('k:', k)
  if n == 1:
    return [1]

  pl, curr, res, hold, first = [i for i in range(1,n+1)], 0, [], 0, False
#  print('pl:', pl)

  k -= 1
  curr = k

  if k >= n:
#    print('active')
    hold = k % n
    first = True
#  print('hold:', hold)

  while len(pl) > 1:
    if first:
#      print('active2')
      curr = hold
      first = False
#    print('\nCURR:', curr)
    res.append(pl[curr])
    pl.pop(curr)
#    print('UPDATED PL ===', pl)
#    print('RES:', res)
    curr = (curr + k) % len(pl)
  res.append(pl[0])
#  print('FINAL RES', res)
  return res


# Problem 22 ––––––––––––––––––––––––
# 

def group_and_skip(n, out, ins):

  res = []

  while n != 0:
    leftover = n % out
    leftoverWhole = n//out
    res.append(leftover)
    n = leftoverWhole*ins

  return res


# Problem 23 ––––––––––––––––––––––––
# 0.2 seconds

def recaman(n):

  res, final = {0}, []

  if n == 0:
    return res

  last = 0

  for i in range(1,n+1):
    current = last - i 
    if current > 0 and current not in res:
      res.add(current)
    else:
      current = last + i
      res.add(current)
    final.append(current)
    last = current

  return final


# Problem 24 ––––––––––––––––––––––––
# 2 seconds

def pyramid_blocks(n, m, h):

  count = 0

  for i in range(h):
    count += n*m
    n += 1
    m += 1
  return count


# Problem 25 ––––––––––––––––––––––––
# 8 seconds

def count_growlers(animals):
  
  res = 0

  if not animals:
    return 0

  for i in range(len(animals)):
    cats, dogs = 0, 0
    if animals[i] == 'tac' or animals[i] == 'god': # Facing Right
      for j in range(i+1, len(animals)):
        if animals[j] == 'cat' or animals[j] == 'tac':
          cats += 1
        if animals[j] == 'dog' or animals[j] == 'god':
          dogs += 1
      if dogs > cats:
        res += 1
    if animals[i] == 'cat' or animals[i] == 'dog': # Facing Left
      for j in range(i):
        if animals[j] == 'cat' or animals[j] == 'tac':
          cats += 1
        if animals[j] == 'dog' or animals[j] == 'god':
          dogs += 1
      if dogs > cats:
        res += 1

  return res


# Problem 26 –––––––––––––––––––––––– 
#

def bulgarian_solitaire(piles, k):
  goal = list(range(1, k+1))
  count = 0

  while True:
    if (sorted(piles) == goal):
      return count
    
    piles = [p-1 for p in piles if p > 1] + [len(piles)]
    count += 1





# Problem 29 ––––––––––––––––––––––––
# 3.5 seconds

def tukeys_ninthers(items):

  res = []

  if len(items) == 1:
    return items[0]

  for i in range(0, len(items), 3):
    a, b, c = items[i], items[i+1], items[i+2]

    if b > c and b < a:
      res.append(b)
    if c > b and c < a:
      res.append(c)
    if a > c and a < b:
      res.append(a)
    if c > a and c < b:
      res.append(c)
    if a > b and a < c:
      res.append(a)
    if b > a and b < c:
      res.append(b)

  return tukeys_ninthers(res)


# Problem 30 ––––––––––––––––––––––––
# 0.1 seconds

def is_zigzag(n): 

  check, count = False, 0
  li = [int(i) for i in str(n)]

  if len(li) == 1:
    return True

  for i in range(1, len(li)):
    if li[0] < li[1]:
      if i % 2 == 1 and li[i] > li[i-1]:
        count += 1
      if i % 2 == 0 and li[i] < li[i-1]:
        count += 1
    if li[0] > li[1]:
      if i % 2 == 1 and li[i] < li[i-1]:
        count += 1
      if i % 2 == 0 and li[i] > li[i-1]:
        count += 1

  if count == len(li)-1:
    check = True

  return check


# Problem 32 ––––––––––––––––––––––––
# 30 seconds

def two_summers(items, goal):
  smaller, larger = 0, len(items)-1

  while smaller < larger:
    s = items[smaller] + items[larger]

    if s > goal:
      larger -= 1
    elif s < goal:
      smaller += 1
    else:
      return True
  
  return False

def three_summers(items, goal):

  for i in range(len(items)):
    temp = items[:]
    del(temp[i])

    if (two_summers(temp, goal - items[i])):
      return True
  return False


# Problem 33 ––––––––––––––––––––––––
# 1 second

def sum_of_two_squares(n): 

  sq, x, tup = set(), math.trunc(math.sqrt(n)), ()

  for i in range(1, x+1):

    square = i*i
    sq.add(square)
    
    if (n - square) in sq:
      tup = (i,  math.trunc((math.sqrt(n - square))))

  if tup:
    return tup
  else: 
    return None


# Problem 34 ––––––––––––––––––––––––
# 1 second

def count_carries(a, b):

  if a >= b:
    large = a
    lower = b
  if a < b:
    large = b
    lower = a

  li = [int(i) for i in str(large)]

  current, ones =  0, 0

  for i in range(len(li)): 
    if (large % 10) + (lower % 10) + current >= 10:
      current = ((large % 10) + (lower % 10) + current) // 10
      ones += 1
    else:
      current = 0
    large = large // 10
    lower = lower // 10

  return ones


# Problem 35 ––––––––––––––––––––––––
# 

def expand_intervals(intervals):

  res = []

  for interval in intervals.split(','):
    parts = interval.partition('-')

    if parts[1] == '':
      res.append(int(parts[0]))
    else:
      i1 = int(parts[0])
      i2 = int(parts[2])
      res += list(range(i1, i2+1))
    
  return res


# Problem 36 ––––––––––––––––––––––––
# 2 seconds

def collapse_intervals(items):

  if not items:
    return ''
  if len(items) == 1:
    return str(items[0])

  res, start, end, first,  i = '', 0, 0, 1, 0

  while i < len(items):
    start = items[i]

    while i < len(items) - 1 and items[i+1] == items[i] + 1:
      i += 1
    end = items[i]
    
    if first == 1:
      first = 0
      if start == end:
        res += str(start)
      else:
        res += str(start) + '-' + str(end)
    else:
      if start == end:
        res += ',' + str(start)
      else:
        res += ',' + str(start) + '-' + str(end)
    i += 1

  return res


# Problem 37 –––––––––––––––––––––––– 
#

def reverse_reversed(items):

  if type(items) != list:
    return items
  else:
    res = []

    for e in items:
      item = reverse_reversed(e)
      res.append(item)  

    res.reverse()
    return res


# Problem 38 ––––––––––––––––––––––––
# 2 seconds

def count_word_dominators(words):

  counter = 0

  if len(words) == 1:
    return 1

  for i in range(1,len(words)):
    mx = words[i-1]
    count = 0
    newList = words[i:]
  
    for j in range(len(newList)):
      count = 0

      for k in range(len(newList[0])):
        if mx[k] > newList[j][k]:
          count += 1
      if count < len(newList[j]) // 2 + 1:
        break
    if count >= len(newList[j]) // 2 + 1:
      counter += 1

  return counter + 1


# Problem 39 ––––––––––––––––––––––––
# 0.1 seconds

def duplicate_digit_bonus(n):
  li = str(n)
  count, initial, total, calc = 1, li[0], 0, 0

  for i in range(1,len(li)):
    if initial == li[i]:
      count += 1
      if i+1 == len(li):
          total += 2*10**(count-2)
    else:
      if count >= 2:
          total += 10**(count-2)
      count = 1

    initial = li[i]

  return total


# Problem 40 ––––––––––––––––––––––––
# 6 seconds

def nearest_smaller(items):

  res, n = [], len(items)

  for i, e in enumerate(items):
    j = 1

    while j < n:
      if i >= j:
        left = items[i-j]
      else:
        left = e
      
      if i+j < n:
        right = items[i+j]
      else:
        right = e
      
      sm = min(left, right)
      
      if sm < e:
        res.append(sm)
        break

      j += 1

    else:
      res.append(e)
  
  return res


# Problem 41 ––––––––––––––––––––––––
# 3 seconds

def squares_intersect(s1, s2):

  x1, x2, y1, y2, l1, l2 = s1[0], s2[0], s1[1], s2[1], s1[2], s2[2]

  if x2 > x1:
    if x2-x1 > l1:
      return False
  if x1 > x2:
    if x1-x2 > l2:
      return False
  if y2 > y1:
    if y2 - y1 > l1:
      return False
  if y1 > y2:
    if y1 - y2 > l2:
      return False
  
  return True



# Problem 42 ––––––––––––––––––––––––
# 3 seconds

def oware_move(board, house):

  initial, last, i, capture = board[house], 0, house, False

  while board[house] > 0:
    board[i] += 1
    board[house] -= 1
    if board[house] == 0:
      last = i
      break
    elif i == len(board)-1:
      i = -1
    elif i == house:
      i += 1
      continue
    i += 1

  if last < len(board)//2:
    capture = False
  else:
    capture = True

  player = board[:len(board)//2]
  opponent = board[len(board)//2:]

  if capture == True and (board[last] == 2 or board[last] == 3):
    i = last-len(board)//2
    while i < len(opponent):
      val = opponent[i]
      if val == 2 or val == 3:
        opponent[i] = 0
      if val > 3 or val == 1:
        break
      if i == 0:
        break
      i -= 1
    board = player + opponent

  return board


# Problem 43 ––––––––––––––––––––––––
# 18 seconds

def remove_after_kth(items, k=1):

  if k == 0:
    return []

  li, res = set(items), []
  di = dict.fromkeys(li, 0)

  for i in range(len(items)):
    di[items[i]] += 1
    if di[items[i]] <= k:
      res.append(items[i])

  return res





# Problem 45 ––––––––––––––––––––––––
# 0 seconds

def count_consecutive_summers(n):

  count = 0

  for i in range((n//2)+1):
#    print('\ni:', i)
    temp = n-i*(i+1)//2
#    print('temp:', temp)
#    temp = (n - i*(i+1)//2)*(1/(i+1))
    if temp < 1:
      break
    elif temp % (i+1) == 0:
      count += 1

  return count


# Problem 47 ––––––––––––––––––––––––
# 29 seconds

def first_preceded_by_smaller(items, k=1):

#  print('\n\nITEMS ==', items)
#  print('k:', k)

  if len(items) == 1:
    return None

  mx = items[1]
  
  for i in range(1, len(items)):
    mx, count, countList, first = items[i], 0, [], 1
#    print('\nmx:', mx)
    for j in range(i, 0, -1):
#      print('items[j]:', items[j])
      if mx > items[0] and first == 1:
        count += 1
        countList.append(count)
        first = 0
#      print(count)
      if mx > items[j]:
        count += 1
        countList.append(count)
#      print(count)
#      print(countList)
      if k in countList:
        return mx
  return None


# Problem 48 ––––––––––––––––––––––––
# 39 seconds

def eliminate_neighbours(items):
#  print('\n\nitems:', items)

  if len(items) == 1 or len(items) == 2:
    return 1

  operation, elim, mx = 0, set(), max(items)

  for e in range(1, mx+1):
#    print('\ne:', e)
    if e in elim:
      continue
    if len(items) == 2 or len(items) == 1:
      return operation + 1
    j = items.index(e)
#    print('J VALUE:', j)
    if j == 0:
#      print('active')
      right = items[j+1]
      elim.add(right)
      elim.add(items[j])
      items.pop(j+1)
      items.pop(j)
      operation += 1
#      print('ITEMS UPDATED ==', items)
      if right == mx:
#        print('broken')
        break
      continue
    if j == len(items)-1:
#      print('active2')
      left = items[j-1]
      elim.add(left)
      elim.add(items[j])
      items.pop(j)
      items.pop(j-1)
      operation += 1
#      print('2ITEMS UPDATED ==', items)
      if left == mx:
#        print('broken')
        break
      continue
    else:
#      print('active3')
      right = items[j+1]
      left = items[j-1]   
#    print('left:', left)
#    print('right:', right)
    if right > left:
#      print('\nactive4')
      elim.add(right)
      elim.add(items[j])
      items.pop(j+1)
      items.pop(j)
      operation += 1
    else:
#      print('\nactive5')
      elim.add(left)
      elim.add(items[j])
      items.pop(j-1)
      items.pop(j-1)
      operation += 1
    if right == mx or left == mx:
#      print('broken')
      break
#    print('LAST ITEMS UPDATED ==', items)

  return operation


# Problem 49 ––––––––––––––––––––––––
# 3 seconds

def count_and_say(digits):
  if digits == '':
    return ''

  result = ''
  count = 1
  curr = digits[0]

  for c in digits[1:]:
    if c == curr:
      count += 1
    else:
      result += str(count) + curr
      curr = c
      count = 1

  result += str(count) + curr
  
  return result




# Problem 52 ––––––––––––––––––––––––
# 0.4 seconds

def counting_series(n):
#  print('\n\nN == ', n)

  if n < 9:
    return n + 1

  lower, upper, e = 0, 0, 1

  while upper < n:
    lower = upper
    upper += 9*e*(10**(e-1))
    e += 1
  e -= 1
#  print('\nupper:', upper)
#  print('lower:', lower)
#  print('e:', e)
#  print('\n\n')
  di = 10**(e-1) + (n-lower)//e
  digitIn = (n-lower) % e
#  print('di:', di)
#  print('Digit Index:', digitIn) 
  di = str(di)

  for i in range(len(di)):
    if i == digitIn:
      return di[i]


# Problem 53 ––––––––––––––––––––––––
# 

def reverse_vowels(text):
  res = ''
  vowels = [c for c in text if c in 'aeiouAEIOU']

  for c in text:
    if (c in 'aeiouAEIOU'):
      ch = vowels.pop()
      if c.isupper():
        ch = ch.upper()
      else:
        ch = ch.lower() 
      
      res += ch
    else: 
        res += c
  
  return res


# Problem 66 ––––––––––––––––––––––––
# 13 seconds

def reverse_ascending_sublists(items):

  res, curr = [], []

  it = items[:] + [None]

  for e in it:
    if e!= None and (curr == [] or curr[-1] < e):
      curr.append(e)
    else:
      curr.reverse()
      res += curr
      curr = [e] 

  return res


# Problem 67 ––––––––––––––––––––––––
# 0 seconds

def brangelina(first, second):
  groups = []
  inGroup = False

  for i in range(len(first)):
    if first[i] in 'aeiou' and not inGroup:
      groups.append(i)
      inGroup = True
    else:
      inGroup = False

  if len(groups) == 1:
    first = first[:groups[0]]
  else:
    first = first[:groups[-2]]

  i = 0
  while second[i] not in 'aeiou':
    i += 1
  second = second[i:]

  return first + second
  

# Problem 70 ––––––––––––––––––––––––
# 37 seconds

def autocorrect_word(word, words, df):
  best_dist = 100000
  best_word = ''

  for w in words:
    if len(w) == len(word):
      dist = 0
      for i in range(len(w)):
        c1 = w[i]
        c2 = word[i]
        dist += df(c1, c2)
      if dist < best_dist:
        best_dist = dist
        best_word = w

  return best_word


# Problem 76 –––––––––––––––––––––––– 
# 0 seconds

def count_divisibles_in_range(start, end, n):
#  print('\n\nStart:', start)
#  print('End:',end)
#  print('n:', n)
  diff = end//n - start//n
  if start % n == 0:
#    print('active 1')
    return diff + 1
  else:
#    print('active2')
    return diff


# Problem 88 ––––––––––––––––––––––––
# 0.3 seconds

__fibs = [1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_sum(n):
  while n > __fibs[-1]:
    __fibs.append(__fibs[-2] + __fibs[-1])
  
  res, j = [], len(__fibs) - 1

  while n > 0:
    if n >= __fibs[j]:
      n = n - __fibs[j]
      res.append(__fibs[j])
    j -= 1

  return res


# Problem 91 ––––––––––––––––––––––––
# 

def possible_words(words, pattern):

  lp, res = len(pattern), []

  for word in words:
    if len(word) != lp:
      continue
    
    for cw, cp in zip(word, pattern):

      if cp.isalpha() and cp != cw:
        break
      if cp == '*' and cw in pattern:
        break
      
    else:
      res.append(word)

  return res