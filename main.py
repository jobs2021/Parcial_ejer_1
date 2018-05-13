def registrar(cod,precio,can):
    iva=(precio*0.13)*can
    sub=(can*precio)+iva
    return [cod,precio,can,iva,sub]

def update(lista,cod,pre,ca):
    for element in lista:
        if element[0]==cod:
            ca+=element[2]
            return [lista.index(element),registrar(cod,pre,ca)]

def exist(lista,cod):
    for ele in lista:
        if ele[0]==cod:
            return True
    return False

def formato(s1,s2,s3,s4,s5):
    print(f"{s1:<20}{s2:<20}{s3:<20}{s4:<20}{s5:<20}\n{'-'*100}")

def imprimir(lista):
    total=0.00
    formato("Producto","Precio","Cantidad","IVA","Subtotal")
    for valor in lista:
        total+=valor[4]
        formato(valor[0],valor[1],valor[2],format(valor[3],'.2f'),valor[4])
    formato("","","","Total",total)

def crear_registro(lista):
    print("\nCrear Registro")
    x=input("Codigo del producto: ")
    y=float(input("Precio: "))
    z=int(input("Cantidad: "))

    if exist(lista,x):
        nuevo=update(lista,x,y,z)
        lista[nuevo[0]]=nuevo[1]
    else:
        lista.append(registrar(x,y,z))

    p=int(input("\nDesea agregar otro registro?\n1. Si\n2. No\n>> "))
    if p>0 and p<=2:
        if p==1:
            return crear_registro(lista)
        imprimir(lista)
        return menu()

def menu():
    x=int(input("\nCAJA REGISTRADORA\n1. Crear un registro\n2. Salir\n>> "))
    if x>0 and x<=2:
        if x==1:
            lista=[]
            crear_registro(lista)
        return

while menu():
    pass