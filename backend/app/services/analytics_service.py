from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.analytics import (
    AnalyticsMasterEntity, AnalyticsStatus, AnalyticsPriority, AnalyticsCategoryType,
    AnalyticsRelationalComponent1 ,AnalyticsRelationalComponent2 ,AnalyticsRelationalComponent3 ,AnalyticsRelationalComponent4 ,AnalyticsRelationalComponent5 ,AnalyticsRelationalComponent6 ,AnalyticsRelationalComponent7 ,AnalyticsRelationalComponent8 ,AnalyticsRelationalComponent9 ,AnalyticsRelationalComponent10 ,AnalyticsRelationalComponent11 ,AnalyticsRelationalComponent12 ,AnalyticsRelationalComponent13 ,AnalyticsRelationalComponent14 ,AnalyticsRelationalComponent15 ,AnalyticsRelationalComponent16 ,AnalyticsRelationalComponent17 ,AnalyticsRelationalComponent18 ,AnalyticsRelationalComponent19 ,AnalyticsRelationalComponent20 ,AnalyticsRelationalComponent21 ,AnalyticsRelationalComponent22 ,AnalyticsRelationalComponent23 ,AnalyticsRelationalComponent24 ,AnalyticsRelationalComponent25
)
from app.schemas.analytics import (
    AnalyticsMasterEntityCreate, AnalyticsMasterEntityUpdate,
    AnalyticsRelationalComponent1Create ,AnalyticsRelationalComponent2Create ,AnalyticsRelationalComponent3Create ,AnalyticsRelationalComponent4Create ,AnalyticsRelationalComponent5Create ,AnalyticsRelationalComponent6Create ,AnalyticsRelationalComponent7Create ,AnalyticsRelationalComponent8Create ,AnalyticsRelationalComponent9Create ,AnalyticsRelationalComponent10Create ,AnalyticsRelationalComponent11Create ,AnalyticsRelationalComponent12Create ,AnalyticsRelationalComponent13Create ,AnalyticsRelationalComponent14Create ,AnalyticsRelationalComponent15Create ,AnalyticsRelationalComponent16Create ,AnalyticsRelationalComponent17Create ,AnalyticsRelationalComponent18Create ,AnalyticsRelationalComponent19Create ,AnalyticsRelationalComponent20Create ,AnalyticsRelationalComponent21Create ,AnalyticsRelationalComponent22Create ,AnalyticsRelationalComponent23Create ,AnalyticsRelationalComponent24Create ,AnalyticsRelationalComponent25Create
)

