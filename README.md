# Token ERC20

En este repositorio vamos a desplegar un contrato inteligente que permite emitir un token.

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
https://github.com/camohe90/erc20
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

Ahora si estamos listos para ejecutar ejecutar el script deploy_token_number

```bash
brownie run deploy_guess_number.py --network rinkeby
```

Si al ejecutar este comando se despliega el contrato correctamente deberian recibir un mensaje como el siguiente

```bash
Erc20Project is the active project.

Running 'scripts/deploy_token.py::main'...
Transaction sent: 0xea60b1addbc1736e23a5b2e8a8e780f89971c58e642914ef5f4a8b6561699b43
  Gas price: 1.000000009 gwei   Gas limit: 1115992   Nonce: 441
  Arkdia.constructor confirmed   Block: 10168212   Gas used: 1014539 (90.91%)
  Arkdia deployed at: 0x49e04434fd8668703eeba1409761677e039DaB90
```

Ahora solo haría falta ejecutar el script functions en la parte de mint (emitir los tokents) en la linea 6 debemos colocar la dirección del contrato que se acaba de desplegar y en la linea 7 la dirección de la billetera a la cual queremos enviar los tokens. Para ello debemos ejecutar el siguiente comando.

```bash
brownie run scripts/functions.py mint --network rinkeby
```
Una vez ejecutado podriamos ver el saldo de los tokens emitidos en la billetera de destino que agregamos anteriormente.

Si quisieramos quemar tokens solamente debemos ejecutar en el script funciones la parte de burn.
Para ello ejecutamos el siguiente comando


```bash
brownie run scripts/functions.py burn --network rinkeby
```


## Recursos

Para empezar con brownie:

* Puedes revisar los otros [Brownie mixes](https://github.com/brownie-mix/) que pueden ser usado como punto de partida para tus propios contratos. Allí encontraras ejemplos para emepzar como.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) es un buen tutorial para que te familiarices con Brownie.
* Para más información especifica, puedes revisar la [documentación Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Licencia

This project is licensed under the [MIT license](LICENSE).

