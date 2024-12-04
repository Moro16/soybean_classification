uvicorn:
	uvicorn soybean_prediction.api.fast:app --reload

streamlit:
	streamlit run soybean_prediction/api/app.py
