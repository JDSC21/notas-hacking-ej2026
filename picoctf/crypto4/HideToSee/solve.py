import string

def atbash_decrypt(text):
    # Alfabetos normales
    lower_normal = string.ascii_lowercase
    upper_normal = string.ascii_uppercase
    
    # Alfabetos invertidos (Atbash)
    lower_atbash = lower_normal[::-1]
    upper_atbash = upper_normal[::-1]
    
    # Crear tabla de traducción
    trans_table = str.maketrans(lower_normal + upper_normal, lower_atbash + upper_atbash)
    
    return text.translate(trans_table)

if __name__ == "__main__":
    # Pega aquí el texto que obtuviste de steghide
    encrypted_text = input("Introduce el texto extraído de la imagen: ")
    
    decrypted_flag = atbash_decrypt(encrypted_text)
    print("\n--- Resultado ---")
    print(decrypted_flag)
