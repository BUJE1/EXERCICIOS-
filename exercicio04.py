def somar(lista):
    total = 0 
    for i in lista:
         total += i
    media = total /len(lista) if lista else 0
    return media


