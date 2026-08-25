from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.vendor_management import (
    VendorManagementMasterEntity, VendorManagementStatus,
    VendorManagementRelationalComponent1 ,VendorManagementRelationalComponent2 ,VendorManagementRelationalComponent3 ,VendorManagementRelationalComponent4 ,VendorManagementRelationalComponent5 ,VendorManagementRelationalComponent6 ,VendorManagementRelationalComponent7 ,VendorManagementRelationalComponent8 ,VendorManagementRelationalComponent9 ,VendorManagementRelationalComponent10 ,VendorManagementRelationalComponent11 ,VendorManagementRelationalComponent12 ,VendorManagementRelationalComponent13 ,VendorManagementRelationalComponent14 ,VendorManagementRelationalComponent15 ,VendorManagementRelationalComponent16 ,VendorManagementRelationalComponent17 ,VendorManagementRelationalComponent18 ,VendorManagementRelationalComponent19 ,VendorManagementRelationalComponent20 ,VendorManagementRelationalComponent21 ,VendorManagementRelationalComponent22 ,VendorManagementRelationalComponent23 ,VendorManagementRelationalComponent24 ,VendorManagementRelationalComponent25
)
from app.schemas.vendor_management import (
    VendorManagementMasterEntityCreate, VendorManagementMasterEntityUpdate,
    VendorManagementRelationalComponent1Create ,VendorManagementRelationalComponent2Create ,VendorManagementRelationalComponent3Create ,VendorManagementRelationalComponent4Create ,VendorManagementRelationalComponent5Create ,VendorManagementRelationalComponent6Create ,VendorManagementRelationalComponent7Create ,VendorManagementRelationalComponent8Create ,VendorManagementRelationalComponent9Create ,VendorManagementRelationalComponent10Create ,VendorManagementRelationalComponent11Create ,VendorManagementRelationalComponent12Create ,VendorManagementRelationalComponent13Create ,VendorManagementRelationalComponent14Create ,VendorManagementRelationalComponent15Create ,VendorManagementRelationalComponent16Create ,VendorManagementRelationalComponent17Create ,VendorManagementRelationalComponent18Create ,VendorManagementRelationalComponent19Create ,VendorManagementRelationalComponent20Create ,VendorManagementRelationalComponent21Create ,VendorManagementRelationalComponent22Create ,VendorManagementRelationalComponent23Create ,VendorManagementRelationalComponent24Create ,VendorManagementRelationalComponent25Create
)

