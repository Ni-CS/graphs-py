from operator import attrgetter
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.adjacencylist = {}
        self.edges = []
        self.departments = []

    def find_dept_by_id(self, num):
        for dept in self.departments:
            if dept.id == num:
                return dept

    def find_dept_by_name(self, name):
        for dept in self.departments:
            if dept.name == name:
                return dept

    def find_edge(self, dep1, dep2, dist):
        for edge in self.edges:
            if edge.dept1 == dep1 and edge.dept2 == dep2 and edge.dist == dist:
                return edge

    def add_departments(self, dep):
        self.adjacencylist[dep.id] = []
        self.departments.append(dep)

    def remove_departments(self, dep):
        for edge in self.edges:
            if edge.dept1 == dep or edge.dept2 == dep:
                self.remove_edge(edge.dept1, edge.dept2, edge.dist)
        self.adjacencylist.pop(dep.id)
        self.departments.remove(dep)

    def remove_edge(self, dep1, dep2, dist):
        self.adjacencylist[dep1.id].remove(dep2)
        self.adjacencylist[dep2.id].remove(dep1)
        edge = self.find_edge(dep1, dep2, dist)
        self.edges.remove(edge)

    def add_path(self, edge):
        self.edges.append(edge)
        self.adjacencylist[edge.dept1.id].append(edge.dept2)
        self.adjacencylist[edge.dept2.id].append(edge.dept1)

    def print_department(self, dep):
        print("({})".format(dep.id + 1), self.find_dept_by_id(dep.id).name, ":", end=" ")
        for dept in self.adjacencylist[dep.id]:
            print(dept.name, end="; ")
        print()
        print("----------------------------")

    def print_graph(self):
        print("Número de Departamentos Cadastrados: ", len(self.adjacencylist))

        keys = self.adjacencylist.keys()

        for key in keys:
            if key is not None:
                print("({})".format(key + 1), self.find_dept_by_id(key).name, ":", end=" ")
                for dept in self.adjacencylist[key]:
                    print(dept.name, end="; ")
                print()
                print("----------------------------")

    def print_paths(self):
        for path in self.edges:
            print(path.get_path_info())

    def encontrar_pai(self, pai, dept):
        if pai[dept] == dept:
            return dept
        return self.encontrar_pai(pai, pai[dept])

    def kruskal(self):
        self.edges.sort(key=lambda x: x.dist)  # Ordena as arestas por peso
        pai = {}
        arvore_minima = []

        for dept in self.departments:
            pai[dept] = dept

        for edge in self.edges:
            origem_pai = self.encontrar_pai(pai, edge.dept1)
            destino_pai = self.encontrar_pai(pai, edge.dept2)

            if origem_pai != destino_pai:
                arvore_minima.append(edge)
                pai[origem_pai] = destino_pai

        return arvore_minima

    def gerar_relatorio(self):
        arvore_minima = self.kruskal()
        distancia_total = 0
        departamentos = []
        for edge in arvore_minima:
            distancia_total += edge.dist
            if not (departamentos.__contains__(edge.dept1)):
                departamentos.append(edge.dept1)
            if not (departamentos.__contains__(edge.dept2)):
                departamentos.append(edge.dept2)
        quantia_pessoas = 0
        for dept in departamentos:
            quantia_pessoas += dept.people_amount
        print("O custo total do projeto com {}m é R${} e impactou {} pessoas".format(distancia_total,
                                                                                     distancia_total * 1.80,
                                                                                     quantia_pessoas))

    def imprimir_arvore_minima(self):
        arvore_minima = self.kruskal()
        print('')

        if not arvore_minima:
            print("A árvore geradora mínima não foi criada ou é vazia.")
            print(' ')
            return

        print("Árvore Geradora Mínima:")
        for edge in arvore_minima:
            origem = edge.dept1.name
            destino = edge.dept2.name
            distancia = edge.dist
            print("{} <-----{}-----> {}".format(origem, distancia, destino))

            print('')

    def interface_grafica_grafo(self):
        G = nx.Graph()

        for edge in self.edges:
            G.add_edge(edge.dept1.name, edge.dept2.name, weight=int(edge.dist))

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

        pos = nx.spring_layout(G, seed=6)

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=800, node_color="green")

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2)
        nx.draw_networkx_edges(
            G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="black", style="dashed"
        )

        # node labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", font_weight="bold")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.margins(0.2)
        plt.tight_layout()
        plt.show()

    def interface_grafica_arvoreminima(self):
        grafo = nx.Graph()

        edges = self.kruskal()

        for edge in edges:
            grafo.add_edge(edge.dept1.name, edge.dept2.name, weight=int(edge.dist))

        elarge = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] > 0.5]
        esmall = [(u, v) for (u, v, d) in grafo.edges(data=True) if d["weight"] <= 0.5]

        pos = nx.spring_layout(grafo, seed=5)

        # nodes
        nx.draw_networkx_nodes(grafo, pos, node_size=800, node_color="green")

        # edges
        nx.draw_networkx_edges(grafo, pos, edgelist=elarge, width=2)
        nx.draw_networkx_edges(
            grafo, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="black", style="dashed"
        )

        # node labels
        nx.draw_networkx_labels(grafo, pos, font_size=10, font_family="sans-serif", font_weight="bold")
        # edge weight labels
        edge_labels = nx.get_edge_attributes(grafo, "weight")
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.margins(0.2)
        plt.tight_layout()
        plt.show()
