# Instrucciones para Codex — Pequeño Mundo

Lee primero `README.md`, `docs/ESTADO.md`, `docs/DECISIONES.md`, `docs/ROADMAP.md` y `app/INFORME_AUDITORIA_TOTAL_V11.md`.

## Reglas no negociables
- Proyecto educativo de matemáticas para niños de 3–5 años, gratuito, sin anuncios, cuentas, compras ni suscripciones; PWA offline-first.
- Evaluar propuestas críticamente desde pedagogía infantil, diseño profesional de juegos y UX de prelectores. No afirmar eficacia pedagógica sin evidencia.
- Mantener los tres juegos: Repartimos, Clasificamos y Comparamos; 5 actividades/etapas por juego como diseño objetivo (Comparamos implementa diez oportunidades según auditoría V11).
- Conservar `app/` como línea base funcional V11. No reemplazarla por prototipos visuales sin integración y regresión completa.
- Dirección artística B: videojuego educativo premium, personajes expresivos, ilustración cálida con volumen, objetos manipulables protagonistas.
- **Cada asset nuevo se genera individualmente**, nunca láminas y recortes. Los PNG candidatos no se consideran arte aprobado para producción.
- Personajes/mesas/vasos deben ser capas separadas; transparencia alfa real donde aplique; fondo sin objetos interactivos incrustados.
- Botones y textos en HTML/CSS, no horneados en imágenes. Audio y demostraciones visuales para niños prelectores.
- Entrada táctil: arrastre continuo y alternativa de dos toques. Errores motores no deben penalizarse; errores matemáticos permiten corregir.
- La actividad 3 de Repartimos parte de tres niños con vasos 2–0–1; corregir hasta 1–1–1. No mostrar una pista que revele el movimiento correcto.
- Validar todas las actividades, pantallas y estados; responsive 844×390, 390×844 y 1280×800 además de la matriz existente.
- Distinguir resultados de tests automatizados, navegación HTTP, service worker/offline, audio audible y pruebas con niños: ninguno se infiere de otro.
- No declarar 'listo para producción' sin validación real.

## Primera tarea recomendada
1. Inspeccionar V11 y reproducir auditoría secuencial.
2. Levantar entorno local HTTP y probar PWA/servicio worker con navegador real.
3. Elaborar backlog de defectos por juego y resolución.
4. Integrar una sola actividad visual con assets **individuales aprobados**, sin alterar el resto.
5. Ejecutar regresión integral antes de extender el sistema visual.