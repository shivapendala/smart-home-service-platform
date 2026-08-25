from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.payments_billing import (
    PaymentsBillingMasterEntity, PaymentsBillingStatus, PaymentsBillingPriority, PaymentsBillingCategoryType,
    PaymentsBillingRelationalComponent1 ,PaymentsBillingRelationalComponent2 ,PaymentsBillingRelationalComponent3 ,PaymentsBillingRelationalComponent4 ,PaymentsBillingRelationalComponent5 ,PaymentsBillingRelationalComponent6 ,PaymentsBillingRelationalComponent7 ,PaymentsBillingRelationalComponent8 ,PaymentsBillingRelationalComponent9 ,PaymentsBillingRelationalComponent10 ,PaymentsBillingRelationalComponent11 ,PaymentsBillingRelationalComponent12 ,PaymentsBillingRelationalComponent13 ,PaymentsBillingRelationalComponent14 ,PaymentsBillingRelationalComponent15 ,PaymentsBillingRelationalComponent16 ,PaymentsBillingRelationalComponent17 ,PaymentsBillingRelationalComponent18 ,PaymentsBillingRelationalComponent19 ,PaymentsBillingRelationalComponent20 ,PaymentsBillingRelationalComponent21 ,PaymentsBillingRelationalComponent22 ,PaymentsBillingRelationalComponent23 ,PaymentsBillingRelationalComponent24 ,PaymentsBillingRelationalComponent25
)
from app.schemas.payments_billing import (
    PaymentsBillingMasterEntityCreate, PaymentsBillingMasterEntityUpdate,
    PaymentsBillingRelationalComponent1Create ,PaymentsBillingRelationalComponent2Create ,PaymentsBillingRelationalComponent3Create ,PaymentsBillingRelationalComponent4Create ,PaymentsBillingRelationalComponent5Create ,PaymentsBillingRelationalComponent6Create ,PaymentsBillingRelationalComponent7Create ,PaymentsBillingRelationalComponent8Create ,PaymentsBillingRelationalComponent9Create ,PaymentsBillingRelationalComponent10Create ,PaymentsBillingRelationalComponent11Create ,PaymentsBillingRelationalComponent12Create ,PaymentsBillingRelationalComponent13Create ,PaymentsBillingRelationalComponent14Create ,PaymentsBillingRelationalComponent15Create ,PaymentsBillingRelationalComponent16Create ,PaymentsBillingRelationalComponent17Create ,PaymentsBillingRelationalComponent18Create ,PaymentsBillingRelationalComponent19Create ,PaymentsBillingRelationalComponent20Create ,PaymentsBillingRelationalComponent21Create ,PaymentsBillingRelationalComponent22Create ,PaymentsBillingRelationalComponent23Create ,PaymentsBillingRelationalComponent24Create ,PaymentsBillingRelationalComponent25Create
)

