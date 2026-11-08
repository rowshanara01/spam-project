"""Step 1: Data -> Model train -> Evaluate -> Save"""
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

# 1. Data load
df = pd.read_csv("data/messages.csv")
df["y"] = df["label"].map({"ham": 0, "spam": 1})
print(df["label"].value_counts(), "\n")

# 2. Train/test split (stratify = duto class er onupat same thakbe)
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["y"], test_size=0.25, random_state=42, stratify=df["y"]
)

# 3. Pipeline: text -> numbers (TF-IDF) -> Logistic Regression
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000)),
])

# 4. Cross-validation (model kotota stable seta dekhar jonno)
cv = cross_val_score(pipe, X_train, y_train, cv=3, scoring="f1")
print("CV F1 scores:", cv.round(2), "| mean:", cv.mean().round(2), "\n")

# 5. Final train + test evaluation
pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print(classification_report(y_test, pred, target_names=["ham", "spam"]))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))

# 6. Model save (API eta load korbe)
joblib.dump(pipe, "model/spam_model.joblib")
print("\nModel saved -> model/spam_model.joblib")
