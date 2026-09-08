from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.admin_oversight import (
    AdminOversightMasterEntity, AdminOversightStatus,
    AdminOversightRelationalComponent1 ,AdminOversightRelationalComponent2 ,AdminOversightRelationalComponent3 ,AdminOversightRelationalComponent4 ,AdminOversightRelationalComponent5 ,AdminOversightRelationalComponent6 ,AdminOversightRelationalComponent7 ,AdminOversightRelationalComponent8 ,AdminOversightRelationalComponent9 ,AdminOversightRelationalComponent10 ,AdminOversightRelationalComponent11 ,AdminOversightRelationalComponent12 ,AdminOversightRelationalComponent13 ,AdminOversightRelationalComponent14 ,AdminOversightRelationalComponent15 ,AdminOversightRelationalComponent16 ,AdminOversightRelationalComponent17 ,AdminOversightRelationalComponent18 ,AdminOversightRelationalComponent19 ,AdminOversightRelationalComponent20 ,AdminOversightRelationalComponent21 ,AdminOversightRelationalComponent22 ,AdminOversightRelationalComponent23 ,AdminOversightRelationalComponent24 ,AdminOversightRelationalComponent25
)
from app.schemas.admin_oversight import (
    AdminOversightMasterEntityCreate, AdminOversightMasterEntityUpdate,
    AdminOversightRelationalComponent1Create ,AdminOversightRelationalComponent2Create ,AdminOversightRelationalComponent3Create ,AdminOversightRelationalComponent4Create ,AdminOversightRelationalComponent5Create ,AdminOversightRelationalComponent6Create ,AdminOversightRelationalComponent7Create ,AdminOversightRelationalComponent8Create ,AdminOversightRelationalComponent9Create ,AdminOversightRelationalComponent10Create ,AdminOversightRelationalComponent11Create ,AdminOversightRelationalComponent12Create ,AdminOversightRelationalComponent13Create ,AdminOversightRelationalComponent14Create ,AdminOversightRelationalComponent15Create ,AdminOversightRelationalComponent16Create ,AdminOversightRelationalComponent17Create ,AdminOversightRelationalComponent18Create ,AdminOversightRelationalComponent19Create ,AdminOversightRelationalComponent20Create ,AdminOversightRelationalComponent21Create ,AdminOversightRelationalComponent22Create ,AdminOversightRelationalComponent23Create ,AdminOversightRelationalComponent24Create ,AdminOversightRelationalComponent25Create
)

