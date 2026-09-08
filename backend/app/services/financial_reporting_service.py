from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.financial_reporting import (
    FinancialReportingMasterEntity, FinancialReportingStatus,
    FinancialReportingRelationalComponent1 ,FinancialReportingRelationalComponent2 ,FinancialReportingRelationalComponent3 ,FinancialReportingRelationalComponent4 ,FinancialReportingRelationalComponent5 ,FinancialReportingRelationalComponent6 ,FinancialReportingRelationalComponent7 ,FinancialReportingRelationalComponent8 ,FinancialReportingRelationalComponent9 ,FinancialReportingRelationalComponent10 ,FinancialReportingRelationalComponent11 ,FinancialReportingRelationalComponent12 ,FinancialReportingRelationalComponent13 ,FinancialReportingRelationalComponent14 ,FinancialReportingRelationalComponent15 ,FinancialReportingRelationalComponent16 ,FinancialReportingRelationalComponent17 ,FinancialReportingRelationalComponent18 ,FinancialReportingRelationalComponent19 ,FinancialReportingRelationalComponent20 ,FinancialReportingRelationalComponent21 ,FinancialReportingRelationalComponent22 ,FinancialReportingRelationalComponent23 ,FinancialReportingRelationalComponent24 ,FinancialReportingRelationalComponent25
)
from app.schemas.financial_reporting import (
    FinancialReportingMasterEntityCreate, FinancialReportingMasterEntityUpdate,
    FinancialReportingRelationalComponent1Create ,FinancialReportingRelationalComponent2Create ,FinancialReportingRelationalComponent3Create ,FinancialReportingRelationalComponent4Create ,FinancialReportingRelationalComponent5Create ,FinancialReportingRelationalComponent6Create ,FinancialReportingRelationalComponent7Create ,FinancialReportingRelationalComponent8Create ,FinancialReportingRelationalComponent9Create ,FinancialReportingRelationalComponent10Create ,FinancialReportingRelationalComponent11Create ,FinancialReportingRelationalComponent12Create ,FinancialReportingRelationalComponent13Create ,FinancialReportingRelationalComponent14Create ,FinancialReportingRelationalComponent15Create ,FinancialReportingRelationalComponent16Create ,FinancialReportingRelationalComponent17Create ,FinancialReportingRelationalComponent18Create ,FinancialReportingRelationalComponent19Create ,FinancialReportingRelationalComponent20Create ,FinancialReportingRelationalComponent21Create ,FinancialReportingRelationalComponent22Create ,FinancialReportingRelationalComponent23Create ,FinancialReportingRelationalComponent24Create ,FinancialReportingRelationalComponent25Create
)

