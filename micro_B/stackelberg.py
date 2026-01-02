class Market:
    def __init__(self, a, b):
        """
        需要関数: P = a - bQ
        """
        self.a = a  # 需要曲線の切片
        self.b = b  # 需要曲線の傾き

    def price(self, Q):
        """
        市場価格を計算
        価格式: P = a - bQ
        """
        return self.a - self.b * Q
    
class Player:
  def __init__(self, q, c):
    """
    q: 生産量
    c: 限界費用
    """
    self.q = q
    self.c = c

  def profit(self, M, q_a):
    """
    P = a - b(self.q + q_a)
    U = (P - c)self.q
    return: 利潤
    """
    # return (M.a - M.b * (self.q + q_a) - self.c) * self.q
    return (M.price(self.q + q_a) - self.c) * self.q

  def optimal_react(self, M , q_a):
    """
    d_profit_dq: (M.a - M.b * q_a - self.c) - 2.0 * M.b * self.q
    上記の場合において self.q の最大を求める
    return: 最適反応である self.q
    """
    q = (M.a - M.b * q_a - self.c) / (2.0 * M.b)
    return max(0.0, q)

class Stackelberg:
  def __init__(self, a, b, c1, c2):
    self.M = Market(a, b)
    self.P1 = Player(None, c1)
    self.P2 = Player(None, c2)

  def P1_strategy(self):
    """
    後手の最適反応を代入した先手の戦略
    """
    q1 = ((self.M.a + self.P2.c) - 2.0 * self.P1.c) / (2.0 * self.M.b)
    return max(0.0, q1)

  def equilibrium(self):
    # 先手の戦略
    self.P1.q = self.P1_strategy()
    # 先手の戦略をもとに行う後手の最適反応
    self.P2.q = self.P2.optimal_react(self.M, self.P1.q)
    # 価格
    Price = self.M.price(self.P1.q + self.P2.q)
    # 利潤
    profit1 = self.P1.profit(self.M, self.P2.q)
    profit2 = self.P2.profit(self.M, self.P1.q)

    return {
        "q1": self.P1.q,
        "q2": self.P2.q,
        "P": Price,
        "Π1": profit1,
        "Π2": profit2,
    }
  
# ミクロ経済B例題14
"""
P = 20 - 2q
c1 = c2 = 4
"""

def main():
  s = Stackelberg(a=20, b=2, c1=4, c2=4)
  print(s.equilibrium())

if __name__ == "__main__":
  main()