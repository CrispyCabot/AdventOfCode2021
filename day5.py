#day5
def main():
  lines = open('day5.txt', 'r').readlines()
  for index, line in enumerate(lines):
    lines[index] = line.strip()
  pointsCovered = {}
  for line in lines:
    # print(line)
    vals = line.split('->')
    x1, y1 = map(int, vals[0].split(','))
    x2, y2 = map(int, vals[1].split(','))
    #make sure it's horizontal or vertical
    if not (x1 == x2 or y1 == y2):
      #diagonal
      y = y1
      positive = x1 < x2
      for x in range(x1, x2+1 if positive else x2-1, 1 if positive else -1):
        if str([x, y]) in pointsCovered:
          pointsCovered[str([x,y])] += 1
        else:
          pointsCovered[str([x, y])] = 1 
        if y < y2:
          y += 1
        else:
          y -= 1
      continue
    #get all x's
    for x in range(min(x1, x2), max(x1, x2)+1):
      #get all ys
      for y in range(min(y1, y2), max(y1, y2)+1):
        if str([x, y]) in pointsCovered:
          pointsCovered[str([x,y])] += 1
        else:
          pointsCovered[str([x, y])] = 1 

  count = 0
  for key in pointsCovered:
    if pointsCovered[key] > 1:
      count += 1
  print(count)
main()