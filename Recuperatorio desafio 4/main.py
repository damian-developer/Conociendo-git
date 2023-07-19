from aplicacion import *
from celular import *
from contacto import *

# Tarea 1: Instanciar un objeto Celular, dos Aplicaciones y dos Contactos.
samsung20 = Celular("Samsung", "S20")
instagram = Aplicacion("Instagram", "2.1.0")
chatgpt = Aplicacion("ChatGPT", "4.0.0")
facebook = Aplicacion("Facebook", "4.0.0")
matias = Contacto("Matias", "387123321")
ramiro = Contacto("Ramiro", "387567765")
damian = Contacto("Damian", "387567765")

# Tarea 2: Instalar las dos aplicaciones en el celular.
samsung20.instalar_aplicacion(instagram)
samsung20.instalar_aplicacion(chatgpt)


# Tarea 3: Agregar los dos contactos al celular.
samsung20.agregar_contacto(matias)
samsung20.agregar_contacto(ramiro)

# Tarea 4: Mostrar todas las aplicaciones instaladas en el celular.
samsung20.mostrar_aplicaciones()
print("")

# Tarea 5: Mostrar todos los contactos guardados en el celular.
samsung20.mostrar_contactos()

# Tarea 6: Actualizar la versión de una de las aplicaciones instaladas en el celular.
samsung20.actualizar_aplicacion(facebook, "3.0.0")

# Tarea 7: Eliminar uno de los contactos del celular.
samsung20.eliminar_contacto(damian)


# Tarea 8: Eliminar aplicaciones con versiones anteriores a la 1.5.0
samsung20.limpiar_aplicaciones("5.0.0")

samsung20.mostrar_aplicaciones()
