from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import VeiculoCreate
from acoes import create_veiculo
from database import get_db
from schema import Veiculo

router = APIRouter()

@router.post("/veiculos", response_model=Veiculo)
def create_veiculo(veiculo: VeiculoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo veículo.
    """
    return create_veiculo(db, veiculo)
