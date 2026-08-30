import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def serve_dashboard(port: int = 8080):
    """
    Serves the proofline_audit_report.html natively using http.server.
    """
    report_file = "proofline_audit_report.html"
    if not Path(report_file).exists():
        print(f"Error: {report_file} not found. Please run 'proofline analyze' first.")
        return False

    Handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"\033[92mProofline Dashboard serving at http://localhost:{port}/{report_file}\033[0m")
            print("Press Ctrl+C to stop the server.")
            
            # Automatically open the browser
            webbrowser.open_new_tab(f"http://localhost:{port}/{report_file}")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nShutting down server gracefully...")
                return True
    except OSError as e:
        if e.errno == 98 or e.errno == 10048: # Address already in use
            print(f"Error: Port {port} is already in use. Trying {port+1}...")
            return serve_dashboard(port + 1)
        else:
            print(f"Server error: {e}")
            return False
