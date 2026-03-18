import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from main import inicializar_sistema, recomendar


class NetflixRecommenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Netflix Recommender System")
        self.root.geometry("700x600")
        self.root.configure(bg="#222222")
        
        # Cargar datos
        self.status_label = ttk.Label(root, text="Cargando dataset...", foreground="yellow")
        self.status_label.pack(pady=10)
        self.root.update()
        
        try:
            self.df, self.similitud = inicializar_sistema()
            self.status_label.config(text=f"Dataset cargado: {len(self.df)} títulos", foreground="green")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el dataset: {e}")
            self.root.quit()
            return
        
        # Crear UI
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea los elementos de la interfaz gráfica"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Título
        titulo_label = ttk.Label(main_frame, text="Sistema de Recomendación Netflix", 
                                 font=("Arial", 16, "bold"))
        titulo_label.pack(pady=10)
        
        # Campo de búsqueda
        busqueda_frame = ttk.Frame(main_frame)
        busqueda_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(busqueda_frame, text="Buscar título:").pack(side=tk.LEFT, padx=5)
        self.entrada = ttk.Entry(busqueda_frame, width=40)
        self.entrada.pack(side=tk.LEFT, padx=5)
        self.entrada.bind("<Return>", lambda e: self.buscar())
        
        # Botón buscar
        self.boton_buscar = ttk.Button(busqueda_frame, text="Buscar", command=self.buscar)
        self.boton_buscar.pack(side=tk.LEFT, padx=5)
        
        # Selector de recomendaciones
        top_n_frame = ttk.Frame(main_frame)
        top_n_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(top_n_frame, text="Número de recomendaciones:").pack(side=tk.LEFT, padx=5)
        self.top_n_var = tk.IntVar(value=5)
        top_n_spin = ttk.Spinbox(top_n_frame, from_=1, to=20, textvariable=self.top_n_var, width=5)
        top_n_spin.pack(side=tk.LEFT, padx=5)
        
        # Área de resultados
        resultados_label = ttk.Label(main_frame, text="Recomendaciones:", font=("Arial", 12, "bold"))
        resultados_label.pack(pady=(20, 5))
        
        # Frame con scrollbar para resultados
        scroll_frame = ttk.Frame(main_frame)
        scroll_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(scroll_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.resultado_text = tk.Text(scroll_frame, height=15, width=80, 
                                      yscrollcommand=scrollbar.set, bg="#333333", 
                                      fg="#00FF00", font=("Courier", 10))
        self.resultado_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.resultado_text.yview)
        
        # Frame inferior con información
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=10)
        
        self.info_label = ttk.Label(info_frame, text="Listo para buscar", foreground="cyan")
        self.info_label.pack()
    
    def buscar(self):
        """Busca recomendaciones para el título ingresado"""
        titulo = self.entrada.get().strip()
        
        if not titulo:
            messagebox.showwarning("Advertencia", "Por favor ingresa un título")
            return
        
        try:
            top_n = self.top_n_var.get()
            recomendaciones = recomendar(titulo, self.df, self.similitud, top_n=top_n)
            
            # Limpiar área de resultados
            self.resultado_text.config(state=tk.NORMAL)
            self.resultado_text.delete(1.0, tk.END)
            
            # Mostrar título buscado
            self.resultado_text.insert(tk.END, f"Título buscado: {titulo.upper()}\n")
            self.resultado_text.insert(tk.END, "=" * 70 + "\n\n")
            
            # Mostrar recomendaciones
            self.resultado_text.insert(tk.END, f"Top {top_n} recomendaciones:\n\n")
            for i, (idx, recomendacion) in enumerate(recomendaciones.items(), 1):
                self.resultado_text.insert(tk.END, f"{i}. {recomendacion}\n")
            
            self.resultado_text.config(state=tk.DISABLED)
            self.info_label.config(text=f"✓ Se encontraron {len(recomendaciones)} recomendaciones")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.info_label.config(text=f"✗ {str(e)}", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {e}")
            self.info_label.config(text=f"✗ Error: {str(e)}", foreground="red")


def main():
    root = tk.Tk()
    gui = NetflixRecommenderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()