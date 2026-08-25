from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.support_tickets import (
    SupportTicketsMasterEntity, SupportTicketsStatus, SupportTicketsPriority, SupportTicketsCategoryType,
    SupportTicketsRelationalComponent1 ,SupportTicketsRelationalComponent2 ,SupportTicketsRelationalComponent3 ,SupportTicketsRelationalComponent4 ,SupportTicketsRelationalComponent5 ,SupportTicketsRelationalComponent6 ,SupportTicketsRelationalComponent7 ,SupportTicketsRelationalComponent8 ,SupportTicketsRelationalComponent9 ,SupportTicketsRelationalComponent10 ,SupportTicketsRelationalComponent11 ,SupportTicketsRelationalComponent12 ,SupportTicketsRelationalComponent13 ,SupportTicketsRelationalComponent14 ,SupportTicketsRelationalComponent15 ,SupportTicketsRelationalComponent16 ,SupportTicketsRelationalComponent17 ,SupportTicketsRelationalComponent18 ,SupportTicketsRelationalComponent19 ,SupportTicketsRelationalComponent20 ,SupportTicketsRelationalComponent21 ,SupportTicketsRelationalComponent22 ,SupportTicketsRelationalComponent23 ,SupportTicketsRelationalComponent24 ,SupportTicketsRelationalComponent25
)
from app.schemas.support_tickets import (
    SupportTicketsMasterEntityCreate, SupportTicketsMasterEntityUpdate,
    SupportTicketsRelationalComponent1Create ,SupportTicketsRelationalComponent2Create ,SupportTicketsRelationalComponent3Create ,SupportTicketsRelationalComponent4Create ,SupportTicketsRelationalComponent5Create ,SupportTicketsRelationalComponent6Create ,SupportTicketsRelationalComponent7Create ,SupportTicketsRelationalComponent8Create ,SupportTicketsRelationalComponent9Create ,SupportTicketsRelationalComponent10Create ,SupportTicketsRelationalComponent11Create ,SupportTicketsRelationalComponent12Create ,SupportTicketsRelationalComponent13Create ,SupportTicketsRelationalComponent14Create ,SupportTicketsRelationalComponent15Create ,SupportTicketsRelationalComponent16Create ,SupportTicketsRelationalComponent17Create ,SupportTicketsRelationalComponent18Create ,SupportTicketsRelationalComponent19Create ,SupportTicketsRelationalComponent20Create ,SupportTicketsRelationalComponent21Create ,SupportTicketsRelationalComponent22Create ,SupportTicketsRelationalComponent23Create ,SupportTicketsRelationalComponent24Create ,SupportTicketsRelationalComponent25Create
)

