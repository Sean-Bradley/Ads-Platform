from sqlalchemy.orm import Session

from . import models


def get_ads(db: Session):
    return db.query(models.Ad).all()


def get_ad(db: Session, ad_id: int):
    return db.query(models.Ad).filter(models.Ad.id == ad_id).first()


def create_ad(db: Session, title: str, description: str, price: str):
    ad = models.Ad(
        title=title,
        description=description,
        price=price,
    )

    db.add(ad)
    db.commit()
    db.refresh(ad)

    return ad


def update_ad(db: Session, ad_id: int, title: str, description: str, price: str):
    ad = get_ad(db, ad_id)

    if not ad:
        return None

    ad.title = title
    ad.description = description
    ad.price = price

    db.commit()
    db.refresh(ad)

    return ad


def delete_ad(db: Session, ad_id: int):
    ad = get_ad(db, ad_id)

    if not ad:
        return None

    db.delete(ad)
    db.commit()

    return ad    
