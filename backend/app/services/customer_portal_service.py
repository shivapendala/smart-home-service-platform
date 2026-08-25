from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.customer_portal import (
    CustomerPortalMasterEntity, CustomerPortalStatus, CustomerPortalPriority, CustomerPortalCategoryType,
    CustomerPortalRelationalComponent1 ,CustomerPortalRelationalComponent2 ,CustomerPortalRelationalComponent3 ,CustomerPortalRelationalComponent4 ,CustomerPortalRelationalComponent5 ,CustomerPortalRelationalComponent6 ,CustomerPortalRelationalComponent7 ,CustomerPortalRelationalComponent8 ,CustomerPortalRelationalComponent9 ,CustomerPortalRelationalComponent10 ,CustomerPortalRelationalComponent11 ,CustomerPortalRelationalComponent12 ,CustomerPortalRelationalComponent13 ,CustomerPortalRelationalComponent14 ,CustomerPortalRelationalComponent15 ,CustomerPortalRelationalComponent16 ,CustomerPortalRelationalComponent17 ,CustomerPortalRelationalComponent18 ,CustomerPortalRelationalComponent19 ,CustomerPortalRelationalComponent20 ,CustomerPortalRelationalComponent21 ,CustomerPortalRelationalComponent22 ,CustomerPortalRelationalComponent23 ,CustomerPortalRelationalComponent24 ,CustomerPortalRelationalComponent25
)
from app.schemas.customer_portal import (
    CustomerPortalMasterEntityCreate, CustomerPortalMasterEntityUpdate,
    CustomerPortalRelationalComponent1Create ,CustomerPortalRelationalComponent2Create ,CustomerPortalRelationalComponent3Create ,CustomerPortalRelationalComponent4Create ,CustomerPortalRelationalComponent5Create ,CustomerPortalRelationalComponent6Create ,CustomerPortalRelationalComponent7Create ,CustomerPortalRelationalComponent8Create ,CustomerPortalRelationalComponent9Create ,CustomerPortalRelationalComponent10Create ,CustomerPortalRelationalComponent11Create ,CustomerPortalRelationalComponent12Create ,CustomerPortalRelationalComponent13Create ,CustomerPortalRelationalComponent14Create ,CustomerPortalRelationalComponent15Create ,CustomerPortalRelationalComponent16Create ,CustomerPortalRelationalComponent17Create ,CustomerPortalRelationalComponent18Create ,CustomerPortalRelationalComponent19Create ,CustomerPortalRelationalComponent20Create ,CustomerPortalRelationalComponent21Create ,CustomerPortalRelationalComponent22Create ,CustomerPortalRelationalComponent23Create ,CustomerPortalRelationalComponent24Create ,CustomerPortalRelationalComponent25Create
)

