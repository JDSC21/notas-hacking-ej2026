# Rust fixme 1

## Descripción

Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz).
## Solución

```
#Descomprimimos el tar

┌──(flavio㉿kali)-[~/picoCTF/Examen1/rustfixme2]
└─$ tar -xvzf fixme1.tar.gz                                                                                                               

fixme1/
fixme1/Cargo.toml
fixme1/Cargo.lock
fixme1/src/
fixme1/src/main.rs

#Inspeccionamos el archivo con cargo

┌──(flavio㉿kali)-[~/picoCTF/Examen1/fixme1]
└─$ cargo check                                   
    Checking rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/fixme1)
error: expected `;`, found keyword `let`
 --> src/main.rs:5:37
  |
5 |     let key = String::from("CSUCKS") // How do we end statements in Rust?
  |                                     ^ help: add `;` here
...
8 |     let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];
  |     --- unexpected token

error: argument never used
  --> src/main.rs:26:9
   |
25 |         ":?", // How do we print out a variable in the println function? 
   |         ---- formatting specifier missing
26 |         String::from_utf8_lossy(&decrypted_buffer)
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ argument never used
   |
help: format specifiers use curly braces, consider adding a format specifier
   |
25 |         ":?{}", // How do we print out a variable in the println function? 
   |            ++


#Arreglamos el código

┌─
└─$ cargo check     
    Checking rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/fixme1)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.15s
                                                                                                                                                                                                                                            

└─$ cargo run                
   Compiling rust_proj v0.1.0 (/home/flavio/picoCTF/Examen1/fixme1)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.97s
     Running `target/debug/rust_proj`
"picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}"
```

picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
## Notas adicionales

Usamos cargo para verificar la integridad del archivo, nos da errores de sintaxis y cuando los arreglamos nos arroja la flag.
## Referencias

https://doc.rust-lang.org/book/ch01-03-hello-cargo.html

https://doc.rust-lang.org/std/macro.println.html