from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.booking_fulfillment import (
    BookingFulfillmentMasterEntity, BookingFulfillmentStatus,
    BookingFulfillmentRelationalComponent1 ,BookingFulfillmentRelationalComponent2 ,BookingFulfillmentRelationalComponent3 ,BookingFulfillmentRelationalComponent4 ,BookingFulfillmentRelationalComponent5 ,BookingFulfillmentRelationalComponent6 ,BookingFulfillmentRelationalComponent7 ,BookingFulfillmentRelationalComponent8 ,BookingFulfillmentRelationalComponent9 ,BookingFulfillmentRelationalComponent10 ,BookingFulfillmentRelationalComponent11 ,BookingFulfillmentRelationalComponent12 ,BookingFulfillmentRelationalComponent13 ,BookingFulfillmentRelationalComponent14 ,BookingFulfillmentRelationalComponent15 ,BookingFulfillmentRelationalComponent16 ,BookingFulfillmentRelationalComponent17 ,BookingFulfillmentRelationalComponent18 ,BookingFulfillmentRelationalComponent19 ,BookingFulfillmentRelationalComponent20 ,BookingFulfillmentRelationalComponent21 ,BookingFulfillmentRelationalComponent22 ,BookingFulfillmentRelationalComponent23 ,BookingFulfillmentRelationalComponent24 ,BookingFulfillmentRelationalComponent25
)
from app.schemas.booking_fulfillment import (
    BookingFulfillmentMasterEntityCreate, BookingFulfillmentMasterEntityUpdate,
    BookingFulfillmentRelationalComponent1Create ,BookingFulfillmentRelationalComponent2Create ,BookingFulfillmentRelationalComponent3Create ,BookingFulfillmentRelationalComponent4Create ,BookingFulfillmentRelationalComponent5Create ,BookingFulfillmentRelationalComponent6Create ,BookingFulfillmentRelationalComponent7Create ,BookingFulfillmentRelationalComponent8Create ,BookingFulfillmentRelationalComponent9Create ,BookingFulfillmentRelationalComponent10Create ,BookingFulfillmentRelationalComponent11Create ,BookingFulfillmentRelationalComponent12Create ,BookingFulfillmentRelationalComponent13Create ,BookingFulfillmentRelationalComponent14Create ,BookingFulfillmentRelationalComponent15Create ,BookingFulfillmentRelationalComponent16Create ,BookingFulfillmentRelationalComponent17Create ,BookingFulfillmentRelationalComponent18Create ,BookingFulfillmentRelationalComponent19Create ,BookingFulfillmentRelationalComponent20Create ,BookingFulfillmentRelationalComponent21Create ,BookingFulfillmentRelationalComponent22Create ,BookingFulfillmentRelationalComponent23Create ,BookingFulfillmentRelationalComponent24Create ,BookingFulfillmentRelationalComponent25Create
)

