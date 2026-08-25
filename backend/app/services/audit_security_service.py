from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.audit_security import (
    AuditSecurityMasterEntity, AuditSecurityStatus, AuditSecurityPriority, AuditSecurityCategoryType,
    AuditSecurityRelationalComponent1 ,AuditSecurityRelationalComponent2 ,AuditSecurityRelationalComponent3 ,AuditSecurityRelationalComponent4 ,AuditSecurityRelationalComponent5 ,AuditSecurityRelationalComponent6 ,AuditSecurityRelationalComponent7 ,AuditSecurityRelationalComponent8 ,AuditSecurityRelationalComponent9 ,AuditSecurityRelationalComponent10 ,AuditSecurityRelationalComponent11 ,AuditSecurityRelationalComponent12 ,AuditSecurityRelationalComponent13 ,AuditSecurityRelationalComponent14 ,AuditSecurityRelationalComponent15 ,AuditSecurityRelationalComponent16 ,AuditSecurityRelationalComponent17 ,AuditSecurityRelationalComponent18 ,AuditSecurityRelationalComponent19 ,AuditSecurityRelationalComponent20 ,AuditSecurityRelationalComponent21 ,AuditSecurityRelationalComponent22 ,AuditSecurityRelationalComponent23 ,AuditSecurityRelationalComponent24 ,AuditSecurityRelationalComponent25
)
from app.schemas.audit_security import (
    AuditSecurityMasterEntityCreate, AuditSecurityMasterEntityUpdate,
    AuditSecurityRelationalComponent1Create ,AuditSecurityRelationalComponent2Create ,AuditSecurityRelationalComponent3Create ,AuditSecurityRelationalComponent4Create ,AuditSecurityRelationalComponent5Create ,AuditSecurityRelationalComponent6Create ,AuditSecurityRelationalComponent7Create ,AuditSecurityRelationalComponent8Create ,AuditSecurityRelationalComponent9Create ,AuditSecurityRelationalComponent10Create ,AuditSecurityRelationalComponent11Create ,AuditSecurityRelationalComponent12Create ,AuditSecurityRelationalComponent13Create ,AuditSecurityRelationalComponent14Create ,AuditSecurityRelationalComponent15Create ,AuditSecurityRelationalComponent16Create ,AuditSecurityRelationalComponent17Create ,AuditSecurityRelationalComponent18Create ,AuditSecurityRelationalComponent19Create ,AuditSecurityRelationalComponent20Create ,AuditSecurityRelationalComponent21Create ,AuditSecurityRelationalComponent22Create ,AuditSecurityRelationalComponent23Create ,AuditSecurityRelationalComponent24Create ,AuditSecurityRelationalComponent25Create
)

