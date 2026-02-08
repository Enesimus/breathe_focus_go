# Flujo de trabajo App Registro Puntajes

## Objetivo

Definir la lógica del proceso.

En esta aplicación el primer paso es __crear un entrenamiento__.

### Entrenamiento

El entrenamiento cuenta con las siguientes propiedades:

1. Se definen al __inicio__ del entrenamiento
   - Identificador 🆔
   - Fecha 📆
   - Hora de inicio ⌚️
   - Hora de finalización ⌚️
   - Lugar 📌
   - Tipo de Lugar 🏠
   - Clima ☀️
   - Tipo de entrenamiento
   - Tipo de arco 🏹
   - Usa diana 🎯
   - Tipo de diana
   - Distancia 📏
   - Objetivos ☑️
2. Se definen __durante__ el entrenamiento
   - Rondas
   - Tandas
   - Flechas
3. Se definen al __final__ del entrenamiento
   - Feedback 😄
   - Observaciones 👀

Una vez creado en entrenamiento, __automáticamente se crea la primera ronda__.

Finalizar entrenamiento cierra la tanda y la ronda.

### Rondas

Cada entrenamiento debe tener al menos una ronda.

Cada ronda puede ser puntuada o no.

Cada ronda puede tener un objetivo específico, feedback y observaciones. El feedback y observaciones se registran __al final__ de la ronda.

Cada ronda puede tener un numero variable de tandas.

Al crear la primera ronda, se crea automáticamente la primera tanda

> 💡A considerar más tarde
>
> Podrian existir rondas no relacionadas a flechas, sino a ejercicios

Crear nueva Ronda vs finalizar Ronda y crear nueva.

### Tanda

Cada tanda debe tener __al menos una flecha__.

Cada tanda puede tener un número variable de flechas.

Cada tanda puede tener una observación breve final.

Finalizar tanda vs crear nueva

### Flechas

Las flechas se crean al introducir __al menos una__ o todas sus propiedades

Las propiedades de una flecha son:

- Puntaje
- Sector
- Logro

Nueva flecha

Boton para borrar flechas

#### Puntaje

Es un valor opcional y dependerá si la ronda es puntuada o no.

El puntaje está determinado por la cercanía al centro.

Una flecha que no cae dentro de la diana se considerará "Miss", se registrará con una "M" y tendra valor 0.

Dependerá del tipo de diana el rango de puntajes:

- Diana Target : 1-10. El 10 central se registra como "X", se contabiliza aparte pero tiene el mismo valor
- Diana Target Reducida: 6-10. X
- Diana Field: 1-5
- Entre otros...

Debe existir un diccionario de dianas con sus propiedades.

#### Sector

Es una forma arbitraria de registrar la dispersión y dirección de una flecha.

Es un valor opcional

Se dividirá la diana en sectores iguales (8-12-16) a definir segun el nivel de precisión necesario para el análisis.

Probablemente entre 8 y 12 sea suficiente y práctico, dado que es una estimación. A menos que se puedan modificar dianas colocandole los sectores.

En caso de una flecha puntuada con 10 o X, no es requerido registrar el sector.

#### Logro

Se refiere a la percepción del arquero de conseguir un objetivo específico.

Se propone la siguiente nomenclatura

- Logrado ✅
- No Logrado ❎
- Dudoso ❓

## Métricas

Serán mediciones calculadas y no almacenadas.

Las mediciones básicas según nivel de organizacion serán:

- Tanda actual
  - Número de flechas
  - Suma de puntajes
  - Promedio de puntajes
  - Flechas especiales
    - X : recuento y porcentaje
    - 10 : recuento y porcentaje
    - 9 : recuento y porcentaje
    - Gold (X + 10 + 9): recuento y porcentaje
    - Miss: recuento y porcentaje
  - Logro:
    - Logrado: porcentaje
    - Dudoso: porcentaje
- Ronda actual: _Podria omitirse y solo resumir por entrenamiento_
  - Número de tandas
  - Número de flechas
  - Suma de puntajes
  - Promedio de puntajes
  - Flechas especiales
    - X : porcentaje
    - 10 : porcentaje
    - 9 : porcentaje
    - Gold (X + 10 + 9): porcentaje
    - Miss: porcentaje
  - Logro:
    - Logrado: porcentaje
    - Dudoso: porcentaje
- Entrenamiento
  - Número de rondas
  - Número de tandas
  - Número de flechas
  - Suma de puntajes
  - Promedio de puntajes
  - Flechas especiales
    - X : porcentaje
    - 10 : porcentaje
    - 9 : porcentaje
    - Gold (X + 10 + 9): porcentaje
    - Miss: porcentaje
  - Logro:
    - Logrado: porcentaje
    - Dudoso: porcentaje

## Análisis

1. Evolución en el tiempo
2. Rendimiento por tanda
3. Rendimiento por flecha
4. Segmentacion por distancia, clima, tipo de entrenamiento

## Otras ideas

Para considerar implementar, más adelante:

- Sistema de registro de agrupación
- Volcado en base de datos
- Acceso a base de datos para analisis historico
- Multiusuario: varios arqueros
