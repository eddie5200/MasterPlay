def printTurn(name):
    print("%s 的回合" % name)

def noDamage():
    print("攻击没有任何效果！")

def battleOver():
    print("战斗结束！")

def gameOver():
    print("战斗失败，游戏结束！")

def petDie(name):
    print("%s 死亡，战斗结束！" % name)

def petThink(name):
    print("%s 正在思考！" % name)

def petSelectSkill(name):
    print("%s 正在开始释放技能!" % name)

def petUseRun(name):
    print("%s 开始逃跑了" % name)

def petUseOrdinaryAttack(name):
    print("%s 使用普通攻击" % name)

def petUseDefense(name):
    print("%s 开始了防御姿态" % name)

def showSelect():
    print("请选择使用的指令1：特殊攻击 2.交换精灵 3.使用道具 4.临阵脱逃")

def showPetStatus(obj):
    '''
    显示精灵状态
    :param obj:
    :return:
    '''
    print("%s 的生命值：%s  攻击值 %s 防御值 %s" % (obj.name,obj.health,obj.attack,obj.getDefense()))

def showPetSkills(obj):
    for key,value in obj.skill_list.items():
        print(key,':',value.skill_show_name)