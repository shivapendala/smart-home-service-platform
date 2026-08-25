from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.customer_feedback import (
    CustomerFeedbackMasterEntity, CustomerFeedbackStatus,
    CustomerFeedbackRelationalComponent1 ,CustomerFeedbackRelationalComponent2 ,CustomerFeedbackRelationalComponent3 ,CustomerFeedbackRelationalComponent4 ,CustomerFeedbackRelationalComponent5 ,CustomerFeedbackRelationalComponent6 ,CustomerFeedbackRelationalComponent7 ,CustomerFeedbackRelationalComponent8 ,CustomerFeedbackRelationalComponent9 ,CustomerFeedbackRelationalComponent10 ,CustomerFeedbackRelationalComponent11 ,CustomerFeedbackRelationalComponent12 ,CustomerFeedbackRelationalComponent13 ,CustomerFeedbackRelationalComponent14 ,CustomerFeedbackRelationalComponent15 ,CustomerFeedbackRelationalComponent16 ,CustomerFeedbackRelationalComponent17 ,CustomerFeedbackRelationalComponent18 ,CustomerFeedbackRelationalComponent19 ,CustomerFeedbackRelationalComponent20 ,CustomerFeedbackRelationalComponent21 ,CustomerFeedbackRelationalComponent22 ,CustomerFeedbackRelationalComponent23 ,CustomerFeedbackRelationalComponent24 ,CustomerFeedbackRelationalComponent25
)
from app.schemas.customer_feedback import (
    CustomerFeedbackMasterEntityCreate, CustomerFeedbackMasterEntityUpdate,
    CustomerFeedbackRelationalComponent1Create ,CustomerFeedbackRelationalComponent2Create ,CustomerFeedbackRelationalComponent3Create ,CustomerFeedbackRelationalComponent4Create ,CustomerFeedbackRelationalComponent5Create ,CustomerFeedbackRelationalComponent6Create ,CustomerFeedbackRelationalComponent7Create ,CustomerFeedbackRelationalComponent8Create ,CustomerFeedbackRelationalComponent9Create ,CustomerFeedbackRelationalComponent10Create ,CustomerFeedbackRelationalComponent11Create ,CustomerFeedbackRelationalComponent12Create ,CustomerFeedbackRelationalComponent13Create ,CustomerFeedbackRelationalComponent14Create ,CustomerFeedbackRelationalComponent15Create ,CustomerFeedbackRelationalComponent16Create ,CustomerFeedbackRelationalComponent17Create ,CustomerFeedbackRelationalComponent18Create ,CustomerFeedbackRelationalComponent19Create ,CustomerFeedbackRelationalComponent20Create ,CustomerFeedbackRelationalComponent21Create ,CustomerFeedbackRelationalComponent22Create ,CustomerFeedbackRelationalComponent23Create ,CustomerFeedbackRelationalComponent24Create ,CustomerFeedbackRelationalComponent25Create
)

