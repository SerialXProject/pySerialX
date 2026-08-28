import queue
import socket
import threading
import time


class TcpController:

    def __init__(self, host, port, on_error=None):
        """Initialize the TcpController with the specified TCP host and port."""
        self.sock = socket.create_connection((host, port), timeout=1)
        self.sock.settimeout(1)  # timeout per le recv, come faceva Serial(timeout=1)
        self._recv_buffer = b''
        self.messages = queue.Queue()
        self.on_error = on_error
        self._stop_thread = False
        self.thread = threading.Thread(target=self._read_socket, daemon=True)
        self.thread.start()

    def _read_socket(self):
        """Read lines from the socket in a separate thread and put them in a queue."""
        while not self._stop_thread:
            try:
                try:
                    chunk = self.sock.recv(1024)
                    if not chunk:
                        # connessione chiusa dal peer
                        raise ConnectionError("Connection closed by remote host")
                    self._recv_buffer += chunk
                except socket.timeout:
                    continue

                while b'\n' in self._recv_buffer:
                    line, self._recv_buffer = self._recv_buffer.split(b'\n', 1)
                    decoded = line.decode('utf-8', errors='ignore').rstrip()
                    if decoded:
                        self.messages.put(decoded)
            except Exception as e:
                if self.on_error:
                    self.on_error(e)
                break

    def read_line(self, timeout=0):
        """Return a line if available, otherwise None"""
        try:
            return self.messages.get(timeout=timeout)
        except queue.Empty:
            return None

    def send_line(self, cmd):
        """Send a command over TCP."""
        self.sock.sendall((cmd + '\n').encode('utf-8'))
        time.sleep(0.05)

    def close(self):
        """Stop the reading thread and close the socket."""
        self._stop_thread = True
        self.thread.join(timeout=1)
        self.sock.close()