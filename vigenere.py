import tkinter as tk
from tkinter import messagebox

def cifrar_vigenere(texto, clave):
    texto_cifrado = ''
    clave_longitud = len(clave)
    for i in range(len(texto)):
        caracter = texto[i]
        if 'a' <= caracter <= 'z':
            desplazamiento = ord(clave[i % clave_longitud].lower()) - ord('a')
            texto_cifrado += chr(((ord(caracter) - ord('a') + desplazamiento) % 26) + ord('a'))
        elif 'A' <= caracter <= 'Z':
            desplazamiento = ord(clave[i % clave_longitud].lower()) - ord('a')
            texto_cifrado += chr(((ord(caracter) - ord('A') + desplazamiento) % 26) + ord('A'))
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrar_vigenere(texto, clave):
    texto_descifrado = ''
    clave_longitud = len(clave)
    for i in range(len(texto)):
        caracter = texto[i]
        if 'a' <= caracter <= 'z':
            desplazamiento = ord(clave[i % clave_longitud].lower()) - ord('a')
            texto_descifrado += chr(((ord(caracter) - ord('a') - desplazamiento) % 26) + ord('a'))
        elif 'A' <= caracter <= 'Z':
            desplazamiento = ord(clave[i % clave_longitud].lower()) - ord('a')
            texto_descifrado += chr(((ord(caracter) - ord('A') - desplazamiento) % 26) + ord('A'))
        else:
            texto_descifrado += caracter
    return texto_descifrado

def procesar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()

    if not texto or not clave:
        messagebox.showerror("Error", "Por favor, ingrese el texto y la clave.")
        return

    if not clave.isalpha():
        messagebox.showerror("Error", "La clave debe contener solo letras.")
        return

    if modo.get() == "Cifrar":
        resultado = cifrar_vigenere(texto, clave)
    elif modo.get() == "Descifrar":
        resultado = descifrar_vigenere(texto, clave)
    else:
        messagebox.showerror("Error", "Seleccione un modo válido.")
        return

    salida_resultado.delete("1.0", tk.END)
    salida_resultado.insert(tk.END, resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado Vigenère")

# Etiquetas y entradas
tk.Label(ventana, text="Texto:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entrada_texto = tk.Text(ventana, height=5, width=40)
entrada_texto.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Clave:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entrada_clave = tk.Entry(ventana, width=30)
entrada_clave.grid(row=1, column=1, padx=10, pady=5)

# Opciones de modo
modo = tk.StringVar(value="Cifrar")
tk.Radiobutton(ventana, text="Cifrar", variable=modo, value="Cifrar").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Radiobutton(ventana, text="Descifrar", variable=modo, value="Descifrar").grid(row=2, column=1, sticky="w", padx=10, pady=5)

# Botón de procesamiento
boton_procesar = tk.Button(ventana, text="Procesar", command=procesar_texto)
boton_procesar.grid(row=3, column=0, columnspan=2, pady=10)

# Área de resultados
tk.Label(ventana, text="Resultado:").grid(row=4, column=0, sticky="nw", padx=10, pady=5)
salida_resultado = tk.Text(ventana, height=5, width=40, state="normal")
salida_resultado.grid(row=4, column=1, padx=10, pady=5)

# Iniciar la aplicación
ventana.mainloop()
