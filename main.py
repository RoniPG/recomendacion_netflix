import pandas as pd
import re
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = Path("data/netflix_titles.csv")
TEXT_COLS = ["listed_in", "director", "cast", "description"]

def crear_perfil_textual(df: pd.DataFrame) -> pd.Series:
    """
    Combina las columnas textuales en un solo perfil por título
    """
    return (
        df["listed_in"] + " " +
        df["director"] + " " +
        df["cast"] + " " +
        df["description"]
    )


def calcular_similitud(perfiles: pd.Series):
    """
    Vectoriza los perfiles y calcula la similitud por coseno
    """
    vectorizer = CountVectorizer(stop_words="english")
    matriz = vectorizer.fit_transform(perfiles)
    similitud = cosine_similarity(matriz)
    return similitud

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
    df.columns = df.columns.str.strip()
    print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
    print(df.columns.tolist())
    
    return limpiar_dataset(df)

def main():
        df = cargar_dataset(DATA_PATH)

        perfiles = crear_perfil_textual(df)
        similitud = calcular_similitud(perfiles)

        print("Dataset limpio y preparado")
        print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
        print(df[TEXT_COLS].head(3))
        
        print("Matriz de similitud creada")
        print(f"Dimensiones: {similitud.shape}")
        print(similitud[:2, :2])
        
if __name__ == "__main__":
     main()

