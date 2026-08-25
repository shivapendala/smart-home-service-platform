from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.technician_mgmt import (
    TechnicianMgmtMasterEntity, TechnicianMgmtStatus, TechnicianMgmtPriority, TechnicianMgmtCategoryType,
    TechnicianMgmtRelationalComponent1 ,TechnicianMgmtRelationalComponent2 ,TechnicianMgmtRelationalComponent3 ,TechnicianMgmtRelationalComponent4 ,TechnicianMgmtRelationalComponent5 ,TechnicianMgmtRelationalComponent6 ,TechnicianMgmtRelationalComponent7 ,TechnicianMgmtRelationalComponent8 ,TechnicianMgmtRelationalComponent9 ,TechnicianMgmtRelationalComponent10 ,TechnicianMgmtRelationalComponent11 ,TechnicianMgmtRelationalComponent12 ,TechnicianMgmtRelationalComponent13 ,TechnicianMgmtRelationalComponent14 ,TechnicianMgmtRelationalComponent15 ,TechnicianMgmtRelationalComponent16 ,TechnicianMgmtRelationalComponent17 ,TechnicianMgmtRelationalComponent18 ,TechnicianMgmtRelationalComponent19 ,TechnicianMgmtRelationalComponent20 ,TechnicianMgmtRelationalComponent21 ,TechnicianMgmtRelationalComponent22 ,TechnicianMgmtRelationalComponent23 ,TechnicianMgmtRelationalComponent24 ,TechnicianMgmtRelationalComponent25
)
from app.schemas.technician_mgmt import (
    TechnicianMgmtMasterEntityCreate, TechnicianMgmtMasterEntityUpdate,
    TechnicianMgmtRelationalComponent1Create ,TechnicianMgmtRelationalComponent2Create ,TechnicianMgmtRelationalComponent3Create ,TechnicianMgmtRelationalComponent4Create ,TechnicianMgmtRelationalComponent5Create ,TechnicianMgmtRelationalComponent6Create ,TechnicianMgmtRelationalComponent7Create ,TechnicianMgmtRelationalComponent8Create ,TechnicianMgmtRelationalComponent9Create ,TechnicianMgmtRelationalComponent10Create ,TechnicianMgmtRelationalComponent11Create ,TechnicianMgmtRelationalComponent12Create ,TechnicianMgmtRelationalComponent13Create ,TechnicianMgmtRelationalComponent14Create ,TechnicianMgmtRelationalComponent15Create ,TechnicianMgmtRelationalComponent16Create ,TechnicianMgmtRelationalComponent17Create ,TechnicianMgmtRelationalComponent18Create ,TechnicianMgmtRelationalComponent19Create ,TechnicianMgmtRelationalComponent20Create ,TechnicianMgmtRelationalComponent21Create ,TechnicianMgmtRelationalComponent22Create ,TechnicianMgmtRelationalComponent23Create ,TechnicianMgmtRelationalComponent24Create ,TechnicianMgmtRelationalComponent25Create
)

