from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.workflow_automation import (
    WorkflowAutomationMasterEntity, WorkflowAutomationStatus,
    WorkflowAutomationRelationalComponent1 ,WorkflowAutomationRelationalComponent2 ,WorkflowAutomationRelationalComponent3 ,WorkflowAutomationRelationalComponent4 ,WorkflowAutomationRelationalComponent5 ,WorkflowAutomationRelationalComponent6 ,WorkflowAutomationRelationalComponent7 ,WorkflowAutomationRelationalComponent8 ,WorkflowAutomationRelationalComponent9 ,WorkflowAutomationRelationalComponent10 ,WorkflowAutomationRelationalComponent11 ,WorkflowAutomationRelationalComponent12 ,WorkflowAutomationRelationalComponent13 ,WorkflowAutomationRelationalComponent14 ,WorkflowAutomationRelationalComponent15 ,WorkflowAutomationRelationalComponent16 ,WorkflowAutomationRelationalComponent17 ,WorkflowAutomationRelationalComponent18 ,WorkflowAutomationRelationalComponent19 ,WorkflowAutomationRelationalComponent20 ,WorkflowAutomationRelationalComponent21 ,WorkflowAutomationRelationalComponent22 ,WorkflowAutomationRelationalComponent23 ,WorkflowAutomationRelationalComponent24 ,WorkflowAutomationRelationalComponent25
)
from app.schemas.workflow_automation import (
    WorkflowAutomationMasterEntityCreate, WorkflowAutomationMasterEntityUpdate,
    WorkflowAutomationRelationalComponent1Create ,WorkflowAutomationRelationalComponent2Create ,WorkflowAutomationRelationalComponent3Create ,WorkflowAutomationRelationalComponent4Create ,WorkflowAutomationRelationalComponent5Create ,WorkflowAutomationRelationalComponent6Create ,WorkflowAutomationRelationalComponent7Create ,WorkflowAutomationRelationalComponent8Create ,WorkflowAutomationRelationalComponent9Create ,WorkflowAutomationRelationalComponent10Create ,WorkflowAutomationRelationalComponent11Create ,WorkflowAutomationRelationalComponent12Create ,WorkflowAutomationRelationalComponent13Create ,WorkflowAutomationRelationalComponent14Create ,WorkflowAutomationRelationalComponent15Create ,WorkflowAutomationRelationalComponent16Create ,WorkflowAutomationRelationalComponent17Create ,WorkflowAutomationRelationalComponent18Create ,WorkflowAutomationRelationalComponent19Create ,WorkflowAutomationRelationalComponent20Create ,WorkflowAutomationRelationalComponent21Create ,WorkflowAutomationRelationalComponent22Create ,WorkflowAutomationRelationalComponent23Create ,WorkflowAutomationRelationalComponent24Create ,WorkflowAutomationRelationalComponent25Create
)

