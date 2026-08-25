from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.fleet_logistics import (
    FleetLogisticsMasterEntity, FleetLogisticsStatus,
    FleetLogisticsRelationalComponent1 ,FleetLogisticsRelationalComponent2 ,FleetLogisticsRelationalComponent3 ,FleetLogisticsRelationalComponent4 ,FleetLogisticsRelationalComponent5 ,FleetLogisticsRelationalComponent6 ,FleetLogisticsRelationalComponent7 ,FleetLogisticsRelationalComponent8 ,FleetLogisticsRelationalComponent9 ,FleetLogisticsRelationalComponent10 ,FleetLogisticsRelationalComponent11 ,FleetLogisticsRelationalComponent12 ,FleetLogisticsRelationalComponent13 ,FleetLogisticsRelationalComponent14 ,FleetLogisticsRelationalComponent15 ,FleetLogisticsRelationalComponent16 ,FleetLogisticsRelationalComponent17 ,FleetLogisticsRelationalComponent18 ,FleetLogisticsRelationalComponent19 ,FleetLogisticsRelationalComponent20 ,FleetLogisticsRelationalComponent21 ,FleetLogisticsRelationalComponent22 ,FleetLogisticsRelationalComponent23 ,FleetLogisticsRelationalComponent24 ,FleetLogisticsRelationalComponent25
)
from app.schemas.fleet_logistics import (
    FleetLogisticsMasterEntityCreate, FleetLogisticsMasterEntityUpdate,
    FleetLogisticsRelationalComponent1Create ,FleetLogisticsRelationalComponent2Create ,FleetLogisticsRelationalComponent3Create ,FleetLogisticsRelationalComponent4Create ,FleetLogisticsRelationalComponent5Create ,FleetLogisticsRelationalComponent6Create ,FleetLogisticsRelationalComponent7Create ,FleetLogisticsRelationalComponent8Create ,FleetLogisticsRelationalComponent9Create ,FleetLogisticsRelationalComponent10Create ,FleetLogisticsRelationalComponent11Create ,FleetLogisticsRelationalComponent12Create ,FleetLogisticsRelationalComponent13Create ,FleetLogisticsRelationalComponent14Create ,FleetLogisticsRelationalComponent15Create ,FleetLogisticsRelationalComponent16Create ,FleetLogisticsRelationalComponent17Create ,FleetLogisticsRelationalComponent18Create ,FleetLogisticsRelationalComponent19Create ,FleetLogisticsRelationalComponent20Create ,FleetLogisticsRelationalComponent21Create ,FleetLogisticsRelationalComponent22Create ,FleetLogisticsRelationalComponent23Create ,FleetLogisticsRelationalComponent24Create ,FleetLogisticsRelationalComponent25Create
)

