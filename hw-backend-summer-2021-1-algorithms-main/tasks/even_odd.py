__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных чисел к сумме нечетных чисел."""
    b = 0 
    c = 0 
    
    for num in numbers:
        if num % 2 == 0:  
            b += num
        else:            
            c += num
    
    if sum_odd == 0:
        return 0.0
    
    return b / c
