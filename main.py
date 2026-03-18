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
        df["listed_in"]
        + " "
        + df["director"]
        + " "
        + df["cast"]
        + " "
        + df["description"]
    )


def calcular_similitud(perfiles: pd.Series):
    """
    Vectoriza los perfiles y calcula la similitud por coseno
    """
    vectorizer = CountVectorizer(stop_words="english")
    matriz = vectorizer.fit_transform(perfiles)
    similitud = cosine_similarity(matriz)
    return similitud


def recomendar(titulo: str, df: pd.DataFrame, similitud, top_n: int = 5):
    """
    Devuelve recomendaciones basadas en similitud de contenido
    """
    titulo = titulo.lower()

    if titulo not in df["title"].str.lower().values:
        raise ValueError("Título no encontrado en el dataset")

    idx = df[df["title"].str.lower() == titulo].index[0]
    scores = list(enumerate(similitud[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    indices_recomendados = [i for i, score in scores[1 : top_n + 1]]

    return df.iloc[indices_recomendados]["title"]


def limpiar_texto(texto: str) -> str:
    """
    Limpia el texto de caracteres no deseados
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    return texto.strip()


def limpiar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset previeamente cargado
    """
    df.columns = df.columns.str.strip()
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

    return limpiar_dataset(df)


def inicializar_sistema():
    """
    Inicializa el sistema cargando y preparando el dataset
    """
    df = cargar_dataset(DATA_PATH)
    perfiles = crear_perfil_textual(df)
    similitud = calcular_similitud(perfiles)
    return df, similitud


if __name__ == "__main__":
    df, similitud = inicializar_sistema()
    recomendaciones = recomendar("Intrusion", df, similitud, top_n=5)
    print("\nRecomendaciones:")
    print(recomendaciones)
