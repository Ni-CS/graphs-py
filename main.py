from graph import Graph
from edge import Edge
from department import Department

quantiaDepartamentos = 0

print("Simulador de Rede Elétrica da Rural")
print("Deseja criar uma nova simulação(1) ou utilizar a padrão(2)?")
resp = int(input())
graph = Graph()
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

    for dept in dpts:
        graph.add_departments(dept)

    quantiaDepartamentos = 6

    for path in edges:
        graph.add_path(path)

    graph.print_graph()

    menu = -1
    while menu != 8:
        print("\n===========Este é o Grafo Pré-definido=============")
        print("\n====================Operações=====================")
        print("\n1-Gerenciar Departamentos\n2-Gerenciar Caminhos\n3-Ver Árvore Geradora Mínima\n4-Ver Relatório\n5- Ver"
              "Grafo\n6- Ver Grafo com Interface\n7- Ver Árvore Geradora Mínima com Interface\n8- Sair")
        menu = int(input())
        op = -1
        if menu == 1:
            while op != 4:
                print("\n1-Adicionar Departamento\n2- Remover Departamento\n3- Buscar Departamento\n4- Voltar")
                op = int(input())

                if op == 1:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    print("\nDigite a quantia de pessoas no Departamento: ")
                    qtt = int(input())

                    dep = Department(quantiaDepartamentos, nome, qtt)
                    graph.add_departments(dep)
                    quantiaDepartamentos += 1
                if op == 2:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    dep = graph.find_dept_by_name(nome)
                    graph.remove_departments(dep)
                if op == 3:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    dep = graph.find_dept_by_name(nome)
                    graph.print_department(dep)
        if menu == 2:
            while op != 4:
                print("\n1-Adicionar Caminho\n2- Remover Caminho\n3- Ver Caminhos\n4- Voltar")
                op = int(input())
                if op == 1:
                    print("\nDigite o nome do Departamento de origem: ")
                    nomeDep1 = input()
                    print("\nDigite o nome do Departamento de destino: ")
                    nomeDep2 = input()
                    print("\nDigite a distância de um departamento a outro: ")
                    dist = int(input())

                    edge = Edge(graph.find_dept_by_name(nomeDep1), graph.find_dept_by_name(nomeDep2), dist)
                    graph.add_path(edge)
                if op == 2:
                    print("\nDigite o nome do Departamento de origem: ")
                    nomeDep1 = input()
                    print("\nDigite o nome do Departamento de destino: ")
                    nomeDep2 = input()
                    print("\nDigite a distância de um departamento a outro: ")
                    dist = int(input())
                    graph.remove_edge(graph.find_dept_by_name(nomeDep1), graph.find_dept_by_name(nomeDep2), dist)
                if op == 3:
                    graph.print_paths()
        if menu == 3:
            graph.imprimir_arvore_minima()
        if menu == 4:
            graph.gerar_relatorio()
        if menu == 5:
            graph.print_graph()
        if menu == 6:
            graph.interface_grafica_grafo()
        if menu == 7:
            graph.interface_grafica_arvoreminima()

if resp == 1:
    menu = -1
    while menu != 8:
        print("\n====================Operações=====================")
        print("\n1-Gerenciar Departamentos\n2-Gerenciar Caminhos\n3-Ver Árvore Geradora Mínima\n4-Ver Relatório\n5- Ver"
              "Grafo\n6- Ver Grafo com Interface\n7- Ver Árvore Geradora Mínima com Interface\n8- Sair")
        menu = int(input())
        op = -1
        if menu == 1:
            while op != 4:
                print("\n1-Adicionar Departamento\n2- Remover Departamento\n3- Buscar Departamento\n4- Voltar")
                op = int(input())

                if op == 1:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    print("\nDigite a quantia de pessoas no Departamento: ")
                    qtt = int(input())

                    dep = Department(quantiaDepartamentos, nome, qtt)
                    graph.add_departments(dep)
                    quantiaDepartamentos += 1
                if op == 2:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    dep = graph.find_dept_by_name(nome)
                    graph.remove_departments(dep)
                if op == 3:
                    print("\nDigite o nome do Departamento: ")
                    nome = input()
                    dep = graph.find_dept_by_name(nome)
                    graph.print_department(dep)
        if menu == 2:
            while op != 4:
                print("\n1-Adicionar Caminho\n2- Remover Caminho\n3- Ver Caminhos\n4- Voltar")
                op = int(input())
                if op == 1:
                    print("\nDigite o nome do Departamento de origem: ")
                    nomeDep1 = input()
                    print("\nDigite o nome do Departamento de destino: ")
                    nomeDep2 = input()
                    print("\nDigite a distância de um departamento a outro: ")
                    dist = int(input())

                    edge = Edge(graph.find_dept_by_name(nomeDep1), graph.find_dept_by_name(nomeDep2), dist)
                    graph.add_path(edge)
                if op == 2:
                    print("\nDigite o nome do Departamento de origem: ")
                    nomeDep1 = input()
                    print("\nDigite o nome do Departamento de destino: ")
                    nomeDep2 = input()
                    print("\nDigite a distância de um departamento a outro: ")
                    dist = int(input())
                    graph.remove_edge(graph.find_dept_by_name(nomeDep1), graph.find_dept_by_name(nomeDep2), dist)
                if op == 3:
                    graph.print_paths()
        if menu == 3:
            graph.imprimir_arvore_minima()
        if menu == 4:
            graph.gerar_relatorio()
        if menu == 5:
            graph.print_graph()
        if menu == 6:
            graph.interface_grafica_grafo()
        if menu == 7:
            graph.interface_grafica_arvoreminima()
