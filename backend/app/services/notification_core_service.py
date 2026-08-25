from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.notification_core import (
    NotificationCoreMasterEntity, NotificationCoreStatus,
    NotificationCoreRelationalComponent1 ,NotificationCoreRelationalComponent2 ,NotificationCoreRelationalComponent3 ,NotificationCoreRelationalComponent4 ,NotificationCoreRelationalComponent5 ,NotificationCoreRelationalComponent6 ,NotificationCoreRelationalComponent7 ,NotificationCoreRelationalComponent8 ,NotificationCoreRelationalComponent9 ,NotificationCoreRelationalComponent10 ,NotificationCoreRelationalComponent11 ,NotificationCoreRelationalComponent12 ,NotificationCoreRelationalComponent13 ,NotificationCoreRelationalComponent14 ,NotificationCoreRelationalComponent15 ,NotificationCoreRelationalComponent16 ,NotificationCoreRelationalComponent17 ,NotificationCoreRelationalComponent18 ,NotificationCoreRelationalComponent19 ,NotificationCoreRelationalComponent20 ,NotificationCoreRelationalComponent21 ,NotificationCoreRelationalComponent22 ,NotificationCoreRelationalComponent23 ,NotificationCoreRelationalComponent24 ,NotificationCoreRelationalComponent25
)
from app.schemas.notification_core import (
    NotificationCoreMasterEntityCreate, NotificationCoreMasterEntityUpdate,
    NotificationCoreRelationalComponent1Create ,NotificationCoreRelationalComponent2Create ,NotificationCoreRelationalComponent3Create ,NotificationCoreRelationalComponent4Create ,NotificationCoreRelationalComponent5Create ,NotificationCoreRelationalComponent6Create ,NotificationCoreRelationalComponent7Create ,NotificationCoreRelationalComponent8Create ,NotificationCoreRelationalComponent9Create ,NotificationCoreRelationalComponent10Create ,NotificationCoreRelationalComponent11Create ,NotificationCoreRelationalComponent12Create ,NotificationCoreRelationalComponent13Create ,NotificationCoreRelationalComponent14Create ,NotificationCoreRelationalComponent15Create ,NotificationCoreRelationalComponent16Create ,NotificationCoreRelationalComponent17Create ,NotificationCoreRelationalComponent18Create ,NotificationCoreRelationalComponent19Create ,NotificationCoreRelationalComponent20Create ,NotificationCoreRelationalComponent21Create ,NotificationCoreRelationalComponent22Create ,NotificationCoreRelationalComponent23Create ,NotificationCoreRelationalComponent24Create ,NotificationCoreRelationalComponent25Create
)

