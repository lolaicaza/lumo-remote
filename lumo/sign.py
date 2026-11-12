#!/usr/bin/env python3
"""Firma lumo/config.json con la llave privada de Lumo Remote y genera lumo/custom.txt.

Uso: python3 lumo/sign.py RUTA_A_LLAVE_PRIVADA
Requiere: pip install pynacl
El archivo custom.txt va junto al ejecutable (en macOS, dentro de Resources).
"""
import base64, json, sys
from pathlib import Path
from nacl.signing import SigningKey

here = Path(__file__).parent
seed = base64.b64decode(Path(sys.argv[1]).read_text().strip())
cfg = json.dumps(json.loads((here / "config.json").read_text()), separators=(",", ":")).encode()
signed = SigningKey(seed).sign(cfg)
(here / "custom.txt").write_text(base64.b64encode(bytes(signed)).decode() + "\n")
print("custom.txt generado")
