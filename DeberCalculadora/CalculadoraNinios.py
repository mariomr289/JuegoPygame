#-*- coding: utf-8 -*-

"""
Calculadora simple en python con GTK
Autores: Mario Merlo, Fernando Recalde
Licencia: Creative Commons
Versión: 1.0
"""

import pygtk
pygtk.require('2.0')
import gtk

class interface():

    def __init__(self):

        self.entryValues = ''

        # Crea la ventana principal y conecta la señal de delete_event signal para finalizar la aplicación
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_border_width(15)
        self.window.set_size_request(600,550)
        self.window.connect("delete-event", self.closeWindow)
        self.window.set_title("Calculadora para Niños")

        # un cuadro de texto donde mostrar los resultados
        self.resultado = gtk.Entry(255)
        self.resultado.set_text("")

        #un contenedor de imagen para el número 7
        self.animation7 = gtk.gdk.PixbufAnimation("numeros/7.gif")
        self.image7 = gtk.Image()
        self.image7.set_from_animation(self.animation7)
        # un botón que contenga el control de imagen del número 7
        self.button7 = gtk.Button()
        self.button7.add(self.image7)
        self.button7.connect("clicked", self.button_clicked, "7")

        # un contenedor de imagen para el número 8
        self.animation8 = gtk.gdk.PixbufAnimation("numeros/8.gif")
        self.image8 = gtk.Image()
        self.image8.set_from_animation(self.animation8)
        # un botón que contenga el control de imagen del número 8
        self.button8 = gtk.Button()
        self.button8.add(self.image8)
        self.button8.connect("clicked", self.button_clicked, "8")

        # un contenedor de imagen para el número 9
        self.animation9 = gtk.gdk.PixbufAnimation("numeros/9.gif")
        self.image9 = gtk.Image()
        self.image9.set_from_animation(self.animation9)
        # un botón que contenga el control de imagen del número 9
        self.button9 = gtk.Button()
        self.button9.add(self.image9)
        self.button9.connect("clicked", self.button_clicked, "9")

        # un contenedor de imagen para el signo +
        self.animationMas = gtk.gdk.PixbufAnimation("numeros/mas.gif")
        self.imageMas = gtk.Image()
        self.imageMas.set_from_animation(self.animationMas)
        # un botón que contenga el control de imagen del signo +
        self.buttonMas = gtk.Button()
        self.buttonMas.add(self.imageMas)
        self.buttonMas.connect("clicked", self.button_clicked, "+")

        # un contenedor de imagen para el número 4
        self.animation4 = gtk.gdk.PixbufAnimation("numeros/4.gif")
        self.image4 = gtk.Image()
        self.image4.set_from_animation(self.animation4)
        # un botón que contenga el control de imagen del número 4
        self.button4 = gtk.Button()
        self.button4.add(self.image4)
        self.button4.connect("clicked", self.button_clicked, "4")

        # un contenedor de imagen para el número 5
        self.animation5 = gtk.gdk.PixbufAnimation("numeros/5.gif")
        self.image5 = gtk.Image()
        self.image5.set_from_animation(self.animation5)
        # un botón que contenga el control de imagen del número 5
        self.button5 = gtk.Button()
        self.button5.add(self.image5)
        self.button5.connect("clicked", self.button_clicked, "5")

        # un contenedor de imagen para el número 6
        self.animation6 = gtk.gdk.PixbufAnimation("numeros/6.gif")
        self.image6 = gtk.Image()
        self.image6.set_from_animation(self.animation6)
        # un botón que contenga el control de imagen del número 6
        self.button6 = gtk.Button()
        self.button6.add(self.image6)
        self.button6.connect("clicked", self.button_clicked, "6")

        # un contenedor de imagen para el signo -
        self.animationMenos = gtk.gdk.PixbufAnimation("numeros/menos.gif")
        self.imageMenos = gtk.Image()
        self.imageMenos.set_from_animation(self.animationMenos)
        # un botón que contenga el control de imagen del signo -
        self.buttonMenos = gtk.Button()
        self.buttonMenos.add(self.imageMenos)
        self.buttonMenos.connect("clicked", self.button_clicked, "-")

        # un contenedor de imagen para el número 1
        self.animation1 = gtk.gdk.PixbufAnimation("numeros/1.gif")
        self.image1 = gtk.Image()
        self.image1.set_from_animation(self.animation1)
        # un botón que contenga el control de imagen del número 1
        self.button1 = gtk.Button()
        self.button1.add(self.image1)
        self.button1.connect("clicked", self.button_clicked, "1")

        # un contenedor de imagen para el número 2
        self.animation2 = gtk.gdk.PixbufAnimation("numeros/2.gif")
        self.image2 = gtk.Image()
        self.image2.set_from_animation(self.animation2)
        # un botón que contenga el control de imagen del número 2
        self.button2 = gtk.Button()
        self.button2.add(self.image2)
        self.button2.connect("clicked", self.button_clicked, "2")

        # un contenedor de imagen para el número 3
        self.animation3 = gtk.gdk.PixbufAnimation("numeros/3.gif")
        self.image3 = gtk.Image()
        self.image3.set_from_animation(self.animation3)
        # un botón que contenga el control de imagen del número 3
        self.button3 = gtk.Button()
        self.button3.add(self.image3)
        self.button3.connect("clicked", self.button_clicked, "3")

        # un contenedor de imagen para el signo =
        self.animationIgual = gtk.gdk.PixbufAnimation("numeros/igual.gif")
        self.imageIgual = gtk.Image()
        self.imageIgual.set_from_animation(self.animationIgual)
        # un botón que contenga el control de imagen del signo =
        self.buttonIgual = gtk.Button()
        self.buttonIgual.add(self.imageIgual)
        self.buttonIgual.connect("clicked", self.button_clicked, "=")

        # un contenedor de imagen para el numero 0
        self.animationCero = gtk.gdk.PixbufAnimation("numeros/0.gif")
        self.imageCero = gtk.Image()
        self.imageCero.set_from_animation(self.animationCero)
        # un botón que contenga el control de imagen del signo borrar
        self.buttonCero = gtk.Button()
        self.buttonCero.add(self.imageCero)
        self.buttonCero.connect("clicked", self.button_clicked, "0")

        # un contenedor de imagen para el signo borrar
        self.animationBorrar = gtk.gdk.PixbufAnimation("numeros/borrar3.gif")
        self.imageBorrar = gtk.Image()
        self.imageBorrar.set_from_animation(self.animationBorrar)
        # un botón que contenga el control de imagen del signo borrar
        self.buttonBorrar = gtk.Button()
        self.buttonBorrar.add(self.imageBorrar)
        self.buttonBorrar.connect("clicked",  self.clearScreen, None)

        # un contenedor de imagen para el boton salir
        self.animationSalir = gtk.gdk.PixbufAnimation("numeros/salir3.gif")
        self.imageSalir = gtk.Image()
        self.imageSalir.set_from_animation(self.animationSalir)
        # un botón que contenga el control de imagen de salir
        self.buttonSalir = gtk.Button()
        self.buttonSalir.add(self.imageSalir)
        self.buttonSalir.connect("clicked", self.closeWindow, None)

        # una caja horizontal que contenga el cuadro de texto
        self.canvas1 = gtk.HBox()
        self.canvas1.pack_start(self.resultado)

        # una caja horizontal que contenga los botones
        self.canvas2 = gtk.HBox()
        self.canvas2.pack_start(self.button7)
        self.canvas2.pack_start(self.button8)
        self.canvas2.pack_start(self.button9)
        self.canvas2.pack_start(self.buttonMas)

        # una caja horizontal que contenga los botones
        self.canvas3 = gtk.HBox()
        self.canvas3.pack_start(self.button4)
        self.canvas3.pack_start(self.button5)
        self.canvas3.pack_start(self.button6)
        self.canvas3.pack_start(self.buttonMenos)

        # una caja horizontal que contenga los botones
        self.canvas4 = gtk.HBox()
        self.canvas4.pack_start(self.button1)
        self.canvas4.pack_start(self.button2)
        self.canvas4.pack_start(self.button3)
        self.canvas4.pack_start(self.buttonIgual)

        # una caja horizontal que contenga los botones
        self.canvas5 = gtk.HBox()
        self.canvas5.pack_start(self.buttonCero)
        self.canvas5.pack_start(self.buttonBorrar)
        self.canvas5.pack_start(self.buttonSalir)

        # una caja principal para contener a todos los botonos
        self.canvasMain = gtk.VBox()
        self.window.add(self.canvasMain)
        self.canvasMain.pack_start(self.canvas1)
        self.canvasMain.pack_start(self.canvas2)
        self.canvasMain.pack_start(self.canvas3)
        self.canvasMain.pack_start(self.canvas4)
        self.canvasMain.pack_start(self.canvas5)


        # mostrar los elementos del formulario
        self.window.show()
        self.canvas1.show()
        self.canvas2.show()
        self.canvas3.show()
        self.canvas4.show()
        self.canvas5.show()
        self.canvasMain.show()
        self.button7.show()
        self.button8.show()
        self.button9.show()
        self.buttonMas.show()
        self.button4.show()
        self.button5.show()
        self.button6.show()
        self.buttonMenos.show()
        self.button1.show()
        self.button2.show()
        self.button3.show()
        self.buttonIgual.show()
        self.buttonCero.show()
        self.buttonBorrar.show()
        self.buttonSalir.show()
        self.image7.show()
        self.image8.show()
        self.image9.show()
        self.imageMas.show()
        self.image4.show()
        self.image5.show()
        self.image6.show()
        self.imageMenos.show()
        self.image1.show()
        self.image2.show()
        self.image3.show()
        self.imageIgual.show()
        self.imageCero.show()
        self.imageBorrar.show()
        self.imageSalir.show()
        self.resultado.show()


    # cuando se invoca (con la señal delete_event), finaliza la aplicación
    def closeWindow(self, widget, data=None):
        gtk.main_quit()
        return gtk.FALSE

    # se invoca cuando el botón es pulsado.  Simplemente imprime un mensaje.
    def button_clicked(self, widget, data=None):
        if (data == "="):
            self.__setResult()
        else:
            self.entryValues += data
        self.resultado.set_text(self.entryValues)

    # se invoca para borrar el cuadro de texto
    def clearScreen(self, widget, data=None):
        self.entryValues = ""
        self.resultado.set_text("")

    def __setResult(self):
        ''' Hace las cuentas matematicas y muestra los resultados '''
        self.entryValues = str(eval(self.entryValues))
        self.resultado.set_text(self.entryValues)

    def main(self):
        gtk.main()
        return 0


if __name__ == "__main__":
    winCalculadora = interface()
    winCalculadora.main()