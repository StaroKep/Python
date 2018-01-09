# Высота башни
n = int(input())

# x - начальная башня
# y - конечная башня
def move(n, x, y):
    if height >= 1:
        # Определим среднюю (неиспользуемую) башню ( m - middle )
        if (x == 1 and y == 2) or (x == 2 and y == 1): m = 3
        elif (x == 1 and y == 3) or (x == 3 and y == 1): m = 2
        else: m = 1

        move(n-1, x, y)
        moveDisk(x, y)
        move(n-1, m, y)



def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")
