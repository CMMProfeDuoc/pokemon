def alimentar (pkm:dict, comida:int) -> None:
    hambre = int(pkm['hambre'])
    hambre -= comida
    if (hambre < 0):
        hambre = 0
    pkm['hambre'] = str(hambre)

#hagan cosas aca
