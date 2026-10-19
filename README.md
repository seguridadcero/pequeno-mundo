# Pequeño Mundo — transferencia a Codex

Juego educativo de matemáticas para edades 3–5, gratuito y offline-first. **Base integrada: V11; no está validada para publicación final.**

## Estructura
- `app/`: copia íntegra de V11 (juegos, shell, PWA, scripts y auditoría).
- `docs/`: decisiones, estado verificable, roadmap.
- `AGENTS.md`: instrucciones prioritarias para Codex.
- `assets/personajes-candidatos/`: personajes individuales experimentales, no aprobados ni integrados.
- `prototipos/repartimos-arte-v4/`: prototipo de composición; sus recursos provienen de recortes y no son arte de producción.

## Ejecutar
Desde `app/`: `python3 -m http.server 8000` y abrir `http://localhost:8000` en un navegador. Para tests: instalar dependencias Playwright/Chromium y ejecutar `python3 auditoria_secuencial.py`; el entorno original bloqueaba navegación por URL, por lo que esos tests usaban `page.set_content`.

## Continuidad
Abrir el repositorio en Codex y pedir: «Lee AGENTS.md y docs/, inspecciona app/ como baseline V11, reproduce la auditoría y propón un plan de correcciones priorizadas sin cambiar aún las reglas pedagógicas».