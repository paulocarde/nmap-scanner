import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading
from queue import Queue
from datetime import datetime


class PortScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🛡️ Python Security Scanner")
        self.root.geometry("600x500")

        # Configuración de estilo (Tema oscuro)
        self.bg_color = "#1e1e1e"
        self.fg_color = "#00ff00"  # Verde terminal
        self.btn_color = "#333333"
        self.root.configure(bg=self.bg_color)

        # --- 1. Sección de Entrada (IP) ---
        self.frame_top = tk.Frame(root, bg=self.bg_color)
        self.frame_top.pack(pady=20)

        self.label_ip = tk.Label(self.frame_top, text="Objetivo (IP/Dominio):",
                                 bg=self.bg_color, fg="white", font=("Consolas", 12))
        self.label_ip.grid(row=0, column=0, padx=10)

        self.entry_ip = tk.Entry(self.frame_top, font=("Consolas", 12), width=25)
        self.entry_ip.grid(row=0, column=1, padx=10)

        # --- 2. Botón de Escaneo ---
        self.btn_scan = tk.Button(self.frame_top, text="INICIAR ESCANEO", command=self.start_scan_thread,
                                  bg=self.btn_color, fg="white", font=("Consolas", 10, "bold"),
                                  activebackground=self.fg_color, activeforeground="black")
        self.btn_scan.grid(row=0, column=2, padx=10)

        # --- 3. Área de Resultados ---
        self.label_results = tk.Label(root, text="Resultados:", bg=self.bg_color, fg="white", font=("Consolas", 12))
        self.label_results.pack(pady=(10, 0))

        # ScrolledText es una caja de texto con barra de desplazamiento automática
        self.text_area = scrolledtext.ScrolledText(root, width=70, height=20,
                                                   font=("Consolas", 10), bg="black", fg=self.fg_color)
        self.text_area.pack(pady=10)

        # Variables de control
        self.queue = Queue()
        self.open_ports = []
        self.is_scanning = False

    def get_service_name(self, port):
        try:
            return socket.getservbyport(port)
        except:
            return "Desconocido"

    def scan_logic(self, target):
        """Lógica del escáner (similar al script anterior)"""

        def worker():
            while not self.queue.empty():
                port = self.queue.get()

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                try:
                    con = s.connect_ex((target, port))
                    if con == 0:
                        service = self.get_service_name(port)
                        # Actualizamos la GUI desde el hilo (usando un método seguro)
                        msg = f"[+] Puerto {port:<5} ABIERTO  ({service})\n"
                        self.update_text_area(msg)
                except:
                    pass
                finally:
                    s.close()
                    self.queue.task_done()

        # Preparamos la cola (Rango 1-65536)
        for p in range(1, 65536):
            self.queue.put(p)

        # Lanzamos 250 hilos
        threads = []
        for _ in range(250):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
            threads.append(t)

        self.queue.join()

        # Mensaje final
        scan_time = datetime.now() - self.start_time
        self.update_text_area(f"\n✅ Escaneo finalizado en {scan_time}\n")
        self.btn_scan.config(state=tk.NORMAL, text="INICIAR ESCANEO")

    def update_text_area(self, message):
        """Inserta texto en la caja de resultados de forma segura"""
        self.text_area.insert(tk.END, message)
        self.text_area.see(tk.END)  # Auto-scroll al final

    def start_scan_thread(self):
        """Prepara la interfaz y lanza el hilo principal del escáner"""
        target_input = self.entry_ip.get()

        if not target_input:
            messagebox.showerror("Error", "Por favor ingresa una IP")
            return

        try:
            target = socket.gethostbyname(target_input)
        except socket.gaierror:
            messagebox.showerror("Error", "No se pudo resolver el host")
            return

        # Limpiar área de texto
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"🚀 Iniciando escaneo en: {target}...\n")
        self.text_area.insert(tk.END, "-" * 50 + "\n")

        # Bloquear botón para evitar doble clic
        self.btn_scan.config(state=tk.DISABLED, text="ESCANEANDO...")
        self.start_time = datetime.now()

        # IMPORTANTE: Lanzar la lógica pesada en un hilo separado
        t = threading.Thread(target=self.scan_logic, args=(target,))
        t.start()


# --- Ejecución de la App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PortScannerApp(root)
    root.mainloop()