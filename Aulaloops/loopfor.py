# Exemplo crescente
for i in range(0,10,2):
    #print(i)
    pass

# Exemplo descrecente
for i in range(10,0,-1):
    #print(i)
    pass

# Com dois parâmetros
# começo, fim
# quando não passado o incremento ele começa do um
for _ in range(0, 10):
    #print(f"{_} : oi")
    pass

#Passando conta
n = 10
for i in range(n//2):
    #print(i)
    pass
    

# for dentro de for
# for i in range(11):
#     print(f'Tabuada do {i}')
#     for y in range(11):
#         print(f"{i} x {y} = {i * y}")
    
#     print('\n')


# Else no for
# for i in range(10):
#     print(i)
# else:
#     print("Fim")

# break
# for i in range(1,11):
#     print(i)
#     if i + 1 == 4:
#         break



# continue
for i in range(1,11):
    if i == 5:
        continue
    print("Iteração ", i)