class FleetLogisticsService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: FleetLogisticsMasterEntityCreate) -> FleetLogisticsMasterEntity:
        existing = db.query(FleetLogisticsMasterEntity).filter(FleetLogisticsMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = FleetLogisticsMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> FleetLogisticsMasterEntity:
        entity = db.query(FleetLogisticsMasterEntity).filter(FleetLogisticsMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Technician Fleet & Logistics Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[FleetLogisticsStatus] = None) -> List[FleetLogisticsMasterEntity]:
        query = db.query(FleetLogisticsMasterEntity)
        if status_filter:
            query = query.filter(FleetLogisticsMasterEntity.status == status_filter)
        return query.order_by(FleetLogisticsMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: FleetLogisticsMasterEntityUpdate) -> FleetLogisticsMasterEntity:
        entity = FleetLogisticsService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = FleetLogisticsService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: FleetLogisticsRelationalComponent1Create) -> FleetLogisticsRelationalComponent1:
        comp = FleetLogisticsRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent1]:
        query = db.query(FleetLogisticsRelationalComponent1)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: FleetLogisticsRelationalComponent2Create) -> FleetLogisticsRelationalComponent2:
        comp = FleetLogisticsRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent2]:
        query = db.query(FleetLogisticsRelationalComponent2)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: FleetLogisticsRelationalComponent3Create) -> FleetLogisticsRelationalComponent3:
        comp = FleetLogisticsRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent3]:
        query = db.query(FleetLogisticsRelationalComponent3)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: FleetLogisticsRelationalComponent4Create) -> FleetLogisticsRelationalComponent4:
        comp = FleetLogisticsRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent4]:
        query = db.query(FleetLogisticsRelationalComponent4)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: FleetLogisticsRelationalComponent5Create) -> FleetLogisticsRelationalComponent5:
        comp = FleetLogisticsRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent5]:
        query = db.query(FleetLogisticsRelationalComponent5)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: FleetLogisticsRelationalComponent6Create) -> FleetLogisticsRelationalComponent6:
        comp = FleetLogisticsRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent6]:
        query = db.query(FleetLogisticsRelationalComponent6)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: FleetLogisticsRelationalComponent7Create) -> FleetLogisticsRelationalComponent7:
        comp = FleetLogisticsRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent7]:
        query = db.query(FleetLogisticsRelationalComponent7)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: FleetLogisticsRelationalComponent8Create) -> FleetLogisticsRelationalComponent8:
        comp = FleetLogisticsRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent8]:
        query = db.query(FleetLogisticsRelationalComponent8)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: FleetLogisticsRelationalComponent9Create) -> FleetLogisticsRelationalComponent9:
        comp = FleetLogisticsRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent9]:
        query = db.query(FleetLogisticsRelationalComponent9)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: FleetLogisticsRelationalComponent10Create) -> FleetLogisticsRelationalComponent10:
        comp = FleetLogisticsRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent10]:
        query = db.query(FleetLogisticsRelationalComponent10)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: FleetLogisticsRelationalComponent11Create) -> FleetLogisticsRelationalComponent11:
        comp = FleetLogisticsRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent11]:
        query = db.query(FleetLogisticsRelationalComponent11)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: FleetLogisticsRelationalComponent12Create) -> FleetLogisticsRelationalComponent12:
        comp = FleetLogisticsRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent12]:
        query = db.query(FleetLogisticsRelationalComponent12)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: FleetLogisticsRelationalComponent13Create) -> FleetLogisticsRelationalComponent13:
        comp = FleetLogisticsRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent13]:
        query = db.query(FleetLogisticsRelationalComponent13)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: FleetLogisticsRelationalComponent14Create) -> FleetLogisticsRelationalComponent14:
        comp = FleetLogisticsRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent14]:
        query = db.query(FleetLogisticsRelationalComponent14)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: FleetLogisticsRelationalComponent15Create) -> FleetLogisticsRelationalComponent15:
        comp = FleetLogisticsRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent15]:
        query = db.query(FleetLogisticsRelationalComponent15)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: FleetLogisticsRelationalComponent16Create) -> FleetLogisticsRelationalComponent16:
        comp = FleetLogisticsRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent16]:
        query = db.query(FleetLogisticsRelationalComponent16)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: FleetLogisticsRelationalComponent17Create) -> FleetLogisticsRelationalComponent17:
        comp = FleetLogisticsRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent17]:
        query = db.query(FleetLogisticsRelationalComponent17)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: FleetLogisticsRelationalComponent18Create) -> FleetLogisticsRelationalComponent18:
        comp = FleetLogisticsRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent18]:
        query = db.query(FleetLogisticsRelationalComponent18)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: FleetLogisticsRelationalComponent19Create) -> FleetLogisticsRelationalComponent19:
        comp = FleetLogisticsRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent19]:
        query = db.query(FleetLogisticsRelationalComponent19)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: FleetLogisticsRelationalComponent20Create) -> FleetLogisticsRelationalComponent20:
        comp = FleetLogisticsRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent20]:
        query = db.query(FleetLogisticsRelationalComponent20)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: FleetLogisticsRelationalComponent21Create) -> FleetLogisticsRelationalComponent21:
        comp = FleetLogisticsRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent21]:
        query = db.query(FleetLogisticsRelationalComponent21)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: FleetLogisticsRelationalComponent22Create) -> FleetLogisticsRelationalComponent22:
        comp = FleetLogisticsRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent22]:
        query = db.query(FleetLogisticsRelationalComponent22)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: FleetLogisticsRelationalComponent23Create) -> FleetLogisticsRelationalComponent23:
        comp = FleetLogisticsRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent23]:
        query = db.query(FleetLogisticsRelationalComponent23)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: FleetLogisticsRelationalComponent24Create) -> FleetLogisticsRelationalComponent24:
        comp = FleetLogisticsRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent24]:
        query = db.query(FleetLogisticsRelationalComponent24)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: FleetLogisticsRelationalComponent25Create) -> FleetLogisticsRelationalComponent25:
        comp = FleetLogisticsRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent25]:
        query = db.query(FleetLogisticsRelationalComponent25)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: FleetLogisticsRelationalComponent26Create) -> FleetLogisticsRelationalComponent26:
        comp = FleetLogisticsRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent26]:
        query = db.query(FleetLogisticsRelationalComponent26)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: FleetLogisticsRelationalComponent27Create) -> FleetLogisticsRelationalComponent27:
        comp = FleetLogisticsRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent27]:
        query = db.query(FleetLogisticsRelationalComponent27)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: FleetLogisticsRelationalComponent28Create) -> FleetLogisticsRelationalComponent28:
        comp = FleetLogisticsRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent28]:
        query = db.query(FleetLogisticsRelationalComponent28)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: FleetLogisticsRelationalComponent29Create) -> FleetLogisticsRelationalComponent29:
        comp = FleetLogisticsRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent29]:
        query = db.query(FleetLogisticsRelationalComponent29)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: FleetLogisticsRelationalComponent30Create) -> FleetLogisticsRelationalComponent30:
        comp = FleetLogisticsRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[FleetLogisticsRelationalComponent30]:
        query = db.query(FleetLogisticsRelationalComponent30)
        if master_entity_id:
            query = query.filter(FleetLogisticsRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
