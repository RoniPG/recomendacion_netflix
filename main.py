import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/netflix_titles.csv")
FEATURES = [
     "title", "type","listed_in", "director",
     "cast", "country", "rating", "description",
]

def limpiar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset previeamente cargado
    """
    df = df[FEATURES]
    df = df.fillna("")
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
        print(df.head(3))

        
if __name__ == "__main__":
     main()

