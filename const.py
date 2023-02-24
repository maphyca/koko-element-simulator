ELEMENTS = ['水', '火', '雷', '草', '冰','风', '岩']
ELEMENT_MASS = [1, 1.5, 2, 4]
SETTING_TITLE = ['启用', '序号', '名称', '元素', '元素量', '攻击方式', '攻击目标', '起始时刻(s)', '持续时间(s)', '攻击冷却(s)', '附着冷却(s)']
BASIC_ELEMENT_DICT = {1: '水', 2: '火', 3: '风', 4: '雷', 5: '草', 6: '冰', 7: '岩'}
ATTACH_ELEMENT_DICT = {1: '水', 2: '火', 3: '冰', 4: '雷', 5: '草', 6: '冻', 7: '激', 8: '燃'}
ELEMENT_REACTION_DICT = {2: '蒸发', 3: '冻结', 4: '融化', 5: '超导', 6: '感电', 7: '超载',
                         8: '水扩散', 9: '火扩散', 10: '雷扩散', 11: '冰扩散', 12: '冻扩散',
                         13: '原激化', 14: '超激化', 15: '蔓激化', 16: '草原核', 17: '绽放', 18: '烈绽放', 19: '超绽放',
                         20: '燃烧', 21: '水结晶', 22: '火结晶', 23: '雷结晶', 24: '冰结晶', 25: '冻结晶', 26: '碎冰'}
ELEMENT_REACTION_DICT_REV = {'蒸发': 2, '冻结': 3, '融化': 4, '超导': 5, '感电': 6, '超载': 7,
                             '水扩散': 8, '火扩散': 9, '雷扩散': 10, '冰扩散': 11, '冻扩散': 12,
                             '原激化': 13, '超激化': 14, '蔓激化': 15, '草原核': 16, '绽放': 17, '烈绽放': 18, '超绽放': 19,
                             '燃烧': 20, '水结晶': 21, '火结晶': 22, '雷结晶': 23, '冰结晶': 24, '冻结晶': 25, '碎冰': 26}
VERSION = 0.9
SETTING_VERSION = 1
ACCEPTABLE_SETTING_VERSION = [1]
APP_TITLE = 'KOKO元素反应模拟器V' + str(VERSION)

def decrease_speed(element, element_mass):
    spd = 0
    if element == '水' or element == '火' or element == '雷' or element == '冰' or element == '草':  # 水，火，雷，冰，草附着
        spd = 0.8 * element_mass / (element_mass * 2.5 + 7)
    if element == '激':
        spd = element_mass / (5 * element_mass + 6)
    return spd


def swirl_element_mass(anemo_mass, target_mass):
    if anemo_mass / 2 < target_mass:
        return 0.95 + 1.25 * anemo_mass
    else:
        return 0.95 + 1.25 * target_mass
