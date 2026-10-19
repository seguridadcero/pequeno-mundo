# Pequeño Mundo Integrado V11

Tres juegos: Repartimos, Clasificamos y Comparamos.

## Auditoría reproducible

Instalar `playwright` para Python, Node.js y Chromium en `/usr/bin/chromium`. Ejecutar `python auditoria_secuencial.py`. Los nueve casos se ejecutan **secuencialmente**, cada uno con un límite de 30 segundos, y el informe se escribe en `resultados_v11.json`.

La prueba usa `page.set_content` por la restricción de navegación del entorno de pruebas. Comprueba estados principales, no la PWA por HTTP ni la interacción física de niños.
