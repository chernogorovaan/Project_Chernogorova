try:
    N = int(input("Введите число N (>1): "))
    
    if N <= 1:
        print("Ошибка: N должно быть больше 1")
    else:
        K = 0 
        current_sum = 0 
       
        while current_sum < N:
            K += 1              
            current_sum += K    
        
        print(f"Наименьшее K: {K}")
        print(f"Сумма 1 + 2 + ... + {K} = {current_sum}")

except ValueError:
    print("Ошибка: Введите целое число!")