from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schema import Veiculo, VeiculoCreate
from acoes import get_veiculos, get_veiculo_by_id

router = APIRouter()

@router.get("/veiculos", response_model=list[Veiculo])
def read_veiculos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retorna a lista de veículos com paginação.
    """
    return get_veiculos(db, skip=skip, limit=limit)

@router.get("/veiculos/{veiculo_id}", response_model=Veiculo)
def read_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    """
    Retorna um veículo específico pelo ID.
    """
    veiculo = get_veiculo_by_id(db, veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo
