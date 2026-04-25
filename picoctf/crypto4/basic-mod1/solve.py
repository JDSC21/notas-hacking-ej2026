import string
import os

def decode_message(filename):
    """
    Lee un archivo con números, aplica módulo 37 a cada uno
    y mapea el resultado a un set de caracteres específico:
    0-25: A-Z
    26-35: 0-9
    36: _
    """
    with open(filename, 'r') as file:
        # Leer el contenido del archivo y separar los números
        numbers = file.read().strip().split()

    decrypted_message = ""
    
    for num in numbers:
        mod_val = int(num) % 37
        
        # Mapear según las reglas del reto
        if 0 <= mod_val <= 25:
            decrypted_message += string.ascii_uppercase[mod_val]
        elif 26 <= mod_val <= 35:
            decrypted_message += string.digits[mod_val - 26]
        elif mod_val == 36:
            decrypted_message += "_"
            
    # Devolver el mensaje envuelto en el formato de la bandera
    return f"picoCTF{{{decrypted_message}}}"

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio donde se encuentra este script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Nombre del archivo proporcionado en el reto
    filename = os.path.join(script_dir, "message.txt")
    flag = decode_message(filename)
    print("La bandera es:", flag)
