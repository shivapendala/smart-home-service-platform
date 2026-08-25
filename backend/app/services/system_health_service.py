from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.system_health import (
    SystemHealthMasterEntity, SystemHealthStatus,
    SystemHealthRelationalComponent1 ,SystemHealthRelationalComponent2 ,SystemHealthRelationalComponent3 ,SystemHealthRelationalComponent4 ,SystemHealthRelationalComponent5 ,SystemHealthRelationalComponent6 ,SystemHealthRelationalComponent7 ,SystemHealthRelationalComponent8 ,SystemHealthRelationalComponent9 ,SystemHealthRelationalComponent10 ,SystemHealthRelationalComponent11 ,SystemHealthRelationalComponent12 ,SystemHealthRelationalComponent13 ,SystemHealthRelationalComponent14 ,SystemHealthRelationalComponent15 ,SystemHealthRelationalComponent16 ,SystemHealthRelationalComponent17 ,SystemHealthRelationalComponent18 ,SystemHealthRelationalComponent19 ,SystemHealthRelationalComponent20 ,SystemHealthRelationalComponent21 ,SystemHealthRelationalComponent22 ,SystemHealthRelationalComponent23 ,SystemHealthRelationalComponent24 ,SystemHealthRelationalComponent25
)
from app.schemas.system_health import (
    SystemHealthMasterEntityCreate, SystemHealthMasterEntityUpdate,
    SystemHealthRelationalComponent1Create ,SystemHealthRelationalComponent2Create ,SystemHealthRelationalComponent3Create ,SystemHealthRelationalComponent4Create ,SystemHealthRelationalComponent5Create ,SystemHealthRelationalComponent6Create ,SystemHealthRelationalComponent7Create ,SystemHealthRelationalComponent8Create ,SystemHealthRelationalComponent9Create ,SystemHealthRelationalComponent10Create ,SystemHealthRelationalComponent11Create ,SystemHealthRelationalComponent12Create ,SystemHealthRelationalComponent13Create ,SystemHealthRelationalComponent14Create ,SystemHealthRelationalComponent15Create ,SystemHealthRelationalComponent16Create ,SystemHealthRelationalComponent17Create ,SystemHealthRelationalComponent18Create ,SystemHealthRelationalComponent19Create ,SystemHealthRelationalComponent20Create ,SystemHealthRelationalComponent21Create ,SystemHealthRelationalComponent22Create ,SystemHealthRelationalComponent23Create ,SystemHealthRelationalComponent24Create ,SystemHealthRelationalComponent25Create
)

