# Faça uma função que receba 3 valores inteiros por parâmetro e
# imprima-os ordenados em ordem crescente.

def ordem(n1,n2,n3):
    if(n1<n2 and n1<n3):
        if(n2<n3):
            return n1,n2,n3
        elif(n3<n2):
            return n1,n3,n2
        elif(n2==n3):
            return n1,n2,n3
    elif(n2<n1 and n2<n3):
        if(n1<n3):
            return n2,n1,n3
        elif(n3<n1):
            return n2,n3,n1
        elif(n1==n3):
            return n2,n1,n3
    elif(n3<n1 and n3<n2):
        if(n1<n2):
            return n3,n1,n2
        elif(n2<n1):
            return n3,n2,n1
        elif(n1==n2):
            return n3,n2,n1
    elif(n1 == n2 and n2 == n3):
        return n1,n2,n3

print(ordem(1,3,1))