"""Tiny local server for the static TrackFlow demo (Python 3, stdlib only)."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
print("TrackFlow demo: http://127.0.0.1:8000 (Ctrl+C to stop)")
ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler).serve_forever()
