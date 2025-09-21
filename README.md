# Derivate Project

Acest proiect generează animații cu **formulele derivatelor** folosind Manim și le afișează cu Streamlit.

## Structură
- `animations/` – scripturile Manim
- `videos/` – videoclipurile generate
- `app.py` – aplicația Streamlit
- `requirements.txt` – dependențele Python

## Cum se folosește
1. Instalează dependențele:
```
pip install -r requirements.txt
```
2. Generează videoclipul:
```
python animations/derivate_formulas.py
```
3. Rulează aplicația Streamlit:
```
streamlit run app.py
```
4. Videoclipurile generate apar în aplicație.