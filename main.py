"""
Practice 1
A program which inputs arrow coordinates on a target and outputs the score.
Emma Gustafsson - January 2025
"""

import math

# Take coordinates and return the score it counts as on the target.

def arrow_score(coordinates, target_circles, target_radius) -> int:
  # Find distance.
  distance_rings: float = target_radius / target_circles
  coordinates = coordinates.replace("-", "")
  x, y = coordinates.split(" ")
  x: float = float(x)
  y: float = float(y)
  distance: float = math.sqrt(x ** 2 + y ** 2)
  # Check if arrow is outside of target.
  if distance > target_radius:
    return 0
  # Calculate score.
  arrow_ring: int = int(distance // distance_rings + 1)
  score: int = target_circles + 1 - arrow_ring
  return score


def main() -> None:
  
  # Define variables for score, dimensions of the target, and how many arrows are shot.

  total_score: int = 0
  arrows: int = 3
  target_circles: int = 10
  target_radius: float = 61.0
  
  # Calculate total score of all arrows added together.

  for _ in range (arrows):
    coordinates: str = input("")
    total_score += arrow_score(coordinates, target_circles, target_radius)
  
  # Print score.

  print(total_score)

if __name__ == "__main__":
  main()
  