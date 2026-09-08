from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.technician_dispatch import (
    TechnicianDispatchMasterEntity, TechnicianDispatchStatus,
    TechnicianDispatchRelationalComponent1 ,TechnicianDispatchRelationalComponent2 ,TechnicianDispatchRelationalComponent3 ,TechnicianDispatchRelationalComponent4 ,TechnicianDispatchRelationalComponent5 ,TechnicianDispatchRelationalComponent6 ,TechnicianDispatchRelationalComponent7 ,TechnicianDispatchRelationalComponent8 ,TechnicianDispatchRelationalComponent9 ,TechnicianDispatchRelationalComponent10 ,TechnicianDispatchRelationalComponent11 ,TechnicianDispatchRelationalComponent12 ,TechnicianDispatchRelationalComponent13 ,TechnicianDispatchRelationalComponent14 ,TechnicianDispatchRelationalComponent15 ,TechnicianDispatchRelationalComponent16 ,TechnicianDispatchRelationalComponent17 ,TechnicianDispatchRelationalComponent18 ,TechnicianDispatchRelationalComponent19 ,TechnicianDispatchRelationalComponent20 ,TechnicianDispatchRelationalComponent21 ,TechnicianDispatchRelationalComponent22 ,TechnicianDispatchRelationalComponent23 ,TechnicianDispatchRelationalComponent24 ,TechnicianDispatchRelationalComponent25
)
from app.schemas.technician_dispatch import (
    TechnicianDispatchMasterEntityCreate, TechnicianDispatchMasterEntityUpdate,
    TechnicianDispatchRelationalComponent1Create ,TechnicianDispatchRelationalComponent2Create ,TechnicianDispatchRelationalComponent3Create ,TechnicianDispatchRelationalComponent4Create ,TechnicianDispatchRelationalComponent5Create ,TechnicianDispatchRelationalComponent6Create ,TechnicianDispatchRelationalComponent7Create ,TechnicianDispatchRelationalComponent8Create ,TechnicianDispatchRelationalComponent9Create ,TechnicianDispatchRelationalComponent10Create ,TechnicianDispatchRelationalComponent11Create ,TechnicianDispatchRelationalComponent12Create ,TechnicianDispatchRelationalComponent13Create ,TechnicianDispatchRelationalComponent14Create ,TechnicianDispatchRelationalComponent15Create ,TechnicianDispatchRelationalComponent16Create ,TechnicianDispatchRelationalComponent17Create ,TechnicianDispatchRelationalComponent18Create ,TechnicianDispatchRelationalComponent19Create ,TechnicianDispatchRelationalComponent20Create ,TechnicianDispatchRelationalComponent21Create ,TechnicianDispatchRelationalComponent22Create ,TechnicianDispatchRelationalComponent23Create ,TechnicianDispatchRelationalComponent24Create ,TechnicianDispatchRelationalComponent25Create
)

