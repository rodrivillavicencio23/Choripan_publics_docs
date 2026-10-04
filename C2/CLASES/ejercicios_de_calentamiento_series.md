# Guía de Ejercicios de Calentamiento: Series de Potencias y de Taylor
**Contenidos:** Clases 9 a 13 (Cálculo 2 - MAT1620)

Esta guía está diseñada para repasar los fundamentos antes de pasar a problemas de certámenes. Te recomiendo resolverlos paso a paso, justificando cada criterio matemático que utilices.

---

### Parte I: Series Alternantes y Convergencia (Clase 9)

**Ejercicio 1:** 
Determine si la siguiente serie es **absolutamente convergente**, **condicionalmente convergente** o **divergente**. Justifique su respuesta utilizando el Criterio de la Serie Alternante y algún criterio de comparación para el valor absoluto.
$$ \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{\sqrt{n^2 + 4}} $$

---

### Parte II: Series de Potencias e Intervalos de Convergencia (Clases 10 y 11)

**Ejercicio 2:**
Encuentre el **radio de convergencia ($R$)** y el **intervalo de convergencia** de la siguiente serie de potencias. 
*(¡No olvides evaluar el comportamiento de la serie en los extremos del intervalo!)*
$$ \sum_{n=1}^{\infty} \frac{(-1)^n (x+1)^n}{n \cdot 2^n} $$

**Ejercicio 3:**
Determine el radio y el intervalo de convergencia de una serie que involucra factoriales. ¿Qué te dice el Criterio de la Razón en este caso sobre el dominio de la función resultante?
$$ \sum_{n=0}^{\infty} \frac{n! (x-3)^n}{5^n} $$

---

### Parte III: Representación de Funciones como Series de Potencias (Clase 12)

**Ejercicio 4:**
A partir de la serie geométrica conocida $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$, encuentre una representación en serie de potencias para la función:
$$ f(x) = \frac{x^2}{1 + 4x^3} $$
Indique además cuál es el radio de convergencia de esta nueva serie.

**Ejercicio 5 (Derivación/Integración término a término):**
Sabemos que $f(x) = \ln(1+x)$ se puede obtener integrando la función $\frac{1}{1+x}$. Utilice este hecho para encontrar la representación en serie de potencias de $f(x) = \ln(1+x)$ y determine su radio de convergencia.

---

### Parte IV: Series de Taylor y Maclaurin (Clase 13)

**Ejercicio 6:**
Utilizando la definición formal (calculando las derivadas $f^{(n)}(a)$), encuentre la **Serie de Taylor** para la función $f(x) = e^{2x}$ centrada en $a = 1$.

**Ejercicio 7:**
En lugar de usar la definición desde cero, utilice la serie de Maclaurin conocida para $\cos(x)$ (que vimos en los ejemplos de la clase 13) para encontrar la serie de Maclaurin de la función:
$$ g(x) = x^2 \cos(3x) $$