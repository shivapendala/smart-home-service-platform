from datetime import datetime, timezone, date, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.review_ratings import (
    ReviewRatingsMasterEntity, ReviewRatingsStatus,
    ReviewRatingsRelationalComponent1 ,ReviewRatingsRelationalComponent2 ,ReviewRatingsRelationalComponent3 ,ReviewRatingsRelationalComponent4 ,ReviewRatingsRelationalComponent5 ,ReviewRatingsRelationalComponent6 ,ReviewRatingsRelationalComponent7 ,ReviewRatingsRelationalComponent8 ,ReviewRatingsRelationalComponent9 ,ReviewRatingsRelationalComponent10 ,ReviewRatingsRelationalComponent11 ,ReviewRatingsRelationalComponent12 ,ReviewRatingsRelationalComponent13 ,ReviewRatingsRelationalComponent14 ,ReviewRatingsRelationalComponent15 ,ReviewRatingsRelationalComponent16 ,ReviewRatingsRelationalComponent17 ,ReviewRatingsRelationalComponent18 ,ReviewRatingsRelationalComponent19 ,ReviewRatingsRelationalComponent20 ,ReviewRatingsRelationalComponent21 ,ReviewRatingsRelationalComponent22 ,ReviewRatingsRelationalComponent23 ,ReviewRatingsRelationalComponent24 ,ReviewRatingsRelationalComponent25
)
from app.schemas.review_ratings import (
    ReviewRatingsMasterEntityCreate, ReviewRatingsMasterEntityUpdate,
    ReviewRatingsRelationalComponent1Create ,ReviewRatingsRelationalComponent2Create ,ReviewRatingsRelationalComponent3Create ,ReviewRatingsRelationalComponent4Create ,ReviewRatingsRelationalComponent5Create ,ReviewRatingsRelationalComponent6Create ,ReviewRatingsRelationalComponent7Create ,ReviewRatingsRelationalComponent8Create ,ReviewRatingsRelationalComponent9Create ,ReviewRatingsRelationalComponent10Create ,ReviewRatingsRelationalComponent11Create ,ReviewRatingsRelationalComponent12Create ,ReviewRatingsRelationalComponent13Create ,ReviewRatingsRelationalComponent14Create ,ReviewRatingsRelationalComponent15Create ,ReviewRatingsRelationalComponent16Create ,ReviewRatingsRelationalComponent17Create ,ReviewRatingsRelationalComponent18Create ,ReviewRatingsRelationalComponent19Create ,ReviewRatingsRelationalComponent20Create ,ReviewRatingsRelationalComponent21Create ,ReviewRatingsRelationalComponent22Create ,ReviewRatingsRelationalComponent23Create ,ReviewRatingsRelationalComponent24Create ,ReviewRatingsRelationalComponent25Create
)

