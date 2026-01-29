# 🛡️ PyScanGUI - Port Scanner Multihilo

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Terminado-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Descripción
**PyScanGUI** es una herramienta de reconocimiento de red desarrollada en Python. A diferencia de los escáneres secuenciales tradicionales, esta herramienta utiliza **Multi-threading (hilos)** para escanear miles de puertos en segundos.

Cuenta con una interfaz gráfica (GUI) amigable que permite visualizar los puertos abiertos y los servicios estimados en tiempo real, sin congelar la aplicación durante el proceso.

![Captura de pantalla de la herramienta](ruta/de/tu/imagen_o_gif.png)
*(¡Sube una captura de tu herramienta funcionando aquí!)*

## ✨ Características Principales
* **Alto Rendimiento:** Implementación de colas (`Queue`) y hilos (`Threading`) para concurrencia.
* **Interfaz Gráfica:** Desarrollada con `Tkinter`, separando la lógica de escaneo del hilo de la interfaz (UI non-blocking).
* **Resolución de Servicios:** Identifica automáticamente el servicio asociado al puerto (ej: 80 -> http, 22 -> ssh).
* **Rango Completo:** Capacidad de escanear desde el puerto 1 hasta el 65535.
* **Portable:** Empaquetado como ejecutable `.exe` para Windows (no requiere instalación de Python).

## 🛠️ Tecnologías Utilizadas
Este proyecto demuestra el dominio de las siguientes librerías y conceptos:
* **`socket`**: Manejo de conexiones TCP/IP de bajo nivel.
* **`threading` & `queue`**: Gestión de concurrencia y sincronización de hilos.
* **`tkinter`**: Desarrollo de aplicaciones de escritorio (GUI).
* **`pyinstaller`**: Empaquetado y distribución de software.

## 🚀 Instalación y Uso

### Opción A: Ejecutar desde código fuente
1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/TU_USUARIO/PyScanGUI.git](https://github.com/TU_USUARIO/PyScanGUI.git)
    ```
2.  Navega a la carpeta:
    ```bash
    cd PyScanGUI
    ```
3.  Ejecuta el script:
    ```bash
    python scanner_gui.py
    ```

### Opción B: Usar el Ejecutable (Windows)
1.  Ve a la sección de [Releases](link_a_tus_releases) de este repositorio.
2.  Descarga el archivo `CiberScanner.exe`.
3.  Ejecútalo (No requiere Python instalado).

## ⚠️ Aviso Legal (Disclaimer)
Esta herramienta ha sido creada con fines **estrictamente educativos** y para pruebas de ciberseguridad en redes propias o autorizadas.
El autor no se hace responsable del mal uso que se le pueda dar. Escanear redes sin permiso es un delito.

---
**Desarrollado por [Tu Nombre]**
[LinkedIn](Tu Link) | [Portfolio](Tu Link)