class AuditSecurityService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: AuditSecurityMasterEntityCreate) -> AuditSecurityMasterEntity:
        existing = db.query(AuditSecurityMasterEntity).filter(AuditSecurityMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = AuditSecurityMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> AuditSecurityMasterEntity:
        entity = db.query(AuditSecurityMasterEntity).filter(AuditSecurityMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Audit & Security System Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[AuditSecurityStatus] = None) -> List[AuditSecurityMasterEntity]:
        query = db.query(AuditSecurityMasterEntity)
        if status_filter:
            query = query.filter(AuditSecurityMasterEntity.status == status_filter)
        return query.order_by(AuditSecurityMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: AuditSecurityMasterEntityUpdate) -> AuditSecurityMasterEntity:
        entity = AuditSecurityService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = AuditSecurityService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: AuditSecurityRelationalComponent1Create) -> AuditSecurityRelationalComponent1:
        comp = AuditSecurityRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent1]:
        query = db.query(AuditSecurityRelationalComponent1)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: AuditSecurityRelationalComponent2Create) -> AuditSecurityRelationalComponent2:
        comp = AuditSecurityRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent2]:
        query = db.query(AuditSecurityRelationalComponent2)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: AuditSecurityRelationalComponent3Create) -> AuditSecurityRelationalComponent3:
        comp = AuditSecurityRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent3]:
        query = db.query(AuditSecurityRelationalComponent3)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: AuditSecurityRelationalComponent4Create) -> AuditSecurityRelationalComponent4:
        comp = AuditSecurityRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent4]:
        query = db.query(AuditSecurityRelationalComponent4)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: AuditSecurityRelationalComponent5Create) -> AuditSecurityRelationalComponent5:
        comp = AuditSecurityRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent5]:
        query = db.query(AuditSecurityRelationalComponent5)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: AuditSecurityRelationalComponent6Create) -> AuditSecurityRelationalComponent6:
        comp = AuditSecurityRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent6]:
        query = db.query(AuditSecurityRelationalComponent6)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: AuditSecurityRelationalComponent7Create) -> AuditSecurityRelationalComponent7:
        comp = AuditSecurityRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent7]:
        query = db.query(AuditSecurityRelationalComponent7)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: AuditSecurityRelationalComponent8Create) -> AuditSecurityRelationalComponent8:
        comp = AuditSecurityRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent8]:
        query = db.query(AuditSecurityRelationalComponent8)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: AuditSecurityRelationalComponent9Create) -> AuditSecurityRelationalComponent9:
        comp = AuditSecurityRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent9]:
        query = db.query(AuditSecurityRelationalComponent9)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: AuditSecurityRelationalComponent10Create) -> AuditSecurityRelationalComponent10:
        comp = AuditSecurityRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent10]:
        query = db.query(AuditSecurityRelationalComponent10)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: AuditSecurityRelationalComponent11Create) -> AuditSecurityRelationalComponent11:
        comp = AuditSecurityRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent11]:
        query = db.query(AuditSecurityRelationalComponent11)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: AuditSecurityRelationalComponent12Create) -> AuditSecurityRelationalComponent12:
        comp = AuditSecurityRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent12]:
        query = db.query(AuditSecurityRelationalComponent12)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: AuditSecurityRelationalComponent13Create) -> AuditSecurityRelationalComponent13:
        comp = AuditSecurityRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent13]:
        query = db.query(AuditSecurityRelationalComponent13)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: AuditSecurityRelationalComponent14Create) -> AuditSecurityRelationalComponent14:
        comp = AuditSecurityRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent14]:
        query = db.query(AuditSecurityRelationalComponent14)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: AuditSecurityRelationalComponent15Create) -> AuditSecurityRelationalComponent15:
        comp = AuditSecurityRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent15]:
        query = db.query(AuditSecurityRelationalComponent15)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: AuditSecurityRelationalComponent16Create) -> AuditSecurityRelationalComponent16:
        comp = AuditSecurityRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent16]:
        query = db.query(AuditSecurityRelationalComponent16)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: AuditSecurityRelationalComponent17Create) -> AuditSecurityRelationalComponent17:
        comp = AuditSecurityRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent17]:
        query = db.query(AuditSecurityRelationalComponent17)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: AuditSecurityRelationalComponent18Create) -> AuditSecurityRelationalComponent18:
        comp = AuditSecurityRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent18]:
        query = db.query(AuditSecurityRelationalComponent18)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: AuditSecurityRelationalComponent19Create) -> AuditSecurityRelationalComponent19:
        comp = AuditSecurityRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent19]:
        query = db.query(AuditSecurityRelationalComponent19)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: AuditSecurityRelationalComponent20Create) -> AuditSecurityRelationalComponent20:
        comp = AuditSecurityRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent20]:
        query = db.query(AuditSecurityRelationalComponent20)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: AuditSecurityRelationalComponent21Create) -> AuditSecurityRelationalComponent21:
        comp = AuditSecurityRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent21]:
        query = db.query(AuditSecurityRelationalComponent21)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: AuditSecurityRelationalComponent22Create) -> AuditSecurityRelationalComponent22:
        comp = AuditSecurityRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent22]:
        query = db.query(AuditSecurityRelationalComponent22)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: AuditSecurityRelationalComponent23Create) -> AuditSecurityRelationalComponent23:
        comp = AuditSecurityRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent23]:
        query = db.query(AuditSecurityRelationalComponent23)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: AuditSecurityRelationalComponent24Create) -> AuditSecurityRelationalComponent24:
        comp = AuditSecurityRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent24]:
        query = db.query(AuditSecurityRelationalComponent24)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: AuditSecurityRelationalComponent25Create) -> AuditSecurityRelationalComponent25:
        comp = AuditSecurityRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[AuditSecurityRelationalComponent25]:
        query = db.query(AuditSecurityRelationalComponent25)
        if master_entity_id:
            query = query.filter(AuditSecurityRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
