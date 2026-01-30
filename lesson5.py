class SoundEquipment:
    def switch_on(self):
        self.state = True

    def switch_off(self):
        self.state = False

class Microphone(SoundEquipment):
    def __init__(self,volume,state=False):
        if 10>=int(volume)>=0:
            self.volume=volume
        self.state = state
    def adjust_volume(self,vol):
        if 10>=int(vol)>=0:
            self.volume = vol
            print(f"Volume is now {self.volume}")

class Speaker(SoundEquipment):
    def __init__(self,bass,state=False):
        if 10>=int(bass)>=0:
            self.bass=bass
        self.state = state
    def adjust_bass(self,bas):
        if 10>=int(bas)>=0:
            self.bass = bas
            print(f"Bass level is now {self.bass}")


# Создаём объект микрофон с громкостью 5 состоянием "включен"
mic = Microphone(volume=5, state=True)
# Отключаем микрофон
mic.switch_off()
# Устаналиваем новый уровень громкости
mic.adjust_volume(7)

# Volume is now 7


# Создаём объект динамик с уровнем басов 7 и состоянием "выключен"
sp = Speaker(7, False)
# Включили динамик
sp.switch_on()
# Устанавливаем новый уровень басов
sp.adjust_bass(8)

# Bass level is now 8

print(Speaker(bass = 10, state = True).bass)
#10
