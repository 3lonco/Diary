from Agent import *


class EstimationAgent(Agent):  ###EstimationAgent3 (1,2,6,7行目を記載)
    def __init__(self, nu, omega, estimator):
        super().__init__(nu, omega)
        self.estimator = estimator

    def draw(self, ax, elems):  # 追加
        self.estimator.draw(ax, elems)
