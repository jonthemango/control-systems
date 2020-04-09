from control import *
from control.matlab import *
import numpy as np

G = tf(1, [240, 0, 1400])
s = tf('s')
goal_rise_time = 2
goal_overshoot = 20
goal_settling_time = 5
WORST_SCORE = 100000000
STEP = 70
MAX_DEPTH = 120


class Node:
    kp = 0
    kd = 0
    children = []
    score = WORST_SCORE  # set this to big as fuck by default (lol)
    best_child = None
    depth = 0

    def __init__(self, kp, kd, depth):
        self.kp = kp
        self.kd = kd
        self.depth = depth
        self.compute_score()

    def compute_score(self):
        C = self.kp + self.kd*s
        closed_loop = feedback(series(C, G), 1)
        try:
            info = step_info(closed_loop)
            rise_time = info['RiseTime']  # 2s
            overshoot = info['Overshoot']  # 30
            settling_time = info['SettlingTime']  # 5s

            diff_a = abs(rise_time-goal_rise_time)*2
            diff_b = abs(overshoot-goal_overshoot)
            diff_c = abs(settling_time-goal_settling_time)
            score = diff_a + diff_b + diff_c
        except Exception as e:
            print(e)
            score = WORST_SCORE

        self.score = score

    def generate_children(self):
        if self.depth == MAX_DEPTH:
            return None
        if self.is_goal_state():
            return self

        c1 = Node(self.kp+STEP, self.kd, self.depth+1)
        c2 = Node(self.kp-STEP, self.kd, self.depth+1)
        c3 = Node(self.kp, self.kd+STEP, self.depth+1)
        c4 = Node(self.kp, self.kd-STEP, self.depth+1)
        c5 = Node(self.kp+STEP, self.kd+STEP, self.depth+1)
        c6 = Node(self.kp-STEP, self.kd-STEP, self.depth+1)
        c7 = Node(self.kp+STEP, self.kd-STEP, self.depth+1)
        c8 = Node(self.kp-STEP, self.kd+STEP, self.depth+1)
        self.children = [c1, c2, c3, c4, c5, c6, c7, c8]

        self.children = sorted(
            self.children, key=lambda node: node.score, reverse=False)

        self.best_child = self.children[0]

        for index, child in enumerate(self.children):
            print(f'i: {index}, depth: {self.depth}, score:{child.score}')
            if child.is_goal_state():
                return child
            else:
                solution = child.generate_children()
                if solution is not None:
                    return solution

    def is_goal_state(self):
        return abs(self.score - 4) < 2


if __name__ == '__main__':
    node = Node(200, 1000, 0)
    solution_node = node.generate_children()
    print(
        f'score: {solution_node.score}, kd:{solution_node.kd}, kp:{solution_node.kp}')
