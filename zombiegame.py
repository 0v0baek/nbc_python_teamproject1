import random
import time
import os


class Character:

    def __init__(self, name, hp, normal_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.normal_power = normal_power


class Player(Character):

    def __init__(self, name, hp, sp, normal_power, magic_power):
        super().__init__(name, hp, normal_power)
        self.max_sp = sp
        self.sp = sp
        self.magic_power = magic_power
        self.level = 1

    def magic_attack(self, other):
        if self.sp < 5:
            print("마나가 부족합니다.")
            return
        self.sp -= 5
        damage = random.randint(self.magic_power, self.magic_power + 4)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 마법데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def player_status(self):
        print(
            f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, sp {self.sp}/{self.max_sp}")

    def level_up(self):
        self.level += 1
        self.max_hp += 100
        self.hp = self.max_hp
        self.max_sp += 5
        self.sp = self.max_sp
        self.normal_power += 20
        self.magic_power += 30


class Job(Player):
    def __init__(self, name, hp, sp, normal_power, skill_power, skill_cost, dodge):
        super().__init__(name, hp, sp, normal_power, skill_power)
        self.skill_cost = skill_cost
        self.dodge = dodge
    # 일반 공격

    def normal_attack(self, other):
        attack_power = random.randint(
            int(self.normal_power * 0.8), int(self.normal_power * 1.2))

        if random.random() < 0.7:
            attack_power *= 2
            other.hp = max(other.hp - attack_power, 0)
            print(
                f"{self.name}의 크리티컬 공격!! {other.name}에게 {attack_power}의 크리티컬 데미지를 입혔습니다.")
        # 공격
        else:
            other.hp = max(other.hp - attack_power, 0)
            print(f"{self.name}의 일반공격! {other.name}에게 {attack_power}의 일반데미지를 입혔습니다.")
            if other.hp == 0:
                print(f"{other.name}이(가) 쓰러졌습니다.")


job_list = [
    Job("백수", 100, 10, 100, 10, 1, 0.9),
    Job("소방관", 100, 10, 100, 10, 1, 0.9),
    Job("경찰관", 100, 10, 100, 10, 1, 0.9),
    Job("경비원", 100, 10, 100, 10, 1, 0.9),
    Job("주방장", 100, 10, 100, 10, 1, 0.9),
    Job("기술자", 100, 10, 100, 10, 1, 0.9),
    Job("의사", 100, 10, 100, 10, 1, 0.9),
    Job("트레이너", 100, 100, 10, 10, 1, 0.9),
    Job("군인", 100, 10, 100, 10, 1, 0.9),
    Job("선생님", 100, 10, 100, 10, 1, 0.9),
    Job("학생", 100, 10, 100, 10, 1, 0.9)
]


class Zombie(Character):

    def __init__(self, name, hp, normal_power):
        super().__init__(name, hp, normal_power)

    def zombie_status(self):
        if self.hp <= 0:
            print(f"{self.name}의 상태: 처치 완료")
        else:
            print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

    def bite(self, other):
        bite_damage = random.randint(
            int(self.normal_power * 0.8), int(self.normal_power * 1.2))
        if random.random() < 0.1:
            bite_damage *= 2
            print(f"좀비가 당신을 더 세게 물었습니다! hp가 {bite_damage}만큼 달았습니다.")
        else:
            other.hp -= bite_damage
            print(f"좀비가 당신을 물었습니다! hp가 {bite_damage}만큼 달았습니다.")


class Stage:

    def __init__(self, name, level, zombies):
        self.name = name
        self.level = level
        self.zombies = zombies


print("=== 게임 시작 ===")
print("당신의 직업을 추첨합니다")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
player = random.choice(job_list)
print(f"당신의 직업은 {player.name}입니다.")
time.sleep(1)

stages = [
    Stage("stage 1", 1, [Zombie("일반 좀비", 30, 5), Zombie("경찰 좀비", 40, 6)]),
    Stage("stage 2", 2, [Zombie("좀비 3", 50, 7), Zombie("좀비 4", 60, 8)]),
    Stage("stage 3", 3, [Zombie("좀비 5", 70, 9), Zombie("좀비 6", 80, 10)]),
    Stage("stage 4", 4, [Zombie("좀비 7", 90, 11), Zombie("좀비 8", 100, 12)]),
    Stage("stage 5", 5, [Zombie("좀비 9", 120, 13), Zombie("좀비 10", 140, 14)]),
    Stage("stage 6", 6, [Zombie("좀비 11", 160, 15), Zombie("좀비 12", 180, 16)]),
    Stage("stage 7", 7, [Zombie("좀비 13", 200, 17), Zombie("좀비 14", 220, 18)]),
    Stage("stage 8", 8, [Zombie("좀비 15", 240, 19), Zombie("좀비 16", 260, 20)]),
    Stage("stage 9", 9, [Zombie("좀비 17", 280, 21), Zombie("좀비 18", 300, 22)]),
    Stage("stage 10", 10, [Zombie("보스좀비", 500, 50), Zombie("쪼렙 좀비", 30, 5)])
]


current_stage_index = 0

while True:
    os.system("cls")
    current_stage = stages[current_stage_index]
    print(f"\n=== {current_stage.name} ===")

    for i in range(0, len(current_stage.zombies), 2):
        zombie1 = current_stage.zombies[i]
        zombie2 = current_stage.zombies[i + 1] if i + \
            1 < len(current_stage.zombies) else None

        print(f"{zombie1.name}과(와) {zombie2.name}이(가) 나타났습니다!")
        while True:
            print("\n=== 새로운 턴 ===")
            player.player_status()
            zombie1.zombie_status()
            zombie2.zombie_status()

            for i, zombie in enumerate(current_stage.zombies):
                print(f"{i+1}: {zombie.name} - HP: {zombie.hp}")

            try:
                attack_num = int(input("어떤 좀비를 공격하시겠습니까? (숫자 입력) "))
                if attack_num < 1 or attack_num > len(current_stage.zombies):
                    print("잘못된 입력입니다. 다시 입력해주세요.")
                    continue
                else:
                    zombie = current_stage.zombies[attack_num-1]

                    action = input("어떤 공격을 사용하시겠습니까? (1: 일반공격, 2: 마법공격) ")
                    if action == "1":
                        player.normal_attack(zombie)
                    elif action == "2":
                        player.magic_attack(zombie)
                    else:
                        print("잘못된 입력입니다. 다시 입력해주세요.")
                        continue
            except ValueError:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue

            for i in range(len(current_stage.zombies)):
                i = 0
                if current_stage.zombies[i].hp == 0:
                    del current_stage.zombies[i]
                    i += 1
                    print(f"{zombie.name}을(를) 물리쳤습니다!")
                    break

            if not current_stage.zombies:
                print("="*20)
                print(f"{current_stage.name}을(를) 클리어했습니다!")
                print("="*20)
                player.level_up()
                time.sleep(0.7)
                print(f"{player.name}의 레벨이 {player.level}로 올라갔습니다.")
                time.sleep(0.7)
                print(
                    f"{player.name}의 HP가 {player.max_hp - 10}에서 {player.max_hp}로 증가했습니다.")
                time.sleep(0.7)
                print(
                    f"{player.name}의 sp가 {player.max_sp - 5}에서 {player.max_sp}로 증가했습니다.")
                time.sleep(0.7)
                print(
                    f"{player.name}의 공격력이 {player.normal_power - 2}에서 {player.normal_power}로 증가했습니다.")
                time.sleep(0.7)
                print(
                    f"{player.name}의 마법력이 {player.magic_power - 3}에서 {player.magic_power}로 증가했습니다.")
                time.sleep(0.7)
                print("="*20)
                print("다음 스테이지로 이동합니다.")
                time.sleep(1)
                break
            else:
                zombie.bite(player)

            if player.hp < 0:
                print("게임에서 패배했습니다.")
                quit()

    current_stage_index += 1
    if current_stage_index == len(stages):
        print("모든 스테이지를 클리어했습니다. 게임을 종료합니다.")
        break

print("=== 게임 종료 ===")
