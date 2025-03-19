def calc_troco(cambio, valor): 
    # sort cambio values 
    cambio = sorted(cambio, reverse=True)
    troco = { k: 0 for k in cambio }
    troco_total = 0
    print("Valor a se pagar:", valor)
    
    while troco_total < valor: 
        for i in cambio:
            if round((troco_total + i), 2) <= valor:
                troco[i] += 1
                troco_total = round((troco_total + i), 2)

    print(troco)

if __name__ == '__main__':
    # ! optimal solution case
    cambio = [0.05, 0.10, 0.25, 0.50, 1.00]
    valor = 1.75

    # # ! not optimal solution case
    # cambio = [0.01, 0.03, 0.04]
    # valor = 0.06
    calc_troco(cambio, valor)