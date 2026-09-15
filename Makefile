.PHONY: clean-data test app

clean-data:
	python src/data/clean_data.py

test: clean-data
	python -m pytest -q

app: clean-data
	streamlit run app/streamlit_app.py
