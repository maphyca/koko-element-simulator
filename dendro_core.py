import attack


class DendroCore:
    
    def __init__(self, count, source, tgt):
        self.name = '草核' + str(count)
        self.life = 6
        self.parent = tgt
        self.source = source


class DCManager:

    def __init__(self, monitor):
        self.dc_count = 0
        self.dc_list: list[DendroCore] = []
        self.monitor = monitor

    def clear(self):
        self.dc_count = 0
        self.dc_list = []

    def new_dc(self, source, tgt):
        self.dc_count += 1
        self.dc_list.append(DendroCore(self.dc_count, source, tgt))
        if len(self.dc_list) > 5:
            self.core_bloom(0, 0)

    def time_advance(self, dt):
        if len(self.dc_list) == 0:
            return
        for dc in self.dc_list:
            dc.life -= dt
        self.check_life()

    def check_life(self):
        if len(self.dc_list) == 0:
            return
        while self.dc_list[0].life < 0:
            self.core_bloom(0, 0)
            if len(self.dc_list) == 0:
                break

    def core_reaction(self, tgt, atk):
        if len(self.dc_list) == 0:
            return
        for i in range(len(self.dc_list)).__reversed__():
            if self.dc_list[i].parent == tgt:
                if atk.element == '雷':
                    self.core_bloom(i, 1, atk.name)
                    self.monitor.attack_list.append(attack.Attack('超绽放', '草', -1))
                elif atk.element == '火':
                    self.core_bloom(i, 2, atk.name)
                    self.monitor.attack_list.append(attack.Attack('烈绽放', '草', -1))

    def core_bloom(self, core_id, method, trigger='None'):
        core = self.dc_list.pop(core_id)
        if method == 0:  # 普通绽放
            self.monitor.log_action("%s由%s产生的草核原绽放" % (core.name, core.source))
        elif method == 1:  # 超绽放
            self.monitor.log_action("%s超绽放，由%s触发，目标为%s" % (core.name, trigger, core.parent.name))
        elif method == 2:  # 烈绽放
            self.monitor.log_action("%s烈绽放，由%s触发" % (core.name, trigger))
        elif method == 3:  # 妮绽放
            pass