class AdminOversightService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: AdminOversightMasterEntityCreate) -> AdminOversightMasterEntity:
        existing = db.query(AdminOversightMasterEntity).filter(AdminOversightMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = AdminOversightMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> AdminOversightMasterEntity:
        entity = db.query(AdminOversightMasterEntity).filter(AdminOversightMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin Oversight Center Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[AdminOversightStatus] = None) -> List[AdminOversightMasterEntity]:
        query = db.query(AdminOversightMasterEntity)
        if status_filter:
            query = query.filter(AdminOversightMasterEntity.status == status_filter)
        return query.order_by(AdminOversightMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: AdminOversightMasterEntityUpdate) -> AdminOversightMasterEntity:
        entity = AdminOversightService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = AdminOversightService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: AdminOversightRelationalComponent1Create) -> AdminOversightRelationalComponent1:
        comp = AdminOversightRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent1]:
        query = db.query(AdminOversightRelationalComponent1)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: AdminOversightRelationalComponent2Create) -> AdminOversightRelationalComponent2:
        comp = AdminOversightRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent2]:
        query = db.query(AdminOversightRelationalComponent2)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: AdminOversightRelationalComponent3Create) -> AdminOversightRelationalComponent3:
        comp = AdminOversightRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent3]:
        query = db.query(AdminOversightRelationalComponent3)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: AdminOversightRelationalComponent4Create) -> AdminOversightRelationalComponent4:
        comp = AdminOversightRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent4]:
        query = db.query(AdminOversightRelationalComponent4)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: AdminOversightRelationalComponent5Create) -> AdminOversightRelationalComponent5:
        comp = AdminOversightRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent5]:
        query = db.query(AdminOversightRelationalComponent5)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: AdminOversightRelationalComponent6Create) -> AdminOversightRelationalComponent6:
        comp = AdminOversightRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent6]:
        query = db.query(AdminOversightRelationalComponent6)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: AdminOversightRelationalComponent7Create) -> AdminOversightRelationalComponent7:
        comp = AdminOversightRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent7]:
        query = db.query(AdminOversightRelationalComponent7)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: AdminOversightRelationalComponent8Create) -> AdminOversightRelationalComponent8:
        comp = AdminOversightRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent8]:
        query = db.query(AdminOversightRelationalComponent8)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: AdminOversightRelationalComponent9Create) -> AdminOversightRelationalComponent9:
        comp = AdminOversightRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent9]:
        query = db.query(AdminOversightRelationalComponent9)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: AdminOversightRelationalComponent10Create) -> AdminOversightRelationalComponent10:
        comp = AdminOversightRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent10]:
        query = db.query(AdminOversightRelationalComponent10)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: AdminOversightRelationalComponent11Create) -> AdminOversightRelationalComponent11:
        comp = AdminOversightRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent11]:
        query = db.query(AdminOversightRelationalComponent11)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: AdminOversightRelationalComponent12Create) -> AdminOversightRelationalComponent12:
        comp = AdminOversightRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent12]:
        query = db.query(AdminOversightRelationalComponent12)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: AdminOversightRelationalComponent13Create) -> AdminOversightRelationalComponent13:
        comp = AdminOversightRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent13]:
        query = db.query(AdminOversightRelationalComponent13)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: AdminOversightRelationalComponent14Create) -> AdminOversightRelationalComponent14:
        comp = AdminOversightRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent14]:
        query = db.query(AdminOversightRelationalComponent14)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: AdminOversightRelationalComponent15Create) -> AdminOversightRelationalComponent15:
        comp = AdminOversightRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent15]:
        query = db.query(AdminOversightRelationalComponent15)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: AdminOversightRelationalComponent16Create) -> AdminOversightRelationalComponent16:
        comp = AdminOversightRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent16]:
        query = db.query(AdminOversightRelationalComponent16)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: AdminOversightRelationalComponent17Create) -> AdminOversightRelationalComponent17:
        comp = AdminOversightRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent17]:
        query = db.query(AdminOversightRelationalComponent17)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: AdminOversightRelationalComponent18Create) -> AdminOversightRelationalComponent18:
        comp = AdminOversightRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent18]:
        query = db.query(AdminOversightRelationalComponent18)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: AdminOversightRelationalComponent19Create) -> AdminOversightRelationalComponent19:
        comp = AdminOversightRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent19]:
        query = db.query(AdminOversightRelationalComponent19)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: AdminOversightRelationalComponent20Create) -> AdminOversightRelationalComponent20:
        comp = AdminOversightRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent20]:
        query = db.query(AdminOversightRelationalComponent20)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: AdminOversightRelationalComponent21Create) -> AdminOversightRelationalComponent21:
        comp = AdminOversightRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent21]:
        query = db.query(AdminOversightRelationalComponent21)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: AdminOversightRelationalComponent22Create) -> AdminOversightRelationalComponent22:
        comp = AdminOversightRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent22]:
        query = db.query(AdminOversightRelationalComponent22)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: AdminOversightRelationalComponent23Create) -> AdminOversightRelationalComponent23:
        comp = AdminOversightRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent23]:
        query = db.query(AdminOversightRelationalComponent23)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: AdminOversightRelationalComponent24Create) -> AdminOversightRelationalComponent24:
        comp = AdminOversightRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent24]:
        query = db.query(AdminOversightRelationalComponent24)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: AdminOversightRelationalComponent25Create) -> AdminOversightRelationalComponent25:
        comp = AdminOversightRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent25]:
        query = db.query(AdminOversightRelationalComponent25)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: AdminOversightRelationalComponent26Create) -> AdminOversightRelationalComponent26:
        comp = AdminOversightRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent26]:
        query = db.query(AdminOversightRelationalComponent26)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: AdminOversightRelationalComponent27Create) -> AdminOversightRelationalComponent27:
        comp = AdminOversightRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent27]:
        query = db.query(AdminOversightRelationalComponent27)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: AdminOversightRelationalComponent28Create) -> AdminOversightRelationalComponent28:
        comp = AdminOversightRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent28]:
        query = db.query(AdminOversightRelationalComponent28)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: AdminOversightRelationalComponent29Create) -> AdminOversightRelationalComponent29:
        comp = AdminOversightRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent29]:
        query = db.query(AdminOversightRelationalComponent29)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: AdminOversightRelationalComponent30Create) -> AdminOversightRelationalComponent30:
        comp = AdminOversightRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[AdminOversightRelationalComponent30]:
        query = db.query(AdminOversightRelationalComponent30)
        if master_entity_id:
            query = query.filter(AdminOversightRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
