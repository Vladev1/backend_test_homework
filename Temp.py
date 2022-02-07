class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
    training_type: str,
    duration: float,
    distance: float,
    speed: float,
    calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        Message: str = (f"Тип тренировки: {self.training_type};" 
        f"Длительность: {self.duration} ч.;" 
        f"Дистанция: {self.distance} км"
        f"Ср. скорость: {self.speed} км/ч;"
        f"Потрачено ккал: {self.calories}.")
        return Message
        
    def show_training_info(self):
        print(f"{self.get_message}")

InfoMessage("1",2,3,4,5)