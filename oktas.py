def calcOktas(pct):
  if pct == 0:
    return 0
  elif pct < 18.75:
    return 1
  elif pct < 31.25:
    return 2
  elif pct < 43.75:
    return 3
  elif pct < 56.25:
    return 4
  elif pct < 68.75:
    return 5
  elif pct < 81.25:
    return 6
  elif pct < 100:
    return 7
  elif pct == 100:
    return 8