class NotificationCoreService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: NotificationCoreMasterEntityCreate) -> NotificationCoreMasterEntity:
        existing = db.query(NotificationCoreMasterEntity).filter(NotificationCoreMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = NotificationCoreMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> NotificationCoreMasterEntity:
        entity = db.query(NotificationCoreMasterEntity).filter(NotificationCoreMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Core Notification Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[NotificationCoreStatus] = None) -> List[NotificationCoreMasterEntity]:
        query = db.query(NotificationCoreMasterEntity)
        if status_filter:
            query = query.filter(NotificationCoreMasterEntity.status == status_filter)
        return query.order_by(NotificationCoreMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: NotificationCoreMasterEntityUpdate) -> NotificationCoreMasterEntity:
        entity = NotificationCoreService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = NotificationCoreService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: NotificationCoreRelationalComponent1Create) -> NotificationCoreRelationalComponent1:
        comp = NotificationCoreRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent1]:
        query = db.query(NotificationCoreRelationalComponent1)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: NotificationCoreRelationalComponent2Create) -> NotificationCoreRelationalComponent2:
        comp = NotificationCoreRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent2]:
        query = db.query(NotificationCoreRelationalComponent2)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: NotificationCoreRelationalComponent3Create) -> NotificationCoreRelationalComponent3:
        comp = NotificationCoreRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent3]:
        query = db.query(NotificationCoreRelationalComponent3)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: NotificationCoreRelationalComponent4Create) -> NotificationCoreRelationalComponent4:
        comp = NotificationCoreRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent4]:
        query = db.query(NotificationCoreRelationalComponent4)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: NotificationCoreRelationalComponent5Create) -> NotificationCoreRelationalComponent5:
        comp = NotificationCoreRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent5]:
        query = db.query(NotificationCoreRelationalComponent5)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: NotificationCoreRelationalComponent6Create) -> NotificationCoreRelationalComponent6:
        comp = NotificationCoreRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent6]:
        query = db.query(NotificationCoreRelationalComponent6)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: NotificationCoreRelationalComponent7Create) -> NotificationCoreRelationalComponent7:
        comp = NotificationCoreRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent7]:
        query = db.query(NotificationCoreRelationalComponent7)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: NotificationCoreRelationalComponent8Create) -> NotificationCoreRelationalComponent8:
        comp = NotificationCoreRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent8]:
        query = db.query(NotificationCoreRelationalComponent8)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: NotificationCoreRelationalComponent9Create) -> NotificationCoreRelationalComponent9:
        comp = NotificationCoreRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent9]:
        query = db.query(NotificationCoreRelationalComponent9)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: NotificationCoreRelationalComponent10Create) -> NotificationCoreRelationalComponent10:
        comp = NotificationCoreRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent10]:
        query = db.query(NotificationCoreRelationalComponent10)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: NotificationCoreRelationalComponent11Create) -> NotificationCoreRelationalComponent11:
        comp = NotificationCoreRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent11]:
        query = db.query(NotificationCoreRelationalComponent11)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: NotificationCoreRelationalComponent12Create) -> NotificationCoreRelationalComponent12:
        comp = NotificationCoreRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent12]:
        query = db.query(NotificationCoreRelationalComponent12)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: NotificationCoreRelationalComponent13Create) -> NotificationCoreRelationalComponent13:
        comp = NotificationCoreRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent13]:
        query = db.query(NotificationCoreRelationalComponent13)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: NotificationCoreRelationalComponent14Create) -> NotificationCoreRelationalComponent14:
        comp = NotificationCoreRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent14]:
        query = db.query(NotificationCoreRelationalComponent14)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: NotificationCoreRelationalComponent15Create) -> NotificationCoreRelationalComponent15:
        comp = NotificationCoreRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent15]:
        query = db.query(NotificationCoreRelationalComponent15)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: NotificationCoreRelationalComponent16Create) -> NotificationCoreRelationalComponent16:
        comp = NotificationCoreRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent16]:
        query = db.query(NotificationCoreRelationalComponent16)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: NotificationCoreRelationalComponent17Create) -> NotificationCoreRelationalComponent17:
        comp = NotificationCoreRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent17]:
        query = db.query(NotificationCoreRelationalComponent17)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: NotificationCoreRelationalComponent18Create) -> NotificationCoreRelationalComponent18:
        comp = NotificationCoreRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent18]:
        query = db.query(NotificationCoreRelationalComponent18)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: NotificationCoreRelationalComponent19Create) -> NotificationCoreRelationalComponent19:
        comp = NotificationCoreRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent19]:
        query = db.query(NotificationCoreRelationalComponent19)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: NotificationCoreRelationalComponent20Create) -> NotificationCoreRelationalComponent20:
        comp = NotificationCoreRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent20]:
        query = db.query(NotificationCoreRelationalComponent20)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: NotificationCoreRelationalComponent21Create) -> NotificationCoreRelationalComponent21:
        comp = NotificationCoreRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent21]:
        query = db.query(NotificationCoreRelationalComponent21)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: NotificationCoreRelationalComponent22Create) -> NotificationCoreRelationalComponent22:
        comp = NotificationCoreRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent22]:
        query = db.query(NotificationCoreRelationalComponent22)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: NotificationCoreRelationalComponent23Create) -> NotificationCoreRelationalComponent23:
        comp = NotificationCoreRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent23]:
        query = db.query(NotificationCoreRelationalComponent23)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: NotificationCoreRelationalComponent24Create) -> NotificationCoreRelationalComponent24:
        comp = NotificationCoreRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent24]:
        query = db.query(NotificationCoreRelationalComponent24)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: NotificationCoreRelationalComponent25Create) -> NotificationCoreRelationalComponent25:
        comp = NotificationCoreRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[NotificationCoreRelationalComponent25]:
        query = db.query(NotificationCoreRelationalComponent25)
        if master_entity_id:
            query = query.filter(NotificationCoreRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
