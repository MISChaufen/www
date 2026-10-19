#!/usr/bin/env python3
"""Dev server — JS-free style switching via ?style= query param + cookie."""
import http.server
import os

PORT = 8000
STYLES = {"v1", "v2", "v3", "v4"}
DEFAULT = "v4"


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

    def send_response(self, code, message=None):
        super().send_response(code, message)
        if getattr(self, "_new_style", None) and code == 200:
            self.send_header("Set-Cookie", f"style={self._new_style}; Path=/; SameSite=Lax")

    def copyfile(self, source, outputfile):
        if self.path.endswith(".html") or self.path.endswith("/") or self.path in ("", "/"):
            content = source.read()
            active = getattr(self, "_active_style", DEFAULT)
            content = content.replace(b"style.css", f"style-{active}.css".encode())
            outputfile.write(content)
        else:
            super().copyfile(source, outputfile)

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
    print(f"  ?style=v1  — clean  (warm beige, benni.tech inspired)")
    print(f"  ?style=v2  — warez  (matrix green, CRT scanlines)")
    print(f"  ?style=v3  — cyber  (Cyberpunk 2077, yellow glow)")
    print(f"  ?style=v4  — network (raw.ag dark navy)  [default]")
    http.server.test(HandlerClass=Handler, port=PORT, bind="0.0.0.0")
