from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.service_catalog import (
    ServiceCatalogMasterEntity, ServiceCatalogStatus,
    ServiceCatalogRelationalComponent1 ,ServiceCatalogRelationalComponent2 ,ServiceCatalogRelationalComponent3 ,ServiceCatalogRelationalComponent4 ,ServiceCatalogRelationalComponent5 ,ServiceCatalogRelationalComponent6 ,ServiceCatalogRelationalComponent7 ,ServiceCatalogRelationalComponent8 ,ServiceCatalogRelationalComponent9 ,ServiceCatalogRelationalComponent10 ,ServiceCatalogRelationalComponent11 ,ServiceCatalogRelationalComponent12 ,ServiceCatalogRelationalComponent13 ,ServiceCatalogRelationalComponent14 ,ServiceCatalogRelationalComponent15 ,ServiceCatalogRelationalComponent16 ,ServiceCatalogRelationalComponent17 ,ServiceCatalogRelationalComponent18 ,ServiceCatalogRelationalComponent19 ,ServiceCatalogRelationalComponent20 ,ServiceCatalogRelationalComponent21 ,ServiceCatalogRelationalComponent22 ,ServiceCatalogRelationalComponent23 ,ServiceCatalogRelationalComponent24 ,ServiceCatalogRelationalComponent25
)
from app.schemas.service_catalog import (
    ServiceCatalogMasterEntityCreate, ServiceCatalogMasterEntityUpdate,
    ServiceCatalogRelationalComponent1Create ,ServiceCatalogRelationalComponent2Create ,ServiceCatalogRelationalComponent3Create ,ServiceCatalogRelationalComponent4Create ,ServiceCatalogRelationalComponent5Create ,ServiceCatalogRelationalComponent6Create ,ServiceCatalogRelationalComponent7Create ,ServiceCatalogRelationalComponent8Create ,ServiceCatalogRelationalComponent9Create ,ServiceCatalogRelationalComponent10Create ,ServiceCatalogRelationalComponent11Create ,ServiceCatalogRelationalComponent12Create ,ServiceCatalogRelationalComponent13Create ,ServiceCatalogRelationalComponent14Create ,ServiceCatalogRelationalComponent15Create ,ServiceCatalogRelationalComponent16Create ,ServiceCatalogRelationalComponent17Create ,ServiceCatalogRelationalComponent18Create ,ServiceCatalogRelationalComponent19Create ,ServiceCatalogRelationalComponent20Create ,ServiceCatalogRelationalComponent21Create ,ServiceCatalogRelationalComponent22Create ,ServiceCatalogRelationalComponent23Create ,ServiceCatalogRelationalComponent24Create ,ServiceCatalogRelationalComponent25Create
)

