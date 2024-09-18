from sqlalchemy.orm import Session
from models import Veiculo  # Import absoluto
from schema import VeiculoCreate, VeiculoUpdate

# ==============================
#         GET Requests
# ==============================

def get_veiculos(db: Session, skip: int = 0, limit: int = 10):
    """Retorna a lista de todos os veículos"""
    return db.query(Veiculo).offset(skip).limit(limit).all()

def get_veiculo_by_id(db: Session, veiculo_id: int):
    """Retorna um veículo específico pelo ID"""
    return db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()

# ==============================
#         POST Request
# ==============================

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    """Cria um novo veículo e salva no banco de dados"""
    db_veiculo = Veiculo(nome=veiculo.nome, status=veiculo.status or "DESCONECTADO")
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

# ==============================
#         PUT Request
# ==============================

def update_veiculo_status(db: Session, veiculo_id: int, status: str):
    """Atualiza o status de um veículo para 'CONNECTADO' ou 'DESCONECTADO'"""
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo:
        veiculo.status = status
        db.commit()
        return veiculo
    return None

def update_veiculo(db: Session, veiculo_id: int, veiculo_update: VeiculoUpdate):
    """Atualiza as informações de um veículo (nome, status)"""
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo:
        veiculo.nome = veiculo_update.nome or veiculo.nome
        veiculo.status = veiculo_update.status or veiculo.status
        db.commit()
        return veiculo
    return None

# ==============================
#         DELETE Request
# ==============================

def delete_veiculo(db: Session, veiculo_id: int):
    """Exclui um veículo pelo ID"""
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo:
        db.delete(veiculo)
        db.commit()
        return True
    return False
