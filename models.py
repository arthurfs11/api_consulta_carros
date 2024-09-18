from database import Base  # Import absoluto
from sqlalchemy import Column, Integer, String

class Veiculo(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    status = Column(String, default="DESCONECTADO")
