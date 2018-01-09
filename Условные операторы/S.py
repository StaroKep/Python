x1 = int(input())
y1 = int(input())
z1 = int(input())

x2 = int(input())
y2 = int(input())
z2 = int(input())

# Инициализируем переменные
n_x_x = x1 // x2
n_x_y = x1 // y2
n_x_z = x1 // z2

n_y_x = y1 // x2
n_y_y = y1 // y2
n_y_z = y1 // z2

n_z_x = z1 // x2
n_z_y = z1 // y2
n_z_z = z1 // z2

if (n_x_x > n_x_y) and (n_x_x > n_x_z):
    l = x2
    n_y_x = -1
    n_z_x = -1
elif (n_x_y > n_x_x) and (n_x_y > n_x_z):
    l = y2
    n_y_y = -1
    n_z_y = -1
else:
    l = z2
    n_y_z = -1
    n_z_z = -1

if (n_y_x > n_y_y) and (n_y_x > n_y_z):
    b = x2
    n_z_x = -1
elif (n_y_y > n_y_x) and (n_y_y > n_y_z):
    b = y2
    n_z_y = -1
else:
    b = z2
    n_z_z = -1

if (n_z_x > n_z_y) and (n_z_x > n_z_z):
    h = x2
elif (n_z_y > n_z_x) and (n_z_y > n_z_z):
    h = y2
else:
    h = z2

X = ((x1 // l) * l)
Y = ((y1 // b) * b)
Z = ((z1 // h) * h)
result = (X*Y*Z) // (x2*y2*z2)
print(result)
