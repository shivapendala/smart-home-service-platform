from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.ai_recommendations import (
    AiRecommendationsMasterEntity, AiRecommendationsStatus, AiRecommendationsPriority, AiRecommendationsCategoryType,
    AiRecommendationsRelationalComponent1 ,AiRecommendationsRelationalComponent2 ,AiRecommendationsRelationalComponent3 ,AiRecommendationsRelationalComponent4 ,AiRecommendationsRelationalComponent5 ,AiRecommendationsRelationalComponent6 ,AiRecommendationsRelationalComponent7 ,AiRecommendationsRelationalComponent8 ,AiRecommendationsRelationalComponent9 ,AiRecommendationsRelationalComponent10 ,AiRecommendationsRelationalComponent11 ,AiRecommendationsRelationalComponent12 ,AiRecommendationsRelationalComponent13 ,AiRecommendationsRelationalComponent14 ,AiRecommendationsRelationalComponent15 ,AiRecommendationsRelationalComponent16 ,AiRecommendationsRelationalComponent17 ,AiRecommendationsRelationalComponent18 ,AiRecommendationsRelationalComponent19 ,AiRecommendationsRelationalComponent20 ,AiRecommendationsRelationalComponent21 ,AiRecommendationsRelationalComponent22 ,AiRecommendationsRelationalComponent23 ,AiRecommendationsRelationalComponent24 ,AiRecommendationsRelationalComponent25
)
from app.schemas.ai_recommendations import (
    AiRecommendationsMasterEntityCreate, AiRecommendationsMasterEntityUpdate,
    AiRecommendationsRelationalComponent1Create ,AiRecommendationsRelationalComponent2Create ,AiRecommendationsRelationalComponent3Create ,AiRecommendationsRelationalComponent4Create ,AiRecommendationsRelationalComponent5Create ,AiRecommendationsRelationalComponent6Create ,AiRecommendationsRelationalComponent7Create ,AiRecommendationsRelationalComponent8Create ,AiRecommendationsRelationalComponent9Create ,AiRecommendationsRelationalComponent10Create ,AiRecommendationsRelationalComponent11Create ,AiRecommendationsRelationalComponent12Create ,AiRecommendationsRelationalComponent13Create ,AiRecommendationsRelationalComponent14Create ,AiRecommendationsRelationalComponent15Create ,AiRecommendationsRelationalComponent16Create ,AiRecommendationsRelationalComponent17Create ,AiRecommendationsRelationalComponent18Create ,AiRecommendationsRelationalComponent19Create ,AiRecommendationsRelationalComponent20Create ,AiRecommendationsRelationalComponent21Create ,AiRecommendationsRelationalComponent22Create ,AiRecommendationsRelationalComponent23Create ,AiRecommendationsRelationalComponent24Create ,AiRecommendationsRelationalComponent25Create
)

