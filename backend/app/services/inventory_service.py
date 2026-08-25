from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.inventory import (
    InventoryMasterEntity, InventoryStatus, InventoryPriority, InventoryCategoryType,
    InventoryRelationalComponent1 ,InventoryRelationalComponent2 ,InventoryRelationalComponent3 ,InventoryRelationalComponent4 ,InventoryRelationalComponent5 ,InventoryRelationalComponent6 ,InventoryRelationalComponent7 ,InventoryRelationalComponent8 ,InventoryRelationalComponent9 ,InventoryRelationalComponent10 ,InventoryRelationalComponent11 ,InventoryRelationalComponent12 ,InventoryRelationalComponent13 ,InventoryRelationalComponent14 ,InventoryRelationalComponent15 ,InventoryRelationalComponent16 ,InventoryRelationalComponent17 ,InventoryRelationalComponent18 ,InventoryRelationalComponent19 ,InventoryRelationalComponent20 ,InventoryRelationalComponent21 ,InventoryRelationalComponent22 ,InventoryRelationalComponent23 ,InventoryRelationalComponent24 ,InventoryRelationalComponent25
)
from app.schemas.inventory import (
    InventoryMasterEntityCreate, InventoryMasterEntityUpdate,
    InventoryRelationalComponent1Create ,InventoryRelationalComponent2Create ,InventoryRelationalComponent3Create ,InventoryRelationalComponent4Create ,InventoryRelationalComponent5Create ,InventoryRelationalComponent6Create ,InventoryRelationalComponent7Create ,InventoryRelationalComponent8Create ,InventoryRelationalComponent9Create ,InventoryRelationalComponent10Create ,InventoryRelationalComponent11Create ,InventoryRelationalComponent12Create ,InventoryRelationalComponent13Create ,InventoryRelationalComponent14Create ,InventoryRelationalComponent15Create ,InventoryRelationalComponent16Create ,InventoryRelationalComponent17Create ,InventoryRelationalComponent18Create ,InventoryRelationalComponent19Create ,InventoryRelationalComponent20Create ,InventoryRelationalComponent21Create ,InventoryRelationalComponent22Create ,InventoryRelationalComponent23Create ,InventoryRelationalComponent24Create ,InventoryRelationalComponent25Create
)

class InventoryService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: InventoryMasterEntityCreate) -> InventoryMasterEntity:
        existing = db.query(InventoryMasterEntity).filter(InventoryMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = InventoryMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> InventoryMasterEntity:
        entity = db.query(InventoryMasterEntity).filter(InventoryMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inventory & Spare Parts Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[InventoryStatus] = None) -> List[InventoryMasterEntity]:
        query = db.query(InventoryMasterEntity)
        if status_filter:
            query = query.filter(InventoryMasterEntity.status == status_filter)
        return query.order_by(InventoryMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: InventoryMasterEntityUpdate) -> InventoryMasterEntity:
        entity = InventoryService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = InventoryService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: InventoryRelationalComponent1Create) -> InventoryRelationalComponent1:
        comp = InventoryRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent1]:
        query = db.query(InventoryRelationalComponent1)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: InventoryRelationalComponent2Create) -> InventoryRelationalComponent2:
        comp = InventoryRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent2]:
        query = db.query(InventoryRelationalComponent2)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: InventoryRelationalComponent3Create) -> InventoryRelationalComponent3:
        comp = InventoryRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent3]:
        query = db.query(InventoryRelationalComponent3)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: InventoryRelationalComponent4Create) -> InventoryRelationalComponent4:
        comp = InventoryRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent4]:
        query = db.query(InventoryRelationalComponent4)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: InventoryRelationalComponent5Create) -> InventoryRelationalComponent5:
        comp = InventoryRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent5]:
        query = db.query(InventoryRelationalComponent5)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: InventoryRelationalComponent6Create) -> InventoryRelationalComponent6:
        comp = InventoryRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent6]:
        query = db.query(InventoryRelationalComponent6)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: InventoryRelationalComponent7Create) -> InventoryRelationalComponent7:
        comp = InventoryRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent7]:
        query = db.query(InventoryRelationalComponent7)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: InventoryRelationalComponent8Create) -> InventoryRelationalComponent8:
        comp = InventoryRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent8]:
        query = db.query(InventoryRelationalComponent8)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: InventoryRelationalComponent9Create) -> InventoryRelationalComponent9:
        comp = InventoryRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent9]:
        query = db.query(InventoryRelationalComponent9)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: InventoryRelationalComponent10Create) -> InventoryRelationalComponent10:
        comp = InventoryRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent10]:
        query = db.query(InventoryRelationalComponent10)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: InventoryRelationalComponent11Create) -> InventoryRelationalComponent11:
        comp = InventoryRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent11]:
        query = db.query(InventoryRelationalComponent11)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: InventoryRelationalComponent12Create) -> InventoryRelationalComponent12:
        comp = InventoryRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent12]:
        query = db.query(InventoryRelationalComponent12)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: InventoryRelationalComponent13Create) -> InventoryRelationalComponent13:
        comp = InventoryRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent13]:
        query = db.query(InventoryRelationalComponent13)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: InventoryRelationalComponent14Create) -> InventoryRelationalComponent14:
        comp = InventoryRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent14]:
        query = db.query(InventoryRelationalComponent14)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: InventoryRelationalComponent15Create) -> InventoryRelationalComponent15:
        comp = InventoryRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent15]:
        query = db.query(InventoryRelationalComponent15)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: InventoryRelationalComponent16Create) -> InventoryRelationalComponent16:
        comp = InventoryRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent16]:
        query = db.query(InventoryRelationalComponent16)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: InventoryRelationalComponent17Create) -> InventoryRelationalComponent17:
        comp = InventoryRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent17]:
        query = db.query(InventoryRelationalComponent17)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: InventoryRelationalComponent18Create) -> InventoryRelationalComponent18:
        comp = InventoryRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent18]:
        query = db.query(InventoryRelationalComponent18)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: InventoryRelationalComponent19Create) -> InventoryRelationalComponent19:
        comp = InventoryRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent19]:
        query = db.query(InventoryRelationalComponent19)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: InventoryRelationalComponent20Create) -> InventoryRelationalComponent20:
        comp = InventoryRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent20]:
        query = db.query(InventoryRelationalComponent20)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: InventoryRelationalComponent21Create) -> InventoryRelationalComponent21:
        comp = InventoryRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent21]:
        query = db.query(InventoryRelationalComponent21)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: InventoryRelationalComponent22Create) -> InventoryRelationalComponent22:
        comp = InventoryRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent22]:
        query = db.query(InventoryRelationalComponent22)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: InventoryRelationalComponent23Create) -> InventoryRelationalComponent23:
        comp = InventoryRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent23]:
        query = db.query(InventoryRelationalComponent23)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: InventoryRelationalComponent24Create) -> InventoryRelationalComponent24:
        comp = InventoryRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent24]:
        query = db.query(InventoryRelationalComponent24)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: InventoryRelationalComponent25Create) -> InventoryRelationalComponent25:
        comp = InventoryRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[InventoryRelationalComponent25]:
        query = db.query(InventoryRelationalComponent25)
        if master_entity_id:
            query = query.filter(InventoryRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
