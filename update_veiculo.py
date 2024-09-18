from sqlalchemy.orm import Session
from models import Veiculo as VeiculoModel
from schemas import Veiculo

def update_veiculo_status(db: Session, veiculo_id: int, status: str) -> Veiculo:
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id == veiculo_id).first()
    if veiculo is None:
        return None
    veiculo.status = status
    db.commit()
    db.refresh(veiculo)
    return veiculo