class TechnicianDispatchService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: TechnicianDispatchMasterEntityCreate) -> TechnicianDispatchMasterEntity:
        existing = db.query(TechnicianDispatchMasterEntity).filter(TechnicianDispatchMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = TechnicianDispatchMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> TechnicianDispatchMasterEntity:
        entity = db.query(TechnicianDispatchMasterEntity).filter(TechnicianDispatchMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Technician Dispatch Center Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[TechnicianDispatchStatus] = None) -> List[TechnicianDispatchMasterEntity]:
        query = db.query(TechnicianDispatchMasterEntity)
        if status_filter:
            query = query.filter(TechnicianDispatchMasterEntity.status == status_filter)
        return query.order_by(TechnicianDispatchMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: TechnicianDispatchMasterEntityUpdate) -> TechnicianDispatchMasterEntity:
        entity = TechnicianDispatchService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = TechnicianDispatchService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: TechnicianDispatchRelationalComponent1Create) -> TechnicianDispatchRelationalComponent1:
        comp = TechnicianDispatchRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent1]:
        query = db.query(TechnicianDispatchRelationalComponent1)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: TechnicianDispatchRelationalComponent2Create) -> TechnicianDispatchRelationalComponent2:
        comp = TechnicianDispatchRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent2]:
        query = db.query(TechnicianDispatchRelationalComponent2)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: TechnicianDispatchRelationalComponent3Create) -> TechnicianDispatchRelationalComponent3:
        comp = TechnicianDispatchRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent3]:
        query = db.query(TechnicianDispatchRelationalComponent3)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: TechnicianDispatchRelationalComponent4Create) -> TechnicianDispatchRelationalComponent4:
        comp = TechnicianDispatchRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent4]:
        query = db.query(TechnicianDispatchRelationalComponent4)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: TechnicianDispatchRelationalComponent5Create) -> TechnicianDispatchRelationalComponent5:
        comp = TechnicianDispatchRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent5]:
        query = db.query(TechnicianDispatchRelationalComponent5)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: TechnicianDispatchRelationalComponent6Create) -> TechnicianDispatchRelationalComponent6:
        comp = TechnicianDispatchRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent6]:
        query = db.query(TechnicianDispatchRelationalComponent6)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: TechnicianDispatchRelationalComponent7Create) -> TechnicianDispatchRelationalComponent7:
        comp = TechnicianDispatchRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent7]:
        query = db.query(TechnicianDispatchRelationalComponent7)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: TechnicianDispatchRelationalComponent8Create) -> TechnicianDispatchRelationalComponent8:
        comp = TechnicianDispatchRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent8]:
        query = db.query(TechnicianDispatchRelationalComponent8)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: TechnicianDispatchRelationalComponent9Create) -> TechnicianDispatchRelationalComponent9:
        comp = TechnicianDispatchRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent9]:
        query = db.query(TechnicianDispatchRelationalComponent9)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: TechnicianDispatchRelationalComponent10Create) -> TechnicianDispatchRelationalComponent10:
        comp = TechnicianDispatchRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent10]:
        query = db.query(TechnicianDispatchRelationalComponent10)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: TechnicianDispatchRelationalComponent11Create) -> TechnicianDispatchRelationalComponent11:
        comp = TechnicianDispatchRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent11]:
        query = db.query(TechnicianDispatchRelationalComponent11)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: TechnicianDispatchRelationalComponent12Create) -> TechnicianDispatchRelationalComponent12:
        comp = TechnicianDispatchRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent12]:
        query = db.query(TechnicianDispatchRelationalComponent12)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: TechnicianDispatchRelationalComponent13Create) -> TechnicianDispatchRelationalComponent13:
        comp = TechnicianDispatchRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent13]:
        query = db.query(TechnicianDispatchRelationalComponent13)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: TechnicianDispatchRelationalComponent14Create) -> TechnicianDispatchRelationalComponent14:
        comp = TechnicianDispatchRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent14]:
        query = db.query(TechnicianDispatchRelationalComponent14)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: TechnicianDispatchRelationalComponent15Create) -> TechnicianDispatchRelationalComponent15:
        comp = TechnicianDispatchRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent15]:
        query = db.query(TechnicianDispatchRelationalComponent15)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: TechnicianDispatchRelationalComponent16Create) -> TechnicianDispatchRelationalComponent16:
        comp = TechnicianDispatchRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent16]:
        query = db.query(TechnicianDispatchRelationalComponent16)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: TechnicianDispatchRelationalComponent17Create) -> TechnicianDispatchRelationalComponent17:
        comp = TechnicianDispatchRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent17]:
        query = db.query(TechnicianDispatchRelationalComponent17)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: TechnicianDispatchRelationalComponent18Create) -> TechnicianDispatchRelationalComponent18:
        comp = TechnicianDispatchRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent18]:
        query = db.query(TechnicianDispatchRelationalComponent18)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: TechnicianDispatchRelationalComponent19Create) -> TechnicianDispatchRelationalComponent19:
        comp = TechnicianDispatchRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent19]:
        query = db.query(TechnicianDispatchRelationalComponent19)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: TechnicianDispatchRelationalComponent20Create) -> TechnicianDispatchRelationalComponent20:
        comp = TechnicianDispatchRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent20]:
        query = db.query(TechnicianDispatchRelationalComponent20)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: TechnicianDispatchRelationalComponent21Create) -> TechnicianDispatchRelationalComponent21:
        comp = TechnicianDispatchRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent21]:
        query = db.query(TechnicianDispatchRelationalComponent21)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: TechnicianDispatchRelationalComponent22Create) -> TechnicianDispatchRelationalComponent22:
        comp = TechnicianDispatchRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent22]:
        query = db.query(TechnicianDispatchRelationalComponent22)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: TechnicianDispatchRelationalComponent23Create) -> TechnicianDispatchRelationalComponent23:
        comp = TechnicianDispatchRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent23]:
        query = db.query(TechnicianDispatchRelationalComponent23)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: TechnicianDispatchRelationalComponent24Create) -> TechnicianDispatchRelationalComponent24:
        comp = TechnicianDispatchRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent24]:
        query = db.query(TechnicianDispatchRelationalComponent24)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: TechnicianDispatchRelationalComponent25Create) -> TechnicianDispatchRelationalComponent25:
        comp = TechnicianDispatchRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent25]:
        query = db.query(TechnicianDispatchRelationalComponent25)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: TechnicianDispatchRelationalComponent26Create) -> TechnicianDispatchRelationalComponent26:
        comp = TechnicianDispatchRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent26]:
        query = db.query(TechnicianDispatchRelationalComponent26)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: TechnicianDispatchRelationalComponent27Create) -> TechnicianDispatchRelationalComponent27:
        comp = TechnicianDispatchRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent27]:
        query = db.query(TechnicianDispatchRelationalComponent27)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: TechnicianDispatchRelationalComponent28Create) -> TechnicianDispatchRelationalComponent28:
        comp = TechnicianDispatchRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent28]:
        query = db.query(TechnicianDispatchRelationalComponent28)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: TechnicianDispatchRelationalComponent29Create) -> TechnicianDispatchRelationalComponent29:
        comp = TechnicianDispatchRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent29]:
        query = db.query(TechnicianDispatchRelationalComponent29)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: TechnicianDispatchRelationalComponent30Create) -> TechnicianDispatchRelationalComponent30:
        comp = TechnicianDispatchRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[TechnicianDispatchRelationalComponent30]:
        query = db.query(TechnicianDispatchRelationalComponent30)
        if master_entity_id:
            query = query.filter(TechnicianDispatchRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
