import tkinter as tk
from tkinter import messagebox

def cifrar_cesar(texto, desplazamiento):
    """Cifra un texto usando el cifrado César."""
    resultado = ''
    for caracter in texto:
        if 'a' <= caracter <= 'z':
            resultado += chr(((ord(caracter) - ord('a') + desplazamiento) % 26) + ord('a'))
        elif 'A' <= caracter <= 'Z':
            resultado += chr(((ord(caracter) - ord('A') + desplazamiento) % 26) + ord('A'))
        else:
            resultado += caracter
    return resultado

def descifrar_cesar(texto, desplazamiento):
    """Descifra un texto cifrado con el cifrado César."""
    return cifrar_cesar(texto, -desplazamiento)

def realizar_cifrado():
    texto = entry_texto.get()  # Obtener el texto desde la interfaz
    try:
        desplazamiento = int(entry_desplazamiento.get())  # Obtener el desplazamiento
        if not texto:
            raise ValueError("El texto no puede estar vacío.")
        texto_cifrado = cifrar_cesar(texto, desplazamiento)  # Cifrar
        resultado_cifrado.set(f"Texto cifrado: {texto_cifrado}")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

def realizar_descifrado():
    texto = entry_texto.get()  # Obtener el texto desde la interfaz
    try:
        desplazamiento = int(entry_desplazamiento.get())  # Obtener el desplazamiento
        if not texto:
            raise ValueError("El texto no puede estar vacío.")
        texto_descifrado = descifrar_cesar(texto, desplazamiento)  # Descifrar
        resultado_descifrado.set(f"Texto descifrado: {texto_descifrado}")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado César")

# Crear etiquetas y entradas
tk.Label(root, text="Texto:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_texto = tk.Entry(root, width=40)
entry_texto.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Desplazamiento:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_desplazamiento = tk.Entry(root, width=20)
entry_desplazamiento.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Crear botones
btn_cifrar = tk.Button(root, text="Cifrar", command=realizar_cifrado)
btn_cifrar.grid(row=2, column=0, padx=10, pady=10)

btn_descifrar = tk.Button(root, text="Descifrar", command=realizar_descifrado)
btn_descifrar.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Mostrar resultados
resultado_cifrado = tk.StringVar()
resultado_descifrado = tk.StringVar()

tk.Label(root, textvariable=resultado_cifrado, fg="blue").grid(row=3, column=0, columnspan=2, padx=10, pady=5)
tk.Label(root, textvariable=resultado_descifrado, fg="green").grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Ejecutar el bucle principal de la interfaz
root.mainloop()
