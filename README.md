#  Evaluador de Fortaleza de Contraseñas

Script en Python que analiza si una contraseña ingresada por el usuario es **segura o débil**, basándose en criterios estándar de seguridad, con la opción de reintentar hasta lograr una contraseña fuerte.

Desarrollado para el curso de **Ética Hacking — 9° Semestre**.

---

##  Propósito

Las contraseñas débiles son la puerta de entrada más común en ataques informáticos. Este script busca:

-  **Educar sobre buenas prácticas**: mostrar exactamente qué le falta a una contraseña para ser segura
-  **Prevenir ataques de fuerza bruta**: contraseñas complejas son exponencialmente más difíciles de romper
-  **Conciencia en seguridad**: comprender por qué ciertos requisitos importan
-  **Primer paso en políticas de contraseñas**: base para implementar validaciones en sistemas reales

---

##  Criterios de seguridad evaluados

| Criterio | Validación | ¿Por qué importa? |
|---|---|---|
|  **Longitud mínima** | ≥ 8 caracteres | Más caracteres = más combinaciones posibles |
|  **Letras mayúsculas** | Al menos una `A-Z` | Amplía el espacio de claves |
|  **Letras minúsculas** | Al menos una `a-z` | Amplía el espacio de claves |
|  **Dígitos numéricos** | Al menos un `0-9` | Agrega variación al patrón |
|  **Caracteres especiales** | `! @ # $ % ^ & *` etc. | Los más difíciles de predecir en fuerza bruta |

---

##  ¿Cómo funciona?

```
Inicio
  └─ Solicitar contraseña al usuario
      └─ Evaluar 5 criterios con expresiones regulares
          ├─ ¿Todos se cumplen? → FUERTE  → Fin
          └─ ¿Alguno falla? → DÉBIL 
              └─ Mostrar requisitos
                  └─ ¿Quiere reintentar? → Sí → volver al inicio
                                         → No → Fin
```

### Función central

```python
check_password_strength(password: str) -> bool
```

Usa **expresiones regulares** (`re`) para validar cada criterio de forma precisa y retorna `True` si la contraseña cumple **todos** los requisitos.

---

## Ejemplo de salida

```
=== Security Assessment Tool ===

Enter password to test: hola
[-] Status: Password is WEAK.
   Requirements: 8+ chars, upper & lower letters, digits, and special symbols.

Do you want to change it? (y/n): y

Enter password to test: Segura#2024!
[+] Status: Password is STRONG and secure!
```

---

## Tecnologías

| Librería | Uso |
|---|---|
| `re` | Expresiones regulares para validación de patrones |

> Solo usa librerías de la **biblioteca estándar de Python** — sin dependencias externas.

---

## 🚀 Cómo ejecutarlo

```bash
python pass_segura.py
```

---

## Conceptos de seguridad aplicados

- **Política de contraseñas (Password Policy)**: estándar en cualquier sistema que maneje autenticación
- **Entropía de contraseña**: a mayor variedad de caracteres, mayor entropía y más resistencia a ataques
- **Ataques de diccionario vs. fuerza bruta**: contraseñas complejas resisten ambos tipos
- **OWASP Authentication Guidelines**: los criterios implementados siguen recomendaciones de la OWASP para contraseñas seguras

---

## ¿Qué tan segura es una contraseña?

| Contraseña | Tiempo estimado para romperla (fuerza bruta) |
|---|---|
| `abc` | Instantáneo |
| `password123` | Segundos (está en diccionarios) |
| `Pass1!` | Minutos |
| `Segura#2024!` | Siglos |
