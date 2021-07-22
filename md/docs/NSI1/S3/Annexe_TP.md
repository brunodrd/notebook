Structure d'un fichier BMP - résumé
=============================

Un fichier BMP comporte trois parties obligatoires: l'entête du fichier, l'entête de l'image et le tableau d'octets représentant l'image. Il peut y avoir également des parties optionnelles.  
Voici une description, issue de [wikipedia](https://en.wikipedia.org/wiki/BMP_file_format), des deux entêtes.

## Entête du fichier

| Offset(hex) | Offset(dec) | Size    | Purpose                                                                                                                                                                                                                                                                                              |
|------------|------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 00         | 0          | 2 bytes | The header field used to identify the BMP and DIB file is 0x42 0x4D in hexadecimal, same as BM in ASCII. The following entries are possible:
||||**BM**: Windows 3.1x, 95, NT, ... etc|
||||**BA**: OS/2 struct bitmap array|
||||**CI**: OS/2 struct color icon|
||||**CP**: OS/2 const color pointer|
||||**IC**: OS/2 struct icon|
||||**PT**: OS/2 pointer|
| 02         | 2          | 4 bytes | The size of the BMP file in bytes                                                                                                                                                                                                                                                                    |
| 06         | 6          | 2 bytes | Reserved; actual value depends on the application that creates the image, if created manually can be 0                                                                                                                                                                                               |
| 08         | 8          | 2 bytes | Reserved; actual value depends on the application that creates the image, if created manually can be 0                                                                                                                                                                                               |
| 0A         | 10         | 4 bytes | The offset, i.e. starting address, of the byte where the bitmap image data (pixel array) can be found.                                                                                                                                                                                               |


## Entête de l'image

| Offset (hex) | Offset (dec) | Size (bytes) | Windows BITMAPINFOHEADER[2]                                                                                     |
|--------------|--------------|--------------|-----------------------------------------------------------------------------------------------------------------|
| 0E           | 14           | 4            | the size of this header, in bytes (40)                                                                          |
| 12           | 18           | 4            | the bitmap width in pixels (signed integer)                                                                     |
| 16           | 22           | 4            | the bitmap height in pixels (signed integer)                                                                    |
| 1A           | 26           | 2            | the number of color planes (must be 1)                                                                          |
| 1C           | 28           | 2            | the number of bits per pixel, which is the color depth of the image. Typical values are 1, 4, 8, 16, 24 and 32. |
| 1E           | 30           | 4            | the compression method being used. See the next table for a list of possible values                             |
| 22           | 34           | 4            | the image size. This is the size of the raw bitmap data; a dummy 0 can be given for BI_RGB bitmaps.             |
| 26           | 38           | 4            | the horizontal resolution of the image. (pixel per metre, signed integer)                                       |
| 2A           | 42           | 4            | the vertical resolution of the image. (pixel per metre, signed integer)                                         |
| 2E           | 46           | 4            | the number of colors in the color palette, or 0 to default to 2n                                                |
| 32           | 50           | 4            | the number of important colors used, or 0 when every color is important; generally ignored                      |

