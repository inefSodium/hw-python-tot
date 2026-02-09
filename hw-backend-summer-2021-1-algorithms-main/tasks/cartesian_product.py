from typing import TypeVar

__all__ = ("cartesian_product",)

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def cartesian_product(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    result = []
    for item1 in arr1:
        for item2 in arr2:
            result.append((item1, item2))
    
    return result