class CustomerPortalService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: CustomerPortalMasterEntityCreate) -> CustomerPortalMasterEntity:
        existing = db.query(CustomerPortalMasterEntity).filter(CustomerPortalMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = CustomerPortalMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> CustomerPortalMasterEntity:
        entity = db.query(CustomerPortalMasterEntity).filter(CustomerPortalMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer Portal Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[CustomerPortalStatus] = None) -> List[CustomerPortalMasterEntity]:
        query = db.query(CustomerPortalMasterEntity)
        if status_filter:
            query = query.filter(CustomerPortalMasterEntity.status == status_filter)
        return query.order_by(CustomerPortalMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: CustomerPortalMasterEntityUpdate) -> CustomerPortalMasterEntity:
        entity = CustomerPortalService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = CustomerPortalService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: CustomerPortalRelationalComponent1Create) -> CustomerPortalRelationalComponent1:
        comp = CustomerPortalRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent1]:
        query = db.query(CustomerPortalRelationalComponent1)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: CustomerPortalRelationalComponent2Create) -> CustomerPortalRelationalComponent2:
        comp = CustomerPortalRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent2]:
        query = db.query(CustomerPortalRelationalComponent2)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: CustomerPortalRelationalComponent3Create) -> CustomerPortalRelationalComponent3:
        comp = CustomerPortalRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent3]:
        query = db.query(CustomerPortalRelationalComponent3)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: CustomerPortalRelationalComponent4Create) -> CustomerPortalRelationalComponent4:
        comp = CustomerPortalRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent4]:
        query = db.query(CustomerPortalRelationalComponent4)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: CustomerPortalRelationalComponent5Create) -> CustomerPortalRelationalComponent5:
        comp = CustomerPortalRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent5]:
        query = db.query(CustomerPortalRelationalComponent5)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: CustomerPortalRelationalComponent6Create) -> CustomerPortalRelationalComponent6:
        comp = CustomerPortalRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent6]:
        query = db.query(CustomerPortalRelationalComponent6)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: CustomerPortalRelationalComponent7Create) -> CustomerPortalRelationalComponent7:
        comp = CustomerPortalRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent7]:
        query = db.query(CustomerPortalRelationalComponent7)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: CustomerPortalRelationalComponent8Create) -> CustomerPortalRelationalComponent8:
        comp = CustomerPortalRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent8]:
        query = db.query(CustomerPortalRelationalComponent8)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: CustomerPortalRelationalComponent9Create) -> CustomerPortalRelationalComponent9:
        comp = CustomerPortalRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent9]:
        query = db.query(CustomerPortalRelationalComponent9)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: CustomerPortalRelationalComponent10Create) -> CustomerPortalRelationalComponent10:
        comp = CustomerPortalRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent10]:
        query = db.query(CustomerPortalRelationalComponent10)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: CustomerPortalRelationalComponent11Create) -> CustomerPortalRelationalComponent11:
        comp = CustomerPortalRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent11]:
        query = db.query(CustomerPortalRelationalComponent11)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: CustomerPortalRelationalComponent12Create) -> CustomerPortalRelationalComponent12:
        comp = CustomerPortalRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent12]:
        query = db.query(CustomerPortalRelationalComponent12)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: CustomerPortalRelationalComponent13Create) -> CustomerPortalRelationalComponent13:
        comp = CustomerPortalRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent13]:
        query = db.query(CustomerPortalRelationalComponent13)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: CustomerPortalRelationalComponent14Create) -> CustomerPortalRelationalComponent14:
        comp = CustomerPortalRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent14]:
        query = db.query(CustomerPortalRelationalComponent14)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: CustomerPortalRelationalComponent15Create) -> CustomerPortalRelationalComponent15:
        comp = CustomerPortalRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent15]:
        query = db.query(CustomerPortalRelationalComponent15)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: CustomerPortalRelationalComponent16Create) -> CustomerPortalRelationalComponent16:
        comp = CustomerPortalRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent16]:
        query = db.query(CustomerPortalRelationalComponent16)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: CustomerPortalRelationalComponent17Create) -> CustomerPortalRelationalComponent17:
        comp = CustomerPortalRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent17]:
        query = db.query(CustomerPortalRelationalComponent17)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: CustomerPortalRelationalComponent18Create) -> CustomerPortalRelationalComponent18:
        comp = CustomerPortalRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent18]:
        query = db.query(CustomerPortalRelationalComponent18)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: CustomerPortalRelationalComponent19Create) -> CustomerPortalRelationalComponent19:
        comp = CustomerPortalRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent19]:
        query = db.query(CustomerPortalRelationalComponent19)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: CustomerPortalRelationalComponent20Create) -> CustomerPortalRelationalComponent20:
        comp = CustomerPortalRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent20]:
        query = db.query(CustomerPortalRelationalComponent20)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: CustomerPortalRelationalComponent21Create) -> CustomerPortalRelationalComponent21:
        comp = CustomerPortalRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent21]:
        query = db.query(CustomerPortalRelationalComponent21)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: CustomerPortalRelationalComponent22Create) -> CustomerPortalRelationalComponent22:
        comp = CustomerPortalRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent22]:
        query = db.query(CustomerPortalRelationalComponent22)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: CustomerPortalRelationalComponent23Create) -> CustomerPortalRelationalComponent23:
        comp = CustomerPortalRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent23]:
        query = db.query(CustomerPortalRelationalComponent23)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: CustomerPortalRelationalComponent24Create) -> CustomerPortalRelationalComponent24:
        comp = CustomerPortalRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent24]:
        query = db.query(CustomerPortalRelationalComponent24)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: CustomerPortalRelationalComponent25Create) -> CustomerPortalRelationalComponent25:
        comp = CustomerPortalRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[CustomerPortalRelationalComponent25]:
        query = db.query(CustomerPortalRelationalComponent25)
        if master_entity_id:
            query = query.filter(CustomerPortalRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
