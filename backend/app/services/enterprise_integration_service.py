from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.enterprise_integration import (
    EnterpriseIntegrationMasterEntity, EnterpriseIntegrationStatus,
    EnterpriseIntegrationRelationalComponent1 ,EnterpriseIntegrationRelationalComponent2 ,EnterpriseIntegrationRelationalComponent3 ,EnterpriseIntegrationRelationalComponent4 ,EnterpriseIntegrationRelationalComponent5 ,EnterpriseIntegrationRelationalComponent6 ,EnterpriseIntegrationRelationalComponent7 ,EnterpriseIntegrationRelationalComponent8 ,EnterpriseIntegrationRelationalComponent9 ,EnterpriseIntegrationRelationalComponent10 ,EnterpriseIntegrationRelationalComponent11 ,EnterpriseIntegrationRelationalComponent12 ,EnterpriseIntegrationRelationalComponent13 ,EnterpriseIntegrationRelationalComponent14 ,EnterpriseIntegrationRelationalComponent15 ,EnterpriseIntegrationRelationalComponent16 ,EnterpriseIntegrationRelationalComponent17 ,EnterpriseIntegrationRelationalComponent18 ,EnterpriseIntegrationRelationalComponent19 ,EnterpriseIntegrationRelationalComponent20 ,EnterpriseIntegrationRelationalComponent21 ,EnterpriseIntegrationRelationalComponent22 ,EnterpriseIntegrationRelationalComponent23 ,EnterpriseIntegrationRelationalComponent24 ,EnterpriseIntegrationRelationalComponent25
)
from app.schemas.enterprise_integration import (
    EnterpriseIntegrationMasterEntityCreate, EnterpriseIntegrationMasterEntityUpdate,
    EnterpriseIntegrationRelationalComponent1Create ,EnterpriseIntegrationRelationalComponent2Create ,EnterpriseIntegrationRelationalComponent3Create ,EnterpriseIntegrationRelationalComponent4Create ,EnterpriseIntegrationRelationalComponent5Create ,EnterpriseIntegrationRelationalComponent6Create ,EnterpriseIntegrationRelationalComponent7Create ,EnterpriseIntegrationRelationalComponent8Create ,EnterpriseIntegrationRelationalComponent9Create ,EnterpriseIntegrationRelationalComponent10Create ,EnterpriseIntegrationRelationalComponent11Create ,EnterpriseIntegrationRelationalComponent12Create ,EnterpriseIntegrationRelationalComponent13Create ,EnterpriseIntegrationRelationalComponent14Create ,EnterpriseIntegrationRelationalComponent15Create ,EnterpriseIntegrationRelationalComponent16Create ,EnterpriseIntegrationRelationalComponent17Create ,EnterpriseIntegrationRelationalComponent18Create ,EnterpriseIntegrationRelationalComponent19Create ,EnterpriseIntegrationRelationalComponent20Create ,EnterpriseIntegrationRelationalComponent21Create ,EnterpriseIntegrationRelationalComponent22Create ,EnterpriseIntegrationRelationalComponent23Create ,EnterpriseIntegrationRelationalComponent24Create ,EnterpriseIntegrationRelationalComponent25Create
)

