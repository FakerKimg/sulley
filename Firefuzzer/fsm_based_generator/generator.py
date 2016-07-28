from transformer import Transformer
from pattern_generator import *

class FSM_based_Generator(object):
    def __init__(self, _type, _regex):
        self.tr = Transformer(_type, _regex)
        self.dead_state = self.find_dead_state()
        return

    def check_dead_state(self, dead_state):
        validg = self.tr.correct_graph
        invalidg = self.tr.incorrect_graph
        for invalid_edge in invalidg.edges():
            # check corresponding edges in valid graph
            valid_start = invalid_edge[0] if invalid_edge[0]<dead_state else invalid_edge[0]-1
            valid_end = invalid_edge[1] if invalid_edge[1]<dead_state else invalid_edge[1]-1
            valid_edge = (valid_start, valid_end)
            if invalid_edge[0]==dead_state or invalid_edge[1]==dead_state:
                continue

            if valid_edge in validg.edges():
                if set(validg.edge[valid_start][valid_end]["_inputs"])!=set(invalidg.edge[invalid_edge[0]][invalid_edge[1]]["_inputs"]):
                    return False

        return True

    def find_dead_state(self):
        dead_state = 0
        while True:
            if self.check_dead_state(dead_state):
                break

            if dead_state==len(self.tr.incorrect_graph.nodes()):
                print "error while finding dead state"
                assert(False)

            dead_state = dead_state + 1

        self.dead_state = dead_state
        return

    def output_cases(self, scc_type, condense_type, valid, filename):
        _ggg, output_paths = generate_patterns(self.tr._type, scc_type, condense_type, False, self.tr.correct_graph, self.tr.incorrect_graph, self.dead_state)
        output_patterns(filename, _ggg, output_paths, len(output_paths), "a")

        return

