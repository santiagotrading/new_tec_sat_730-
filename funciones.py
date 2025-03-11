


#us-001/creat_register

user = []

def user_regirter():
  id = int(input("ingresar id"))
  user.append(id)
  name = input("agregar su nombre")
  user.append(name)
  last_name = input("agrega tu apellido")
  user.append(last_name)
  email = input("agrega su email")
  user.append(email)
  password = input("cree un password de 8 caracteres")
  user.append(password)
  print("usuario creado con exito")
  print(user)

#creando login
def user_login():
  print("login")  