class EnterpriseIntegrationService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: EnterpriseIntegrationMasterEntityCreate) -> EnterpriseIntegrationMasterEntity:
        existing = db.query(EnterpriseIntegrationMasterEntity).filter(EnterpriseIntegrationMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = EnterpriseIntegrationMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> EnterpriseIntegrationMasterEntity:
        entity = db.query(EnterpriseIntegrationMasterEntity).filter(EnterpriseIntegrationMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enterprise Third-Party Integrations Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[EnterpriseIntegrationStatus] = None) -> List[EnterpriseIntegrationMasterEntity]:
        query = db.query(EnterpriseIntegrationMasterEntity)
        if status_filter:
            query = query.filter(EnterpriseIntegrationMasterEntity.status == status_filter)
        return query.order_by(EnterpriseIntegrationMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: EnterpriseIntegrationMasterEntityUpdate) -> EnterpriseIntegrationMasterEntity:
        entity = EnterpriseIntegrationService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = EnterpriseIntegrationService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: EnterpriseIntegrationRelationalComponent1Create) -> EnterpriseIntegrationRelationalComponent1:
        comp = EnterpriseIntegrationRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent1]:
        query = db.query(EnterpriseIntegrationRelationalComponent1)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: EnterpriseIntegrationRelationalComponent2Create) -> EnterpriseIntegrationRelationalComponent2:
        comp = EnterpriseIntegrationRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent2]:
        query = db.query(EnterpriseIntegrationRelationalComponent2)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: EnterpriseIntegrationRelationalComponent3Create) -> EnterpriseIntegrationRelationalComponent3:
        comp = EnterpriseIntegrationRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent3]:
        query = db.query(EnterpriseIntegrationRelationalComponent3)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: EnterpriseIntegrationRelationalComponent4Create) -> EnterpriseIntegrationRelationalComponent4:
        comp = EnterpriseIntegrationRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent4]:
        query = db.query(EnterpriseIntegrationRelationalComponent4)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: EnterpriseIntegrationRelationalComponent5Create) -> EnterpriseIntegrationRelationalComponent5:
        comp = EnterpriseIntegrationRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent5]:
        query = db.query(EnterpriseIntegrationRelationalComponent5)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: EnterpriseIntegrationRelationalComponent6Create) -> EnterpriseIntegrationRelationalComponent6:
        comp = EnterpriseIntegrationRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent6]:
        query = db.query(EnterpriseIntegrationRelationalComponent6)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: EnterpriseIntegrationRelationalComponent7Create) -> EnterpriseIntegrationRelationalComponent7:
        comp = EnterpriseIntegrationRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent7]:
        query = db.query(EnterpriseIntegrationRelationalComponent7)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: EnterpriseIntegrationRelationalComponent8Create) -> EnterpriseIntegrationRelationalComponent8:
        comp = EnterpriseIntegrationRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent8]:
        query = db.query(EnterpriseIntegrationRelationalComponent8)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: EnterpriseIntegrationRelationalComponent9Create) -> EnterpriseIntegrationRelationalComponent9:
        comp = EnterpriseIntegrationRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent9]:
        query = db.query(EnterpriseIntegrationRelationalComponent9)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: EnterpriseIntegrationRelationalComponent10Create) -> EnterpriseIntegrationRelationalComponent10:
        comp = EnterpriseIntegrationRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent10]:
        query = db.query(EnterpriseIntegrationRelationalComponent10)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: EnterpriseIntegrationRelationalComponent11Create) -> EnterpriseIntegrationRelationalComponent11:
        comp = EnterpriseIntegrationRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent11]:
        query = db.query(EnterpriseIntegrationRelationalComponent11)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: EnterpriseIntegrationRelationalComponent12Create) -> EnterpriseIntegrationRelationalComponent12:
        comp = EnterpriseIntegrationRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent12]:
        query = db.query(EnterpriseIntegrationRelationalComponent12)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: EnterpriseIntegrationRelationalComponent13Create) -> EnterpriseIntegrationRelationalComponent13:
        comp = EnterpriseIntegrationRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent13]:
        query = db.query(EnterpriseIntegrationRelationalComponent13)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: EnterpriseIntegrationRelationalComponent14Create) -> EnterpriseIntegrationRelationalComponent14:
        comp = EnterpriseIntegrationRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent14]:
        query = db.query(EnterpriseIntegrationRelationalComponent14)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: EnterpriseIntegrationRelationalComponent15Create) -> EnterpriseIntegrationRelationalComponent15:
        comp = EnterpriseIntegrationRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent15]:
        query = db.query(EnterpriseIntegrationRelationalComponent15)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: EnterpriseIntegrationRelationalComponent16Create) -> EnterpriseIntegrationRelationalComponent16:
        comp = EnterpriseIntegrationRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent16]:
        query = db.query(EnterpriseIntegrationRelationalComponent16)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: EnterpriseIntegrationRelationalComponent17Create) -> EnterpriseIntegrationRelationalComponent17:
        comp = EnterpriseIntegrationRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent17]:
        query = db.query(EnterpriseIntegrationRelationalComponent17)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: EnterpriseIntegrationRelationalComponent18Create) -> EnterpriseIntegrationRelationalComponent18:
        comp = EnterpriseIntegrationRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent18]:
        query = db.query(EnterpriseIntegrationRelationalComponent18)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: EnterpriseIntegrationRelationalComponent19Create) -> EnterpriseIntegrationRelationalComponent19:
        comp = EnterpriseIntegrationRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent19]:
        query = db.query(EnterpriseIntegrationRelationalComponent19)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: EnterpriseIntegrationRelationalComponent20Create) -> EnterpriseIntegrationRelationalComponent20:
        comp = EnterpriseIntegrationRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent20]:
        query = db.query(EnterpriseIntegrationRelationalComponent20)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: EnterpriseIntegrationRelationalComponent21Create) -> EnterpriseIntegrationRelationalComponent21:
        comp = EnterpriseIntegrationRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent21]:
        query = db.query(EnterpriseIntegrationRelationalComponent21)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: EnterpriseIntegrationRelationalComponent22Create) -> EnterpriseIntegrationRelationalComponent22:
        comp = EnterpriseIntegrationRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent22]:
        query = db.query(EnterpriseIntegrationRelationalComponent22)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: EnterpriseIntegrationRelationalComponent23Create) -> EnterpriseIntegrationRelationalComponent23:
        comp = EnterpriseIntegrationRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent23]:
        query = db.query(EnterpriseIntegrationRelationalComponent23)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: EnterpriseIntegrationRelationalComponent24Create) -> EnterpriseIntegrationRelationalComponent24:
        comp = EnterpriseIntegrationRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent24]:
        query = db.query(EnterpriseIntegrationRelationalComponent24)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: EnterpriseIntegrationRelationalComponent25Create) -> EnterpriseIntegrationRelationalComponent25:
        comp = EnterpriseIntegrationRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent25]:
        query = db.query(EnterpriseIntegrationRelationalComponent25)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: EnterpriseIntegrationRelationalComponent26Create) -> EnterpriseIntegrationRelationalComponent26:
        comp = EnterpriseIntegrationRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent26]:
        query = db.query(EnterpriseIntegrationRelationalComponent26)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: EnterpriseIntegrationRelationalComponent27Create) -> EnterpriseIntegrationRelationalComponent27:
        comp = EnterpriseIntegrationRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent27]:
        query = db.query(EnterpriseIntegrationRelationalComponent27)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: EnterpriseIntegrationRelationalComponent28Create) -> EnterpriseIntegrationRelationalComponent28:
        comp = EnterpriseIntegrationRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent28]:
        query = db.query(EnterpriseIntegrationRelationalComponent28)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: EnterpriseIntegrationRelationalComponent29Create) -> EnterpriseIntegrationRelationalComponent29:
        comp = EnterpriseIntegrationRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent29]:
        query = db.query(EnterpriseIntegrationRelationalComponent29)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: EnterpriseIntegrationRelationalComponent30Create) -> EnterpriseIntegrationRelationalComponent30:
        comp = EnterpriseIntegrationRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[EnterpriseIntegrationRelationalComponent30]:
        query = db.query(EnterpriseIntegrationRelationalComponent30)
        if master_entity_id:
            query = query.filter(EnterpriseIntegrationRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
