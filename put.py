from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import VeiculoUpdate
from acoes import update_veiculo_status
from database import get_db
from schema import Veiculo

router = APIRouter()

@router.put("/veiculos/{veiculo_id}/status", response_model=Veiculo)
def change_status(veiculo_id: int, veiculo_update: VeiculoUpdate, db: Session = Depends(get_db)):
    """
    Atualiza o status de um veículo para CONNECTADO ou DESCONECTADO.
    """
    veiculo = update_veiculo_status(db, veiculo_id, veiculo_update.status)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo
