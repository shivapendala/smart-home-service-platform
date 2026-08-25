from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.warranty_amc import (
    WarrantyAmcMasterEntity, WarrantyAmcStatus, WarrantyAmcPriority, WarrantyAmcCategoryType,
    WarrantyAmcRelationalComponent1 ,WarrantyAmcRelationalComponent2 ,WarrantyAmcRelationalComponent3 ,WarrantyAmcRelationalComponent4 ,WarrantyAmcRelationalComponent5 ,WarrantyAmcRelationalComponent6 ,WarrantyAmcRelationalComponent7 ,WarrantyAmcRelationalComponent8 ,WarrantyAmcRelationalComponent9 ,WarrantyAmcRelationalComponent10 ,WarrantyAmcRelationalComponent11 ,WarrantyAmcRelationalComponent12 ,WarrantyAmcRelationalComponent13 ,WarrantyAmcRelationalComponent14 ,WarrantyAmcRelationalComponent15 ,WarrantyAmcRelationalComponent16 ,WarrantyAmcRelationalComponent17 ,WarrantyAmcRelationalComponent18 ,WarrantyAmcRelationalComponent19 ,WarrantyAmcRelationalComponent20 ,WarrantyAmcRelationalComponent21 ,WarrantyAmcRelationalComponent22 ,WarrantyAmcRelationalComponent23 ,WarrantyAmcRelationalComponent24 ,WarrantyAmcRelationalComponent25
)
from app.schemas.warranty_amc import (
    WarrantyAmcMasterEntityCreate, WarrantyAmcMasterEntityUpdate,
    WarrantyAmcRelationalComponent1Create ,WarrantyAmcRelationalComponent2Create ,WarrantyAmcRelationalComponent3Create ,WarrantyAmcRelationalComponent4Create ,WarrantyAmcRelationalComponent5Create ,WarrantyAmcRelationalComponent6Create ,WarrantyAmcRelationalComponent7Create ,WarrantyAmcRelationalComponent8Create ,WarrantyAmcRelationalComponent9Create ,WarrantyAmcRelationalComponent10Create ,WarrantyAmcRelationalComponent11Create ,WarrantyAmcRelationalComponent12Create ,WarrantyAmcRelationalComponent13Create ,WarrantyAmcRelationalComponent14Create ,WarrantyAmcRelationalComponent15Create ,WarrantyAmcRelationalComponent16Create ,WarrantyAmcRelationalComponent17Create ,WarrantyAmcRelationalComponent18Create ,WarrantyAmcRelationalComponent19Create ,WarrantyAmcRelationalComponent20Create ,WarrantyAmcRelationalComponent21Create ,WarrantyAmcRelationalComponent22Create ,WarrantyAmcRelationalComponent23Create ,WarrantyAmcRelationalComponent24Create ,WarrantyAmcRelationalComponent25Create
)

