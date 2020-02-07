from jobs import *
import math
import random

# 게임 진행 스크립트
# 마피아 = -1, 시민 = 0, 의사 = 1, 경찰 = 2

# 마피아는 매일 밤 시민 중 1명을 공격, 경찰 발견시 우선 공격.
# 시민은 첫날을 제외하고 매일 낮 임의 1명에게 투표, 마피아 발견시 마피아에게 투표.
# 의사는 매일 밤 자기 자신을 치료. 단, 경찰이 있을 경우 경찰 치료.
# 경찰은 매일 밤 1명을 조사. 마피아 발견시 경찰임을 선언하고 마피아를 지목.

def playGame(PAR):
    table = []
    alive = []
    for i in range(0, PAR):
        table.append(0)
        alive.append(True)
    num_mafia = int(math.sqrt(PAR))
    initialSetting(table, PAR, num_mafia)
    print("게임을 시작합니다.")


def initialSetting(table, PAR, num_mafia):
    num_police = 1
    num_doctor = 1

    print("이 게임에는 %d명이 참여합니다." %PAR)
    print("마피아는 %d명입니다." %num_mafia)

    mafia_seed = -1
    print("마피아를 뽑습니다.")
    for i in range(0, num_mafia):
        while True:
            mafia_seed = random.randint(0, PAR-1)
            if table[mafia_seed] == 0:
                break
        print("%d번님이 마피아가 되었습니다." %mafia_seed)
        table[mafia_seed] = -1
    
    print("의사를 뽑습니다.")
    while True:
        mafia_seed = random.randint(0, PAR-1)
        if table[mafia_seed] == 0:
            break
    print("%d번님이 의사가 되었습니다." %mafia_seed)
    table[mafia_seed] = 1

    print("경찰을 뽑습니다.")
    while True:
        mafia_seed = random.randint(0, PAR-1)
        if table[mafia_seed] == 0:
            break
    print("%d번님이 경찰이 되었습니다." %mafia_seed)
    table[mafia_seed] = 2