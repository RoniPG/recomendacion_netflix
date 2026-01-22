import pandas as pd
import re
from pathlib import Path

DATA_PATH = Path("data/netflix_titles.csv")
TEXT_COLS = ["listed_in", "director", "cast", "description"]


def limpiar_texto(texto: str) -> str:
     texto = texto.lower()
     texto = re.sub(r"[^a-z0-9\s]", "", texto)
     return texto.strip()

def limpiar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset previeamente cargado
    """
    df = df.fillna("")
    for col in TEXT_COLS:
        df[col] = df[col].apply(limpiar_texto)
    return df

def cargar_dataset(ruta: Path) -> pd.DataFrame:
    """
    Carga el dataset de Netflix desde la ruta especificada.
    """
    if not ruta.exists():
        raise FileNotFoundError("Dataset no encontrado.")
    
    print("Dataset cargado correctamente")
    df = pd.read_csv(ruta)
    print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
    print(df.columns.tolist())
    
    return limpiar_dataset(df)

def main():
        df = cargar_dataset(DATA_PATH)
        print("Dataset limpio y preparado")
        print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
        print(df[TEXT_COLS].head(3))

        
if __name__ == "__main__":
     main()

