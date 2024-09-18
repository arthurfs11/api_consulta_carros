from pydantic import BaseModel

# Schema para a criação de um veículo
class VeiculoCreate(BaseModel):
    nome: str
    marca: str
    ano: int
    status: str

# Schema para a leitura de um veículo (por exemplo, ao fazer um GET)
class Veiculo(BaseModel):
    id: int
    nome: str
    marca: str
    ano: int
    status: str

    class Config:
        orm_mode = True

# Schema para a atualização de status de um veículo (PUT)
class VeiculoUpdate(BaseModel):
    status: str
