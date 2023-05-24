
def find(A, weights, k ,s, result):
    if A[k][s] == 0:
        return result
    if A[k-1][s] == A[k][s]:
        find(A, weights, k-1, s, result)
    else:
        result.append(k-1)
        find(A, weights, k-1, s-weights[k-1], result)
        
def make_matrix(jews: list , max_weight):
    weights, prices = list(zip(*jews))
    count = len(weights)
    A = [ [0 for i in range(max_weight+1)] for i in range(count+1)]
    for k in range(0, count+1): # Проход по предметам
        for s in range(0, max_weight+1): # Проход по весам 
            if k == 0 or s == 0: 
                A[k][s] = 0 # Нули, потому что во вместимость нуль ничего не влезет :)
            else:
                if s >= weights[k-1]:
                    A[k][s] = max(A[k-1][s],A[k-1][s- weights[k-1]] + prices[k-1])
                    #Выбор элементов, если берем или не берем определенный элемент 
                else:
                    A[k][s] = A[k-1][s]
    result = []
    find(A, weights, count, max_weight,result)
    _ = [jews[i] for i in result]
    
    for i in _: jews.remove(i)
    
    return _

def find_result(jews, max_weight, repeats):
    result = []
    for i in range(repeats):
        result += make_matrix(jews, max_weight)
    return result, sum([i[1] for i in result])
             
weights = [3,4,5,8,9]
prices = [1,6,4,7,6]
jews = list(zip(weights, prices))

print(jews)
print('*' *80)
print('Использованные:', find_result(jews, 13, 2)[0])
print('*' *80)
print('Оставшиеся:',jews)

