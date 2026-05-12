# Rust fixme 2

## Descripción

The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee? Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/babfbee79718a6363826ba86300173ffde6d81577e9dd07d4130c53a7eecf6c3/fixme2.tar.gz).
## Solución

```
#Descomprimimos el tar


└─$ tar -xvzf fixme2.tar.gz
cd fixme2 
fixme2/
fixme2/Cargo.toml
fixme2/Cargo.lock
fixme2/src/
fixme2/src/main.rs

#Vemos los errores de sintaxis

└─$ cargo check  
   Compiling crossbeam-utils v0.8.20
   Compiling rayon-core v1.12.1
    Checking either v1.13.0
    Checking crossbeam-epoch v0.9.18
    Checking crossbeam-deque v0.8.5
    Checking rayon v1.10.0
    Checking xor_cryptor v1.2.3
    Checking rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/rustfixme2/fixme2)
error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference
 --> src/main.rs:9:5
  |
9 |     borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
  |     ^^^^^^^^^^^^^^^ `borrowed_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable
  |
help: consider changing this to be a mutable reference
  |
3 | fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // How do we pass values to a function that we want to change?
  |                                                        +++

error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference
  --> src/main.rs:20:5
   |
20 |     borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
   |     ^^^^^^^^^^^^^^^ `borrowed_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable
   |
help: consider changing this to be a mutable reference
   |
 3 | fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // How do we pass values to a function that we want to change?
   |                                                        +++

For more information about this error, try `rustc --explain E0596`.
error: could not compile `rust_proj` (bin "rust_proj") due to 2 previous errors

#Arreglamos el código
use xor_cryptor::XORCryptor;

fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // Recibimos una referencia mutable

    // Key for decryption
    let key = String::from("CSUCKS");

    // Editing our borrowed value
    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return; 
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
    println!("{}", borrowed_string);
}


fn main() {
    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "0d", "c4", "60", "f2", "12", "a0", "18", "03", "51", "03", "36", "05", "0e", "f9", "42", "5b"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    let mut party_foul = String::from("Using memory unsafe languages is a: "); // Declaramos la variable como mutable
    decrypt(encrypted_buffer, &mut party_foul); // Pasamos una referencia mutable
}

#Y lo ejecutamos
                                                                                                                                                                                                                                            

└─$ cargo check     
    Checking rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/rustfixme2/fixme2)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.25s
                                                                                                                                                                                                                                            

└─$ cargo run              
   Compiling crossbeam-utils v0.8.20
   Compiling either v1.13.0
   Compiling crossbeam-epoch v0.9.18
   Compiling crossbeam-deque v0.8.5
   Compiling rayon-core v1.12.1
   Compiling rayon v1.10.0
   Compiling xor_cryptor v1.2.3
   Compiling rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/rustfixme2/fixme2)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 11.25s
     Running `target/debug/rust_proj`
Using memory unsafe languages is a: PARTY FOUL! Here is your flag: picoCTF{4r3_y0u_h4v1n5_fun_y31?}

```

picoCTF{4r3_y0u_h4v1n5_fun_y31?}
## Notas adicionales

Mas errores de sintaxis con códigos de cargo.
## Referencias