class TechnicianMgmtService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: TechnicianMgmtMasterEntityCreate) -> TechnicianMgmtMasterEntity:
        existing = db.query(TechnicianMgmtMasterEntity).filter(TechnicianMgmtMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = TechnicianMgmtMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> TechnicianMgmtMasterEntity:
        entity = db.query(TechnicianMgmtMasterEntity).filter(TechnicianMgmtMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Technician Management Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[TechnicianMgmtStatus] = None) -> List[TechnicianMgmtMasterEntity]:
        query = db.query(TechnicianMgmtMasterEntity)
        if status_filter:
            query = query.filter(TechnicianMgmtMasterEntity.status == status_filter)
        return query.order_by(TechnicianMgmtMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: TechnicianMgmtMasterEntityUpdate) -> TechnicianMgmtMasterEntity:
        entity = TechnicianMgmtService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = TechnicianMgmtService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: TechnicianMgmtRelationalComponent1Create) -> TechnicianMgmtRelationalComponent1:
        comp = TechnicianMgmtRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent1]:
        query = db.query(TechnicianMgmtRelationalComponent1)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: TechnicianMgmtRelationalComponent2Create) -> TechnicianMgmtRelationalComponent2:
        comp = TechnicianMgmtRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent2]:
        query = db.query(TechnicianMgmtRelationalComponent2)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: TechnicianMgmtRelationalComponent3Create) -> TechnicianMgmtRelationalComponent3:
        comp = TechnicianMgmtRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent3]:
        query = db.query(TechnicianMgmtRelationalComponent3)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: TechnicianMgmtRelationalComponent4Create) -> TechnicianMgmtRelationalComponent4:
        comp = TechnicianMgmtRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent4]:
        query = db.query(TechnicianMgmtRelationalComponent4)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: TechnicianMgmtRelationalComponent5Create) -> TechnicianMgmtRelationalComponent5:
        comp = TechnicianMgmtRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent5]:
        query = db.query(TechnicianMgmtRelationalComponent5)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: TechnicianMgmtRelationalComponent6Create) -> TechnicianMgmtRelationalComponent6:
        comp = TechnicianMgmtRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent6]:
        query = db.query(TechnicianMgmtRelationalComponent6)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: TechnicianMgmtRelationalComponent7Create) -> TechnicianMgmtRelationalComponent7:
        comp = TechnicianMgmtRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent7]:
        query = db.query(TechnicianMgmtRelationalComponent7)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: TechnicianMgmtRelationalComponent8Create) -> TechnicianMgmtRelationalComponent8:
        comp = TechnicianMgmtRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent8]:
        query = db.query(TechnicianMgmtRelationalComponent8)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: TechnicianMgmtRelationalComponent9Create) -> TechnicianMgmtRelationalComponent9:
        comp = TechnicianMgmtRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent9]:
        query = db.query(TechnicianMgmtRelationalComponent9)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: TechnicianMgmtRelationalComponent10Create) -> TechnicianMgmtRelationalComponent10:
        comp = TechnicianMgmtRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent10]:
        query = db.query(TechnicianMgmtRelationalComponent10)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: TechnicianMgmtRelationalComponent11Create) -> TechnicianMgmtRelationalComponent11:
        comp = TechnicianMgmtRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent11]:
        query = db.query(TechnicianMgmtRelationalComponent11)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: TechnicianMgmtRelationalComponent12Create) -> TechnicianMgmtRelationalComponent12:
        comp = TechnicianMgmtRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent12]:
        query = db.query(TechnicianMgmtRelationalComponent12)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: TechnicianMgmtRelationalComponent13Create) -> TechnicianMgmtRelationalComponent13:
        comp = TechnicianMgmtRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent13]:
        query = db.query(TechnicianMgmtRelationalComponent13)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: TechnicianMgmtRelationalComponent14Create) -> TechnicianMgmtRelationalComponent14:
        comp = TechnicianMgmtRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent14]:
        query = db.query(TechnicianMgmtRelationalComponent14)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: TechnicianMgmtRelationalComponent15Create) -> TechnicianMgmtRelationalComponent15:
        comp = TechnicianMgmtRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent15]:
        query = db.query(TechnicianMgmtRelationalComponent15)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: TechnicianMgmtRelationalComponent16Create) -> TechnicianMgmtRelationalComponent16:
        comp = TechnicianMgmtRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent16]:
        query = db.query(TechnicianMgmtRelationalComponent16)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: TechnicianMgmtRelationalComponent17Create) -> TechnicianMgmtRelationalComponent17:
        comp = TechnicianMgmtRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent17]:
        query = db.query(TechnicianMgmtRelationalComponent17)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: TechnicianMgmtRelationalComponent18Create) -> TechnicianMgmtRelationalComponent18:
        comp = TechnicianMgmtRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent18]:
        query = db.query(TechnicianMgmtRelationalComponent18)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: TechnicianMgmtRelationalComponent19Create) -> TechnicianMgmtRelationalComponent19:
        comp = TechnicianMgmtRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent19]:
        query = db.query(TechnicianMgmtRelationalComponent19)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: TechnicianMgmtRelationalComponent20Create) -> TechnicianMgmtRelationalComponent20:
        comp = TechnicianMgmtRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent20]:
        query = db.query(TechnicianMgmtRelationalComponent20)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: TechnicianMgmtRelationalComponent21Create) -> TechnicianMgmtRelationalComponent21:
        comp = TechnicianMgmtRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent21]:
        query = db.query(TechnicianMgmtRelationalComponent21)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: TechnicianMgmtRelationalComponent22Create) -> TechnicianMgmtRelationalComponent22:
        comp = TechnicianMgmtRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent22]:
        query = db.query(TechnicianMgmtRelationalComponent22)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: TechnicianMgmtRelationalComponent23Create) -> TechnicianMgmtRelationalComponent23:
        comp = TechnicianMgmtRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent23]:
        query = db.query(TechnicianMgmtRelationalComponent23)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: TechnicianMgmtRelationalComponent24Create) -> TechnicianMgmtRelationalComponent24:
        comp = TechnicianMgmtRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent24]:
        query = db.query(TechnicianMgmtRelationalComponent24)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: TechnicianMgmtRelationalComponent25Create) -> TechnicianMgmtRelationalComponent25:
        comp = TechnicianMgmtRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianMgmtRelationalComponent25]:
        query = db.query(TechnicianMgmtRelationalComponent25)
        if master_entity_id:
            query = query.filter(TechnicianMgmtRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
