from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.booking_engine import (
    BookingEngineMasterEntity, BookingEngineStatus, BookingEnginePriority, BookingEngineCategoryType,
    BookingEngineRelationalComponent1 ,BookingEngineRelationalComponent2 ,BookingEngineRelationalComponent3 ,BookingEngineRelationalComponent4 ,BookingEngineRelationalComponent5 ,BookingEngineRelationalComponent6 ,BookingEngineRelationalComponent7 ,BookingEngineRelationalComponent8 ,BookingEngineRelationalComponent9 ,BookingEngineRelationalComponent10 ,BookingEngineRelationalComponent11 ,BookingEngineRelationalComponent12 ,BookingEngineRelationalComponent13 ,BookingEngineRelationalComponent14 ,BookingEngineRelationalComponent15 ,BookingEngineRelationalComponent16 ,BookingEngineRelationalComponent17 ,BookingEngineRelationalComponent18 ,BookingEngineRelationalComponent19 ,BookingEngineRelationalComponent20 ,BookingEngineRelationalComponent21 ,BookingEngineRelationalComponent22 ,BookingEngineRelationalComponent23 ,BookingEngineRelationalComponent24 ,BookingEngineRelationalComponent25
)
from app.schemas.booking_engine import (
    BookingEngineMasterEntityCreate, BookingEngineMasterEntityUpdate,
    BookingEngineRelationalComponent1Create ,BookingEngineRelationalComponent2Create ,BookingEngineRelationalComponent3Create ,BookingEngineRelationalComponent4Create ,BookingEngineRelationalComponent5Create ,BookingEngineRelationalComponent6Create ,BookingEngineRelationalComponent7Create ,BookingEngineRelationalComponent8Create ,BookingEngineRelationalComponent9Create ,BookingEngineRelationalComponent10Create ,BookingEngineRelationalComponent11Create ,BookingEngineRelationalComponent12Create ,BookingEngineRelationalComponent13Create ,BookingEngineRelationalComponent14Create ,BookingEngineRelationalComponent15Create ,BookingEngineRelationalComponent16Create ,BookingEngineRelationalComponent17Create ,BookingEngineRelationalComponent18Create ,BookingEngineRelationalComponent19Create ,BookingEngineRelationalComponent20Create ,BookingEngineRelationalComponent21Create ,BookingEngineRelationalComponent22Create ,BookingEngineRelationalComponent23Create ,BookingEngineRelationalComponent24Create ,BookingEngineRelationalComponent25Create
)

