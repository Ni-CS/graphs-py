from graph import Graph
from edge import Edge
from department import Department

print("Simulador de Rede Elétrica da Rural")
print("Deseja criar uma nova simulação(1) ou utilizar a padrão(2)?")
resp = int(input())
if resp == 2:
    dc = Department(0, "DC", 45)
    reitoria = Department(1, "Reitoria", 30)
    ru = Department(2, "RU", 157)
    dmat = Department(3, "DMAT", 200)
    setorial = Department(4, "Biblioteca Setorial", 24)
    cegoe = Department(5, "CEGOE", 133)

    caminho0 = Edge(reitoria, dc, 800)
    caminho1 = Edge(reitoria, ru, 50)
    caminho2 = Edge(reitoria, cegoe, 300)
    caminho3 = Edge(reitoria, dmat, 200)
    caminho4 = Edge(dmat, cegoe, 100)
    caminho5 = Edge(cegoe, setorial, 100)
    caminho6 = Edge(cegoe, dc, 1000)
    caminho7 = Edge(dc, setorial, 500)

    edges = [caminho0, caminho1, caminho2, caminho3, caminho4, caminho5, caminho6, caminho7]
    dpts = [dc, reitoria, ru, dmat, setorial, cegoe]

    graph = Graph()

    for dept in dpts:
        graph.add_departments(dept)

    for path in edges:
        graph.add_path(path)

    graph.print_graph()

   #  print("=====Kruskal=====")
   #  mst = graph.kruskal_algorithm(dpts, edges)
   #  mst.print_graph()
   #  print("=======-------======")
   # # mst.print_paths()
   #  print("=======-------======")
