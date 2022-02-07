class Usuario:
    numero_tarjeta = 1234567890123456
    clave = 1234
    saldo = 0.00

    def validar(self,  clave_usuario):
        if Usuario.clave == clave_usuario:
            return True
        else:
            return False

    def mostrarSaldo(self):
        print("Su saldo es: ", Usuario.saldo)

    def cambiarclave(self):
        clave_validar = 0
        intentos = 0
        clave_nueva = 0
        while(clave_validar != Usuario.clave and intentos <= 3 ):
            clave_validar = int(input("Digite su clave"))
            intentos += 1
        if clave_validar == Usuario.clave:
            while(clave_validar != clave_nueva):    
                clave_validar =  int(input("Digite nueva clave: "))
                clave_nueva = int(input("Introduzca nuevamente la clave: "))
        else:
            print("Intentelo mas tarde su clave es incorrecta")
    
    def depositar(self,cant_depositar):
        Usuario.saldo += cant_depositar
        Usuario.mostrarSaldo()
    
    def extraer(self,cant_extraer):
        if cant_extraer <= Usuario.saldo:
            Usuario.saldo -= cant_extraer
            Usuario.mostrarSaldo()
        else:
            print("Su saldo es insuficiente")