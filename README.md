# api_consulta_carros
API simulando consuta de veículos

# Como funciona?

1. instale as dependências: 
   pip install fastapi sqlalchemy uvicorn pydantic python-jose ## Windows
   python3 -m pip install fastapi sqlalchemy uvicorn pydantic python-jose ## Mac ou Linux 

1.5. Instalar os requirements 
   pip install -r requirements.txt ## Windows
   python3 -m pip install -r requirements.txt ## Mac ou Linux

2. Iniciar o servidor 
   uvicorn main:app --reload ## Windows
   python3 -m uvicorn main:app --reload ## Mac ou Linux

3. Abrir o endpoint http://127.0.0.1:8000/docs no navegador para verificar documentação e o redoc de utilização da api.


  