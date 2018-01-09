n = int(input())

# Инициализация переменных
ten_tickets = 0
one_tickets = 0
# Очевидное количество билетов на 60 поездок
sixty_tickets = n//60

# Количество поездок < 60
n = n - sixty_tickets * 60

if n > 34:
    sixty_tickets += 1
else:
    # Очевидное количество билетов на 10 поездок
    ten_tickets = n//10
    
    # Количество поездок < 10
    n = n - ten_tickets * 10

    if n > 8:
        ten_tickets += 1
    else:
        one_tickets = n

print(one_tickets, ten_tickets, sixty_tickets)
