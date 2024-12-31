import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget, QMainWindow
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView  # Necesario para la ventana web principal


# Clase para mostrar la pantalla de presentación
class SplashScreenApp(QLabel):
    SPLASH_DURATION = 5000  # Tiempo en milisegundos (5000 ms = 5 segundos)

    def __init__(self, image_path, main_window):
        super(SplashScreenApp, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAlignment(Qt.AlignCenter)
        self.main_window = main_window  # Referencia a la ventana principal

        # Intentar cargar la imagen de splash
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.setPixmap(pixmap)
            self.resize(pixmap.width(), pixmap.height())
        else:
            # Si falla la imagen, mostrar un mensaje de error
            self.setText("Error: Splash image not found!")
            self.resize(300, 200)

        self.center_on_screen()

        # Ejecutar el siguiente paso después del tiempo de presentación
        QTimer.singleShot(self.SPLASH_DURATION, self.open_main_window)

    def center_on_screen(self):
        screen = QDesktopWidget().availableGeometry().center()
        frame_rect = self.frameGeometry()
        frame_rect.moveCenter(screen)
        self.move(frame_rect.topLeft())

    def open_main_window(self):
        # Cerrar splash y mostrar la ventana principal
        self.close()
        self.main_window.show()  # Mostrar la ventana principal


# Clase para la ventana principal que carga la URL
class MainWindow(QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Photopea")
        self.setGeometry(100, 100, 1024, 768)

        # Crear la vista web para la URL
        browser = QWebEngineView()
        browser.setUrl(QUrl(url))

        # Configurar el navegador como widget central
        self.setCentralWidget(browser)


# Código principal
def main():
    # Configurar la ruta de la imagen para el splash
    image_path = os.path.abspath("resources/image/splash.png")
    url_to_load = "https://www.photopea.com/"

    # Crear una única instancia de QApplication
    app = QApplication(sys.argv)

    # Crear la ventana principal (URL incrustada)
    main_window = MainWindow(url_to_load)

    # Crear y mostrar la pantalla de presentación
    splash = SplashScreenApp(image_path, main_window)
    splash.show()

    # Ejecutar el ciclo de eventos
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
