from regexfsm.lego import parse
import networkx

class Transformer(object):
    def __init__(self, _type, _regex):
        self._type = _type
        self._regex = _regex
        self._fsm = None
        self.correct_graph = None
        self.incorrect_graph = None
        self.regex_to_fsm()
        self.fsm_to_graphs()

        return

    def regex_to_fsm(self):
        # transfer regex to greenery fsm
        try:
            self._fsm = parse(self._regex).to_fsm()
        except:
            print "error while transforming to fsm"

        return

    def fsm_to_graphs(self):
        # transfer greenery fsm to networkx DiGraph
        try:
            self.correct_graph = networkx.DiGraph(initial=self._fsm.initial, finals=list(self._fsm.finals), alphabet=self._fsm.alphabet)
            self.correct_graph.add_nodes_from(list(self._fsm.states))
            # transform transitions in fsm to edges in graph
            for sindex, edges in self._fsm.map.iteritems():
                for _input, eindex in edges.iteritems():
                    self.correct_graph.add_edge(sindex, eindex)
                    self.correct_graph.edge[sindex][eindex].setdefault("_inputs", [])
                    if _input not in self.correct_graph.edge[sindex][eindex]["_inputs"]:
                        self.correct_graph.edge[sindex][eindex]["_inputs"].append(_input)

            # complement fsm to graph
            fff = self._fsm.everythingbut()
            self.incorrect_graph = networkx.DiGraph(initial=fff.initial, finals=list(fff.finals), alphabet=fff.alphabet)
            self.incorrect_graph.add_nodes_from(list(fff.states))
            # transform transitions in fsm to edges in graph
            for sindex, edges in fff.map.iteritems():
                for _input, eindex in edges.iteritems():
                    self.incorrect_graph.add_edge(sindex, eindex)
                    self.incorrect_graph.edge[sindex][eindex].setdefault("_inputs", [])
                    if _input not in self.incorrect_graph.edge[sindex][eindex]["_inputs"]:
                        self.incorrect_graph.edge[sindex][eindex]["_inputs"].append(_input)
        except:
            print "error while transforming to graph"

        return

