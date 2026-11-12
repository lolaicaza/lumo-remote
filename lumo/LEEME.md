# Lumo Remote: configuración propia

- `config.json`: nombre de la app, servidor y llave del servidor.
- `sign.py`: firma `config.json` con la llave privada de Lumo Remote y genera `custom.txt`.
- `custom.txt`: archivo firmado. Va junto al ejecutable (macOS: dentro de Resources).
- La llave privada NO está en este repositorio. Guárdala en un lugar seguro.
- La llave pública de verificación está en `src/common.rs` (`read_custom_client`).
