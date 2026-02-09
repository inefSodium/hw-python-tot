__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:

    days = seconds // 86400  
    hours = (seconds % 86400) // 3600  
    minutes = (seconds % 3600) // 60  
    sec = seconds % 60  

    result = ""
    
    if days > 0:
        result += f"{days:02d}d"
    if days > 0 or hours > 0:
        result += f"{hours:02d}h"
    if days > 0 or hours > 0 or minutes > 0:
        result += f"{minutes:02d}m"
    if result:
        result += f"{sec:02d}s"
    else:
        result += f"{sec}s"
    
    return result
