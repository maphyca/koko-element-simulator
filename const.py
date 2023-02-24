ELEMENTS = ['水', '火', '雷', '草', '冰', '风', '岩']
ELEMENT_MASS = [1, 1.5, 2, 4]
SETTING_TITLE = ['启用', '序号', '名称', '元素', '元素量', '攻击方式', '攻击目标', '起始时刻(s)', '持续时间(s)',
                 '攻击冷却(s)', '附着冷却(s)']
BASIC_ELEMENT_DICT = {1: '水', 2: '火', 3: '风', 4: '雷', 5: '草', 6: '冰', 7: '岩'}
ATTACH_ELEMENT_DICT = {1: '水', 2: '火', 3: '冰', 4: '雷', 5: '草', 6: '冻', 7: '激', 8: '燃'}
ELEMENT_REACTION_DICT = {2: '蒸发', 3: '冻结', 4: '融化', 5: '超导', 6: '感电', 7: '超载',
                         8: '水扩散', 9: '火扩散', 10: '雷扩散', 11: '冰扩散', 12: '冻扩散',
                         13: '原激化', 14: '超激化', 15: '蔓激化', 16: '草原核', 17: '绽放', 18: '烈绽放', 19: '超绽放',
                         20: '燃烧', 21: '水结晶', 22: '火结晶', 23: '雷结晶', 24: '冰结晶', 25: '冻结晶', 26: '碎冰'}
ELEMENT_REACTION_DICT_REV = {'蒸发': 2, '冻结': 3, '融化': 4, '超导': 5, '感电': 6, '超载': 7,
                             '水扩散': 8, '火扩散': 9, '雷扩散': 10, '冰扩散': 11, '冻扩散': 12,
                             '原激化': 13, '超激化': 14, '蔓激化': 15, '草原核': 16, '绽放': 17, '烈绽放': 18,
                             '超绽放': 19,
                             '燃烧': 20, '水结晶': 21, '火结晶': 22, '雷结晶': 23, '冰结晶': 24, '冻结晶': 25,
                             '碎冰': 26}
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


# 预设
PRESET_NAME = ["水火雷草冰反应炉", "胡桃+夜兰/行秋", "水冰冻结", "感电与扩散", "激化与冻结护草", "草行久+水草雷前台",
               "心雷妲+水冰后台", "心妮妲+草", "燃草+水冰雷前台", "重置"]