class BookingFulfillmentService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: BookingFulfillmentMasterEntityCreate) -> BookingFulfillmentMasterEntity:
        existing = db.query(BookingFulfillmentMasterEntity).filter(BookingFulfillmentMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = BookingFulfillmentMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> BookingFulfillmentMasterEntity:
        entity = db.query(BookingFulfillmentMasterEntity).filter(BookingFulfillmentMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking Fulfillment Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[BookingFulfillmentStatus] = None) -> List[BookingFulfillmentMasterEntity]:
        query = db.query(BookingFulfillmentMasterEntity)
        if status_filter:
            query = query.filter(BookingFulfillmentMasterEntity.status == status_filter)
        return query.order_by(BookingFulfillmentMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: BookingFulfillmentMasterEntityUpdate) -> BookingFulfillmentMasterEntity:
        entity = BookingFulfillmentService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = BookingFulfillmentService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: BookingFulfillmentRelationalComponent1Create) -> BookingFulfillmentRelationalComponent1:
        comp = BookingFulfillmentRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent1]:
        query = db.query(BookingFulfillmentRelationalComponent1)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: BookingFulfillmentRelationalComponent2Create) -> BookingFulfillmentRelationalComponent2:
        comp = BookingFulfillmentRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent2]:
        query = db.query(BookingFulfillmentRelationalComponent2)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: BookingFulfillmentRelationalComponent3Create) -> BookingFulfillmentRelationalComponent3:
        comp = BookingFulfillmentRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent3]:
        query = db.query(BookingFulfillmentRelationalComponent3)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: BookingFulfillmentRelationalComponent4Create) -> BookingFulfillmentRelationalComponent4:
        comp = BookingFulfillmentRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent4]:
        query = db.query(BookingFulfillmentRelationalComponent4)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: BookingFulfillmentRelationalComponent5Create) -> BookingFulfillmentRelationalComponent5:
        comp = BookingFulfillmentRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent5]:
        query = db.query(BookingFulfillmentRelationalComponent5)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: BookingFulfillmentRelationalComponent6Create) -> BookingFulfillmentRelationalComponent6:
        comp = BookingFulfillmentRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent6]:
        query = db.query(BookingFulfillmentRelationalComponent6)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: BookingFulfillmentRelationalComponent7Create) -> BookingFulfillmentRelationalComponent7:
        comp = BookingFulfillmentRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent7]:
        query = db.query(BookingFulfillmentRelationalComponent7)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: BookingFulfillmentRelationalComponent8Create) -> BookingFulfillmentRelationalComponent8:
        comp = BookingFulfillmentRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent8]:
        query = db.query(BookingFulfillmentRelationalComponent8)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: BookingFulfillmentRelationalComponent9Create) -> BookingFulfillmentRelationalComponent9:
        comp = BookingFulfillmentRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent9]:
        query = db.query(BookingFulfillmentRelationalComponent9)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: BookingFulfillmentRelationalComponent10Create) -> BookingFulfillmentRelationalComponent10:
        comp = BookingFulfillmentRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent10]:
        query = db.query(BookingFulfillmentRelationalComponent10)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: BookingFulfillmentRelationalComponent11Create) -> BookingFulfillmentRelationalComponent11:
        comp = BookingFulfillmentRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent11]:
        query = db.query(BookingFulfillmentRelationalComponent11)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: BookingFulfillmentRelationalComponent12Create) -> BookingFulfillmentRelationalComponent12:
        comp = BookingFulfillmentRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent12]:
        query = db.query(BookingFulfillmentRelationalComponent12)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: BookingFulfillmentRelationalComponent13Create) -> BookingFulfillmentRelationalComponent13:
        comp = BookingFulfillmentRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent13]:
        query = db.query(BookingFulfillmentRelationalComponent13)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: BookingFulfillmentRelationalComponent14Create) -> BookingFulfillmentRelationalComponent14:
        comp = BookingFulfillmentRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent14]:
        query = db.query(BookingFulfillmentRelationalComponent14)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: BookingFulfillmentRelationalComponent15Create) -> BookingFulfillmentRelationalComponent15:
        comp = BookingFulfillmentRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent15]:
        query = db.query(BookingFulfillmentRelationalComponent15)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: BookingFulfillmentRelationalComponent16Create) -> BookingFulfillmentRelationalComponent16:
        comp = BookingFulfillmentRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent16]:
        query = db.query(BookingFulfillmentRelationalComponent16)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: BookingFulfillmentRelationalComponent17Create) -> BookingFulfillmentRelationalComponent17:
        comp = BookingFulfillmentRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent17]:
        query = db.query(BookingFulfillmentRelationalComponent17)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: BookingFulfillmentRelationalComponent18Create) -> BookingFulfillmentRelationalComponent18:
        comp = BookingFulfillmentRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent18]:
        query = db.query(BookingFulfillmentRelationalComponent18)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: BookingFulfillmentRelationalComponent19Create) -> BookingFulfillmentRelationalComponent19:
        comp = BookingFulfillmentRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent19]:
        query = db.query(BookingFulfillmentRelationalComponent19)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: BookingFulfillmentRelationalComponent20Create) -> BookingFulfillmentRelationalComponent20:
        comp = BookingFulfillmentRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent20]:
        query = db.query(BookingFulfillmentRelationalComponent20)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: BookingFulfillmentRelationalComponent21Create) -> BookingFulfillmentRelationalComponent21:
        comp = BookingFulfillmentRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent21]:
        query = db.query(BookingFulfillmentRelationalComponent21)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: BookingFulfillmentRelationalComponent22Create) -> BookingFulfillmentRelationalComponent22:
        comp = BookingFulfillmentRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent22]:
        query = db.query(BookingFulfillmentRelationalComponent22)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: BookingFulfillmentRelationalComponent23Create) -> BookingFulfillmentRelationalComponent23:
        comp = BookingFulfillmentRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent23]:
        query = db.query(BookingFulfillmentRelationalComponent23)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: BookingFulfillmentRelationalComponent24Create) -> BookingFulfillmentRelationalComponent24:
        comp = BookingFulfillmentRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent24]:
        query = db.query(BookingFulfillmentRelationalComponent24)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: BookingFulfillmentRelationalComponent25Create) -> BookingFulfillmentRelationalComponent25:
        comp = BookingFulfillmentRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent25]:
        query = db.query(BookingFulfillmentRelationalComponent25)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: BookingFulfillmentRelationalComponent26Create) -> BookingFulfillmentRelationalComponent26:
        comp = BookingFulfillmentRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent26]:
        query = db.query(BookingFulfillmentRelationalComponent26)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: BookingFulfillmentRelationalComponent27Create) -> BookingFulfillmentRelationalComponent27:
        comp = BookingFulfillmentRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent27]:
        query = db.query(BookingFulfillmentRelationalComponent27)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: BookingFulfillmentRelationalComponent28Create) -> BookingFulfillmentRelationalComponent28:
        comp = BookingFulfillmentRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent28]:
        query = db.query(BookingFulfillmentRelationalComponent28)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: BookingFulfillmentRelationalComponent29Create) -> BookingFulfillmentRelationalComponent29:
        comp = BookingFulfillmentRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent29]:
        query = db.query(BookingFulfillmentRelationalComponent29)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: BookingFulfillmentRelationalComponent30Create) -> BookingFulfillmentRelationalComponent30:
        comp = BookingFulfillmentRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[BookingFulfillmentRelationalComponent30]:
        query = db.query(BookingFulfillmentRelationalComponent30)
        if master_entity_id:
            query = query.filter(BookingFulfillmentRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
