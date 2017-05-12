from torres import torres

alcance = 0
dano = 0
velocidade = 0
disponivel = 0
tempo = 0
tipoTiro = ""
img = ""

def iniciar_torres():
    global alcance
    global dano
    global velocidade
    global disponivel
    global tempo
    global tipoTiro
    global img
    
    alcance = 78
    dano = 1
    velocidade = 3
    disponivel = 2
    tempo = 120
    tipoTiro = "b"
    img = "torres/img/island/bobeira.png"

def _diminuir_disponibilidade():
    global disponivel
    disponivel -= 1

def criar_bobeira():
    _diminuir_disponibilidade()
    torre = torres.criar_torre(alcance, velocidade, tipoTiro, dano, tempo, img)
    return torre

def get_disponibilidade():
    return disponivel


iniciar_torres()