class AnalyticsService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: AnalyticsMasterEntityCreate) -> AnalyticsMasterEntity:
        existing = db.query(AnalyticsMasterEntity).filter(AnalyticsMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = AnalyticsMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> AnalyticsMasterEntity:
        entity = db.query(AnalyticsMasterEntity).filter(AnalyticsMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analytics & BI Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[AnalyticsStatus] = None) -> List[AnalyticsMasterEntity]:
        query = db.query(AnalyticsMasterEntity)
        if status_filter:
            query = query.filter(AnalyticsMasterEntity.status == status_filter)
        return query.order_by(AnalyticsMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: AnalyticsMasterEntityUpdate) -> AnalyticsMasterEntity:
        entity = AnalyticsService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = AnalyticsService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: AnalyticsRelationalComponent1Create) -> AnalyticsRelationalComponent1:
        comp = AnalyticsRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent1]:
        query = db.query(AnalyticsRelationalComponent1)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: AnalyticsRelationalComponent2Create) -> AnalyticsRelationalComponent2:
        comp = AnalyticsRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent2]:
        query = db.query(AnalyticsRelationalComponent2)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: AnalyticsRelationalComponent3Create) -> AnalyticsRelationalComponent3:
        comp = AnalyticsRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent3]:
        query = db.query(AnalyticsRelationalComponent3)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: AnalyticsRelationalComponent4Create) -> AnalyticsRelationalComponent4:
        comp = AnalyticsRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent4]:
        query = db.query(AnalyticsRelationalComponent4)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: AnalyticsRelationalComponent5Create) -> AnalyticsRelationalComponent5:
        comp = AnalyticsRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent5]:
        query = db.query(AnalyticsRelationalComponent5)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: AnalyticsRelationalComponent6Create) -> AnalyticsRelationalComponent6:
        comp = AnalyticsRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent6]:
        query = db.query(AnalyticsRelationalComponent6)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: AnalyticsRelationalComponent7Create) -> AnalyticsRelationalComponent7:
        comp = AnalyticsRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent7]:
        query = db.query(AnalyticsRelationalComponent7)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: AnalyticsRelationalComponent8Create) -> AnalyticsRelationalComponent8:
        comp = AnalyticsRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent8]:
        query = db.query(AnalyticsRelationalComponent8)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: AnalyticsRelationalComponent9Create) -> AnalyticsRelationalComponent9:
        comp = AnalyticsRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent9]:
        query = db.query(AnalyticsRelationalComponent9)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: AnalyticsRelationalComponent10Create) -> AnalyticsRelationalComponent10:
        comp = AnalyticsRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent10]:
        query = db.query(AnalyticsRelationalComponent10)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: AnalyticsRelationalComponent11Create) -> AnalyticsRelationalComponent11:
        comp = AnalyticsRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent11]:
        query = db.query(AnalyticsRelationalComponent11)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: AnalyticsRelationalComponent12Create) -> AnalyticsRelationalComponent12:
        comp = AnalyticsRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent12]:
        query = db.query(AnalyticsRelationalComponent12)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: AnalyticsRelationalComponent13Create) -> AnalyticsRelationalComponent13:
        comp = AnalyticsRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent13]:
        query = db.query(AnalyticsRelationalComponent13)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: AnalyticsRelationalComponent14Create) -> AnalyticsRelationalComponent14:
        comp = AnalyticsRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent14]:
        query = db.query(AnalyticsRelationalComponent14)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: AnalyticsRelationalComponent15Create) -> AnalyticsRelationalComponent15:
        comp = AnalyticsRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent15]:
        query = db.query(AnalyticsRelationalComponent15)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: AnalyticsRelationalComponent16Create) -> AnalyticsRelationalComponent16:
        comp = AnalyticsRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent16]:
        query = db.query(AnalyticsRelationalComponent16)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: AnalyticsRelationalComponent17Create) -> AnalyticsRelationalComponent17:
        comp = AnalyticsRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent17]:
        query = db.query(AnalyticsRelationalComponent17)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: AnalyticsRelationalComponent18Create) -> AnalyticsRelationalComponent18:
        comp = AnalyticsRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent18]:
        query = db.query(AnalyticsRelationalComponent18)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: AnalyticsRelationalComponent19Create) -> AnalyticsRelationalComponent19:
        comp = AnalyticsRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent19]:
        query = db.query(AnalyticsRelationalComponent19)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: AnalyticsRelationalComponent20Create) -> AnalyticsRelationalComponent20:
        comp = AnalyticsRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent20]:
        query = db.query(AnalyticsRelationalComponent20)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: AnalyticsRelationalComponent21Create) -> AnalyticsRelationalComponent21:
        comp = AnalyticsRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent21]:
        query = db.query(AnalyticsRelationalComponent21)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: AnalyticsRelationalComponent22Create) -> AnalyticsRelationalComponent22:
        comp = AnalyticsRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent22]:
        query = db.query(AnalyticsRelationalComponent22)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: AnalyticsRelationalComponent23Create) -> AnalyticsRelationalComponent23:
        comp = AnalyticsRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent23]:
        query = db.query(AnalyticsRelationalComponent23)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: AnalyticsRelationalComponent24Create) -> AnalyticsRelationalComponent24:
        comp = AnalyticsRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent24]:
        query = db.query(AnalyticsRelationalComponent24)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: AnalyticsRelationalComponent25Create) -> AnalyticsRelationalComponent25:
        comp = AnalyticsRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[AnalyticsRelationalComponent25]:
        query = db.query(AnalyticsRelationalComponent25)
        if master_entity_id:
            query = query.filter(AnalyticsRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
