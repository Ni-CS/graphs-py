from department import Department


class Edge:

    def __init__(self, dep1, dep2, dist):
        self.dept1 = dep1
        self.dept2 = dep2
        self.dist = dist

    def get_path_info(self):
        return "Caminho: {} <-----{}-----> {}".format(self.dept1.name, self.dist, self.dept2.name)

    def get_dept1(self):
        return self.dept1

    def get_dept2(self):
        return self.dept2
