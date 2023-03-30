G={'A':['B','C'] ,'B':['D'],'C':['E'],'D':['F'],'E':['F'] }

class Grafo_Dirigido:
    def __init__(self):
        self.dicc_grafo = {}
    
    def agregar_nodo(self,nodo):
        self.dicc_grafo[nodo] = []
        if nodo in self.dicc_grafo:
            return "El Nodo ya existe en el grafo"
        self.dicc_grafo[nodo] = []
    
    def agregar_arista(self,arista):
        nodo_origen = arista.get_nodo_origen()
        nodo_destino = arista.get_nodo_destino()
        if nodo_origen not in self.dicc_grafo:
            raise ValueError(f' El Nodo{nodo_origen.get_nombre()} no esta en el grafo')
        if nodo_destino not in self.dicc_grafo:
             raise ValueError(f' El Nodo{nodo_destino.get_nombre()} no esta en el grafo')
        self.dicc_grafo[nodo_origen].append(nodo_destino)

    def comprobar_nodo(self,nodo):
        return nodo in self.dicc_grafo

    def get_nodo(self,nombre_nodo):
        for n in self.dicc_grafo:
            if nombre_nodo == n.get_nombre() : return n
        print(f'El Nodo {nombre_nodo} no existe')

    def get_vecinos(self,nodo):
        return self.dicc_grafo[nodo]

    def __str__(self):
        todos_vertices = ''
        for nodo_origen in self.dicc_grafo:
            for nodo_destino in self.dicc_grafo[nodo_origen]:
                todos_vertices += nodo_origen.get_nombre() + '---->' + nodo_destino.get_nombre() + '\n'
        return todos_vertices

class Grafo_No_Dirigido (Grafo_Dirigido):
    def agregar_arista(self, arista):
        Grafo_Dirigido.agregar_arista(self, arista)
        arista_viceversa = Arista(arista.get_nodo_destino(), arista.get_nodo_origen())
        Grafo_Dirigido.agregar_arista(self, arista_viceversa)
     

class Arista:
    def __init__(self,nodo_origen,nodo_destino):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
    
    def get_nodo_origen(self):
        return self.nodo_origen
    def get_nodo_destino(self):
        return self.nodo_destino
    def __str__(self):
        return self.nodo_origen.get_nombre() + '---->' + self.nodo_destino.get_nombre() 
        
class Nodo:
    def __init__(self,nombre, ruido):
        self.nombre = nombre
        self.ruido = ruido
    def set_ruido(self, ruido):
        self.ruido = ruido
    def get_nombre(self):
        return self.nombre
    def get_ruido(self):
        return self.ruido
    def __str__(self):
        return self.nombre + '  =   ' + str(self.ruido)


    def agregar_arista(self,arista):
        Grafo_Dirigido.agregar_arista(self,arista)
        arista_vuelta = Arista(arista.get_nodo_destino(),arista.get_nodo_origen())
        Grafo_Dirigido.agregar_arista(self,arista_vuelta)
    

def crear_grafo(grafo):
    g=grafo()
    for n in ('a','b','c','d','e','f'):
        g.agregar_nodo(Nodo(n,0))
    g.agregar_arista(Arista(g.get_nodo('a'),g.get_nodo('b')))
    g.agregar_arista(Arista(g.get_nodo('a'),g.get_nodo('f')))
    g.agregar_arista(Arista(g.get_nodo('b'),g.get_nodo('c')))
    g.agregar_arista(Arista(g.get_nodo('c'),g.get_nodo('d')))
    g.agregar_arista(Arista(g.get_nodo('c'),g.get_nodo('f')))
    g.agregar_arista(Arista(g.get_nodo('d'),g.get_nodo('e')))
    g.agregar_arista(Arista(g.get_nodo('e'),g.get_nodo('f')))

    return g

def determinar_ruido(calle, G1:Grafo_No_Dirigido):

    if calle is False:
        print('No hay ruido en la calle')
    else:
        primer_piso_izq:Nodo = G1.get_nodo('a')
        primer_piso_izq.set_ruido(100)
        G1.get_vecinos(primer_piso_izq)[1].set_ruido(50)
        print(G1.get_vecinos(primer_piso_izq)[1])

        primer_piso_der:Nodo = G1.get_nodo('b')
        primer_piso_der.set_ruido(100)
        G1.get_vecinos(primer_piso_der)[1].set_ruido(50)
        print(G1.get_vecinos(primer_piso_der)[1])


    
        

G1 = crear_grafo(Grafo_No_Dirigido)
print(G1)

calle = True
determinar_ruido(calle, G1)

        