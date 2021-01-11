import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config


class Graph():
    def __init__(self, subject, prereq_list, width=300, height=300, directed=False, nodeHighlightBehavior=True, 
    highlightColor="lightblue", collapsible=False, node_size=500):

        self.subject = subject
        self.prereq = prereq_list
        
        self.width = width
        self.height = height
        self.directed = directed
        self.nodeHighlightBehavior = nodeHighlightBehavior
        self.highlightColor = highlightColor
        self.collapsible = collapsible
        self.node_size = node_size

        self.nodes = []
        self.edges = []

        self.config = Config(width=self.width,
                height=self.height,
                directed=self.directed,
                nodeHighlightBehavior=self.nodeHighlightBehavior,
                highlightColor=self.highlightColor,
                collapsible=self.collapsible,
                node_size=self.node_size, highlightStrokeColor="blue", node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                ) 

    def generate_graph(self):
        for pre in self.prereq:
            self.nodes.append(Node(id=pre, size=1000))
        self.nodes.append(Node(self.subject, size=1000))

        for index in range(0, len(self.prereq)):
            print(self.prereq)
            self.edges.append(Edge(source=self.subject, target=self.prereq[index], type="CURVE_SMOOTH"))
        
        return_value = agraph(nodes=self.nodes, edges=self.edges, config=self.config)

        print(return_value)