def solve(numheads, numlegs):
  if numheads < 0 or numlegs < 0:
    raise ValueError("The number of heads and legs must be non-negative.")
  if numlegs % 2 != 0:
    raise ValueError("The number of legs must be even.")
  chickens = (numlegs - 2 * numheads) / 2
  rabbits = numheads - chickens

  if chickens < 0 or rabbits < 0:
    raise ValueError("There is no solution to this puzzle.")

  return int(chickens), int(rabbits)


if __name__ == "__main__":
  numheads = int(input("Enter the number of heads: "))
  numlegs = int(input("Enter the number of legs: "))
  chickens, rabbits = solve(numheads, numlegs)
  print("There are", chickens, "chickens and", rabbits, "rabbits.")