class BookingEngineService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: BookingEngineMasterEntityCreate) -> BookingEngineMasterEntity:
        existing = db.query(BookingEngineMasterEntity).filter(BookingEngineMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = BookingEngineMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> BookingEngineMasterEntity:
        entity = db.query(BookingEngineMasterEntity).filter(BookingEngineMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Advanced Booking Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[BookingEngineStatus] = None) -> List[BookingEngineMasterEntity]:
        query = db.query(BookingEngineMasterEntity)
        if status_filter:
            query = query.filter(BookingEngineMasterEntity.status == status_filter)
        return query.order_by(BookingEngineMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: BookingEngineMasterEntityUpdate) -> BookingEngineMasterEntity:
        entity = BookingEngineService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = BookingEngineService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: BookingEngineRelationalComponent1Create) -> BookingEngineRelationalComponent1:
        comp = BookingEngineRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent1]:
        query = db.query(BookingEngineRelationalComponent1)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: BookingEngineRelationalComponent2Create) -> BookingEngineRelationalComponent2:
        comp = BookingEngineRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent2]:
        query = db.query(BookingEngineRelationalComponent2)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: BookingEngineRelationalComponent3Create) -> BookingEngineRelationalComponent3:
        comp = BookingEngineRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent3]:
        query = db.query(BookingEngineRelationalComponent3)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: BookingEngineRelationalComponent4Create) -> BookingEngineRelationalComponent4:
        comp = BookingEngineRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent4]:
        query = db.query(BookingEngineRelationalComponent4)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: BookingEngineRelationalComponent5Create) -> BookingEngineRelationalComponent5:
        comp = BookingEngineRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent5]:
        query = db.query(BookingEngineRelationalComponent5)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: BookingEngineRelationalComponent6Create) -> BookingEngineRelationalComponent6:
        comp = BookingEngineRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent6]:
        query = db.query(BookingEngineRelationalComponent6)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: BookingEngineRelationalComponent7Create) -> BookingEngineRelationalComponent7:
        comp = BookingEngineRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent7]:
        query = db.query(BookingEngineRelationalComponent7)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: BookingEngineRelationalComponent8Create) -> BookingEngineRelationalComponent8:
        comp = BookingEngineRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent8]:
        query = db.query(BookingEngineRelationalComponent8)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: BookingEngineRelationalComponent9Create) -> BookingEngineRelationalComponent9:
        comp = BookingEngineRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent9]:
        query = db.query(BookingEngineRelationalComponent9)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: BookingEngineRelationalComponent10Create) -> BookingEngineRelationalComponent10:
        comp = BookingEngineRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent10]:
        query = db.query(BookingEngineRelationalComponent10)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: BookingEngineRelationalComponent11Create) -> BookingEngineRelationalComponent11:
        comp = BookingEngineRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent11]:
        query = db.query(BookingEngineRelationalComponent11)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: BookingEngineRelationalComponent12Create) -> BookingEngineRelationalComponent12:
        comp = BookingEngineRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent12]:
        query = db.query(BookingEngineRelationalComponent12)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: BookingEngineRelationalComponent13Create) -> BookingEngineRelationalComponent13:
        comp = BookingEngineRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent13]:
        query = db.query(BookingEngineRelationalComponent13)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: BookingEngineRelationalComponent14Create) -> BookingEngineRelationalComponent14:
        comp = BookingEngineRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent14]:
        query = db.query(BookingEngineRelationalComponent14)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: BookingEngineRelationalComponent15Create) -> BookingEngineRelationalComponent15:
        comp = BookingEngineRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent15]:
        query = db.query(BookingEngineRelationalComponent15)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: BookingEngineRelationalComponent16Create) -> BookingEngineRelationalComponent16:
        comp = BookingEngineRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent16]:
        query = db.query(BookingEngineRelationalComponent16)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: BookingEngineRelationalComponent17Create) -> BookingEngineRelationalComponent17:
        comp = BookingEngineRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent17]:
        query = db.query(BookingEngineRelationalComponent17)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: BookingEngineRelationalComponent18Create) -> BookingEngineRelationalComponent18:
        comp = BookingEngineRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent18]:
        query = db.query(BookingEngineRelationalComponent18)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: BookingEngineRelationalComponent19Create) -> BookingEngineRelationalComponent19:
        comp = BookingEngineRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent19]:
        query = db.query(BookingEngineRelationalComponent19)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: BookingEngineRelationalComponent20Create) -> BookingEngineRelationalComponent20:
        comp = BookingEngineRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent20]:
        query = db.query(BookingEngineRelationalComponent20)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: BookingEngineRelationalComponent21Create) -> BookingEngineRelationalComponent21:
        comp = BookingEngineRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent21]:
        query = db.query(BookingEngineRelationalComponent21)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: BookingEngineRelationalComponent22Create) -> BookingEngineRelationalComponent22:
        comp = BookingEngineRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent22]:
        query = db.query(BookingEngineRelationalComponent22)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: BookingEngineRelationalComponent23Create) -> BookingEngineRelationalComponent23:
        comp = BookingEngineRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent23]:
        query = db.query(BookingEngineRelationalComponent23)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: BookingEngineRelationalComponent24Create) -> BookingEngineRelationalComponent24:
        comp = BookingEngineRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent24]:
        query = db.query(BookingEngineRelationalComponent24)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: BookingEngineRelationalComponent25Create) -> BookingEngineRelationalComponent25:
        comp = BookingEngineRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent25]:
        query = db.query(BookingEngineRelationalComponent25)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: BookingEngineRelationalComponent26Create) -> BookingEngineRelationalComponent26:
        comp = BookingEngineRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent26]:
        query = db.query(BookingEngineRelationalComponent26)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: BookingEngineRelationalComponent27Create) -> BookingEngineRelationalComponent27:
        comp = BookingEngineRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent27]:
        query = db.query(BookingEngineRelationalComponent27)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: BookingEngineRelationalComponent28Create) -> BookingEngineRelationalComponent28:
        comp = BookingEngineRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent28]:
        query = db.query(BookingEngineRelationalComponent28)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: BookingEngineRelationalComponent29Create) -> BookingEngineRelationalComponent29:
        comp = BookingEngineRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent29]:
        query = db.query(BookingEngineRelationalComponent29)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: BookingEngineRelationalComponent30Create) -> BookingEngineRelationalComponent30:
        comp = BookingEngineRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[BookingEngineRelationalComponent30]:
        query = db.query(BookingEngineRelationalComponent30)
        if master_entity_id:
            query = query.filter(BookingEngineRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
