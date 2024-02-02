


input = [[('5/1', 100), ('5/5', 200)], # Company1
 [('5/5', 50), ('5/8', 100)],  # Company2
 [('5/1', 200), ('5/8', 100)]] # Company3


def calculate_shares_amount(input):

  shares_by_days = {}
  prev_value = {i: 0 for i in range(len(input))}
  res = []

  for i in range(len(input)):
    for day,shares in input[i]:
      if day not in shares_by_days:
        shares_by_days[day] = [-1] * len(input)
      shares_by_days[day][i] = shares

  days = list(shares_by_days.keys())
  days.sort()

  for day in days:
    sum = 0
    for i in range(len(input)):
      if shares_by_days[day][i] == -1:
        sum += prev_value[i]
      else:
        sum += shares_by_days[day][i]
        prev_value[i] = shares_by_days[day][i]
    res.append((day,sum))

  return res


print(calculate_shares_amount(input))
