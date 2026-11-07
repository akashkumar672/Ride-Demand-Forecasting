import pandas as pd
import pickle
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from src.pipeline import create_pipeline

DATA_PATH = ROOT_DIR / "data" / "train.csv"
MODEL_PATH = ROOT_DIR / "models" / "model.pkl"

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Training data not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

if "count" not in df.columns:
    raise ValueError("Target column 'count' not found in training data.")

y = df['count']
X = df.drop(columns=['count'])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline
pipeline = create_pipeline()

# Train
pipeline.fit(X_train, y_train)

# Save full pipeline (IMPORTANT)
MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump(pipeline, f)

print("Pipeline trained and saved:", MODEL_PATH)