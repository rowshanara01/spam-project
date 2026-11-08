#### Spam Detector (ML + FastAPI + Next.js)

## Chalanor niyom
1. `pip install -r requirements.txt`
2. `python train.py`                       # model train + save
3. `uvicorn app.main:app --reload`         # API: http://localhost:8000/docs
4. `npx create-next-app@latest web` -> `frontend/page.tsx` ke `web/app/page.tsx` e copy -> `npm run dev`
5. (Optional) `docker build -t spam . && docker run -p 8000:8000 spam`

## Nijer jonno challenge
- data/messages.csv ke Kaggle "SMS Spam Collection" dataset diye replace koro
- LogisticRegression er jaygay RandomForest/NaiveBayes try koro, F1 compare koro
- /predict e top spam words return koro
- Prediction history PostgreSQL/SQLite e save koro