class VendorManagementService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: VendorManagementMasterEntityCreate) -> VendorManagementMasterEntity:
        existing = db.query(VendorManagementMasterEntity).filter(VendorManagementMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = VendorManagementMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> VendorManagementMasterEntity:
        entity = db.query(VendorManagementMasterEntity).filter(VendorManagementMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subcontractor & Vendor Management Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[VendorManagementStatus] = None) -> List[VendorManagementMasterEntity]:
        query = db.query(VendorManagementMasterEntity)
        if status_filter:
            query = query.filter(VendorManagementMasterEntity.status == status_filter)
        return query.order_by(VendorManagementMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: VendorManagementMasterEntityUpdate) -> VendorManagementMasterEntity:
        entity = VendorManagementService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = VendorManagementService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: VendorManagementRelationalComponent1Create) -> VendorManagementRelationalComponent1:
        comp = VendorManagementRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent1]:
        query = db.query(VendorManagementRelationalComponent1)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: VendorManagementRelationalComponent2Create) -> VendorManagementRelationalComponent2:
        comp = VendorManagementRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent2]:
        query = db.query(VendorManagementRelationalComponent2)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: VendorManagementRelationalComponent3Create) -> VendorManagementRelationalComponent3:
        comp = VendorManagementRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent3]:
        query = db.query(VendorManagementRelationalComponent3)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: VendorManagementRelationalComponent4Create) -> VendorManagementRelationalComponent4:
        comp = VendorManagementRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent4]:
        query = db.query(VendorManagementRelationalComponent4)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: VendorManagementRelationalComponent5Create) -> VendorManagementRelationalComponent5:
        comp = VendorManagementRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent5]:
        query = db.query(VendorManagementRelationalComponent5)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: VendorManagementRelationalComponent6Create) -> VendorManagementRelationalComponent6:
        comp = VendorManagementRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent6]:
        query = db.query(VendorManagementRelationalComponent6)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: VendorManagementRelationalComponent7Create) -> VendorManagementRelationalComponent7:
        comp = VendorManagementRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent7]:
        query = db.query(VendorManagementRelationalComponent7)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: VendorManagementRelationalComponent8Create) -> VendorManagementRelationalComponent8:
        comp = VendorManagementRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent8]:
        query = db.query(VendorManagementRelationalComponent8)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: VendorManagementRelationalComponent9Create) -> VendorManagementRelationalComponent9:
        comp = VendorManagementRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent9]:
        query = db.query(VendorManagementRelationalComponent9)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: VendorManagementRelationalComponent10Create) -> VendorManagementRelationalComponent10:
        comp = VendorManagementRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent10]:
        query = db.query(VendorManagementRelationalComponent10)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: VendorManagementRelationalComponent11Create) -> VendorManagementRelationalComponent11:
        comp = VendorManagementRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent11]:
        query = db.query(VendorManagementRelationalComponent11)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: VendorManagementRelationalComponent12Create) -> VendorManagementRelationalComponent12:
        comp = VendorManagementRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent12]:
        query = db.query(VendorManagementRelationalComponent12)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: VendorManagementRelationalComponent13Create) -> VendorManagementRelationalComponent13:
        comp = VendorManagementRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent13]:
        query = db.query(VendorManagementRelationalComponent13)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: VendorManagementRelationalComponent14Create) -> VendorManagementRelationalComponent14:
        comp = VendorManagementRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent14]:
        query = db.query(VendorManagementRelationalComponent14)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: VendorManagementRelationalComponent15Create) -> VendorManagementRelationalComponent15:
        comp = VendorManagementRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent15]:
        query = db.query(VendorManagementRelationalComponent15)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: VendorManagementRelationalComponent16Create) -> VendorManagementRelationalComponent16:
        comp = VendorManagementRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent16]:
        query = db.query(VendorManagementRelationalComponent16)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: VendorManagementRelationalComponent17Create) -> VendorManagementRelationalComponent17:
        comp = VendorManagementRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent17]:
        query = db.query(VendorManagementRelationalComponent17)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: VendorManagementRelationalComponent18Create) -> VendorManagementRelationalComponent18:
        comp = VendorManagementRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent18]:
        query = db.query(VendorManagementRelationalComponent18)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: VendorManagementRelationalComponent19Create) -> VendorManagementRelationalComponent19:
        comp = VendorManagementRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent19]:
        query = db.query(VendorManagementRelationalComponent19)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: VendorManagementRelationalComponent20Create) -> VendorManagementRelationalComponent20:
        comp = VendorManagementRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent20]:
        query = db.query(VendorManagementRelationalComponent20)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: VendorManagementRelationalComponent21Create) -> VendorManagementRelationalComponent21:
        comp = VendorManagementRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent21]:
        query = db.query(VendorManagementRelationalComponent21)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: VendorManagementRelationalComponent22Create) -> VendorManagementRelationalComponent22:
        comp = VendorManagementRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent22]:
        query = db.query(VendorManagementRelationalComponent22)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: VendorManagementRelationalComponent23Create) -> VendorManagementRelationalComponent23:
        comp = VendorManagementRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent23]:
        query = db.query(VendorManagementRelationalComponent23)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: VendorManagementRelationalComponent24Create) -> VendorManagementRelationalComponent24:
        comp = VendorManagementRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent24]:
        query = db.query(VendorManagementRelationalComponent24)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: VendorManagementRelationalComponent25Create) -> VendorManagementRelationalComponent25:
        comp = VendorManagementRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent25]:
        query = db.query(VendorManagementRelationalComponent25)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: VendorManagementRelationalComponent26Create) -> VendorManagementRelationalComponent26:
        comp = VendorManagementRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent26]:
        query = db.query(VendorManagementRelationalComponent26)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: VendorManagementRelationalComponent27Create) -> VendorManagementRelationalComponent27:
        comp = VendorManagementRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent27]:
        query = db.query(VendorManagementRelationalComponent27)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: VendorManagementRelationalComponent28Create) -> VendorManagementRelationalComponent28:
        comp = VendorManagementRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent28]:
        query = db.query(VendorManagementRelationalComponent28)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: VendorManagementRelationalComponent29Create) -> VendorManagementRelationalComponent29:
        comp = VendorManagementRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent29]:
        query = db.query(VendorManagementRelationalComponent29)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: VendorManagementRelationalComponent30Create) -> VendorManagementRelationalComponent30:
        comp = VendorManagementRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[VendorManagementRelationalComponent30]:
        query = db.query(VendorManagementRelationalComponent30)
        if master_entity_id:
            query = query.filter(VendorManagementRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