class PaymentsBillingService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: PaymentsBillingMasterEntityCreate) -> PaymentsBillingMasterEntity:
        existing = db.query(PaymentsBillingMasterEntity).filter(PaymentsBillingMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = PaymentsBillingMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> PaymentsBillingMasterEntity:
        entity = db.query(PaymentsBillingMasterEntity).filter(PaymentsBillingMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payments & Billing System Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[PaymentsBillingStatus] = None) -> List[PaymentsBillingMasterEntity]:
        query = db.query(PaymentsBillingMasterEntity)
        if status_filter:
            query = query.filter(PaymentsBillingMasterEntity.status == status_filter)
        return query.order_by(PaymentsBillingMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: PaymentsBillingMasterEntityUpdate) -> PaymentsBillingMasterEntity:
        entity = PaymentsBillingService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = PaymentsBillingService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: PaymentsBillingRelationalComponent1Create) -> PaymentsBillingRelationalComponent1:
        comp = PaymentsBillingRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent1]:
        query = db.query(PaymentsBillingRelationalComponent1)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: PaymentsBillingRelationalComponent2Create) -> PaymentsBillingRelationalComponent2:
        comp = PaymentsBillingRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent2]:
        query = db.query(PaymentsBillingRelationalComponent2)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: PaymentsBillingRelationalComponent3Create) -> PaymentsBillingRelationalComponent3:
        comp = PaymentsBillingRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent3]:
        query = db.query(PaymentsBillingRelationalComponent3)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: PaymentsBillingRelationalComponent4Create) -> PaymentsBillingRelationalComponent4:
        comp = PaymentsBillingRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent4]:
        query = db.query(PaymentsBillingRelationalComponent4)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: PaymentsBillingRelationalComponent5Create) -> PaymentsBillingRelationalComponent5:
        comp = PaymentsBillingRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent5]:
        query = db.query(PaymentsBillingRelationalComponent5)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: PaymentsBillingRelationalComponent6Create) -> PaymentsBillingRelationalComponent6:
        comp = PaymentsBillingRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent6]:
        query = db.query(PaymentsBillingRelationalComponent6)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: PaymentsBillingRelationalComponent7Create) -> PaymentsBillingRelationalComponent7:
        comp = PaymentsBillingRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent7]:
        query = db.query(PaymentsBillingRelationalComponent7)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: PaymentsBillingRelationalComponent8Create) -> PaymentsBillingRelationalComponent8:
        comp = PaymentsBillingRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent8]:
        query = db.query(PaymentsBillingRelationalComponent8)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: PaymentsBillingRelationalComponent9Create) -> PaymentsBillingRelationalComponent9:
        comp = PaymentsBillingRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent9]:
        query = db.query(PaymentsBillingRelationalComponent9)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: PaymentsBillingRelationalComponent10Create) -> PaymentsBillingRelationalComponent10:
        comp = PaymentsBillingRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent10]:
        query = db.query(PaymentsBillingRelationalComponent10)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: PaymentsBillingRelationalComponent11Create) -> PaymentsBillingRelationalComponent11:
        comp = PaymentsBillingRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent11]:
        query = db.query(PaymentsBillingRelationalComponent11)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: PaymentsBillingRelationalComponent12Create) -> PaymentsBillingRelationalComponent12:
        comp = PaymentsBillingRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent12]:
        query = db.query(PaymentsBillingRelationalComponent12)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: PaymentsBillingRelationalComponent13Create) -> PaymentsBillingRelationalComponent13:
        comp = PaymentsBillingRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent13]:
        query = db.query(PaymentsBillingRelationalComponent13)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: PaymentsBillingRelationalComponent14Create) -> PaymentsBillingRelationalComponent14:
        comp = PaymentsBillingRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent14]:
        query = db.query(PaymentsBillingRelationalComponent14)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: PaymentsBillingRelationalComponent15Create) -> PaymentsBillingRelationalComponent15:
        comp = PaymentsBillingRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent15]:
        query = db.query(PaymentsBillingRelationalComponent15)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: PaymentsBillingRelationalComponent16Create) -> PaymentsBillingRelationalComponent16:
        comp = PaymentsBillingRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent16]:
        query = db.query(PaymentsBillingRelationalComponent16)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: PaymentsBillingRelationalComponent17Create) -> PaymentsBillingRelationalComponent17:
        comp = PaymentsBillingRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent17]:
        query = db.query(PaymentsBillingRelationalComponent17)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: PaymentsBillingRelationalComponent18Create) -> PaymentsBillingRelationalComponent18:
        comp = PaymentsBillingRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent18]:
        query = db.query(PaymentsBillingRelationalComponent18)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: PaymentsBillingRelationalComponent19Create) -> PaymentsBillingRelationalComponent19:
        comp = PaymentsBillingRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent19]:
        query = db.query(PaymentsBillingRelationalComponent19)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: PaymentsBillingRelationalComponent20Create) -> PaymentsBillingRelationalComponent20:
        comp = PaymentsBillingRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent20]:
        query = db.query(PaymentsBillingRelationalComponent20)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: PaymentsBillingRelationalComponent21Create) -> PaymentsBillingRelationalComponent21:
        comp = PaymentsBillingRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent21]:
        query = db.query(PaymentsBillingRelationalComponent21)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: PaymentsBillingRelationalComponent22Create) -> PaymentsBillingRelationalComponent22:
        comp = PaymentsBillingRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent22]:
        query = db.query(PaymentsBillingRelationalComponent22)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: PaymentsBillingRelationalComponent23Create) -> PaymentsBillingRelationalComponent23:
        comp = PaymentsBillingRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent23]:
        query = db.query(PaymentsBillingRelationalComponent23)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: PaymentsBillingRelationalComponent24Create) -> PaymentsBillingRelationalComponent24:
        comp = PaymentsBillingRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent24]:
        query = db.query(PaymentsBillingRelationalComponent24)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: PaymentsBillingRelationalComponent25Create) -> PaymentsBillingRelationalComponent25:
        comp = PaymentsBillingRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[PaymentsBillingRelationalComponent25]:
        query = db.query(PaymentsBillingRelationalComponent25)
        if master_entity_id:
            query = query.filter(PaymentsBillingRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