class SupportTicketsService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: SupportTicketsMasterEntityCreate) -> SupportTicketsMasterEntity:
        existing = db.query(SupportTicketsMasterEntity).filter(SupportTicketsMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = SupportTicketsMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> SupportTicketsMasterEntity:
        entity = db.query(SupportTicketsMasterEntity).filter(SupportTicketsMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support & Ticketing Desk Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[SupportTicketsStatus] = None) -> List[SupportTicketsMasterEntity]:
        query = db.query(SupportTicketsMasterEntity)
        if status_filter:
            query = query.filter(SupportTicketsMasterEntity.status == status_filter)
        return query.order_by(SupportTicketsMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: SupportTicketsMasterEntityUpdate) -> SupportTicketsMasterEntity:
        entity = SupportTicketsService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = SupportTicketsService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: SupportTicketsRelationalComponent1Create) -> SupportTicketsRelationalComponent1:
        comp = SupportTicketsRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent1]:
        query = db.query(SupportTicketsRelationalComponent1)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: SupportTicketsRelationalComponent2Create) -> SupportTicketsRelationalComponent2:
        comp = SupportTicketsRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent2]:
        query = db.query(SupportTicketsRelationalComponent2)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: SupportTicketsRelationalComponent3Create) -> SupportTicketsRelationalComponent3:
        comp = SupportTicketsRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent3]:
        query = db.query(SupportTicketsRelationalComponent3)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: SupportTicketsRelationalComponent4Create) -> SupportTicketsRelationalComponent4:
        comp = SupportTicketsRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent4]:
        query = db.query(SupportTicketsRelationalComponent4)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: SupportTicketsRelationalComponent5Create) -> SupportTicketsRelationalComponent5:
        comp = SupportTicketsRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent5]:
        query = db.query(SupportTicketsRelationalComponent5)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: SupportTicketsRelationalComponent6Create) -> SupportTicketsRelationalComponent6:
        comp = SupportTicketsRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent6]:
        query = db.query(SupportTicketsRelationalComponent6)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: SupportTicketsRelationalComponent7Create) -> SupportTicketsRelationalComponent7:
        comp = SupportTicketsRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent7]:
        query = db.query(SupportTicketsRelationalComponent7)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: SupportTicketsRelationalComponent8Create) -> SupportTicketsRelationalComponent8:
        comp = SupportTicketsRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent8]:
        query = db.query(SupportTicketsRelationalComponent8)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: SupportTicketsRelationalComponent9Create) -> SupportTicketsRelationalComponent9:
        comp = SupportTicketsRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent9]:
        query = db.query(SupportTicketsRelationalComponent9)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: SupportTicketsRelationalComponent10Create) -> SupportTicketsRelationalComponent10:
        comp = SupportTicketsRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent10]:
        query = db.query(SupportTicketsRelationalComponent10)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: SupportTicketsRelationalComponent11Create) -> SupportTicketsRelationalComponent11:
        comp = SupportTicketsRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent11]:
        query = db.query(SupportTicketsRelationalComponent11)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: SupportTicketsRelationalComponent12Create) -> SupportTicketsRelationalComponent12:
        comp = SupportTicketsRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent12]:
        query = db.query(SupportTicketsRelationalComponent12)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: SupportTicketsRelationalComponent13Create) -> SupportTicketsRelationalComponent13:
        comp = SupportTicketsRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent13]:
        query = db.query(SupportTicketsRelationalComponent13)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: SupportTicketsRelationalComponent14Create) -> SupportTicketsRelationalComponent14:
        comp = SupportTicketsRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent14]:
        query = db.query(SupportTicketsRelationalComponent14)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: SupportTicketsRelationalComponent15Create) -> SupportTicketsRelationalComponent15:
        comp = SupportTicketsRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent15]:
        query = db.query(SupportTicketsRelationalComponent15)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: SupportTicketsRelationalComponent16Create) -> SupportTicketsRelationalComponent16:
        comp = SupportTicketsRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent16]:
        query = db.query(SupportTicketsRelationalComponent16)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: SupportTicketsRelationalComponent17Create) -> SupportTicketsRelationalComponent17:
        comp = SupportTicketsRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent17]:
        query = db.query(SupportTicketsRelationalComponent17)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: SupportTicketsRelationalComponent18Create) -> SupportTicketsRelationalComponent18:
        comp = SupportTicketsRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent18]:
        query = db.query(SupportTicketsRelationalComponent18)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: SupportTicketsRelationalComponent19Create) -> SupportTicketsRelationalComponent19:
        comp = SupportTicketsRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent19]:
        query = db.query(SupportTicketsRelationalComponent19)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: SupportTicketsRelationalComponent20Create) -> SupportTicketsRelationalComponent20:
        comp = SupportTicketsRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent20]:
        query = db.query(SupportTicketsRelationalComponent20)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: SupportTicketsRelationalComponent21Create) -> SupportTicketsRelationalComponent21:
        comp = SupportTicketsRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent21]:
        query = db.query(SupportTicketsRelationalComponent21)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: SupportTicketsRelationalComponent22Create) -> SupportTicketsRelationalComponent22:
        comp = SupportTicketsRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent22]:
        query = db.query(SupportTicketsRelationalComponent22)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: SupportTicketsRelationalComponent23Create) -> SupportTicketsRelationalComponent23:
        comp = SupportTicketsRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent23]:
        query = db.query(SupportTicketsRelationalComponent23)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: SupportTicketsRelationalComponent24Create) -> SupportTicketsRelationalComponent24:
        comp = SupportTicketsRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent24]:
        query = db.query(SupportTicketsRelationalComponent24)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: SupportTicketsRelationalComponent25Create) -> SupportTicketsRelationalComponent25:
        comp = SupportTicketsRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[SupportTicketsRelationalComponent25]:
        query = db.query(SupportTicketsRelationalComponent25)
        if master_entity_id:
            query = query.filter(SupportTicketsRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
