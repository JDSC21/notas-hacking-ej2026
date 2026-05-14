# VaultDoor3


## Descripción

This vault uses for-loops and byte arrays.
The source code for this vault is here: VaultDoor3.java
hint: Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solución


Examinamos el código fuente en Java que se nos da
Modificamos el programa en Java para revertir el anagrama
import java.util.*;

```
class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
      //  System.out.print("Enter vault password: ");
     //   String userInput = scanner.next();
    //String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword()) {
        System.out.println("Access granted.");
    } else {
        System.out.println("Access denied!");
        }
    }
    // -Minion #2671
    public boolean checkPassword() {
        String password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String flag = new String(buffer);
        System.out.println(flag);
        return true;
    }
}

```