class CustomerFeedbackService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: CustomerFeedbackMasterEntityCreate) -> CustomerFeedbackMasterEntity:
        existing = db.query(CustomerFeedbackMasterEntity).filter(CustomerFeedbackMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = CustomerFeedbackMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> CustomerFeedbackMasterEntity:
        entity = db.query(CustomerFeedbackMasterEntity).filter(CustomerFeedbackMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer Feedback & NPS Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[CustomerFeedbackStatus] = None) -> List[CustomerFeedbackMasterEntity]:
        query = db.query(CustomerFeedbackMasterEntity)
        if status_filter:
            query = query.filter(CustomerFeedbackMasterEntity.status == status_filter)
        return query.order_by(CustomerFeedbackMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: CustomerFeedbackMasterEntityUpdate) -> CustomerFeedbackMasterEntity:
        entity = CustomerFeedbackService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = CustomerFeedbackService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: CustomerFeedbackRelationalComponent1Create) -> CustomerFeedbackRelationalComponent1:
        comp = CustomerFeedbackRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent1]:
        query = db.query(CustomerFeedbackRelationalComponent1)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: CustomerFeedbackRelationalComponent2Create) -> CustomerFeedbackRelationalComponent2:
        comp = CustomerFeedbackRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent2]:
        query = db.query(CustomerFeedbackRelationalComponent2)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: CustomerFeedbackRelationalComponent3Create) -> CustomerFeedbackRelationalComponent3:
        comp = CustomerFeedbackRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent3]:
        query = db.query(CustomerFeedbackRelationalComponent3)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: CustomerFeedbackRelationalComponent4Create) -> CustomerFeedbackRelationalComponent4:
        comp = CustomerFeedbackRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent4]:
        query = db.query(CustomerFeedbackRelationalComponent4)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: CustomerFeedbackRelationalComponent5Create) -> CustomerFeedbackRelationalComponent5:
        comp = CustomerFeedbackRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent5]:
        query = db.query(CustomerFeedbackRelationalComponent5)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: CustomerFeedbackRelationalComponent6Create) -> CustomerFeedbackRelationalComponent6:
        comp = CustomerFeedbackRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent6]:
        query = db.query(CustomerFeedbackRelationalComponent6)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: CustomerFeedbackRelationalComponent7Create) -> CustomerFeedbackRelationalComponent7:
        comp = CustomerFeedbackRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent7]:
        query = db.query(CustomerFeedbackRelationalComponent7)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: CustomerFeedbackRelationalComponent8Create) -> CustomerFeedbackRelationalComponent8:
        comp = CustomerFeedbackRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent8]:
        query = db.query(CustomerFeedbackRelationalComponent8)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: CustomerFeedbackRelationalComponent9Create) -> CustomerFeedbackRelationalComponent9:
        comp = CustomerFeedbackRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent9]:
        query = db.query(CustomerFeedbackRelationalComponent9)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: CustomerFeedbackRelationalComponent10Create) -> CustomerFeedbackRelationalComponent10:
        comp = CustomerFeedbackRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent10]:
        query = db.query(CustomerFeedbackRelationalComponent10)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: CustomerFeedbackRelationalComponent11Create) -> CustomerFeedbackRelationalComponent11:
        comp = CustomerFeedbackRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent11]:
        query = db.query(CustomerFeedbackRelationalComponent11)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: CustomerFeedbackRelationalComponent12Create) -> CustomerFeedbackRelationalComponent12:
        comp = CustomerFeedbackRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent12]:
        query = db.query(CustomerFeedbackRelationalComponent12)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: CustomerFeedbackRelationalComponent13Create) -> CustomerFeedbackRelationalComponent13:
        comp = CustomerFeedbackRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent13]:
        query = db.query(CustomerFeedbackRelationalComponent13)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: CustomerFeedbackRelationalComponent14Create) -> CustomerFeedbackRelationalComponent14:
        comp = CustomerFeedbackRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent14]:
        query = db.query(CustomerFeedbackRelationalComponent14)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: CustomerFeedbackRelationalComponent15Create) -> CustomerFeedbackRelationalComponent15:
        comp = CustomerFeedbackRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent15]:
        query = db.query(CustomerFeedbackRelationalComponent15)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: CustomerFeedbackRelationalComponent16Create) -> CustomerFeedbackRelationalComponent16:
        comp = CustomerFeedbackRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent16]:
        query = db.query(CustomerFeedbackRelationalComponent16)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: CustomerFeedbackRelationalComponent17Create) -> CustomerFeedbackRelationalComponent17:
        comp = CustomerFeedbackRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent17]:
        query = db.query(CustomerFeedbackRelationalComponent17)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: CustomerFeedbackRelationalComponent18Create) -> CustomerFeedbackRelationalComponent18:
        comp = CustomerFeedbackRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent18]:
        query = db.query(CustomerFeedbackRelationalComponent18)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: CustomerFeedbackRelationalComponent19Create) -> CustomerFeedbackRelationalComponent19:
        comp = CustomerFeedbackRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent19]:
        query = db.query(CustomerFeedbackRelationalComponent19)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: CustomerFeedbackRelationalComponent20Create) -> CustomerFeedbackRelationalComponent20:
        comp = CustomerFeedbackRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent20]:
        query = db.query(CustomerFeedbackRelationalComponent20)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: CustomerFeedbackRelationalComponent21Create) -> CustomerFeedbackRelationalComponent21:
        comp = CustomerFeedbackRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent21]:
        query = db.query(CustomerFeedbackRelationalComponent21)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: CustomerFeedbackRelationalComponent22Create) -> CustomerFeedbackRelationalComponent22:
        comp = CustomerFeedbackRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent22]:
        query = db.query(CustomerFeedbackRelationalComponent22)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: CustomerFeedbackRelationalComponent23Create) -> CustomerFeedbackRelationalComponent23:
        comp = CustomerFeedbackRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent23]:
        query = db.query(CustomerFeedbackRelationalComponent23)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: CustomerFeedbackRelationalComponent24Create) -> CustomerFeedbackRelationalComponent24:
        comp = CustomerFeedbackRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent24]:
        query = db.query(CustomerFeedbackRelationalComponent24)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: CustomerFeedbackRelationalComponent25Create) -> CustomerFeedbackRelationalComponent25:
        comp = CustomerFeedbackRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerFeedbackRelationalComponent25]:
        query = db.query(CustomerFeedbackRelationalComponent25)
        if master_entity_id:
            query = query.filter(CustomerFeedbackRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
