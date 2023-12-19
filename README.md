<div align="center"><h1> 🎮✨ Tetris ✨🎮 </h1></div>


En este proyecto se construyó el mítico juego 🕹️ **Tetris** 🕹️ mediante el uso de la librería **pygame** 👾.

Se lograron implementar **todas** las funcionalidades solicitadas, por lo que no debería haber problemas de funcionamiento 👌.

## Ejecución 💻

El proyecto fue realizado mediante **python 3.11.6**, por lo que cualquier problema respecto a la ejecución podría deberse a la versión de **python** utilizada.

Además, debe estar instalada la librería **pygame**. Para esto, basta ejecutar el comando:

```
pip3 install pygame
```

Para ejecutar el programa, basta con abrir una terminal desde el directorio principal y ejecutar:

```
python3 main.py
```

## Importante ⚠️

Este proyecto fue implemetado con una resolución de 2880 x 1800. Si se utiliza una resolución de menor tamaño, **es importante** ajustar el parámetro de **CELL_SIZE**. Por defecto, es de 40. Sin embargo, si hace falta, es recomendable ajustarlo a 30 de la siguiente forma

```py
# parameters.py
CELL_SIZE = 30
```

## Aspectos implementados 📝

En la siguiente tabla se muestran los aspectos implementados según el **criterio de evaluación**. Por lo general se encuentran todos los aspectos implementados, a menos que haya algún detalle menor.

| Criterio | Implementación | Detalle |
|----------|:---------:|--------|
| Interfaz de juego       | ✅ Logrado | Se pueden comprobar en la ejecución     |
| Sistema de rotación     | ✅ Logrado | Se pueden comprobar en la ejecución    |
| Generación de piezas    | ✅ Logrado | [tetris.py L35-L38](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/tetris.py#L35) |
| Controles               | ✅ Logrado | [game.py L89-L125](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L89)    |
| Pieza fantasma          | ✅ Logrado | Se pueden comprobar en la ejecución    |
| Pieza en retención      | ✅ Logrado | Se pueden comprobar en la ejecución    |
| Niveles y velocidad     | ✅ Logrado | [game.py L50-L54](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L50),  [game.py L70-L72](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L70)     |
| Puntaje                 | ✅ Logrado | [game.py L60-L74](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L60), [game.py L202](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L202), [game.py L183](https://github.com/matiasmasjuan/Tetris-Pygame/blob/3d750ae2fa7ed98fab42da35ef18e30342a25adb/game.py#L183)  |
| Música                  | ✅ Logrado | Se pueden comprobar en la ejecución     |
| Loop de juego           | ✅ Logrado | Se pueden comprobar en la ejecución     |
| Instalación y ejecución | ✅ Logrado |  Este mismo documento    |
| Calidad general         | ✅ Logrado |  Esperemos que así sea 😄  |


<hr>

**Autor**: Matías Masjuan