import tkinter as tk
from tkinter import messagebox

def enviar_mensaje():
    entrada_usuario = entrada.get()
    respuesta = procesar_mensaje(entrada_usuario)
    chat_texto.config(state=tk.NORMAL)
    chat_texto.insert(tk.END, f"Tú: {entrada_usuario}\n")
    chat_texto.insert(tk.END, f"Bot: {respuesta}\n")
    chat_texto.config(state=tk.DISABLED)
    entrada.delete(0, tk.END)

def procesar_mensaje(mensaje):
    if mensaje == "que restaurantes hay cerca mio?":
        return "Aquí tienes algunos restaurantes cercanos:"
    elif mensaje == "hola":
        return "¿Qué tipo de comida estás buscando?"
    elif mensaje == "pizza":
        presupuesto = obtener_presupuesto()
        if presupuesto == "alto":
            return "Aquí tienes algunas opciones de pizza gourmet y sus precios:"
        elif presupuesto == "medio":
            return "Aquí tienes algunas opciones de pizza y sus precios:"
        elif presupuesto == "bajo":
            return "Aquí tienes algunas opciones económicas de pizza y sus precios:"
    elif mensaje == "hamburguesa":
        presupuesto = obtener_presupuesto()
        if presupuesto == "alto":
            return "Aquí tienes algunas opciones de hamburguesas gourmet y sus precios:"
        elif presupuesto == "medio":
            return "Aquí tienes algunas opciones de hamburguesas y sus precios:"
        elif presupuesto == "bajo":
            return "Aquí tienes algunas opciones económicas de hamburguesas y sus precios:"
    elif mensaje == "agregar un restaurante a favoritos":
        return "¿Qué restaurante te gustaría agregar a tus favoritos?"
    elif mensaje == "ver mis restaurantes favoritos":
        return "Aquí están tus restaurantes favoritos:"
    elif mensaje == "que es lo mas barato cerca mio?":
        return "Aquí están las comidas mas economicas cerca de ti:"
    elif mensaje == "que es lo mas caro cerca mio?":
        return "Aquí están las comidas mas caras cerca de ti:"
    else:
        return "Lo siento, no entiendo. ¿Podrías reformular tu pregunta?"

def obtener_presupuesto():
    # Simulación de obtención del presupuesto del usuario
    # Aquí puedes implementar la lógica para obtener el presupuesto del usuario
    presupuesto = "Alto"  # Ejemplo: Presupuesto alto
    return presupuesto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bot de WhatsApp")

# Crear y configurar la ventana de chat
chat_texto = tk.Text(ventana, width=50, height=10)
chat_texto.config(state=tk.DISABLED)
chat_texto.pack(pady=10)

# Crear el campo de entrada
entrada = tk.Entry(ventana, width=50)
entrada.pack(pady=5)

# Crear el botón de enviar
boton = tk.Button(ventana, text="Enviar", command=enviar_mensaje, width=10)
boton.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
