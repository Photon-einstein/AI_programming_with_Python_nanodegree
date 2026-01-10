import pandas as pd

# DO NOT CHANGE THE VARIABLE NAMES

# Given a list representing a few planets
planets = ["Earth", "Saturn", "Venus", "Mars", "Jupiter"]

# Given another list representing the distance of each of these planets from the Sun
# The distance from the Sun is in units of 10^6 km
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]

# TO DO: Create a Pandas Series "dist_planets" using the lists above, representing the distance of the planet from the Sun.
# Use the `distance_from_sun` as your data, and `planets` as your index.
dist_planets = pd.Series(data=distance_from_sun, index=planets)

# TO DO: Calculate the time (minutes) it takes light from the Sun to reach each planet.
# You can do this by dividing each planet's distance from the Sun by the speed of light.
# Use the speed of light, c = 18, since light travels 18 x 10^6 km/minute.
c = 18  # 10^6 km/minute units
time_light = dist_planets / c

# TO DO: Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[time_light < 40]

### Notebook grading
import math

distance_from_sun1 = [149.6, 1433.5, 108.2, 227.9, 778.6]
planets1 = ["Earth", "Saturn", "Venus", "Mars", "Jupiter"]
dist_planets1 = pd.Series(data=distance_from_sun, index=planets)
time_light1 = dist_planets1 / 18
close_planets1 = time_light1[time_light1 < 40]

if not dist_planets1.equals(dist_planets):
    print("dist_planets is incorrect")
elif not time_light1.equals(time_light):
    print(
        "time_light is incorrect. Verify that it is created by dividing dist_planets by 18."
    )
elif not close_planets1.equals(close_planets):
    print(
        "close_planets is incorrect. Verify that `close_planets` is created by using `time_light < 40` as a boolean index in `time_light`"
    )
else:
    print("Nice work!")
