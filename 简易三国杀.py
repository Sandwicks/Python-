#三国打

import random as r
import sys as s

basic_cards = {"attack":20,"sidestep":20,"peach":5}
idea_cards = {"throw":4,"get":4,"fight":2}
equipment_cards = {"a1":1,"a2":1}

def get_cards(a,b):
    i = 0
    while i < b:
        if r.randint(1, 3) == 1:
            if r.randint(0, 2) == 0:
                if basic_cards.get('attack') > 0:
                    basic_cards['attack'] -= 1
                    a[1].append('attack')
                    i += 1
            elif r.randint(1, 2) == 1:
                if basic_cards.get('sidestep') > 0:
                    basic_cards['sidestep'] -= 1
                    a[1].append('sidestep')
                    i += 1
            else:
                if basic_cards.get('peach') > 0:
                    basic_cards['peach'] -= 1
                    a[1].append('peach')
                    i += 1
        elif r.randint(1, 2) == 1:
            if r.randint(0, 2) == 0:
                if idea_cards.get('throw') > 0:
                    idea_cards['throw'] -= 1
                    a[1].append('throw')
                    i += 1
            elif r.randint(1, 2) == 1:
                if idea_cards.get('get') > 0:
                    idea_cards['get'] -= 1
                    a[1].append('get')
                    i += 1
            else:
                if idea_cards.get('fight') > 0:
                    idea_cards['fight'] -= 1
                    a[1].append('fight')
                    i += 1
        else:
            if r.randint(0, 1) == 0:
                if equipment_cards.get('a1') > 0:
                    equipment_cards['a1'] -= 1
                    a[1].append('a1')
                    i += 1
            else:
                if equipment_cards.get('a2') > 0:
                    equipment_cards['a2'] -= 1
                    a[1].append('a2')
                    i += 1

def translate(m):
    l = []
    e_c = ['attack','杀','sidestep','闪','peach','桃','throw','过河拆桥',
           'get','顺手牵羊','fight','决斗','a1','诸葛连弩','a2','寒冰剑']
    for n in range(len(m[1])):
        l.append(e_c[e_c.index(m[1][n])+1])
    return l
def hurt(w1,w2):
    w1[0] -= 1
    if w1[0] == 0:
        if w2 == 'cpu':
            print('电脑玩家进入濒死状态！')
            if 'peach' in cpu[1]:
                print('电脑玩家使用了桃')
                cpu[1].remove('peach')
                basic_cards['peach'] += 1
            else:
                print('电脑玩家阵亡！你赢了！')
                s.exit()
        else:
            print('你进入濒死状态！')
            if 'peach' in player[1]:
                print('你自动使用了桃')
                player[1].remove('peach')
                basic_cards['peach'] += 1
            else:
                print('你阵亡了！电脑玩家获胜！')
                s.exit()
def do(x, y):
    global lim
    if x == 'player':
        if y == "attack" and (lim != 0 or 'a1' in player[1]):
            lim -= 1
            print('你使用了杀')
            player[1].remove('attack')
            basic_cards['attack'] += 1
            if 'sidestep' in cpu[1]:
                print('电脑玩家使用了闪')
                cpu[1].remove('sidestep')
                basic_cards['sidestep'] += 1
            else:
                hurt(cpu,'cpu')
        elif y == 'peach' and player[0] < 4:
            print('你使用了桃')
            player[0] += 1
            player[1].remove('peach')
            basic_cards['peach'] += 1
        elif y == 'throw':
            print('你使用了过河拆桥')
            player[1].remove('throw')
            idea_cards['throw'] += 1
            u = r.randint(0, len(cpu[1])-1)
            u = cpu[1][u]
            cpu[1].remove(u)
            if u in basic_cards.keys():
                basic_cards[u]+=1
            elif u in idea_cards.keys():
                idea_cards[u]+=1
            else:
                equipment_cards[u]+=1
        elif y == 'get':
            print('你使用了顺手牵羊')
            player[1].remove('get')
            idea_cards['get'] += 1
            u = r.randint(0, len(cpu[1])-1)
            u = cpu[1][u]
            cpu[1].remove(u)
            player[1].append(u)
        elif y == 'fight':
            print('你使用了决斗')
            player[1].remove('fight')
            idea_cards['fight'] += 1
            while True:
                if 'attack' in cpu[1]:
                    print('电脑玩家打出了杀')
                    cpu[1].remove('attack')
                    basic_cards['attack'] += 1
                else:
                    hurt(cpu,'cpu')
                    break
                if 'attack' in player[1]:
                    print('你打出了杀')
                    player[1].remove('attack')
                    basic_cards['attack'] += 1
                else:
                    hurt(player, 'player')
                    break
        else:
            print('该牌不能被使用')

    else:
        if y == "attack" and (lim != 0 or 'a1' in cpu[1]):
            print('电脑玩家使用了杀')
            lim -= 1
            cpu[1].remove('attack')
            basic_cards['attack'] += 1
            if 'sidestep' in player[1]:
                print('你使用了闪')
                player[1].remove('sidestep')
                basic_cards['sidestep'] += 1
            else:
                hurt(player, 'player')
        elif y == 'peach' and cpu[0] < 4:
            print('电脑玩家使用了桃')
            cpu[0] += 1
            cpu[1].remove('peach')
            basic_cards['peach'] += 1
        elif y == 'throw':
            print('电脑玩家使用了过河拆桥')
            cpu[1].remove('throw')
            idea_cards['throw'] += 1
            
            u = r.randint(0, len(player[1])-1)
            u = player[1][u]
            player[1].remove(u)
            if u in basic_cards.keys():
                basic_cards[u] += 1
            elif u in idea_cards.keys():
                idea_cards[u] += 1
            else:
                equipment_cards[u] += 1
        elif y == 'get':
            print('电脑玩家使用了顺手牵羊')
            cpu[1].remove('get')
            idea_cards['get'] += 1
            
            u = r.randint(0, len(player[1])-1)
            u = player[1][u]
            player[1].remove(u)
            cpu[1].append(u)
        elif y == 'fight':
            print('电脑玩家使用了决斗')
            cpu[1].remove('fight')
            idea_cards['fight'] += 1
    
            while True:
                if 'attack' in player[1]:
                    print('你打出了杀')
                    player[1].remove('attack')
                    basic_cards['attack'] += 1
                else:
                    hurt(player, 'player')
                    break
                if 'attack' in cpu[1]:
                    print('电脑玩家打出了杀')
                    cpu[1].remove('attack')
                    basic_cards['attack'] += 1
                else:
                    hurt(cpu, 'cpu')
                    break

cpu = [4, []]
player = [4,[]]

get_cards(cpu,3)
get_cards(player,3)

print("游戏开始！")

trun = 0
while True:
    lim = 1
    print("现在是你的回合")
    get_cards(player,2)
    while True:
        print('现在你的血量为：',player[0])
        print('现在你的手牌是：',translate(player))
        out = int(input('请输入你要打出的手牌的位置'))-1
        if out not in [a for a in range(len(player[1]))]:
            break
        do('player',player[1][out])
    lim = 1
    print("现在是电脑玩家的回合")
    get_cards(cpu,2)
    for out in cpu[1]:
        do('cpu',out)
        