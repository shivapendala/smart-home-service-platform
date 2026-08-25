from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.communication import (
    CommunicationMasterEntity, CommunicationStatus, CommunicationPriority, CommunicationCategoryType,
    CommunicationRelationalComponent1 ,CommunicationRelationalComponent2 ,CommunicationRelationalComponent3 ,CommunicationRelationalComponent4 ,CommunicationRelationalComponent5 ,CommunicationRelationalComponent6 ,CommunicationRelationalComponent7 ,CommunicationRelationalComponent8 ,CommunicationRelationalComponent9 ,CommunicationRelationalComponent10 ,CommunicationRelationalComponent11 ,CommunicationRelationalComponent12 ,CommunicationRelationalComponent13 ,CommunicationRelationalComponent14 ,CommunicationRelationalComponent15 ,CommunicationRelationalComponent16 ,CommunicationRelationalComponent17 ,CommunicationRelationalComponent18 ,CommunicationRelationalComponent19 ,CommunicationRelationalComponent20 ,CommunicationRelationalComponent21 ,CommunicationRelationalComponent22 ,CommunicationRelationalComponent23 ,CommunicationRelationalComponent24 ,CommunicationRelationalComponent25
)
from app.schemas.communication import (
    CommunicationMasterEntityCreate, CommunicationMasterEntityUpdate,
    CommunicationRelationalComponent1Create ,CommunicationRelationalComponent2Create ,CommunicationRelationalComponent3Create ,CommunicationRelationalComponent4Create ,CommunicationRelationalComponent5Create ,CommunicationRelationalComponent6Create ,CommunicationRelationalComponent7Create ,CommunicationRelationalComponent8Create ,CommunicationRelationalComponent9Create ,CommunicationRelationalComponent10Create ,CommunicationRelationalComponent11Create ,CommunicationRelationalComponent12Create ,CommunicationRelationalComponent13Create ,CommunicationRelationalComponent14Create ,CommunicationRelationalComponent15Create ,CommunicationRelationalComponent16Create ,CommunicationRelationalComponent17Create ,CommunicationRelationalComponent18Create ,CommunicationRelationalComponent19Create ,CommunicationRelationalComponent20Create ,CommunicationRelationalComponent21Create ,CommunicationRelationalComponent22Create ,CommunicationRelationalComponent23Create ,CommunicationRelationalComponent24Create ,CommunicationRelationalComponent25Create
)

class CommunicationService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: CommunicationMasterEntityCreate) -> CommunicationMasterEntity:
        existing = db.query(CommunicationMasterEntity).filter(CommunicationMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = CommunicationMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> CommunicationMasterEntity:
        entity = db.query(CommunicationMasterEntity).filter(CommunicationMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Communication Center Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[CommunicationStatus] = None) -> List[CommunicationMasterEntity]:
        query = db.query(CommunicationMasterEntity)
        if status_filter:
            query = query.filter(CommunicationMasterEntity.status == status_filter)
        return query.order_by(CommunicationMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: CommunicationMasterEntityUpdate) -> CommunicationMasterEntity:
        entity = CommunicationService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = CommunicationService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: CommunicationRelationalComponent1Create) -> CommunicationRelationalComponent1:
        comp = CommunicationRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent1]:
        query = db.query(CommunicationRelationalComponent1)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: CommunicationRelationalComponent2Create) -> CommunicationRelationalComponent2:
        comp = CommunicationRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent2]:
        query = db.query(CommunicationRelationalComponent2)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: CommunicationRelationalComponent3Create) -> CommunicationRelationalComponent3:
        comp = CommunicationRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent3]:
        query = db.query(CommunicationRelationalComponent3)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: CommunicationRelationalComponent4Create) -> CommunicationRelationalComponent4:
        comp = CommunicationRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent4]:
        query = db.query(CommunicationRelationalComponent4)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: CommunicationRelationalComponent5Create) -> CommunicationRelationalComponent5:
        comp = CommunicationRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent5]:
        query = db.query(CommunicationRelationalComponent5)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: CommunicationRelationalComponent6Create) -> CommunicationRelationalComponent6:
        comp = CommunicationRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent6]:
        query = db.query(CommunicationRelationalComponent6)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: CommunicationRelationalComponent7Create) -> CommunicationRelationalComponent7:
        comp = CommunicationRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent7]:
        query = db.query(CommunicationRelationalComponent7)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: CommunicationRelationalComponent8Create) -> CommunicationRelationalComponent8:
        comp = CommunicationRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent8]:
        query = db.query(CommunicationRelationalComponent8)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: CommunicationRelationalComponent9Create) -> CommunicationRelationalComponent9:
        comp = CommunicationRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent9]:
        query = db.query(CommunicationRelationalComponent9)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: CommunicationRelationalComponent10Create) -> CommunicationRelationalComponent10:
        comp = CommunicationRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent10]:
        query = db.query(CommunicationRelationalComponent10)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: CommunicationRelationalComponent11Create) -> CommunicationRelationalComponent11:
        comp = CommunicationRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent11]:
        query = db.query(CommunicationRelationalComponent11)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: CommunicationRelationalComponent12Create) -> CommunicationRelationalComponent12:
        comp = CommunicationRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent12]:
        query = db.query(CommunicationRelationalComponent12)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: CommunicationRelationalComponent13Create) -> CommunicationRelationalComponent13:
        comp = CommunicationRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent13]:
        query = db.query(CommunicationRelationalComponent13)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: CommunicationRelationalComponent14Create) -> CommunicationRelationalComponent14:
        comp = CommunicationRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent14]:
        query = db.query(CommunicationRelationalComponent14)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: CommunicationRelationalComponent15Create) -> CommunicationRelationalComponent15:
        comp = CommunicationRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent15]:
        query = db.query(CommunicationRelationalComponent15)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: CommunicationRelationalComponent16Create) -> CommunicationRelationalComponent16:
        comp = CommunicationRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent16]:
        query = db.query(CommunicationRelationalComponent16)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: CommunicationRelationalComponent17Create) -> CommunicationRelationalComponent17:
        comp = CommunicationRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent17]:
        query = db.query(CommunicationRelationalComponent17)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: CommunicationRelationalComponent18Create) -> CommunicationRelationalComponent18:
        comp = CommunicationRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent18]:
        query = db.query(CommunicationRelationalComponent18)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: CommunicationRelationalComponent19Create) -> CommunicationRelationalComponent19:
        comp = CommunicationRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent19]:
        query = db.query(CommunicationRelationalComponent19)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: CommunicationRelationalComponent20Create) -> CommunicationRelationalComponent20:
        comp = CommunicationRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent20]:
        query = db.query(CommunicationRelationalComponent20)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: CommunicationRelationalComponent21Create) -> CommunicationRelationalComponent21:
        comp = CommunicationRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent21]:
        query = db.query(CommunicationRelationalComponent21)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: CommunicationRelationalComponent22Create) -> CommunicationRelationalComponent22:
        comp = CommunicationRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent22]:
        query = db.query(CommunicationRelationalComponent22)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: CommunicationRelationalComponent23Create) -> CommunicationRelationalComponent23:
        comp = CommunicationRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent23]:
        query = db.query(CommunicationRelationalComponent23)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: CommunicationRelationalComponent24Create) -> CommunicationRelationalComponent24:
        comp = CommunicationRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent24]:
        query = db.query(CommunicationRelationalComponent24)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: CommunicationRelationalComponent25Create) -> CommunicationRelationalComponent25:
        comp = CommunicationRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[CommunicationRelationalComponent25]:
        query = db.query(CommunicationRelationalComponent25)
        if master_entity_id:
            query = query.filter(CommunicationRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
