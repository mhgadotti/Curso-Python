produto = str(input('Digite o produto: '))
preço = float(input('Digite o Preço: '))
desconto = preço - (preço * 5 / 100)
print(f'Seu novo preço com desconto de 5% é R$ {desconto}')