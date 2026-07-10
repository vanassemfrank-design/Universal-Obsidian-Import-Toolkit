from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import webbrowser


def start_gui(
    host: str = "127.0.0.1",
    port: int = 8765,
    open_browser: bool = True,
) -> None:
    gui_path = Path(__file__).parent
    os.chdir(gui_path)

    url = f"http://{host}:{port}"

    if open_browser:
        webbrowser.open(url)

    server = ThreadingHTTPServer(
        (host, port),
        SimpleHTTPRequestHandler,
    )

    print(f"UNOBIT GUI running at {url}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print("UNOBIT GUI stopped.")
    finally:
        server.server_close()