class FinancialReportingService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: FinancialReportingMasterEntityCreate) -> FinancialReportingMasterEntity:
        existing = db.query(FinancialReportingMasterEntity).filter(FinancialReportingMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = FinancialReportingMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> FinancialReportingMasterEntity:
        entity = db.query(FinancialReportingMasterEntity).filter(FinancialReportingMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Financial & Tax Reporting Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[FinancialReportingStatus] = None) -> List[FinancialReportingMasterEntity]:
        query = db.query(FinancialReportingMasterEntity)
        if status_filter:
            query = query.filter(FinancialReportingMasterEntity.status == status_filter)
        return query.order_by(FinancialReportingMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: FinancialReportingMasterEntityUpdate) -> FinancialReportingMasterEntity:
        entity = FinancialReportingService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = FinancialReportingService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: FinancialReportingRelationalComponent1Create) -> FinancialReportingRelationalComponent1:
        comp = FinancialReportingRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent1]:
        query = db.query(FinancialReportingRelationalComponent1)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: FinancialReportingRelationalComponent2Create) -> FinancialReportingRelationalComponent2:
        comp = FinancialReportingRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent2]:
        query = db.query(FinancialReportingRelationalComponent2)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: FinancialReportingRelationalComponent3Create) -> FinancialReportingRelationalComponent3:
        comp = FinancialReportingRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent3]:
        query = db.query(FinancialReportingRelationalComponent3)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: FinancialReportingRelationalComponent4Create) -> FinancialReportingRelationalComponent4:
        comp = FinancialReportingRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent4]:
        query = db.query(FinancialReportingRelationalComponent4)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: FinancialReportingRelationalComponent5Create) -> FinancialReportingRelationalComponent5:
        comp = FinancialReportingRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent5]:
        query = db.query(FinancialReportingRelationalComponent5)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: FinancialReportingRelationalComponent6Create) -> FinancialReportingRelationalComponent6:
        comp = FinancialReportingRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent6]:
        query = db.query(FinancialReportingRelationalComponent6)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: FinancialReportingRelationalComponent7Create) -> FinancialReportingRelationalComponent7:
        comp = FinancialReportingRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent7]:
        query = db.query(FinancialReportingRelationalComponent7)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: FinancialReportingRelationalComponent8Create) -> FinancialReportingRelationalComponent8:
        comp = FinancialReportingRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent8]:
        query = db.query(FinancialReportingRelationalComponent8)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: FinancialReportingRelationalComponent9Create) -> FinancialReportingRelationalComponent9:
        comp = FinancialReportingRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent9]:
        query = db.query(FinancialReportingRelationalComponent9)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: FinancialReportingRelationalComponent10Create) -> FinancialReportingRelationalComponent10:
        comp = FinancialReportingRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent10]:
        query = db.query(FinancialReportingRelationalComponent10)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: FinancialReportingRelationalComponent11Create) -> FinancialReportingRelationalComponent11:
        comp = FinancialReportingRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent11]:
        query = db.query(FinancialReportingRelationalComponent11)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: FinancialReportingRelationalComponent12Create) -> FinancialReportingRelationalComponent12:
        comp = FinancialReportingRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent12]:
        query = db.query(FinancialReportingRelationalComponent12)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: FinancialReportingRelationalComponent13Create) -> FinancialReportingRelationalComponent13:
        comp = FinancialReportingRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent13]:
        query = db.query(FinancialReportingRelationalComponent13)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: FinancialReportingRelationalComponent14Create) -> FinancialReportingRelationalComponent14:
        comp = FinancialReportingRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent14]:
        query = db.query(FinancialReportingRelationalComponent14)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: FinancialReportingRelationalComponent15Create) -> FinancialReportingRelationalComponent15:
        comp = FinancialReportingRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent15]:
        query = db.query(FinancialReportingRelationalComponent15)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: FinancialReportingRelationalComponent16Create) -> FinancialReportingRelationalComponent16:
        comp = FinancialReportingRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent16]:
        query = db.query(FinancialReportingRelationalComponent16)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: FinancialReportingRelationalComponent17Create) -> FinancialReportingRelationalComponent17:
        comp = FinancialReportingRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent17]:
        query = db.query(FinancialReportingRelationalComponent17)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: FinancialReportingRelationalComponent18Create) -> FinancialReportingRelationalComponent18:
        comp = FinancialReportingRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent18]:
        query = db.query(FinancialReportingRelationalComponent18)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: FinancialReportingRelationalComponent19Create) -> FinancialReportingRelationalComponent19:
        comp = FinancialReportingRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent19]:
        query = db.query(FinancialReportingRelationalComponent19)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: FinancialReportingRelationalComponent20Create) -> FinancialReportingRelationalComponent20:
        comp = FinancialReportingRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent20]:
        query = db.query(FinancialReportingRelationalComponent20)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: FinancialReportingRelationalComponent21Create) -> FinancialReportingRelationalComponent21:
        comp = FinancialReportingRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent21]:
        query = db.query(FinancialReportingRelationalComponent21)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: FinancialReportingRelationalComponent22Create) -> FinancialReportingRelationalComponent22:
        comp = FinancialReportingRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent22]:
        query = db.query(FinancialReportingRelationalComponent22)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: FinancialReportingRelationalComponent23Create) -> FinancialReportingRelationalComponent23:
        comp = FinancialReportingRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent23]:
        query = db.query(FinancialReportingRelationalComponent23)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: FinancialReportingRelationalComponent24Create) -> FinancialReportingRelationalComponent24:
        comp = FinancialReportingRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent24]:
        query = db.query(FinancialReportingRelationalComponent24)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: FinancialReportingRelationalComponent25Create) -> FinancialReportingRelationalComponent25:
        comp = FinancialReportingRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent25]:
        query = db.query(FinancialReportingRelationalComponent25)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: FinancialReportingRelationalComponent26Create) -> FinancialReportingRelationalComponent26:
        comp = FinancialReportingRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent26]:
        query = db.query(FinancialReportingRelationalComponent26)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: FinancialReportingRelationalComponent27Create) -> FinancialReportingRelationalComponent27:
        comp = FinancialReportingRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent27]:
        query = db.query(FinancialReportingRelationalComponent27)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: FinancialReportingRelationalComponent28Create) -> FinancialReportingRelationalComponent28:
        comp = FinancialReportingRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent28]:
        query = db.query(FinancialReportingRelationalComponent28)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: FinancialReportingRelationalComponent29Create) -> FinancialReportingRelationalComponent29:
        comp = FinancialReportingRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent29]:
        query = db.query(FinancialReportingRelationalComponent29)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: FinancialReportingRelationalComponent30Create) -> FinancialReportingRelationalComponent30:
        comp = FinancialReportingRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[FinancialReportingRelationalComponent30]:
        query = db.query(FinancialReportingRelationalComponent30)
        if master_entity_id:
            query = query.filter(FinancialReportingRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
