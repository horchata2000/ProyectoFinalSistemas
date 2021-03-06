from Errores import *
import shutil
import os

logger = Logger()


def mover_todo(origen, destino,sobreescribir=False,dentro=False):

    if dentro:
        for contenido in os.listdir(origen):
            if comprobar_existe(destino + contenido) and not sobreescribir:
                raise Exception(f"{destino + contenido} ya existe, -s para sobreescribir")

            elif not comprobar_existe(destino):
                raise Exception(f"{destino} no existe")
            else:
                if comprobar_existe(destino + contenido):
                    os.remove(destino + contenido)
                shutil.move(origen + contenido, destino)
                logger.log(f"Se ha movido {contenido} -> {destino}")
    else:
        shutil.move(origen,destino)

def mover(origen, destino,sobreescribir=False):

    dividir_ruta=origen.split("/")
    ultimo=dividir_ruta.pop()
    if not comprobar_existe(destino):
        raise Exception(f"{destino} no existe")

    if not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

    if comprobar_existe(destino + ultimo) and not sobreescribir:
        raise Exception(f"{destino+ultimo} ya existe, -s para sobreescribir")

    else:
        if comprobar_existe(destino + ultimo):
            os.remove(destino+ultimo)
        shutil.move(origen,destino)
        logger.log(f"Se ha movido {origen} -> {destino}")


def renombrar(origen, destino,sobreescribir=False):
    if comprobar_existe(destino) and not sobreescribir:
        raise Exception(f"{destino} ya existe, -s para sobreescribir")

    elif not comprobar_existe(origen):
        raise Exception(f"{origen} no existe")

    else:
        os.rename(origen, destino)
        logger.log(f"{origen} -> {destino}")
