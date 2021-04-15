def make_chocolate(small, big, goal):
  if goal > small + 5*big or goal % 5 > small:
    return -1
  return goal - 5*min(goal//5, big)
