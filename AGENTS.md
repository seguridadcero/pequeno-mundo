# Instrucciones para Codex — Pequeño Mundo

## Propósito
Desarrollar una PWA educativa en español para niños de 3 a 5 años. Gratuita y universal, sin anuncios, compras, suscripciones ni cuentas. Offline-first.

## Base estable
La última base funcional integrada es **V11** (tres juegos y pruebas). Los experimentos de arte V4/V5 y personajes individuales son prototipos y candidatos, no sustituyen la base funcional. **El código V11 todavía debe importarse desde el paquete de migración.**

## Pedagogía y UX
- Tres juegos de cinco actividades: Repartimos (correspondencia uno a uno), Clasificamos (colores), Comparamos (cantidades).
- Enseñar antes de evaluar. Audio e instrucciones accesibles para prelectores; demostraciones sin revelar respuestas.
- No castigar errores motores. Admitir arrastre y alternativa de dos toques; permitir corrección de decisiones matemáticas.
- Progreso local independiente por juego, sin requerir conexión.
- Mantener una sola navegación y un único shell de aplicación, sin encabezados ni controles duplicados.
- Verificar diseño horizontal 844×390, vertical 390×844 y escritorio 1280×800.

## Arte
Dirección B: videojuego educativo premium, personajes cartoon con volumen, iluminación cálida y objetos manipulables prioritarios. Generar CADA recurso de forma individual; NO generar hojas de assets para recortarlas y afirmar que son recursos independientes. Personajes, vaso, mesa y escenario como capas separadas. Exigir canal alfa genuino en sprites; el escenario es fondo. Botones preferiblemente HTML/CSS.

## Repartimos actividad 3
Tres niños y tres vasos inicialmente 2–0–1. El niño debe redistribuir un vaso del primero al segundo para obtener 1–1–1. Evitar pistas que revelen qué vaso mover. La interfaz debe permitir arrastrar, dos toques, comprobar y reiniciar.

## Ingeniería
- Auditar las 15 actividades, no solo una pantalla.
- Ejecutar y documentar pruebas; no afirmar que se validó HTTP, offline, audio físico ni pruebas con niños sin haberlo hecho.
- No perder funcionalidad al integrar arte.
- Mantener clara separación entre versión estable, candidatos artísticos y trabajo pendiente.