class AiRecommendationsService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: AiRecommendationsMasterEntityCreate) -> AiRecommendationsMasterEntity:
        existing = db.query(AiRecommendationsMasterEntity).filter(AiRecommendationsMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = AiRecommendationsMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> AiRecommendationsMasterEntity:
        entity = db.query(AiRecommendationsMasterEntity).filter(AiRecommendationsMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AI Smart Diagnostics Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[AiRecommendationsStatus] = None) -> List[AiRecommendationsMasterEntity]:
        query = db.query(AiRecommendationsMasterEntity)
        if status_filter:
            query = query.filter(AiRecommendationsMasterEntity.status == status_filter)
        return query.order_by(AiRecommendationsMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: AiRecommendationsMasterEntityUpdate) -> AiRecommendationsMasterEntity:
        entity = AiRecommendationsService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = AiRecommendationsService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: AiRecommendationsRelationalComponent1Create) -> AiRecommendationsRelationalComponent1:
        comp = AiRecommendationsRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent1]:
        query = db.query(AiRecommendationsRelationalComponent1)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: AiRecommendationsRelationalComponent2Create) -> AiRecommendationsRelationalComponent2:
        comp = AiRecommendationsRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent2]:
        query = db.query(AiRecommendationsRelationalComponent2)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: AiRecommendationsRelationalComponent3Create) -> AiRecommendationsRelationalComponent3:
        comp = AiRecommendationsRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent3]:
        query = db.query(AiRecommendationsRelationalComponent3)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: AiRecommendationsRelationalComponent4Create) -> AiRecommendationsRelationalComponent4:
        comp = AiRecommendationsRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent4]:
        query = db.query(AiRecommendationsRelationalComponent4)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: AiRecommendationsRelationalComponent5Create) -> AiRecommendationsRelationalComponent5:
        comp = AiRecommendationsRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent5]:
        query = db.query(AiRecommendationsRelationalComponent5)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: AiRecommendationsRelationalComponent6Create) -> AiRecommendationsRelationalComponent6:
        comp = AiRecommendationsRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent6]:
        query = db.query(AiRecommendationsRelationalComponent6)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: AiRecommendationsRelationalComponent7Create) -> AiRecommendationsRelationalComponent7:
        comp = AiRecommendationsRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent7]:
        query = db.query(AiRecommendationsRelationalComponent7)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: AiRecommendationsRelationalComponent8Create) -> AiRecommendationsRelationalComponent8:
        comp = AiRecommendationsRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent8]:
        query = db.query(AiRecommendationsRelationalComponent8)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: AiRecommendationsRelationalComponent9Create) -> AiRecommendationsRelationalComponent9:
        comp = AiRecommendationsRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent9]:
        query = db.query(AiRecommendationsRelationalComponent9)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: AiRecommendationsRelationalComponent10Create) -> AiRecommendationsRelationalComponent10:
        comp = AiRecommendationsRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent10]:
        query = db.query(AiRecommendationsRelationalComponent10)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: AiRecommendationsRelationalComponent11Create) -> AiRecommendationsRelationalComponent11:
        comp = AiRecommendationsRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent11]:
        query = db.query(AiRecommendationsRelationalComponent11)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: AiRecommendationsRelationalComponent12Create) -> AiRecommendationsRelationalComponent12:
        comp = AiRecommendationsRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent12]:
        query = db.query(AiRecommendationsRelationalComponent12)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: AiRecommendationsRelationalComponent13Create) -> AiRecommendationsRelationalComponent13:
        comp = AiRecommendationsRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent13]:
        query = db.query(AiRecommendationsRelationalComponent13)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: AiRecommendationsRelationalComponent14Create) -> AiRecommendationsRelationalComponent14:
        comp = AiRecommendationsRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent14]:
        query = db.query(AiRecommendationsRelationalComponent14)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: AiRecommendationsRelationalComponent15Create) -> AiRecommendationsRelationalComponent15:
        comp = AiRecommendationsRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent15]:
        query = db.query(AiRecommendationsRelationalComponent15)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: AiRecommendationsRelationalComponent16Create) -> AiRecommendationsRelationalComponent16:
        comp = AiRecommendationsRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent16]:
        query = db.query(AiRecommendationsRelationalComponent16)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: AiRecommendationsRelationalComponent17Create) -> AiRecommendationsRelationalComponent17:
        comp = AiRecommendationsRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent17]:
        query = db.query(AiRecommendationsRelationalComponent17)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: AiRecommendationsRelationalComponent18Create) -> AiRecommendationsRelationalComponent18:
        comp = AiRecommendationsRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent18]:
        query = db.query(AiRecommendationsRelationalComponent18)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: AiRecommendationsRelationalComponent19Create) -> AiRecommendationsRelationalComponent19:
        comp = AiRecommendationsRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent19]:
        query = db.query(AiRecommendationsRelationalComponent19)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: AiRecommendationsRelationalComponent20Create) -> AiRecommendationsRelationalComponent20:
        comp = AiRecommendationsRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent20]:
        query = db.query(AiRecommendationsRelationalComponent20)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: AiRecommendationsRelationalComponent21Create) -> AiRecommendationsRelationalComponent21:
        comp = AiRecommendationsRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent21]:
        query = db.query(AiRecommendationsRelationalComponent21)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: AiRecommendationsRelationalComponent22Create) -> AiRecommendationsRelationalComponent22:
        comp = AiRecommendationsRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent22]:
        query = db.query(AiRecommendationsRelationalComponent22)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: AiRecommendationsRelationalComponent23Create) -> AiRecommendationsRelationalComponent23:
        comp = AiRecommendationsRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent23]:
        query = db.query(AiRecommendationsRelationalComponent23)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: AiRecommendationsRelationalComponent24Create) -> AiRecommendationsRelationalComponent24:
        comp = AiRecommendationsRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent24]:
        query = db.query(AiRecommendationsRelationalComponent24)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: AiRecommendationsRelationalComponent25Create) -> AiRecommendationsRelationalComponent25:
        comp = AiRecommendationsRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[AiRecommendationsRelationalComponent25]:
        query = db.query(AiRecommendationsRelationalComponent25)
        if master_entity_id:
            query = query.filter(AiRecommendationsRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
