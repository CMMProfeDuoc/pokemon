def alimentar (pkm:dict, alimento:dict) -> None:
    hambre = int(pkm['hambre'])
    hambre -= int(alimento['alimentacion'])
    if (hambre < 0):
        hambre = 0
    pkm['hambre'] = str(hambre)

#hagan cosas aca
