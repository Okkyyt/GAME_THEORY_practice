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
    def profit(self):
        """
        利得の計算
        """
        # 価格が低いほうが市場を独占する
        if self.P1.p > self.P2.p:
            pai2 = self.P2.profit(self.M, self.P1.p)
            return 0.0, round(pai2, 3)
        elif self.P2.p > self.P1.p:
            pai1 = self.P1.profit(self.M, self.P2.p)
            return round(pai1, 3), 0.0
        # もし両者の価格が等しければ、両者は市場を半分ずつ分け合う
        else:
            pai1 = self.P1.profit(self.M, self.P2.p)
            pai2 = self.P2.profit(self.M, self.P1.p)
            return round(pai1, 3), round(pai2, 3)