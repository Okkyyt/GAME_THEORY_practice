class Market:
    def __init__(self, a, b):
        self.a = a  # 需要曲線の切片
        self.b = b  # 需要曲線の傾き

    # 需要関数を変形： Q = (a - P) / b

class Player:
    def __init__(self, p: float, c: float):
        self.p = p  # 価格
        self.c = c  # 限界費用

    def profit(self, M: Market, p_other: float) -> float:
        """
        P = self.p
        Q = (a - P) / b
        Q_other = (a - p_other) / b
        q = Q - Q_other
        π = (P - c) * q
        """
        Q = (M.a - self.p) / M.b
        Q_other = (M.a - p_other) / M.b
        q = Q - Q_other
        return (self.p - self.c) * q
    
class Bertrand:
    def __init__(self, M: Market, P1: Player, P2: Player):
        self.M = M
        self.P1 = P1
        self.P2 = P2

# 同質財ベルトラン競争
class Homogeneous_goods(Bertrand):
    def equilibrium(self):
        """
        均衡点の計算
        同質財ベルトラン競争における均衡価格は限界費用に等しい
        """
        p_eq = max(self.P1.c, self.P2.c)
        return round(p_eq, 3), round(p_eq, 3)