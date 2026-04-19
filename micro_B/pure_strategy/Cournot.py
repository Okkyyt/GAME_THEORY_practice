# 数量競争モデルの実装
import pandas as pd

class Market:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
        self.c1 = None
        self.c2 = None

    def price(self, Q: float) -> float:
        """
        価格式: P = a - bQ
        """
        return self.a - self.b * Q
    
class Player:
    def __init__(self, q: float, c: float):
        self.q = q  # 生産量
        self.c = c  # 限界費用

    def profit(self, M: Market, q_other: float) -> float:
        """
        P(Q) = a - b(self.q + q_other)
        π = (P(Q) - c) * q
        """
        Q = self.q + q_other
        P = M.price(Q)
        return (P - self.c) * self.q
    
    def optimal_react(self, M: Market, q_other: float) -> float:
        """
        最適反応関数
        利得の式: π = (a - b(q_self + q_other) - c) * q_self <- q_selfで微分して最適化
        dπ/dq_self = a - b(2q_self + q_other) - c = 0
        q_self = (a - c - b * q_other) / (2b)
        """
        q = (M.a - self.c - M.b * q_other) / (2 * M.b)
        return max(q, 0)  # 生産量は非負
    
class Cournot:
    def __init__(self, M: Market, P1: Player, P2: Player):
        self.M = M
        self.P1 = P1
        self.P2 = P2

    def loop_equilibrium(self, tol=1e-6, max_iter=1000):
        """
        反復法による均衡点の計算
        """
        q1, q2 = self.P1.q, self.P2.q
        for i in range(max_iter):
            q1_new = self.P1.optimal_react(self.M, q2)
            q2_new = self.P2.optimal_react(self.M, q1_new)
            if abs(q1_new - q1) < tol and abs(q2_new - q2) < tol:
                break
            q1, q2 = q1_new, q2_new
    
        return round(q1, 3), round(q2, 3)
    
def main():
    # 市場パラメータ
    a = 100
    b = 2
    M = Market(a, b)

    # プレイヤーの初期化
    c1 = 20  # プレイヤー1の限界費用
    c2 = 20  # プレイヤー2の限界費用
    P1 = Player(q=0, c=c1)
    P2 = Player(q=0, c=c2)

    # クールノットモデルの初期化
    cournot_game = Cournot(M, P1, P2)

    # 均衡点の計算
    q1_eq, q2_eq = cournot_game.loop_equilibrium()
    print(f"均衡生産量: プレイヤー1 = {q1_eq}, プレイヤー2 = {q2_eq}")

    Q = q1_eq + q2_eq
    P = M.price(Q)
    print(f"市場合計Q = {Q}, 価格P = {P}")

if __name__ == "__main__":
    main()
