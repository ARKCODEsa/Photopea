# Photopea Desktop Viewer

Un visor de Photopea que incluye funcionalidades avanzadas como splash screen, barra de carga y efectos visuales. Este proyecto fue desarrollado con Python y PyQt5.

## Características

- **Pantalla de carga (Splash Screen):** Muestra un splash mientras el programa se inicializa.
- **Barra de carga dinámica:** Indica visualmente el progreso de la carga.
- **Interfaz moderna:** Con un diseño amigable y minimalista.
- **Footer personalizado:** Información o controles adicionales en la parte inferior.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/ARKCODEsa/Photopea.git
   cd Photopea
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar la aplicación, simplemente utiliza:

```bash
python src/photopea.py
```

## Requisitos

- Python 3.12.x
- PyQt5
- Otras dependencias especificadas en `requirements.txt`

## Tecnologías utilizadas

- **[Python](https://www.python.org/):** Lenguaje de programación principal del proyecto.
- **[PyQt5](https://riverbankcomputing.com/software/pyqt/intro):** Se utiliza para crear la interfaz gráfica y manejar eventos visuales.

## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con la nueva funcionalidad o corrección de errores:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y súbelos al repositorio:
   ```bash
   git add .
   git commit -m "Añadida nueva funcionalidad"
   git push origin feature/nueva-funcionalidad
   ```
4. Abre un pull request en GitHub.

## Créditos

Desarrollado por [ARKCODEsa](https://github.com/ARKCODEsa). Siente libre de contactar si tienes preguntas o sugerencias.

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).