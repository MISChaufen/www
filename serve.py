#!/usr/bin/env python3
"""Dev server — JS-free style switching via ?style= query param + cookie."""
import http.server
import os

PORT = 8000
STYLES = {"v3", "v5"}
DEFAULT = "v3"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self._new_style = None
        if "?" in self.path:
            path, qs = self.path.split("?", 1)
            for part in qs.split("&"):
                if part.startswith("style="):
                    val = part[6:]
                    if val in STYLES:
                        self._new_style = val
            self.path = path

        cookie_style = self._read_cookie("style")
        self._active_style = self._new_style or cookie_style or DEFAULT

        super().do_GET()

    def send_head(self):
        if self._is_html():
            for h in ("If-Modified-Since", "If-None-Match"):
                try:
                    del self.headers[h]
                except KeyError:
                    pass
        return super().send_head()

    def send_response(self, code, message=None):
        super().send_response(code, message)
        if getattr(self, "_new_style", None) and code == 200:
            self.send_header("Set-Cookie", f"style={self._new_style}; Path=/; SameSite=Lax")

    def end_headers(self):
        if self._is_html():
            self.send_header("Cache-Control", "no-store")
            self._headers_buffer = [
                b for b in self._headers_buffer
                if not b.lower().startswith(b"content-length:")
            ]
            self.close_connection = True
        super().end_headers()

    def copyfile(self, source, outputfile):
        if self.path.endswith(".html") or self.path.endswith("/") or self.path in ("", "/"):
            content = source.read()
            active = getattr(self, "_active_style", DEFAULT)
            content = content.replace(b"style.css", f"style-{active}.css".encode())
            outputfile.write(content)
        else:
            super().copyfile(source, outputfile)

    def _is_html(self):
        p = self.path
        return p.endswith(".html") or p.endswith("/") or p in ("", "/")

    def _read_cookie(self, name):
        for part in self.headers.get("Cookie", "").split(";"):
            part = part.strip()
            if part.startswith(name + "="):
                return part[len(name) + 1:]
        return None

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} {fmt % args}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Serving MISChaufen at http://localhost:{PORT}")
    print(f"  ?style=v3  — cyber  (Cyberpunk 2077, yellow glow)  [default]")
    print(f"  ?style=v5  — tron   (TRON: Legacy cyan grid)")
    http.server.test(HandlerClass=Handler, port=PORT, bind="0.0.0.0")
