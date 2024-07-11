# Oferta Generator

## Descriere
Acest proiect utilizează modelul GPT-2 pentru a genera oferte IT detaliate pe baza cerințelor clientului.

## Dependențe
- Python 3.7+
- Transformers
- Datasets
- Torch

2.Creează un mediu virtual și activează-l:
python -m venv venv

3.Instalează dependențele:
pip install -r requirements.txt

Antrenare Model:
1.Rulează scriptul pentru a extrage textul din fișierele .docx:
python extract_text.py

2.Antrenează modelul cu setul de date generat:
python train_model.py

Generare Ofertă
1.Rulează scriptul pentru a genera o ofertă:
python generate_text.py



