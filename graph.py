from operator import attrgetter


class Graph:
    def __init__(self):
        self.adjacencylist = {}
        self.edges = []
        self.departments = []

    def find_dept(self, num):
        for dept in self.departments:
            if dept.id == num:
                return dept

    def add_departments(self, dep):
        self.adjacencylist[dep.id] = []
        self.departments.append(dep)

    def add_path(self, edge):
        self.edges.append(edge)
        self.adjacencylist[edge.dept1.id].append(edge.dept2)
        self.adjacencylist[edge.dept2.id].append(edge.dept1)

    def print_graph(self):
        print("Número de Departamentos Cadastrados: ", len(self.adjacencylist))

        keys = self.adjacencylist.keys()

        for key in keys:
            print("({})".format(key+1), self.find_dept(key).name, ":",  end=" ")
            for dept in self.adjacencylist[key]:
                print(dept.name, end="; ")
            print()
            print("----------------------------")

    def print_paths(self):
        for path in self.edges:
            print(path.get_path_info())

    def sort_edges(self):
        path_list = self.edges[:]

        path_list.sort(key=attrgetter('dist'))
        return path_list

    def kruskal_algorithm(self, deps, paths):

        mst = Graph()

        edgelist = self.sort_edges()
        for edge in edgelist:
            print("Adicionando caminho na MST", edge.get_path_info())

        return mst
