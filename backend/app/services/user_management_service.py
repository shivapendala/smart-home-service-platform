from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user_management import (
    UserManagementMasterEntity, UserManagementStatus,
    UserManagementRelationalComponent1 ,UserManagementRelationalComponent2 ,UserManagementRelationalComponent3 ,UserManagementRelationalComponent4 ,UserManagementRelationalComponent5 ,UserManagementRelationalComponent6 ,UserManagementRelationalComponent7 ,UserManagementRelationalComponent8 ,UserManagementRelationalComponent9 ,UserManagementRelationalComponent10 ,UserManagementRelationalComponent11 ,UserManagementRelationalComponent12 ,UserManagementRelationalComponent13 ,UserManagementRelationalComponent14 ,UserManagementRelationalComponent15 ,UserManagementRelationalComponent16 ,UserManagementRelationalComponent17 ,UserManagementRelationalComponent18 ,UserManagementRelationalComponent19 ,UserManagementRelationalComponent20 ,UserManagementRelationalComponent21 ,UserManagementRelationalComponent22 ,UserManagementRelationalComponent23 ,UserManagementRelationalComponent24 ,UserManagementRelationalComponent25
)
from app.schemas.user_management import (
    UserManagementMasterEntityCreate, UserManagementMasterEntityUpdate,
    UserManagementRelationalComponent1Create ,UserManagementRelationalComponent2Create ,UserManagementRelationalComponent3Create ,UserManagementRelationalComponent4Create ,UserManagementRelationalComponent5Create ,UserManagementRelationalComponent6Create ,UserManagementRelationalComponent7Create ,UserManagementRelationalComponent8Create ,UserManagementRelationalComponent9Create ,UserManagementRelationalComponent10Create ,UserManagementRelationalComponent11Create ,UserManagementRelationalComponent12Create ,UserManagementRelationalComponent13Create ,UserManagementRelationalComponent14Create ,UserManagementRelationalComponent15Create ,UserManagementRelationalComponent16Create ,UserManagementRelationalComponent17Create ,UserManagementRelationalComponent18Create ,UserManagementRelationalComponent19Create ,UserManagementRelationalComponent20Create ,UserManagementRelationalComponent21Create ,UserManagementRelationalComponent22Create ,UserManagementRelationalComponent23Create ,UserManagementRelationalComponent24Create ,UserManagementRelationalComponent25Create
)

class UserManagementService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: UserManagementMasterEntityCreate) -> UserManagementMasterEntity:
        existing = db.query(UserManagementMasterEntity).filter(UserManagementMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = UserManagementMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> UserManagementMasterEntity:
        entity = db.query(UserManagementMasterEntity).filter(UserManagementMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Enterprise User & Auth Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[UserManagementStatus] = None) -> List[UserManagementMasterEntity]:
        query = db.query(UserManagementMasterEntity)
        if status_filter:
            query = query.filter(UserManagementMasterEntity.status == status_filter)
        return query.order_by(UserManagementMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: UserManagementMasterEntityUpdate) -> UserManagementMasterEntity:
        entity = UserManagementService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = UserManagementService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: UserManagementRelationalComponent1Create) -> UserManagementRelationalComponent1:
        comp = UserManagementRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent1]:
        query = db.query(UserManagementRelationalComponent1)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: UserManagementRelationalComponent2Create) -> UserManagementRelationalComponent2:
        comp = UserManagementRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent2]:
        query = db.query(UserManagementRelationalComponent2)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: UserManagementRelationalComponent3Create) -> UserManagementRelationalComponent3:
        comp = UserManagementRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent3]:
        query = db.query(UserManagementRelationalComponent3)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: UserManagementRelationalComponent4Create) -> UserManagementRelationalComponent4:
        comp = UserManagementRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent4]:
        query = db.query(UserManagementRelationalComponent4)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: UserManagementRelationalComponent5Create) -> UserManagementRelationalComponent5:
        comp = UserManagementRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent5]:
        query = db.query(UserManagementRelationalComponent5)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: UserManagementRelationalComponent6Create) -> UserManagementRelationalComponent6:
        comp = UserManagementRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent6]:
        query = db.query(UserManagementRelationalComponent6)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: UserManagementRelationalComponent7Create) -> UserManagementRelationalComponent7:
        comp = UserManagementRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent7]:
        query = db.query(UserManagementRelationalComponent7)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: UserManagementRelationalComponent8Create) -> UserManagementRelationalComponent8:
        comp = UserManagementRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent8]:
        query = db.query(UserManagementRelationalComponent8)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: UserManagementRelationalComponent9Create) -> UserManagementRelationalComponent9:
        comp = UserManagementRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent9]:
        query = db.query(UserManagementRelationalComponent9)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: UserManagementRelationalComponent10Create) -> UserManagementRelationalComponent10:
        comp = UserManagementRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent10]:
        query = db.query(UserManagementRelationalComponent10)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: UserManagementRelationalComponent11Create) -> UserManagementRelationalComponent11:
        comp = UserManagementRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent11]:
        query = db.query(UserManagementRelationalComponent11)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: UserManagementRelationalComponent12Create) -> UserManagementRelationalComponent12:
        comp = UserManagementRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent12]:
        query = db.query(UserManagementRelationalComponent12)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: UserManagementRelationalComponent13Create) -> UserManagementRelationalComponent13:
        comp = UserManagementRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent13]:
        query = db.query(UserManagementRelationalComponent13)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: UserManagementRelationalComponent14Create) -> UserManagementRelationalComponent14:
        comp = UserManagementRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent14]:
        query = db.query(UserManagementRelationalComponent14)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: UserManagementRelationalComponent15Create) -> UserManagementRelationalComponent15:
        comp = UserManagementRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent15]:
        query = db.query(UserManagementRelationalComponent15)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: UserManagementRelationalComponent16Create) -> UserManagementRelationalComponent16:
        comp = UserManagementRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent16]:
        query = db.query(UserManagementRelationalComponent16)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: UserManagementRelationalComponent17Create) -> UserManagementRelationalComponent17:
        comp = UserManagementRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent17]:
        query = db.query(UserManagementRelationalComponent17)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: UserManagementRelationalComponent18Create) -> UserManagementRelationalComponent18:
        comp = UserManagementRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent18]:
        query = db.query(UserManagementRelationalComponent18)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: UserManagementRelationalComponent19Create) -> UserManagementRelationalComponent19:
        comp = UserManagementRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent19]:
        query = db.query(UserManagementRelationalComponent19)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: UserManagementRelationalComponent20Create) -> UserManagementRelationalComponent20:
        comp = UserManagementRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent20]:
        query = db.query(UserManagementRelationalComponent20)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: UserManagementRelationalComponent21Create) -> UserManagementRelationalComponent21:
        comp = UserManagementRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent21]:
        query = db.query(UserManagementRelationalComponent21)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: UserManagementRelationalComponent22Create) -> UserManagementRelationalComponent22:
        comp = UserManagementRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent22]:
        query = db.query(UserManagementRelationalComponent22)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: UserManagementRelationalComponent23Create) -> UserManagementRelationalComponent23:
        comp = UserManagementRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent23]:
        query = db.query(UserManagementRelationalComponent23)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: UserManagementRelationalComponent24Create) -> UserManagementRelationalComponent24:
        comp = UserManagementRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent24]:
        query = db.query(UserManagementRelationalComponent24)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: UserManagementRelationalComponent25Create) -> UserManagementRelationalComponent25:
        comp = UserManagementRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[UserManagementRelationalComponent25]:
        query = db.query(UserManagementRelationalComponent25)
        if master_entity_id:
            query = query.filter(UserManagementRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
