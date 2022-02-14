# Adivina el número

En este repositorio vamos a desplegar un contrato inteligente básico, al cual se le asigna un número secreto y las personas van a poder adivinar dicho número pero deben pagar 1 eth para participar del juego.

Seguimos la explicación de canal de youtube de Moralis -> https://youtu.be/yJQJ7pw_9C0

## Prerequisitos

Por favor instale o tenga instalado lo siguiente:

- [nodejs y npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)

## Instalación

1. [Instalar brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), sino lo haz hecho, esta es una forma sencilla de hacerlo.


```bash
pip install eth-brownie
```
Sino funciona podrias hacerlo via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```

2. Clone este repo 
```
https://github.com/camohe90/brownie_basic
```

3. Configura las variables de entorno

Configura tus [variables de entorno](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) `WEB3_INFURA_PROJECT_ID`, y `PRIVATE_KEY` . 

Puedes obtener un `WEB3_INFURA_PROJECT_ID` creando una cuenta en [Infura](https://infura.io/). Creas un nuevo proyecto y seleccionas la red de pruebas rinkeby. 

En cuanto a tu `PRIVATE_KEY` las puedes obtener de una wallet como [metamask](https://metamask.io/). 

Tambien vas a necesitar ETH rinkeby de prueba. Puedes obtener ETH usando el siguiente [faucet de rinkeby en el siguiente enlace](https://faucets.chain.link/rinkeby). Si eres nuevo por favor, [mira este video.](https://www.youtube.com/watch?v=P7FX_1PePX0)

Puedes agregar tus variables de entorno en el archivo `.env`:

```
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

Luego, debes estar seguro que tu archivo `brownie-config.yaml` tenga:

```
dotenv: .env
```

## Interactuando con los contratos

Ahora si estamos listos para ejecutar ejecutar el scrip deploy_guess_number

```bash
brownie run deploy_guess_number.py --network rinkeby
```

Si al ejecutar este comando se despliega el contrato correctamente deberian recibir un mensaje como el siguiente

```bash
Running 'scripts/deploy_guess_number.py::main'...
Transaction sent: 0xba68cb3f66183b971a5cc861779b18a32af3bd1535860b7ad7777196185c16b0
  Gas price: 2.32478609 gwei   Gas limit: 291404   Nonce: 433
  Guess_number.constructor confirmed   Block: 10140847   Gas used: 264913 (90.91%)
  Guess_number deployed at: 0x744359d5D5e43e4d7975da6394C30AACb963fb45
```

Ahora solo haría falta ejecutar el script play_guess_number en la linea 6 se debe colocar la dirección del contrato que se desplego anteriormente, por defecto brownie crea un objeto donde agrupa las direcciones de los contratos inteligentes desplegados, y normalmente uno trabaja con la última dirección de contrato.

Pero muchas veces necesitamos trabajar o experimentar con varios contratos ya desplegados por lo cual dejar por defecto la dirección del ultimo desplegado no es recomendable por eso es mejor que en la linea 6 coloques directamente la dirección del contrato.

En la linea 11 el primer parametro que se le pasa a la función play es el número que estoy adivinando.

Para ello usamos el siguiente comando

```bash
brownie run play_guess_number.py --network rinkeby
```
Y por ultimo podemos utilzar el script balance_guess_number que nos permite consultar cuando dinero se llevaria la persona que adivine el número, el resultado lo entrega en Wei

```bash
brownie run balance_guess_number.py --network rinkeby
```


## Recursos

Para empezar con brownie:

* [Canal de youtube de moralis ](https://youtu.be/yJQJ7pw_9C0)
* Puedes revisar los otros [Brownie mixes](https://github.com/brownie-mix/) que pueden ser usado como punto de partida para tus propios contratos. Allí encontraras ejemplos para emepzar como.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).