class WarrantyAmcService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: WarrantyAmcMasterEntityCreate) -> WarrantyAmcMasterEntity:
        existing = db.query(WarrantyAmcMasterEntity).filter(WarrantyAmcMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = WarrantyAmcMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> WarrantyAmcMasterEntity:
        entity = db.query(WarrantyAmcMasterEntity).filter(WarrantyAmcMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warranty & AMC System Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[WarrantyAmcStatus] = None) -> List[WarrantyAmcMasterEntity]:
        query = db.query(WarrantyAmcMasterEntity)
        if status_filter:
            query = query.filter(WarrantyAmcMasterEntity.status == status_filter)
        return query.order_by(WarrantyAmcMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: WarrantyAmcMasterEntityUpdate) -> WarrantyAmcMasterEntity:
        entity = WarrantyAmcService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = WarrantyAmcService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: WarrantyAmcRelationalComponent1Create) -> WarrantyAmcRelationalComponent1:
        comp = WarrantyAmcRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent1]:
        query = db.query(WarrantyAmcRelationalComponent1)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: WarrantyAmcRelationalComponent2Create) -> WarrantyAmcRelationalComponent2:
        comp = WarrantyAmcRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent2]:
        query = db.query(WarrantyAmcRelationalComponent2)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: WarrantyAmcRelationalComponent3Create) -> WarrantyAmcRelationalComponent3:
        comp = WarrantyAmcRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent3]:
        query = db.query(WarrantyAmcRelationalComponent3)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: WarrantyAmcRelationalComponent4Create) -> WarrantyAmcRelationalComponent4:
        comp = WarrantyAmcRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent4]:
        query = db.query(WarrantyAmcRelationalComponent4)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: WarrantyAmcRelationalComponent5Create) -> WarrantyAmcRelationalComponent5:
        comp = WarrantyAmcRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent5]:
        query = db.query(WarrantyAmcRelationalComponent5)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: WarrantyAmcRelationalComponent6Create) -> WarrantyAmcRelationalComponent6:
        comp = WarrantyAmcRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent6]:
        query = db.query(WarrantyAmcRelationalComponent6)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: WarrantyAmcRelationalComponent7Create) -> WarrantyAmcRelationalComponent7:
        comp = WarrantyAmcRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent7]:
        query = db.query(WarrantyAmcRelationalComponent7)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: WarrantyAmcRelationalComponent8Create) -> WarrantyAmcRelationalComponent8:
        comp = WarrantyAmcRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent8]:
        query = db.query(WarrantyAmcRelationalComponent8)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: WarrantyAmcRelationalComponent9Create) -> WarrantyAmcRelationalComponent9:
        comp = WarrantyAmcRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent9]:
        query = db.query(WarrantyAmcRelationalComponent9)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: WarrantyAmcRelationalComponent10Create) -> WarrantyAmcRelationalComponent10:
        comp = WarrantyAmcRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent10]:
        query = db.query(WarrantyAmcRelationalComponent10)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: WarrantyAmcRelationalComponent11Create) -> WarrantyAmcRelationalComponent11:
        comp = WarrantyAmcRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent11]:
        query = db.query(WarrantyAmcRelationalComponent11)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: WarrantyAmcRelationalComponent12Create) -> WarrantyAmcRelationalComponent12:
        comp = WarrantyAmcRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent12]:
        query = db.query(WarrantyAmcRelationalComponent12)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: WarrantyAmcRelationalComponent13Create) -> WarrantyAmcRelationalComponent13:
        comp = WarrantyAmcRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent13]:
        query = db.query(WarrantyAmcRelationalComponent13)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: WarrantyAmcRelationalComponent14Create) -> WarrantyAmcRelationalComponent14:
        comp = WarrantyAmcRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent14]:
        query = db.query(WarrantyAmcRelationalComponent14)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: WarrantyAmcRelationalComponent15Create) -> WarrantyAmcRelationalComponent15:
        comp = WarrantyAmcRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent15]:
        query = db.query(WarrantyAmcRelationalComponent15)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: WarrantyAmcRelationalComponent16Create) -> WarrantyAmcRelationalComponent16:
        comp = WarrantyAmcRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent16]:
        query = db.query(WarrantyAmcRelationalComponent16)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: WarrantyAmcRelationalComponent17Create) -> WarrantyAmcRelationalComponent17:
        comp = WarrantyAmcRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent17]:
        query = db.query(WarrantyAmcRelationalComponent17)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: WarrantyAmcRelationalComponent18Create) -> WarrantyAmcRelationalComponent18:
        comp = WarrantyAmcRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent18]:
        query = db.query(WarrantyAmcRelationalComponent18)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: WarrantyAmcRelationalComponent19Create) -> WarrantyAmcRelationalComponent19:
        comp = WarrantyAmcRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent19]:
        query = db.query(WarrantyAmcRelationalComponent19)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: WarrantyAmcRelationalComponent20Create) -> WarrantyAmcRelationalComponent20:
        comp = WarrantyAmcRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent20]:
        query = db.query(WarrantyAmcRelationalComponent20)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: WarrantyAmcRelationalComponent21Create) -> WarrantyAmcRelationalComponent21:
        comp = WarrantyAmcRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent21]:
        query = db.query(WarrantyAmcRelationalComponent21)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: WarrantyAmcRelationalComponent22Create) -> WarrantyAmcRelationalComponent22:
        comp = WarrantyAmcRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent22]:
        query = db.query(WarrantyAmcRelationalComponent22)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: WarrantyAmcRelationalComponent23Create) -> WarrantyAmcRelationalComponent23:
        comp = WarrantyAmcRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent23]:
        query = db.query(WarrantyAmcRelationalComponent23)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: WarrantyAmcRelationalComponent24Create) -> WarrantyAmcRelationalComponent24:
        comp = WarrantyAmcRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent24]:
        query = db.query(WarrantyAmcRelationalComponent24)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: WarrantyAmcRelationalComponent25Create) -> WarrantyAmcRelationalComponent25:
        comp = WarrantyAmcRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[WarrantyAmcRelationalComponent25]:
        query = db.query(WarrantyAmcRelationalComponent25)
        if master_entity_id:
            query = query.filter(WarrantyAmcRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