class ReviewRatingsService:

    @staticmethod
    def create_master_entity(db: Session, user_id: Optional[int], entity_in: ReviewRatingsMasterEntityCreate) -> ReviewRatingsMasterEntity:
        existing = db.query(ReviewRatingsMasterEntity).filter(ReviewRatingsMasterEntity.entity_code == entity_in.entity_code).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Entity code already exists in domain")

        entity = ReviewRatingsMasterEntity(
            user_id=user_id,
            **entity_in.model_dump()
        )
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def get_master_entity_by_id(db: Session, entity_id: int) -> ReviewRatingsMasterEntity:
        entity = db.query(ReviewRatingsMasterEntity).filter(ReviewRatingsMasterEntity.id == entity_id).first()
        if not entity:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Reviews & Ratings Desk Master Entity not found")
        return entity

    @staticmethod
    def list_master_entities(db: Session, skip: int = 0, limit: int = 100, status_filter: Optional[ReviewRatingsStatus] = None) -> List[ReviewRatingsMasterEntity]:
        query = db.query(ReviewRatingsMasterEntity)
        if status_filter:
            query = query.filter(ReviewRatingsMasterEntity.status == status_filter)
        return query.order_by(ReviewRatingsMasterEntity.created_at.desc()).offset(skip).limit(limit).all()

    @staticmethod
    def update_master_entity(db: Session, entity_id: int, update_in: ReviewRatingsMasterEntityUpdate) -> ReviewRatingsMasterEntity:
        entity = ReviewRatingsService.get_master_entity_by_id(db, entity_id)
        for field, value in update_in.model_dump(exclude_unset=True).items():
            setattr(entity, field, value)
        entity.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(entity)
        return entity

    @staticmethod
    def delete_master_entity(db: Session, entity_id: int) -> bool:
        entity = ReviewRatingsService.get_master_entity_by_id(db, entity_id)
        db.delete(entity)
        db.commit()
        return True

    @staticmethod
    def add_component_1(db: Session, comp_in: ReviewRatingsRelationalComponent1Create) -> ReviewRatingsRelationalComponent1:
        comp = ReviewRatingsRelationalComponent1(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_1(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent1]:
        query = db.query(ReviewRatingsRelationalComponent1)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent1.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_2(db: Session, comp_in: ReviewRatingsRelationalComponent2Create) -> ReviewRatingsRelationalComponent2:
        comp = ReviewRatingsRelationalComponent2(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_2(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent2]:
        query = db.query(ReviewRatingsRelationalComponent2)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent2.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_3(db: Session, comp_in: ReviewRatingsRelationalComponent3Create) -> ReviewRatingsRelationalComponent3:
        comp = ReviewRatingsRelationalComponent3(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_3(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent3]:
        query = db.query(ReviewRatingsRelationalComponent3)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent3.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_4(db: Session, comp_in: ReviewRatingsRelationalComponent4Create) -> ReviewRatingsRelationalComponent4:
        comp = ReviewRatingsRelationalComponent4(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_4(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent4]:
        query = db.query(ReviewRatingsRelationalComponent4)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent4.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_5(db: Session, comp_in: ReviewRatingsRelationalComponent5Create) -> ReviewRatingsRelationalComponent5:
        comp = ReviewRatingsRelationalComponent5(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_5(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent5]:
        query = db.query(ReviewRatingsRelationalComponent5)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent5.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_6(db: Session, comp_in: ReviewRatingsRelationalComponent6Create) -> ReviewRatingsRelationalComponent6:
        comp = ReviewRatingsRelationalComponent6(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_6(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent6]:
        query = db.query(ReviewRatingsRelationalComponent6)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent6.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_7(db: Session, comp_in: ReviewRatingsRelationalComponent7Create) -> ReviewRatingsRelationalComponent7:
        comp = ReviewRatingsRelationalComponent7(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_7(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent7]:
        query = db.query(ReviewRatingsRelationalComponent7)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent7.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_8(db: Session, comp_in: ReviewRatingsRelationalComponent8Create) -> ReviewRatingsRelationalComponent8:
        comp = ReviewRatingsRelationalComponent8(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_8(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent8]:
        query = db.query(ReviewRatingsRelationalComponent8)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent8.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_9(db: Session, comp_in: ReviewRatingsRelationalComponent9Create) -> ReviewRatingsRelationalComponent9:
        comp = ReviewRatingsRelationalComponent9(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_9(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent9]:
        query = db.query(ReviewRatingsRelationalComponent9)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent9.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_10(db: Session, comp_in: ReviewRatingsRelationalComponent10Create) -> ReviewRatingsRelationalComponent10:
        comp = ReviewRatingsRelationalComponent10(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_10(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent10]:
        query = db.query(ReviewRatingsRelationalComponent10)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent10.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_11(db: Session, comp_in: ReviewRatingsRelationalComponent11Create) -> ReviewRatingsRelationalComponent11:
        comp = ReviewRatingsRelationalComponent11(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_11(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent11]:
        query = db.query(ReviewRatingsRelationalComponent11)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent11.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_12(db: Session, comp_in: ReviewRatingsRelationalComponent12Create) -> ReviewRatingsRelationalComponent12:
        comp = ReviewRatingsRelationalComponent12(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_12(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent12]:
        query = db.query(ReviewRatingsRelationalComponent12)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent12.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_13(db: Session, comp_in: ReviewRatingsRelationalComponent13Create) -> ReviewRatingsRelationalComponent13:
        comp = ReviewRatingsRelationalComponent13(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_13(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent13]:
        query = db.query(ReviewRatingsRelationalComponent13)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent13.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_14(db: Session, comp_in: ReviewRatingsRelationalComponent14Create) -> ReviewRatingsRelationalComponent14:
        comp = ReviewRatingsRelationalComponent14(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_14(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent14]:
        query = db.query(ReviewRatingsRelationalComponent14)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent14.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_15(db: Session, comp_in: ReviewRatingsRelationalComponent15Create) -> ReviewRatingsRelationalComponent15:
        comp = ReviewRatingsRelationalComponent15(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_15(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent15]:
        query = db.query(ReviewRatingsRelationalComponent15)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent15.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_16(db: Session, comp_in: ReviewRatingsRelationalComponent16Create) -> ReviewRatingsRelationalComponent16:
        comp = ReviewRatingsRelationalComponent16(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_16(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent16]:
        query = db.query(ReviewRatingsRelationalComponent16)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent16.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_17(db: Session, comp_in: ReviewRatingsRelationalComponent17Create) -> ReviewRatingsRelationalComponent17:
        comp = ReviewRatingsRelationalComponent17(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_17(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent17]:
        query = db.query(ReviewRatingsRelationalComponent17)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent17.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_18(db: Session, comp_in: ReviewRatingsRelationalComponent18Create) -> ReviewRatingsRelationalComponent18:
        comp = ReviewRatingsRelationalComponent18(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_18(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent18]:
        query = db.query(ReviewRatingsRelationalComponent18)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent18.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_19(db: Session, comp_in: ReviewRatingsRelationalComponent19Create) -> ReviewRatingsRelationalComponent19:
        comp = ReviewRatingsRelationalComponent19(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_19(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent19]:
        query = db.query(ReviewRatingsRelationalComponent19)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent19.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_20(db: Session, comp_in: ReviewRatingsRelationalComponent20Create) -> ReviewRatingsRelationalComponent20:
        comp = ReviewRatingsRelationalComponent20(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_20(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent20]:
        query = db.query(ReviewRatingsRelationalComponent20)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent20.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_21(db: Session, comp_in: ReviewRatingsRelationalComponent21Create) -> ReviewRatingsRelationalComponent21:
        comp = ReviewRatingsRelationalComponent21(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_21(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent21]:
        query = db.query(ReviewRatingsRelationalComponent21)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent21.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_22(db: Session, comp_in: ReviewRatingsRelationalComponent22Create) -> ReviewRatingsRelationalComponent22:
        comp = ReviewRatingsRelationalComponent22(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_22(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent22]:
        query = db.query(ReviewRatingsRelationalComponent22)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent22.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_23(db: Session, comp_in: ReviewRatingsRelationalComponent23Create) -> ReviewRatingsRelationalComponent23:
        comp = ReviewRatingsRelationalComponent23(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_23(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent23]:
        query = db.query(ReviewRatingsRelationalComponent23)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent23.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_24(db: Session, comp_in: ReviewRatingsRelationalComponent24Create) -> ReviewRatingsRelationalComponent24:
        comp = ReviewRatingsRelationalComponent24(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_24(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent24]:
        query = db.query(ReviewRatingsRelationalComponent24)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent24.master_entity_id == master_entity_id)
        return query.all()

    @staticmethod
    def add_component_25(db: Session, comp_in: ReviewRatingsRelationalComponent25Create) -> ReviewRatingsRelationalComponent25:
        comp = ReviewRatingsRelationalComponent25(**comp_in.model_dump())
        db.add(comp)
        db.commit()
        db.refresh(comp)
        return comp

    @staticmethod
    def list_components_25(db: Session, master_entity_id: Optional[int] = None) -> List[ReviewRatingsRelationalComponent25]:
        query = db.query(ReviewRatingsRelationalComponent25)
        if master_entity_id:
            query = query.filter(ReviewRatingsRelationalComponent25.master_entity_id == master_entity_id)
        return query.all()
