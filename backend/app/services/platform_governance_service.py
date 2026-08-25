from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.platform_governance import (
    PlatformGovernanceMasterEntity, PlatformGovernanceStatus,
    PlatformGovernanceRelationalComponent1 ,PlatformGovernanceRelationalComponent2 ,PlatformGovernanceRelationalComponent3 ,PlatformGovernanceRelationalComponent4 ,PlatformGovernanceRelationalComponent5 ,PlatformGovernanceRelationalComponent6 ,PlatformGovernanceRelationalComponent7 ,PlatformGovernanceRelationalComponent8 ,PlatformGovernanceRelationalComponent9 ,PlatformGovernanceRelationalComponent10 ,PlatformGovernanceRelationalComponent11 ,PlatformGovernanceRelationalComponent12 ,PlatformGovernanceRelationalComponent13 ,PlatformGovernanceRelationalComponent14 ,PlatformGovernanceRelationalComponent15 ,PlatformGovernanceRelationalComponent16 ,PlatformGovernanceRelationalComponent17 ,PlatformGovernanceRelationalComponent18 ,PlatformGovernanceRelationalComponent19 ,PlatformGovernanceRelationalComponent20 ,PlatformGovernanceRelationalComponent21 ,PlatformGovernanceRelationalComponent22 ,PlatformGovernanceRelationalComponent23 ,PlatformGovernanceRelationalComponent24 ,PlatformGovernanceRelationalComponent25
)
from app.schemas.platform_governance import (
    PlatformGovernanceMasterEntityCreate, PlatformGovernanceMasterEntityUpdate,
    PlatformGovernanceRelationalComponent1Create ,PlatformGovernanceRelationalComponent2Create ,PlatformGovernanceRelationalComponent3Create ,PlatformGovernanceRelationalComponent4Create ,PlatformGovernanceRelationalComponent5Create ,PlatformGovernanceRelationalComponent6Create ,PlatformGovernanceRelationalComponent7Create ,PlatformGovernanceRelationalComponent8Create ,PlatformGovernanceRelationalComponent9Create ,PlatformGovernanceRelationalComponent10Create ,PlatformGovernanceRelationalComponent11Create ,PlatformGovernanceRelationalComponent12Create ,PlatformGovernanceRelationalComponent13Create ,PlatformGovernanceRelationalComponent14Create ,PlatformGovernanceRelationalComponent15Create ,PlatformGovernanceRelationalComponent16Create ,PlatformGovernanceRelationalComponent17Create ,PlatformGovernanceRelationalComponent18Create ,PlatformGovernanceRelationalComponent19Create ,PlatformGovernanceRelationalComponent20Create ,PlatformGovernanceRelationalComponent21Create ,PlatformGovernanceRelationalComponent22Create ,PlatformGovernanceRelationalComponent23Create ,PlatformGovernanceRelationalComponent24Create ,PlatformGovernanceRelationalComponent25Create
)

