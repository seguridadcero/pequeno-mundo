# Estado de transferencia — 19 octubre 2026

## Base funcional
`app/` contiene copia de `pequeno-mundo-integrado-v11` con tres juegos, manifest y service worker, scripts de auditoría y su informe. Es la **última versión integrada sometida a auditoría reproducible**, no una release de producción.

## Evidencia disponible
El informe V11 declara 9 recorridos PASS (3 juegos × 3 resoluciones: 360×740, 390×844, 1280×900). Son pruebas con `page.set_content`, no certifican navegación HTTP, service worker, offline real, gestos táctiles físicos ni aprendizaje infantil. La auditoría se ejecutó previamente; este paquete no afirma una nueva ejecución.

## Arte posterior
`assets/personajes-candidatos/` incluye 3 PNG generados individualmente y comprobación alfa; **son candidatos**, no recursos artísticos definitivos ni integrados. El tercer personaje usa verde en lugar del morado planteado inicialmente: revisar coherencia antes de aceptar. La segmentación alfa del niño azul requiere inspección de bordes. No están generados individualmente vaso, mesa ni aula definitivos.

`prototipos/repartimos-arte-v4/` es un experimento de interacción y composición con recursos obtenidos de recortes de láminas: NO usar como fuente de assets finales ni como sustituto de V11.

## Bloqueos
- Falta auditoría end-to-end sobre HTTP real y offline.
- Falta evaluación pedagógica observacional y pruebas con niños.
- Falta kit premium completo, consistente e integrado.
- Falta confirmación de audio y accesibilidad real.
