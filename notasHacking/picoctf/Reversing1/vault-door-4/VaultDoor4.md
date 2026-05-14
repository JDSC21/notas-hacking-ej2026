# VaultDoor4

## Description

This vault uses ASCII encoding for the password.
The source code for this vault is here: VaultDoor4.java

Use a search engine to find an "ASCII table"

You will also need to know the difference between octal, decimal, and hexadecimal numbers.

## Solución

Examinamos el código fuente en Java que se nos da
La Flag esta codificada en diferentes sistemas numericos solo hay que convertirlos a texto
Forma 1 - javascript
Ejecutamos el siguiente código en una consola javascript del navegador
String.fromCharCode(106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  , 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,0142, 0131, 0164, 063 , 0163, 0137, 0143, 061)  + ['9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e'].join('')

Forma 2 - modificando código en JAva
Modificamos el código fuente en Java para hacerlo
````
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
        //Scanner scanner = new Scanner(System.in);
        //System.out.print("Enter vault password: ");
        //String userInput = scanner.next();
    //String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword()) {
        System.out.println("Access granted.");
    } else {
        System.out.println("Access denied!");
        }
    }

    // -Minion #7781
    public boolean checkPassword() {
        //byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
    /*     for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        } */
        String flag = new String(myBytes);
        System.out.println(flag);
        return true;
    }
}

```