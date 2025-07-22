def solicitar_contraseña():
  clave_correcta = "12351235"
  intentos = 3 

  for intento in range(intentos):
    clave = input("Introduce la contraseña: ")
    if clave == clave_correcta:
      return True
    else:
      print(f"Contraseña incorrecta. Intentos restantes: {intentos - intento - 1}")
  
  print("Demasiados intentos fallidos. Acceso denegado.")
  return False
