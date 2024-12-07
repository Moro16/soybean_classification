from soybean_prediction.arquivos_py.load_model import load_model_sb, load_model_corn
from tensorflow.keras.models import Sequential

class TesteModel:
    @classmethod
    def test_model_sb(cls):
        model = load_model_sb()
        assert model is not None, "Fail to test model, model = None❌"
        assert isinstance(model, Sequential), "Model is not an instance of Sequential❌"
        print('Modelo carregado com sucesso✅')

    @classmethod
    def test_model_corn(cls):
        model = load_model_corn()
        assert model is not None, "Fail to test model, model = None❌"
        assert isinstance(model, Sequential), "Model is not an instance of Sequential❌"
        print('Modelo carregado com sucesso✅')

def main():
    TesteModel.test_model_sb()
    TesteModel.test_model_corn()

if __name__ == "__main__":
    main()
