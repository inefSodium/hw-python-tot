from typing import TypeVar, List

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)

KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    return {value: key for key, value in d.items()}


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, List[KT]]:

    result: dict[KV, List[KT]] = {}
    
    for key, value in d.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    
    return result