class SystemHealthService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: SystemHealthMasterEntityCreate) -> SystemHealthMasterEntity:
        existing = db.query(SystemHealthMasterEntity).filter(SystemHealthMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = SystemHealthMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> SystemHealthMasterEntity:
        entity = db.query(SystemHealthMasterEntity).filter(SystemHealthMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Platform System Health & Monitoring Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[SystemHealthStatus] = None) -> List[SystemHealthMasterEntity]:
        query = db.query(SystemHealthMasterEntity)
        if status_filter:
            query = query.filter(SystemHealthMasterEntity.status == status_filter)
        return query.order_by(SystemHealthMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: SystemHealthMasterEntityUpdate) -> SystemHealthMasterEntity:
        entity = SystemHealthService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = SystemHealthService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: SystemHealthRelationalComponent1Create) -> SystemHealthRelationalComponent1:
        comp = SystemHealthRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent1]:
        query = db.query(SystemHealthRelationalComponent1)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: SystemHealthRelationalComponent2Create) -> SystemHealthRelationalComponent2:
        comp = SystemHealthRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent2]:
        query = db.query(SystemHealthRelationalComponent2)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: SystemHealthRelationalComponent3Create) -> SystemHealthRelationalComponent3:
        comp = SystemHealthRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent3]:
        query = db.query(SystemHealthRelationalComponent3)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: SystemHealthRelationalComponent4Create) -> SystemHealthRelationalComponent4:
        comp = SystemHealthRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent4]:
        query = db.query(SystemHealthRelationalComponent4)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: SystemHealthRelationalComponent5Create) -> SystemHealthRelationalComponent5:
        comp = SystemHealthRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent5]:
        query = db.query(SystemHealthRelationalComponent5)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: SystemHealthRelationalComponent6Create) -> SystemHealthRelationalComponent6:
        comp = SystemHealthRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent6]:
        query = db.query(SystemHealthRelationalComponent6)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: SystemHealthRelationalComponent7Create) -> SystemHealthRelationalComponent7:
        comp = SystemHealthRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent7]:
        query = db.query(SystemHealthRelationalComponent7)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: SystemHealthRelationalComponent8Create) -> SystemHealthRelationalComponent8:
        comp = SystemHealthRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent8]:
        query = db.query(SystemHealthRelationalComponent8)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: SystemHealthRelationalComponent9Create) -> SystemHealthRelationalComponent9:
        comp = SystemHealthRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent9]:
        query = db.query(SystemHealthRelationalComponent9)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: SystemHealthRelationalComponent10Create) -> SystemHealthRelationalComponent10:
        comp = SystemHealthRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent10]:
        query = db.query(SystemHealthRelationalComponent10)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: SystemHealthRelationalComponent11Create) -> SystemHealthRelationalComponent11:
        comp = SystemHealthRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent11]:
        query = db.query(SystemHealthRelationalComponent11)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: SystemHealthRelationalComponent12Create) -> SystemHealthRelationalComponent12:
        comp = SystemHealthRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent12]:
        query = db.query(SystemHealthRelationalComponent12)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: SystemHealthRelationalComponent13Create) -> SystemHealthRelationalComponent13:
        comp = SystemHealthRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent13]:
        query = db.query(SystemHealthRelationalComponent13)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: SystemHealthRelationalComponent14Create) -> SystemHealthRelationalComponent14:
        comp = SystemHealthRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent14]:
        query = db.query(SystemHealthRelationalComponent14)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: SystemHealthRelationalComponent15Create) -> SystemHealthRelationalComponent15:
        comp = SystemHealthRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent15]:
        query = db.query(SystemHealthRelationalComponent15)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: SystemHealthRelationalComponent16Create) -> SystemHealthRelationalComponent16:
        comp = SystemHealthRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent16]:
        query = db.query(SystemHealthRelationalComponent16)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: SystemHealthRelationalComponent17Create) -> SystemHealthRelationalComponent17:
        comp = SystemHealthRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent17]:
        query = db.query(SystemHealthRelationalComponent17)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: SystemHealthRelationalComponent18Create) -> SystemHealthRelationalComponent18:
        comp = SystemHealthRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent18]:
        query = db.query(SystemHealthRelationalComponent18)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: SystemHealthRelationalComponent19Create) -> SystemHealthRelationalComponent19:
        comp = SystemHealthRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent19]:
        query = db.query(SystemHealthRelationalComponent19)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: SystemHealthRelationalComponent20Create) -> SystemHealthRelationalComponent20:
        comp = SystemHealthRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent20]:
        query = db.query(SystemHealthRelationalComponent20)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: SystemHealthRelationalComponent21Create) -> SystemHealthRelationalComponent21:
        comp = SystemHealthRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent21]:
        query = db.query(SystemHealthRelationalComponent21)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: SystemHealthRelationalComponent22Create) -> SystemHealthRelationalComponent22:
        comp = SystemHealthRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent22]:
        query = db.query(SystemHealthRelationalComponent22)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: SystemHealthRelationalComponent23Create) -> SystemHealthRelationalComponent23:
        comp = SystemHealthRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent23]:
        query = db.query(SystemHealthRelationalComponent23)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: SystemHealthRelationalComponent24Create) -> SystemHealthRelationalComponent24:
        comp = SystemHealthRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent24]:
        query = db.query(SystemHealthRelationalComponent24)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: SystemHealthRelationalComponent25Create) -> SystemHealthRelationalComponent25:
        comp = SystemHealthRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[SystemHealthRelationalComponent25]:
        query = db.query(SystemHealthRelationalComponent25)
        if master_entity_id:
            query = query.filter(SystemHealthRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