class WorkflowAutomationService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: WorkflowAutomationMasterEntityCreate) -> WorkflowAutomationMasterEntity:
        existing = db.query(WorkflowAutomationMasterEntity).filter(WorkflowAutomationMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = WorkflowAutomationMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> WorkflowAutomationMasterEntity:
        entity = db.query(WorkflowAutomationMasterEntity).filter(WorkflowAutomationMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workflow Automation Engine Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[WorkflowAutomationStatus] = None) -> List[WorkflowAutomationMasterEntity]:
        query = db.query(WorkflowAutomationMasterEntity)
        if status_filter:
            query = query.filter(WorkflowAutomationMasterEntity.status == status_filter)
        return query.order_by(WorkflowAutomationMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: WorkflowAutomationMasterEntityUpdate) -> WorkflowAutomationMasterEntity:
        entity = WorkflowAutomationService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = WorkflowAutomationService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: WorkflowAutomationRelationalComponent1Create) -> WorkflowAutomationRelationalComponent1:
        comp = WorkflowAutomationRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent1]:
        query = db.query(WorkflowAutomationRelationalComponent1)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: WorkflowAutomationRelationalComponent2Create) -> WorkflowAutomationRelationalComponent2:
        comp = WorkflowAutomationRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent2]:
        query = db.query(WorkflowAutomationRelationalComponent2)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: WorkflowAutomationRelationalComponent3Create) -> WorkflowAutomationRelationalComponent3:
        comp = WorkflowAutomationRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent3]:
        query = db.query(WorkflowAutomationRelationalComponent3)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: WorkflowAutomationRelationalComponent4Create) -> WorkflowAutomationRelationalComponent4:
        comp = WorkflowAutomationRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent4]:
        query = db.query(WorkflowAutomationRelationalComponent4)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: WorkflowAutomationRelationalComponent5Create) -> WorkflowAutomationRelationalComponent5:
        comp = WorkflowAutomationRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent5]:
        query = db.query(WorkflowAutomationRelationalComponent5)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: WorkflowAutomationRelationalComponent6Create) -> WorkflowAutomationRelationalComponent6:
        comp = WorkflowAutomationRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent6]:
        query = db.query(WorkflowAutomationRelationalComponent6)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: WorkflowAutomationRelationalComponent7Create) -> WorkflowAutomationRelationalComponent7:
        comp = WorkflowAutomationRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent7]:
        query = db.query(WorkflowAutomationRelationalComponent7)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: WorkflowAutomationRelationalComponent8Create) -> WorkflowAutomationRelationalComponent8:
        comp = WorkflowAutomationRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent8]:
        query = db.query(WorkflowAutomationRelationalComponent8)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: WorkflowAutomationRelationalComponent9Create) -> WorkflowAutomationRelationalComponent9:
        comp = WorkflowAutomationRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent9]:
        query = db.query(WorkflowAutomationRelationalComponent9)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: WorkflowAutomationRelationalComponent10Create) -> WorkflowAutomationRelationalComponent10:
        comp = WorkflowAutomationRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent10]:
        query = db.query(WorkflowAutomationRelationalComponent10)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: WorkflowAutomationRelationalComponent11Create) -> WorkflowAutomationRelationalComponent11:
        comp = WorkflowAutomationRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent11]:
        query = db.query(WorkflowAutomationRelationalComponent11)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: WorkflowAutomationRelationalComponent12Create) -> WorkflowAutomationRelationalComponent12:
        comp = WorkflowAutomationRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent12]:
        query = db.query(WorkflowAutomationRelationalComponent12)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: WorkflowAutomationRelationalComponent13Create) -> WorkflowAutomationRelationalComponent13:
        comp = WorkflowAutomationRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent13]:
        query = db.query(WorkflowAutomationRelationalComponent13)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: WorkflowAutomationRelationalComponent14Create) -> WorkflowAutomationRelationalComponent14:
        comp = WorkflowAutomationRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent14]:
        query = db.query(WorkflowAutomationRelationalComponent14)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: WorkflowAutomationRelationalComponent15Create) -> WorkflowAutomationRelationalComponent15:
        comp = WorkflowAutomationRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent15]:
        query = db.query(WorkflowAutomationRelationalComponent15)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: WorkflowAutomationRelationalComponent16Create) -> WorkflowAutomationRelationalComponent16:
        comp = WorkflowAutomationRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent16]:
        query = db.query(WorkflowAutomationRelationalComponent16)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: WorkflowAutomationRelationalComponent17Create) -> WorkflowAutomationRelationalComponent17:
        comp = WorkflowAutomationRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent17]:
        query = db.query(WorkflowAutomationRelationalComponent17)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: WorkflowAutomationRelationalComponent18Create) -> WorkflowAutomationRelationalComponent18:
        comp = WorkflowAutomationRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent18]:
        query = db.query(WorkflowAutomationRelationalComponent18)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: WorkflowAutomationRelationalComponent19Create) -> WorkflowAutomationRelationalComponent19:
        comp = WorkflowAutomationRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent19]:
        query = db.query(WorkflowAutomationRelationalComponent19)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: WorkflowAutomationRelationalComponent20Create) -> WorkflowAutomationRelationalComponent20:
        comp = WorkflowAutomationRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent20]:
        query = db.query(WorkflowAutomationRelationalComponent20)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: WorkflowAutomationRelationalComponent21Create) -> WorkflowAutomationRelationalComponent21:
        comp = WorkflowAutomationRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent21]:
        query = db.query(WorkflowAutomationRelationalComponent21)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: WorkflowAutomationRelationalComponent22Create) -> WorkflowAutomationRelationalComponent22:
        comp = WorkflowAutomationRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent22]:
        query = db.query(WorkflowAutomationRelationalComponent22)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: WorkflowAutomationRelationalComponent23Create) -> WorkflowAutomationRelationalComponent23:
        comp = WorkflowAutomationRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent23]:
        query = db.query(WorkflowAutomationRelationalComponent23)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: WorkflowAutomationRelationalComponent24Create) -> WorkflowAutomationRelationalComponent24:
        comp = WorkflowAutomationRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent24]:
        query = db.query(WorkflowAutomationRelationalComponent24)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: WorkflowAutomationRelationalComponent25Create) -> WorkflowAutomationRelationalComponent25:
        comp = WorkflowAutomationRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent25]:
        query = db.query(WorkflowAutomationRelationalComponent25)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_26(db: Session, comp_in: WorkflowAutomationRelationalComponent26Create) -> WorkflowAutomationRelationalComponent26:
        comp = WorkflowAutomationRelationalComponent26(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_26(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent26]:
        query = db.query(WorkflowAutomationRelationalComponent26)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent26.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_27(db: Session, comp_in: WorkflowAutomationRelationalComponent27Create) -> WorkflowAutomationRelationalComponent27:
        comp = WorkflowAutomationRelationalComponent27(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_27(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent27]:
        query = db.query(WorkflowAutomationRelationalComponent27)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent27.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_28(db: Session, comp_in: WorkflowAutomationRelationalComponent28Create) -> WorkflowAutomationRelationalComponent28:
        comp = WorkflowAutomationRelationalComponent28(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_28(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent28]:
        query = db.query(WorkflowAutomationRelationalComponent28)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent28.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_29(db: Session, comp_in: WorkflowAutomationRelationalComponent29Create) -> WorkflowAutomationRelationalComponent29:
        comp = WorkflowAutomationRelationalComponent29(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_29(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent29]:
        query = db.query(WorkflowAutomationRelationalComponent29)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent29.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_30(db: Session, comp_in: WorkflowAutomationRelationalComponent30Create) -> WorkflowAutomationRelationalComponent30:
        comp = WorkflowAutomationRelationalComponent30(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_30(db: Session, master_entity_id: Optional[int] = None) -> List[WorkflowAutomationRelationalComponent30]:
        query = db.query(WorkflowAutomationRelationalComponent30)
        if master_entity_id:
            query = query.filter(WorkflowAutomationRelationalComponent30.master_entity_id == master_entity_id)
        return query.all()
