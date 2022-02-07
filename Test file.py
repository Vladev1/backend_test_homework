from typing import Sequence

def lower_join(seq: Sequence[str]) -> Sequence[str]:
    """Принимает на вход последовательность и создаёт из неё  
    строку в нижнем регистре."""
    return ''.join(seq).lower()
lower_join("Раз")