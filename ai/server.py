#!/usr/bin/env python3
"""DubScript Studio - tiny local server (optional).

Usage:
    python3 server.py [port]

Then open http://localhost:8000 in your browser.
The app also works fully offline by simply opening index.html.
"""
import http.server
import socketserver
import sys
import os

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"DubScript Studio running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
