def binarySearch(number, start, end, count):
    count += 1 # увеличиваем счетчик попыток на единицу
    midpoint = (start + end)//2   # середина интервала   

    if midpoint == number: #если середина интервала равна искомому числу, то число найдено за count попыток.
        return count #Возвращаем число попыток, за которое было найдено искомое число


    elif midpoint < number: #если середина интервала меньше, чем искомое число,
        return(binarySearch(number, midpoint, end, count)) #меняем нижнюю границу интервала (уменьшаем на половину интервал поиска)


    else: #если середина интервала больше, чем искомое число,
        return(binarySearch(number, start, midpoint, count)) #меняем верхнюю границу интервала (уменьшаем на половину интервал поиска)
    
def game_core_v3(number):
    
    count = 0 # счетчик попыток
    #устанавливаем границы поиска:
    start = 1 
    end = 100
    if number < 1 or number > 100:
        print('Заганное число не подходит под условия игры')
        return(0)
    
    return(binarySearch(number, start, end + 1, count)) #используем бинарный поиск
	
	