PRESET_DICT = {
    "水火雷草冰反应炉": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "\u6c34", 0, 1.0, 0, 0, 1.5, 15.0, 1.3, 0.0], [true, "\u706b", 1, 1.0, 0, 0, 2.1, 15.0, 1.5, 0.0], [true, "\u96f7", 2, 1.0, 0, 0, 0.9, 15.0, 1.1, 0.0], [true, "\u8349", 3, 1.0, 0, 0, 1.3, 15.0, 1.7, 0.0], [true, "\u51b0", 4, 1.0, 0, 0, 0.8, 15.0, 1.9, 0.0]]',
    "胡桃+夜兰/行秋": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "\u591c\u5170\u6c34\u7bad", 0, 1.0, 0, 0, 0.3, 15.0, 1.0, 0.0], [true, "\u80e1\u6843A", 1, 1.0, 0, 0, 2.0, 9.0, 1.0, 2.5], [true, "\u80e1\u6843\u91cd", 1, 1.0, 0, 0, 2.1, 9.0, 1.0, 0.0], [false, "\u8840\u6885\u9999", 1, 1.0, 0, 0, 2.2, 12.0, 4.0, 0.0], [false, "\u591c\u51702\u547d", 0, 1.0, 0, 0, 0.3, 15.0, 2.0, 0.0], [false, "\u884c\u79cb\u6c34\u7bad1", 0, 1.0, 0, 0, 0.3, 18.0, 1.0, 0.0], [false, "\u884c\u79cb\u6c34\u7bad2", 0, 1.0, 0, 0, 3.3, 15.0, 3.0, 0.0]]',
    "水冰冻结": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "2s1\u6c34A", 0, 1.0, 0, 0, 0.7, 15.0, 2.0, 0.0], [false, "2s1\u6c34B", 0, 1.0, 0, 0, 2.0, 15.0, 2.0, 0.0], [true, "2s1\u51b0A", 4, 1.0, 0, 0, 2.6, 15.0, 2.0, 0.0], [false, "2s1\u51b0B", 4, 1.0, 0, 0, 1.3, 15.0, 2.0, 0.0], [false, "\u521d\u59cb\u5f3a\u6c34", 0, 2.0, 0, 0, 0.4, 0.0, 1.7, 0.0], [false, "\u521d\u59cb\u5f3a\u51b0", 4, 2.0, 0, 0, 0.3, 0.0, 1.0, 0.0]]',
    "感电与扩散": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "2s\u6c34", 0, 1.0, 0, 2, 2.3, 15.0, 2.0, 0.0], [true, "2s\u96f7", 2, 1.0, 0, 2, 2.0, 15.0, 2.0, 0.0], [false, "2s\u98ce", 5, 1.0, 0, 2, 3.0, 15.0, 2.0, 0.0]]',
    "激化与冻结护草": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "1s\u6c34", 0, 1.0, 0, 0, 1.4, 15.0, 1.0, 0.0], [true, "2s\u8349", 3, 1.0, 0, 0, 2.0, 15.0, 2.0, 0.0], [false, "2s\u96f7", 2, 1.0, 0, 0, 0.9, 18.0, 2.0, 0.0], [false, "2s\u51b0", 4, 1.0, 0, 0, 0.9, 18.0, 2.0, 0.0]]',
    "草行久+水草雷前台": '[1, [20.0, 5, false, true, false, false, true, true, true], [true, "\u884c\u79cb\u6c34\u7bad1", 0, 1.0, 0, 0, 1.3, 18.0, 1.0, 0.0], [true, "\u884c\u79cb\u6c34\u7bad2", 0, 1.0, 0, 0, 4.3, 15.0, 3.0, 0.0], [true, "\u8349\u795e\u534f\u540c", 3, 1.5, 1, 0, 0.1, 20.0, 2.5, 0.0], [true, "\u8349\u795eE", 3, 1.0, 0, 0, 0.1, 0.0, 1.7, 0.0], [true, "97\u96f7\u73af", 2, 1.0, 0, 0, 2.3, 15.0, 1.5, 2.5], [false, "1s\u6c34", 0, 1.0, 0, 0, 3.0, 12.0, 1.0, 0.0], [false, "1s\u96f7", 2, 1.0, 0, 0, 3.0, 12.0, 1.0, 0.0], [false, "1s\u8349", 3, 1.0, 0, 0, 3.0, 12.0, 1.0, 0.0]]',
    "心雷妲+水冰后台": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "\u5fc3\u6d77\u666e\u653b", 0, 1.0, 0, 0, 6.7, 10.0, 0.8, 0.0], [true, "\u5fc3\u6d77\u6c34\u6bcd", 0, 1.0, 0, 0, 0.0, 15.0, 2.0, 0.0], [true, "\u96f7\u795e\u534f\u540c", 2, 1.0, 2, 0, 0.2, 25.0, 0.9, 2.5], [true, "\u8349\u795e\u534f\u540c", 3, 1.5, 1, 0, 1.3, 25.0, 2.5, 0.0], [false, "\u591c\u5170", 0, 1.0, 0, 0, 4.3, 15.0, 1.0, 0.0], [false, "\u4f4e\u9891\u5f31\u51b0", 4, 1.0, 0, 0, 4.3, 10.0, 2.0, 0.0], [false, "\u9ad8\u9891\u5f31\u51b0", 4, 1.0, 0, 0, 5.5, 5.0, 1.0, 0.0]]',
    "心妮妲+草": '[1, [20.0, 5, false, false, false, true, true, false, true], [true, "\u5fc3\u6d77\u666e\u653b", 0, 1.0, 0, 0, 6.7, 10.0, 0.8, 0.0], [true, "\u5fc3\u6d77\u6c34\u6bcd", 0, 1.0, 0, 2, 0.0, 18.0, 2.0, 0.0], [true, "\u59ae\u9732\u6c34\u73af", 0, 1.0, 2, 2, 1.2, 18.0, 2.0, 2.5], [true, "\u8349\u795e\u534f\u540c", 3, 1.5, 1, 2, 1.3, 25.0, 2.5, 0.0], [true, "\u8349\u795eE", 3, 1.0, 0, 2, 1.3, 0.0, 1.0, 0.0], [true, "\u5fc3\u6d77\u5f3a\u6c34", 0, 2.0, 0, 2, 6.0, 0.0, 1.0, 0.0], [false, "3s\u8349", 3, 1.0, 0, 2, 3.3, 6.0, 3.0, 0.0], [false, "1s\u5355\u76ee\u6807\u8349", 3, 1.0, 0, 0, 3.3, 6.0, 1.0, 0.0]]',
    "燃草+水冰雷前台": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "\u9999\u83f1\u9505\u5df4", 1, 1.0, 0, 0, 6.6, 6.0, 2.0, 0.0], [true, "\u9999\u83f1\u706b\u5708", 1, 1.0, 0, 0, 3.4, 14.0, 1.14, 0.0], [true, "\u8349\u795ee", 3, 1.0, 0, 0, 0.8, 0.0, 1.7, 0.0], [true, "\u8349\u795e\u534f\u540c", 3, 1.5, 1, 0, 0.8, 15.0, 2.5, 0.0], [false, "\u5f31\u51b01", 4, 1.0, 0, 0, 5.2, 12.0, 2.0, 0.0], [false, "\u5f31\u51b02", 4, 1.0, 0, 0, 5.5, 12.0, 2.0, 0.0], [false, "1s\u6c34", 0, 1.0, 0, 0, 5.3, 15.0, 1.0, 0.0], [false, "1s\u96f7", 2, 1.0, 0, 0, 5.3, 15.0, 1.0, 0.0], [false, "1s\u96f7", 2, 1.0, 0, 0, 5.6, 15.0, 1.0, 0.0]]',
    "重置": '[1, [20.0, 5, false, false, false, false, true, true, true], [true, "\u6c34", 0, 1.0, 0, 0, 1.9, 15.0, 1.2, 0.0], [true, "\u706b", 1, 1.0, 0, 0, 2.6, 15.0, 1.8, 0.0], [true, "\u96f7", 2, 1.0, 0, 0, 2.1, 15.0, 1.5, 0.0], [false, "\u8349", 3, 1.0, 0, 0, 3.0, 15.0, 1.3, 0.0], [false, "\u51b0", 4, 1.0, 0, 0, 0.7, 15.0, 1.8, 0.0]]'
    }