class PlatformGovernanceService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: PlatformGovernanceMasterEntityCreate) -> PlatformGovernanceMasterEntity:
        existing = db.query(PlatformGovernanceMasterEntity).filter(PlatformGovernanceMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = PlatformGovernanceMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> PlatformGovernanceMasterEntity:
        entity = db.query(PlatformGovernanceMasterEntity).filter(PlatformGovernanceMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Platform Governance & Compliance Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[PlatformGovernanceStatus] = None) -> List[PlatformGovernanceMasterEntity]:
        query = db.query(PlatformGovernanceMasterEntity)
        if status_filter:
            query = query.filter(PlatformGovernanceMasterEntity.status == status_filter)
        return query.order_by(PlatformGovernanceMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: PlatformGovernanceMasterEntityUpdate) -> PlatformGovernanceMasterEntity:
        entity = PlatformGovernanceService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = PlatformGovernanceService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: PlatformGovernanceRelationalComponent1Create) -> PlatformGovernanceRelationalComponent1:
        comp = PlatformGovernanceRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent1]:
        query = db.query(PlatformGovernanceRelationalComponent1)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: PlatformGovernanceRelationalComponent2Create) -> PlatformGovernanceRelationalComponent2:
        comp = PlatformGovernanceRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent2]:
        query = db.query(PlatformGovernanceRelationalComponent2)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: PlatformGovernanceRelationalComponent3Create) -> PlatformGovernanceRelationalComponent3:
        comp = PlatformGovernanceRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent3]:
        query = db.query(PlatformGovernanceRelationalComponent3)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: PlatformGovernanceRelationalComponent4Create) -> PlatformGovernanceRelationalComponent4:
        comp = PlatformGovernanceRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent4]:
        query = db.query(PlatformGovernanceRelationalComponent4)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: PlatformGovernanceRelationalComponent5Create) -> PlatformGovernanceRelationalComponent5:
        comp = PlatformGovernanceRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent5]:
        query = db.query(PlatformGovernanceRelationalComponent5)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: PlatformGovernanceRelationalComponent6Create) -> PlatformGovernanceRelationalComponent6:
        comp = PlatformGovernanceRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent6]:
        query = db.query(PlatformGovernanceRelationalComponent6)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: PlatformGovernanceRelationalComponent7Create) -> PlatformGovernanceRelationalComponent7:
        comp = PlatformGovernanceRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent7]:
        query = db.query(PlatformGovernanceRelationalComponent7)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: PlatformGovernanceRelationalComponent8Create) -> PlatformGovernanceRelationalComponent8:
        comp = PlatformGovernanceRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent8]:
        query = db.query(PlatformGovernanceRelationalComponent8)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: PlatformGovernanceRelationalComponent9Create) -> PlatformGovernanceRelationalComponent9:
        comp = PlatformGovernanceRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent9]:
        query = db.query(PlatformGovernanceRelationalComponent9)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: PlatformGovernanceRelationalComponent10Create) -> PlatformGovernanceRelationalComponent10:
        comp = PlatformGovernanceRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent10]:
        query = db.query(PlatformGovernanceRelationalComponent10)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: PlatformGovernanceRelationalComponent11Create) -> PlatformGovernanceRelationalComponent11:
        comp = PlatformGovernanceRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent11]:
        query = db.query(PlatformGovernanceRelationalComponent11)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: PlatformGovernanceRelationalComponent12Create) -> PlatformGovernanceRelationalComponent12:
        comp = PlatformGovernanceRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent12]:
        query = db.query(PlatformGovernanceRelationalComponent12)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: PlatformGovernanceRelationalComponent13Create) -> PlatformGovernanceRelationalComponent13:
        comp = PlatformGovernanceRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent13]:
        query = db.query(PlatformGovernanceRelationalComponent13)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: PlatformGovernanceRelationalComponent14Create) -> PlatformGovernanceRelationalComponent14:
        comp = PlatformGovernanceRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent14]:
        query = db.query(PlatformGovernanceRelationalComponent14)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: PlatformGovernanceRelationalComponent15Create) -> PlatformGovernanceRelationalComponent15:
        comp = PlatformGovernanceRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent15]:
        query = db.query(PlatformGovernanceRelationalComponent15)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: PlatformGovernanceRelationalComponent16Create) -> PlatformGovernanceRelationalComponent16:
        comp = PlatformGovernanceRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent16]:
        query = db.query(PlatformGovernanceRelationalComponent16)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: PlatformGovernanceRelationalComponent17Create) -> PlatformGovernanceRelationalComponent17:
        comp = PlatformGovernanceRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent17]:
        query = db.query(PlatformGovernanceRelationalComponent17)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: PlatformGovernanceRelationalComponent18Create) -> PlatformGovernanceRelationalComponent18:
        comp = PlatformGovernanceRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent18]:
        query = db.query(PlatformGovernanceRelationalComponent18)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: PlatformGovernanceRelationalComponent19Create) -> PlatformGovernanceRelationalComponent19:
        comp = PlatformGovernanceRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent19]:
        query = db.query(PlatformGovernanceRelationalComponent19)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: PlatformGovernanceRelationalComponent20Create) -> PlatformGovernanceRelationalComponent20:
        comp = PlatformGovernanceRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent20]:
        query = db.query(PlatformGovernanceRelationalComponent20)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: PlatformGovernanceRelationalComponent21Create) -> PlatformGovernanceRelationalComponent21:
        comp = PlatformGovernanceRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent21]:
        query = db.query(PlatformGovernanceRelationalComponent21)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: PlatformGovernanceRelationalComponent22Create) -> PlatformGovernanceRelationalComponent22:
        comp = PlatformGovernanceRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent22]:
        query = db.query(PlatformGovernanceRelationalComponent22)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: PlatformGovernanceRelationalComponent23Create) -> PlatformGovernanceRelationalComponent23:
        comp = PlatformGovernanceRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent23]:
        query = db.query(PlatformGovernanceRelationalComponent23)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: PlatformGovernanceRelationalComponent24Create) -> PlatformGovernanceRelationalComponent24:
        comp = PlatformGovernanceRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent24]:
        query = db.query(PlatformGovernanceRelationalComponent24)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: PlatformGovernanceRelationalComponent25Create) -> PlatformGovernanceRelationalComponent25:
        comp = PlatformGovernanceRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent25]:
        query = db.query(PlatformGovernanceRelationalComponent25)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: PlatformGovernanceRelationalComponent26Create) -> PlatformGovernanceRelationalComponent26:
        comp = PlatformGovernanceRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent26]:
        query = db.query(PlatformGovernanceRelationalComponent26)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: PlatformGovernanceRelationalComponent27Create) -> PlatformGovernanceRelationalComponent27:
        comp = PlatformGovernanceRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent27]:
        query = db.query(PlatformGovernanceRelationalComponent27)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: PlatformGovernanceRelationalComponent28Create) -> PlatformGovernanceRelationalComponent28:
        comp = PlatformGovernanceRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent28]:
        query = db.query(PlatformGovernanceRelationalComponent28)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: PlatformGovernanceRelationalComponent29Create) -> PlatformGovernanceRelationalComponent29:
        comp = PlatformGovernanceRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent29]:
        query = db.query(PlatformGovernanceRelationalComponent29)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: PlatformGovernanceRelationalComponent30Create) -> PlatformGovernanceRelationalComponent30:
        comp = PlatformGovernanceRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[PlatformGovernanceRelationalComponent30]:
        query = db.query(PlatformGovernanceRelationalComponent30)
        if master_entity_id:
            query = query.filter(PlatformGovernanceRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
