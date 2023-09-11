from operator import attrgetter


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
        self.adjacencylist[dep1].remove(dep2)
        self.adjacencylist[dep2].remove(dep1)
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
