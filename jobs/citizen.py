from . import person

class citizen(person):
    # thinkNights 작성하지 않음. 밤에 할 수 있는 행동이 없으므로...

    # 시민은 첫날을 제외하고 매일 낮 임의 1명에게 투표, 마피아 발견시 마피아에게 투표.
    def thinkDays(self, Aggro = -1):
        if Aggro > 0:
            return Aggro
        # PAR = 12
        return pickRandom(12)


