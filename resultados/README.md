# COMMITS HISTORY
![alt text](image-18.png)
![alt text](image-19.png)



# Clone de proyecto. Instalacion librerias python
![image](https://github.com/user-attachments/assets/a18ddd7b-d4db-4e15-b10d-3bf3a520ea41)

![image](https://github.com/user-attachments/assets/f3080e73-df2f-4e6c-ae0d-0760719fec40)

```bash
docker compose up -d
```
![alt text](image.png)

# LUFFY CHALLENGE

```bash
docker exec -it luffy_challenge /bin/bash
```
![alt text](image-6.png)


### En caso de requerir instalar herramientas, utilizar
```bash
docker exec -u root -it luffy_challenge /bin/bash

```

```bash
grep -r --color=auto "flag" / 2>/dev/null
```
![alt text](image-1.png)
![alt text](image-2.png)

```bash
find / -type f \( -name "*.txt" -o -name "*.flag" -o -name "*.hidden" -o -name "*.enc" \) 2>/dev/null


find /home/luffy/ONEPIECE/ -type f -name "flag.txt" -exec cat {} + 2>/dev/null


747d70776d045300075503510a04555100505105000450000605065356010a015506015201
FLAG_0a16e1e85da2dc414b4447cd580d63f3
```
![alt text](image-3.png)

```bash
find / -name "*.zip" 2>/dev/null
```
![alt text](image-4.png)


```bash
find / -name "*.jpg" -o -name "*.png" 2>/dev/null
```
![alt text](image-5.png)

### La contraseña para poder acceder a la imagen del .zip es la misma que la utilizada para ingresar al primer contenedor

```bash
docker cp luffy_challenge:/home/luffy/ONEPIECE/Zou/Left_Hind_Leg/Casa_de_Inuarashi/poneglyph.zip C:\Users\arg21\OneDrive\Documents\uvg\ctf_onepiece_symetric_cipher_p1\
onepiece
imagen extraída
```
![alt text](part1/poneglyph.jpeg)

### Texto decifrado de la imagen
##### b'Crocodile targeted the Arabasta Kingdom because of its Poneglyph, which contained information on the whereabouts of Pluton, '
ejecutar el comando en la raiz del proyecto
```bash
python utils/extract_text_from_image.py
```
![alt text](image-14.png)

# ZORO CHALLENGE

```bash
    docker exec -it zoro_challenge /bin/bash
```
![alt text](image-7.png)

### Lectura de los archivos .txt o cualquier .* que pueda servir

```bash
    find / -type f \( -name "*.txt" -o -name "*.flag" -o -name "*.hidden" -o -name "*.enc" \) 2>/dev/null
```
![alt text](image-8.png)

### Este comando sirve para hacer una cat de cada uno, y tenerlo mas ordenado que en el caso anterior. Se ve mejor y legible la verdad
```bash
    for file in $(find /home/zoro -name "flag.txt"); do
        echo "=== $file ==="
        cat "$file"
        echo ""
    done
```
![alt text](image-9.png)

### Bandera encriptada y desencrpitada respectivamente
c5c698284ebf7b97371a0e693bc84a6fd1bb76346e9dc6d62d0dffe5b8f06d16d53b3d1967
FLAG_71fb5f88e9a62612bd9c1d030b1cab53

![alt text](part2/poneglyph.jpeg)


```bash
find / -name "*.zip" 2>/dev/null
```

### Copia a carpeta de windows
```bash
docker cp zoro_challenge:/home/zoro/ONEPIECE/Zou/Right_Hind_Leg/Casa_de_Inuarashi/poneglyph.zip "C:\Users\arg21\OneDrive\Documents\uvg\ctf_onepice_symmetric_cipher_p1\resultados\part2"

```

### Texto decifrado de la imagen
##### b'and created the Baroque Works syndicate in an attempt to bring down the Arabasta Kingdom and claim Pluton, employing Robin to read the Poneglyph'
ejecutar el comando en la raiz del proyecto
```bash
python utils/extract_text_from_image.py
```
![alt text](image-15.png)


# USOP CHALLENGE

### Lectura de los archivos .txt o cualquier .* que pueda servir

```bash
    find / -type f \( -name "*.txt" -o -name "*.flag" -o -name "*.hidden" -o -name "*.enc" \) 2>/dev/null
``` 
![alt text](image-10.png)

### Este comando sirve para hacer una cat de cada uno, y tenerlo mas ordenado que en el caso anterior. Se ve mejor y legible la verdad
```bash
    for file in $(find /home/usopp -name "flag.txt"); do
        echo "=== $file ==="
        cat "$file"
        echo ""
    done
```
![alt text](image-11.png)

a77742694e1c008c493f3c31d4c5d4794a6b0e62c91c12d9451973b213a39287ee4c57d03b
FLAG_6290739e295d64e0c37f4d839d2f3182


```bash
find / -name "*.zip" 2>/dev/null
```

### Copia a carpeta de windows
```bash
docker cp usopp_challenge:/home/usopp/ONEPIECE/Wano/Onigashima/Casa_de_Yamato/poneglyph.zip "C:\Users\arg21\OneDrive\Documents\uvg\ctf_onepice_symmetric_cipher_p1\resultados\part3"

```

![alt text](part3/poneglyph.jpeg)


### Texto decifrado de la imagen
##### b'When Robin finally got the chance to read this Poneglyph, however, she lied about its contents, which caused Crocodile to turn against her because he no longer needed her'ejecutar el comando en la raiz del proyecto
```bash
python utils/extract_text_from_image.py
```
![alt text](image-16.png)


### NAMI CHALLENGE

### Lectura de los archivos .txt o cualquier .* que pueda servir

```bash
    find / -type f \( -name "*.txt" -o -name "*.flag" -o -name "*.hidden" -o -name "*.enc" \) 2>/dev/null
``` 
![alt text](image-12.png)

### Este comando sirve para hacer una cat de cada uno, y tenerlo mas ordenado que en el caso anterior. Se ve mejor y legible la verdad
```bash
    for file in $(find /home/nami -name "flag.txt"); do
        echo "=== $file ==="
        cat "$file"
        echo ""
    done
```
3fc06ae08a1da3b0dfdd6cdf052435026360b73d778607f9c81ba4c5e3608269653ce10237
FLAG_c8886f1b7ab0ee2d4e12db4db5d2d4a9


![alt text](image-13.png)

```bash
find / -name "*.zip" 2>/dev/null
```


```bash
docker cp nami_challenge:/home/nami/ONEPIECE/Whole_Cake_Island/Whole_Cake_Chateau/Casa_de_Big_Mom/poneglyph.zip "C:\Users\arg21\OneDrive\Documents\uvg\ctf_onepice_symmetric_cipher_p1\resultados\part4"

```

![alt text](part4/poneglyph.jpeg)


### Texto decifrado de la imagen
##### b'When Robin finally got the chance to read this Poneglyph, however, she lied about its contents, which caused Crocodile to turn against her because he no longer needed her'ejecutar el comando en la raiz del proyecto
```bash
python utils/extract_text_from_image.py
```
![alt text](image-17.png)