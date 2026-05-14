# Reto Timer

## Descripción 
You will find the flag after analysing this apk
Download here.

## Solución

Instalar jadx decompilador de java
`sudo apt install jadx`

Abrir el archivo .apk del reto : 
`File - Open Files``

Una vez abierto el archivo Navitation - Text Search y escribe picoCTF
```
package com.example.timer;

/* JADX INFO: loaded from: classes3.dex */
public final class BuildConfig {
    public static final String APPLICATION_ID = "com.example.timer";
    public static final String BUILD_TYPE = "debug";
    public static final boolean DEBUG = Boolean.parseBoolean("true");
    public static final int VERSION_CODE = 1;
    public static final String VERSION_NAME = "picoCTF{...}";
}
```