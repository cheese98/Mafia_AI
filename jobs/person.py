import random

class Person:
    '''
    nick: 사람 번호 (자신의 이름)
    job: 직업 번호
    whitelist: 투표하지 않을 대상. 최초에 자기 자신을 추가.
    '''
    def __init__(self, nick, job):
        self.nick = nick
        self.job = job
        self.whitelist = []
        self.whitelist.append(nick)
    
    def thinkNights(self):
        pass

    def thinkDays(self):
        pass

    # TODO: 그때그때 PAR을 부르지 않고 전역변수화할 방법을 찾을 것
    def pickRandom(self, PAR):
        flag = True
        while flag:
            random_value = random.randint(0, PAR)
            flag =  random_value in self.whitelist
        return random_value

