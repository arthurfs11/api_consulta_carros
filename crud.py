from sqlalchemy.orm import Session
from models import Veiculo  # Import absoluto
from schema import VeiculoCreate

def get_veiculos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Veiculo).offset(skip).limit(limit).all()

def get_veiculo(db: Session, veiculo_id: int):
    return db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    db_veiculo = Veiculo(nome=veiculo.nome)
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def update_veiculo_status(db: Session, veiculo_id: int, status: str):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    veiculo.status = status
    db.commit()
    return veiculo

def delete_veiculo(db: Session, veiculo_id: int):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    db.delete(veiculo)
    db.commit()
