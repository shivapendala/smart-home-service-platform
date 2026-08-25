import re
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.service import Category, Service
from app.schemas.service import CategoryCreate, ServiceCreate, ServiceUpdate


def slugify(text: str) -> str:
    """Helper utility converting strings to URL-safe slugs."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[\s_-]+', '-', text)


class CatalogService:

    @staticmethod
    def get_categories(db: Session) -> List[Category]:
        """Fetch all service categories."""
        categories = db.query(Category).all()
        if not categories:
            # Auto-seed default home service categories if database is fresh
            categories = CatalogService.seed_initial_catalog(db)
        return categories

    @staticmethod
    def create_category(db: Session, category_in: CategoryCreate) -> Category:
        """Create new category (Admin only)."""
        slug = slugify(category_in.name)
        existing = db.query(Category).filter((Category.name == category_in.name) | (Category.slug == slug)).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category with this name or slug already exists."
            )
        category = Category(
            name=category_in.name,
            slug=slug,
            icon=category_in.icon,
            description=category_in.description
        )
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def get_services(
        db: Session,
        category_id: Optional[int] = None,
        search: Optional[str] = None,
        only_active: bool = True
    ) -> List[Service]:
        """Fetch services filtered by category ID or keyword search."""
        # Seed if fresh database
        CatalogService.get_categories(db)

        query = db.query(Service)
        if only_active:
            query = query.filter(Service.is_active == True)
        if category_id:
            query = query.filter(Service.category_id == category_id)
        if search:
            search_pattern = f"%{search}%"
            query = query.filter(
                (Service.name.ilike(search_pattern)) | (Service.description.ilike(search_pattern))
            )
        return query.all()

    @staticmethod
    def get_service_by_id(db: Session, service_id: int) -> Service:
        """Fetch single service item by ID."""
        service = db.query(Service).filter(Service.id == service_id).first()
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service item not found."
            )
        return service

    @staticmethod
    def create_service(db: Session, service_in: ServiceCreate) -> Service:
        """Create new service item (Admin only)."""
        category = db.query(Category).filter(Category.id == service_in.category_id).first()
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Category not found."
            )
        
        slug = slugify(service_in.name)
        existing = db.query(Service).filter(Service.slug == slug).first()
        if existing:
            slug = f"{slug}-{int(datetime.now().timestamp())}"

        service = Service(
            category_id=service_in.category_id,
            name=service_in.name,
            slug=slug,
            description=service_in.description,
            base_price=service_in.base_price,
            duration_minutes=service_in.duration_minutes,
            image_url=service_in.image_url,
            is_active=service_in.is_active
        )
        db.add(service)
        db.commit()
        db.refresh(service)
        return service

    @staticmethod
    def update_service(db: Session, service_id: int, service_in: ServiceUpdate) -> Service:
        """Update service details or pricing (Admin only)."""
        service = CatalogService.get_service_by_id(db, service_id)
        update_data = service_in.model_dump(exclude_unset=True)
        
        if "name" in update_data and update_data["name"]:
            update_data["slug"] = slugify(update_data["name"])

        for field, value in update_data.items():
            setattr(service, field, value)
            
        db.add(service)
        db.commit()
        db.refresh(service)
        return service

    @staticmethod
    def delete_service(db: Session, service_id: int) -> bool:
        """Delete service item (Admin only)."""
        service = CatalogService.get_service_by_id(db, service_id)
        db.delete(service)
        db.commit()
        return True

    @staticmethod
    def seed_initial_catalog(db: Session) -> List[Category]:
        """Initial catalog seeder populating production categories and standard home services."""
        if db.query(Category).first():
            return db.query(Category).all()

        seed_data = [
            {
                "name": "AC Repair & Installation",
                "icon": "❄️",
                "description": "Air conditioner servicing, gas refilling, filter cleaning, AC installation, and compressor repair.",
                "services": [
                    {"name": "AC Repair & Servicing", "price": 49.00, "duration": 60, "desc": "Deep filter cleaning, coil washing, drain flushing, and health diagnostic."},
                    {"name": "AC Installation & Uninstallation", "price": 89.00, "duration": 120, "desc": "Complete split or window AC wall mounting, piping connection & testing."},
                    {"name": "AC Gas Refill & Leak Fix", "price": 79.00, "duration": 90, "desc": "Comprehensive pressure check, leak detection, welding repair & full gas top-up."}
                ]
            },
            {
                "name": "Refrigerator Repair",
                "icon": "🧊",
                "description": "Refrigeration cooling fix, thermostat setup, door seal replacement.",
                "services": [
                    {"name": "Refrigerator Repair & Maintenance", "price": 55.00, "duration": 60, "desc": "Defrost sensor replacement, fan motor check & temperature regulation fix."}
                ]
            },
            {
                "name": "Washing Machine Repair",
                "icon": "🧺",
                "description": "Front load & top load motor repair, drum balancing, water drain fix.",
                "services": [
                    {"name": "Washing Machine Repair", "price": 45.00, "duration": 60, "desc": "Noise diagnostic, belt check, drum alignment & electrical safety test."}
                ]
            },
            {
                "name": "Plumbing",
                "icon": "🚰",
                "description": "Pipe leakage repair, tap/faucet install, blockage removal.",
                "services": [
                    {"name": "Plumbing Repair & Fitting", "price": 35.00, "duration": 45, "desc": "Kitchen/bathroom faucet fitting, washer replacement & pipe leak fix."}
                ]
            },
            {
                "name": "Electrical",
                "icon": "⚡",
                "description": "Short circuit fixing, switchboard installation, light fittings.",
                "services": [
                    {"name": "Electrical Repair & Wiring", "price": 35.00, "duration": 45, "desc": "Loose wire repair, MCB replacement & socket installation."}
                ]
            },
            {
                "name": "TV Repair",
                "icon": "📺",
                "description": "LED/LCD TV screen fix, mother board troubleshooting, power supply repair.",
                "services": [
                    {"name": "TV Repair & Display Service", "price": 65.00, "duration": 60, "desc": "Display panel diagnosis, backlight strip replacement, sound fix & wall mount."}
                ]
            }
        ]

        created_categories = []
        for cat_data in seed_data:
            category = Category(
                name=cat_data["name"],
                slug=slugify(cat_data["name"]),
                icon=cat_data["icon"],
                description=cat_data["description"]
            )
            db.add(category)
            db.flush()

            for s_data in cat_data["services"]:
                service = Service(
                    category_id=category.id,
                    name=s_data["name"],
                    slug=slugify(s_data["name"]),
                    description=s_data["desc"],
                    base_price=s_data["price"],
                    duration_minutes=s_data["duration"],
                    is_active=True
                )
                db.add(service)

            created_categories.append(category)

        db.commit()
        return created_categories
