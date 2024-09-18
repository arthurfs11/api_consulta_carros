from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from acoes import delete_veiculo
from database import get_db

router = APIRouter()

@router.delete("/veiculos/{veiculo_id}", response_model=dict)
def remove_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    """
    Exclui um veículo com base no ID.
    """
    result = delete_veiculo(db, veiculo_id)
    if not result:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return {"detail": "Veículo excluído com sucesso"}
