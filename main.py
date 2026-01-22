import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/netflix_titles.csv")

def cargar_dataset(ruta: Path) -> pd.DataFrame:
    """
    Carga el dataset de Netflix desde la ruta especificada.
    """
    if not ruta.exists():
        raise FileNotFoundError("Dataset no encontrado.")
    return pd.read_csv(ruta)

def main():
        df = cargar_dataset(DATA_PATH)
        print("Dataset cargado correctamente")
        print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
        print(df.columns.tolist())
        
if __name__ == "__main__":
     main()

