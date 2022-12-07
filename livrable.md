```
h = [h1, ..., hn]
l = [l1, ..., ln]

A = (xa, ya, za)
B = (xb, yb, zb)
0 = theta
V = vitesse

robot = Robot(h, l)
robot.traj(A, B, 0, V)
```

```
Courbes pos, vit, acc:
-> s
-> x, y, z
-> q1 ... qn

Autres courbes:
-> 0
-> vitesse en O5
-> X(s) en 3D

```