class ServiceCatalogService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: ServiceCatalogMasterEntityCreate) -> ServiceCatalogMasterEntity:
        existing = db.query(ServiceCatalogMasterEntity).filter(ServiceCatalogMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = ServiceCatalogMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> ServiceCatalogMasterEntity:
        entity = db.query(ServiceCatalogMasterEntity).filter(ServiceCatalogMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service Catalog Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[ServiceCatalogStatus] = None) -> List[ServiceCatalogMasterEntity]:
        query = db.query(ServiceCatalogMasterEntity)
        if status_filter:
            query = query.filter(ServiceCatalogMasterEntity.status == status_filter)
        return query.order_by(ServiceCatalogMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: ServiceCatalogMasterEntityUpdate) -> ServiceCatalogMasterEntity:
        entity = ServiceCatalogService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = ServiceCatalogService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: ServiceCatalogRelationalComponent1Create) -> ServiceCatalogRelationalComponent1:
        comp = ServiceCatalogRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent1]:
        query = db.query(ServiceCatalogRelationalComponent1)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: ServiceCatalogRelationalComponent2Create) -> ServiceCatalogRelationalComponent2:
        comp = ServiceCatalogRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent2]:
        query = db.query(ServiceCatalogRelationalComponent2)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: ServiceCatalogRelationalComponent3Create) -> ServiceCatalogRelationalComponent3:
        comp = ServiceCatalogRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent3]:
        query = db.query(ServiceCatalogRelationalComponent3)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: ServiceCatalogRelationalComponent4Create) -> ServiceCatalogRelationalComponent4:
        comp = ServiceCatalogRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent4]:
        query = db.query(ServiceCatalogRelationalComponent4)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: ServiceCatalogRelationalComponent5Create) -> ServiceCatalogRelationalComponent5:
        comp = ServiceCatalogRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent5]:
        query = db.query(ServiceCatalogRelationalComponent5)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: ServiceCatalogRelationalComponent6Create) -> ServiceCatalogRelationalComponent6:
        comp = ServiceCatalogRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent6]:
        query = db.query(ServiceCatalogRelationalComponent6)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: ServiceCatalogRelationalComponent7Create) -> ServiceCatalogRelationalComponent7:
        comp = ServiceCatalogRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent7]:
        query = db.query(ServiceCatalogRelationalComponent7)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: ServiceCatalogRelationalComponent8Create) -> ServiceCatalogRelationalComponent8:
        comp = ServiceCatalogRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent8]:
        query = db.query(ServiceCatalogRelationalComponent8)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: ServiceCatalogRelationalComponent9Create) -> ServiceCatalogRelationalComponent9:
        comp = ServiceCatalogRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent9]:
        query = db.query(ServiceCatalogRelationalComponent9)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: ServiceCatalogRelationalComponent10Create) -> ServiceCatalogRelationalComponent10:
        comp = ServiceCatalogRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent10]:
        query = db.query(ServiceCatalogRelationalComponent10)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: ServiceCatalogRelationalComponent11Create) -> ServiceCatalogRelationalComponent11:
        comp = ServiceCatalogRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent11]:
        query = db.query(ServiceCatalogRelationalComponent11)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: ServiceCatalogRelationalComponent12Create) -> ServiceCatalogRelationalComponent12:
        comp = ServiceCatalogRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent12]:
        query = db.query(ServiceCatalogRelationalComponent12)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: ServiceCatalogRelationalComponent13Create) -> ServiceCatalogRelationalComponent13:
        comp = ServiceCatalogRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent13]:
        query = db.query(ServiceCatalogRelationalComponent13)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: ServiceCatalogRelationalComponent14Create) -> ServiceCatalogRelationalComponent14:
        comp = ServiceCatalogRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent14]:
        query = db.query(ServiceCatalogRelationalComponent14)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: ServiceCatalogRelationalComponent15Create) -> ServiceCatalogRelationalComponent15:
        comp = ServiceCatalogRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent15]:
        query = db.query(ServiceCatalogRelationalComponent15)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: ServiceCatalogRelationalComponent16Create) -> ServiceCatalogRelationalComponent16:
        comp = ServiceCatalogRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent16]:
        query = db.query(ServiceCatalogRelationalComponent16)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: ServiceCatalogRelationalComponent17Create) -> ServiceCatalogRelationalComponent17:
        comp = ServiceCatalogRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent17]:
        query = db.query(ServiceCatalogRelationalComponent17)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: ServiceCatalogRelationalComponent18Create) -> ServiceCatalogRelationalComponent18:
        comp = ServiceCatalogRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent18]:
        query = db.query(ServiceCatalogRelationalComponent18)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: ServiceCatalogRelationalComponent19Create) -> ServiceCatalogRelationalComponent19:
        comp = ServiceCatalogRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent19]:
        query = db.query(ServiceCatalogRelationalComponent19)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: ServiceCatalogRelationalComponent20Create) -> ServiceCatalogRelationalComponent20:
        comp = ServiceCatalogRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent20]:
        query = db.query(ServiceCatalogRelationalComponent20)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: ServiceCatalogRelationalComponent21Create) -> ServiceCatalogRelationalComponent21:
        comp = ServiceCatalogRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent21]:
        query = db.query(ServiceCatalogRelationalComponent21)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: ServiceCatalogRelationalComponent22Create) -> ServiceCatalogRelationalComponent22:
        comp = ServiceCatalogRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent22]:
        query = db.query(ServiceCatalogRelationalComponent22)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: ServiceCatalogRelationalComponent23Create) -> ServiceCatalogRelationalComponent23:
        comp = ServiceCatalogRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent23]:
        query = db.query(ServiceCatalogRelationalComponent23)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: ServiceCatalogRelationalComponent24Create) -> ServiceCatalogRelationalComponent24:
        comp = ServiceCatalogRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent24]:
        query = db.query(ServiceCatalogRelationalComponent24)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: ServiceCatalogRelationalComponent25Create) -> ServiceCatalogRelationalComponent25:
        comp = ServiceCatalogRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent25]:
        query = db.query(ServiceCatalogRelationalComponent25)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: ServiceCatalogRelationalComponent26Create) -> ServiceCatalogRelationalComponent26:
        comp = ServiceCatalogRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent26]:
        query = db.query(ServiceCatalogRelationalComponent26)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: ServiceCatalogRelationalComponent27Create) -> ServiceCatalogRelationalComponent27:
        comp = ServiceCatalogRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent27]:
        query = db.query(ServiceCatalogRelationalComponent27)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: ServiceCatalogRelationalComponent28Create) -> ServiceCatalogRelationalComponent28:
        comp = ServiceCatalogRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent28]:
        query = db.query(ServiceCatalogRelationalComponent28)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: ServiceCatalogRelationalComponent29Create) -> ServiceCatalogRelationalComponent29:
        comp = ServiceCatalogRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent29]:
        query = db.query(ServiceCatalogRelationalComponent29)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: ServiceCatalogRelationalComponent30Create) -> ServiceCatalogRelationalComponent30:
        comp = ServiceCatalogRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[ServiceCatalogRelationalComponent30]:
        query = db.query(ServiceCatalogRelationalComponent30)
        if master_entity_id:
            query = query.filter(ServiceCatalogRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
