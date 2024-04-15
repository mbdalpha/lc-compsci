import math
import matplotlib.pyplot as plt

class catapult_model:
    def __init__(self, angle, speed):
        self.i = math.cos(math.radians(angle)) * speed
        self.j = math.sin(math.radians(angle)) * speed
        self.x = 0
        self.y = 0

    def run(self, steps_per_second):
        xs = [self.x]
        ys = [self.y]

        while self.y >= 0:
            self.x += self.i / steps_per_second
            self.y += self.j / steps_per_second

            self.i -= 5 /steps_per_second
            self.j -= 9.8 / steps_per_second

            xs.append(self.x)
            ys.append(self.y)

        return xs, ys

    def exact(self):
        return self.i * self.j / 4.9

eg1 = catapult_model(60, 40)
print("Traveled", eg1.exact())
xs, ys = eg1.run(10)

fig, ax = plt.subplots()
ax.plot(xs, ys, marker="o")
ax.axhline(y=0)
plt.show()