import string
condicion1=True
usuarios=[]
while condicion1:
    print('-'*len('1. Registrar usuario \n 2. Suscripcion \n 3. Consultar datos clientes \n 4. Salir'))
    print('1. Registrar usuario \n 2. Suscripcion \n 3. Consultar datos clientes \n 4. Salir')
    print('-'*len('1. Registrar usuario \n 2. Suscripcion \n 3. Consultar datos clientes \n 4. Salir'))
    try:
        opcion=int(input('Ingrese opcion 1, 2, 3, 4_'))
        if 1<=opcion<=4:
            if opcion==1:
                controlador=True
                while controlador:
                    usuario={}
                    rut=int(input('Ingresar rut sin digito verficador ni puntos. Debe estar entre 4000000 y 99999999 '))
                    if 4000000<=rut<=99999999:
                        usuario['RUT']=rut
                        edad=int(input('Ingrese su edad. Esta debe estar entre 0 y 110 '))
                        if 0<=edad<=110:
                            usuario['edad']=edad
                            genero=input('Es usted hombre (H) o mujer (M)? ')
                            if genero=='M' or genero=='H':
                                usuario['Genero']=genero
                                tipo=input('Tipo de suscripcion (PREMIUM/GOLD/SILVER) ')
                                if tipo=='PREMIUM' or tipo=='GOLD' or tipo=='SILVER':
                                    usuario['tipo_suscripcion']=tipo
                                    cont=0
                                    correo=input('ingerse su correo. debe tener al menos un caracter ')
                                    dominio=input('ingese el dominio de su direccion(ie: gmail.com) ' )
                                    for char in correo:
                                        if char in string.punctuation:
                                            cont+=1
                                    if cont>=1:
                                        usuario['Correo_electronico']=f'{correo}@{dominio}'
                                        usuario['Suscripcion']='suscrito'
                                        if usuario not in usuarios:
                                            usuarios.append(usuario)
                                            print('Usuario registrado con exito :)')
                                            controlador=False
                                        else:
                                            print('Usario ya esta registrado')
                                            controlador=False
                                    else:
                                        print('El correo debe contener almenos un caracter')                                    
                                else:
                                    print('Debe selccionar un tipo de suscripcion valido (PREMIUM/GOLD/SILVER)')
                            else:
                                print('OOPS! debe ser mujer o hombre')
                        else:
                            print('ERROR!La edad debe estar entre 0 y 110 ')
                    else:
                        print('ERROR!el RUT debe estar entre 4000000 y 99999999 ')

            elif opcion==2:
                registro=None
                rut=int(input('Ingrese rut sin puntos ni digito verificador_'))
                for usuario in usuarios:
                    if rut in usuario.values():
                        registro='registrado'
                        break
                if registro=='registrado':
                    print('usuario registrado')
                    ops=input('desea suscribirse a Juan Mestro? (si/no)')
                    if ops=='si':
                        fecha=input('Ingrese la fecha (Año/mes/día)_')
                        usuario['Fecha']=fecha
                    else:
                        suscripcion='no suscrito'
                        fecha=input('Ingrese la fecha (Año/mes/día)_')
                        usuario['Suscripcion']=suscripcion
                        usuario['Fecha']=fecha
                else:
                    print('Debe registrar un usuario')
                    

            elif opcion==3:
                rut=int(input('Ingrese RUT sin digito verificador para solicitar informacion de suscripcion_ '))
                for usuario in usuarios:
                    if rut in usuario.values():
                        print('Informacion sobre el usuario')
                        for k,v in usuario.items():
                            print(f'{k} : {v}')

            elif opcion==4:
                print('Gracias por suscribirse a la App de Juan Maestro…'  )
                condicion1=False

        else:
            print('Numero incorrecto. Ingrese opciones 1, 2, 3 o 4')
        
    except:
        print('ERROR! Ingrese opcion 1, 2, 3 o 4.')
